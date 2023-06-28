from typing import List, Dict, Set

from src.pddl.Action import Action
from src.pddl.Atom import Atom
from src.pddl.BinaryPredicate import BinaryPredicate
from src.pddl.Constant import Constant
from src.pddl.Domain import GroundedDomain
from src.pddl.Formula import Formula
from src.pddl.Literal import Literal
from src.pddl.NumericPlan import NumericPlan
from src.pddl.Problem import Problem
from src.pddl.Utilities import Utilities
from src.plan.Pattern import Pattern
from src.plan.TransitionVariables import TransitionVariables
from src.smt.SMTExpression import SMTExpression
from src.smt.SMTNumericVariable import SMTNumericVariable
from src.smt.SMTSolution import SMTSolution

BOUND = 100
EXPLICIT_DELTA = False


class PDDL2SMT:
    domain: GroundedDomain
    problem: Problem

    def __init__(self, domain: GroundedDomain, problem: Problem, horizon: int):
        self.domain = domain
        self.problem = problem
        self.horizon = horizon

        self.transitionVariables: [TransitionVariables] = list()

        self.transitions: [SMTExpression] = []

        self.dummyAction = Action()
        self.dummyAction.isFake = True
        self.dummyAction.name = "dummy_action_do_not_use"

        order: List[Action] = self.domain.getARPG().getActionsOrder()
        order.append(self.dummyAction)

        self.pattern = Pattern.fromOrder(order)
        self.pattern.extendNonLinearities(5)

        self.sign: Dict[Action, Dict[Atom, int]] = self.getSign(self.pattern)

        for index in range(0, horizon + 1):
            var = TransitionVariables(self.domain.allAtoms, self.domain.assList, self.pattern, index)
            self.transitionVariables.append(var)

        self.initial: [SMTExpression] = self.getInitialExpression()
        self.goal: [SMTExpression] = self.getGoalExpression()

        for index in range(1, horizon + 1):
            stepRules = self.getStepRules(index)
            self.transitions.extend(stepRules)

        self.rules = self.initial + self.transitions + [self.goal]

    def getInitialExpression(self) -> List[SMTExpression]:
        tVars = self.transitionVariables[0]
        rules: [SMTExpression] = list()

        trueAtoms: Set[Atom] = set()
        for assignment in self.problem.init:
            atom = assignment.getAtom()
            if atom not in tVars.valueVariables:
                # print(f"Atom {atom} in initial condition doesn't concur in achieving the goal. Pruned.")
                continue
            if isinstance(assignment, BinaryPredicate):
                if assignment.getAtom() not in self.domain.allAtoms:
                    # print(f"Atom {assignments.getAtom()} was pruned since it's a constant")
                    continue
                rules.append(tVars.valueVariables[assignment.getAtom()] == float(str(assignment.rhs)))
            elif isinstance(assignment, Literal):
                rules.append(tVars.valueVariables[assignment.getAtom()] == 1)
                trueAtoms.add(assignment.getAtom())
            else:
                raise NotImplemented("Shouldn't go here")

        for v in self.domain.predicates - trueAtoms:
            rules.append(tVars.valueVariables[v] == -1)

        return rules

    def getGoalRuleFromFormula(self, f: Formula) -> SMTExpression:
        tVars = self.transitionVariables[-1]
        rules: [SMTExpression] = []
        for condition in f.conditions:
            if isinstance(condition, BinaryPredicate):
                expr = SMTExpression.fromPddl(condition, tVars.valueVariables)
                rules.append(expr)
            elif isinstance(condition, Literal):
                if condition.sign == "+":
                    rules.append(tVars.valueVariables[condition.getAtom()] > 0)
                else:
                    rules.append(tVars.valueVariables[condition.getAtom()] < 0)
            elif isinstance(condition, Formula):
                rules.append(self.getGoalRuleFromFormula(condition))
            else:
                raise NotImplemented("Shouldn't go here")

        if f.type == "AND":
            return SMTExpression.andOfExpressionsList(rules)
        if f.type == "OR":
            return SMTExpression.orOfExpressionsList(rules)

    @staticmethod
    def getSign(pattern: Pattern) -> Dict[Action, Dict[Atom, int]]:
        sign: Dict[Action, Dict[Atom, int]] = dict()

        for (i, a) in enumerate(pattern):
            sign[a] = dict()
            addList = a.getAddList()
            delList = a.getDelList()
            for v in addList | delList:
                sA = 0
                for b in pattern[:i]:
                    if (v in addList and v in b.getDelList()) or (v in delList and v in b.getAddList()):
                        sA -= sign[b][v]
                sA += +2 if v in addList else -2
                sign[a][v] = sA

        return sign

    def getGoalExpression(self) -> SMTExpression:
        return self.getGoalRuleFromFormula(self.problem.goal)

    def getMetricExpression(self, metricBound: float) -> SMTExpression or None:

        if self.problem.metric:
            return SMTNumericVariable.fromPddl(self.problem.metric,
                                               self.transitionVariables[-1].valueVariables) < metricBound

        if not self.problem.metric:
            sumOfActions = 0
            for stepVar in self.transitionVariables[1:]:
                for action in self.pattern:
                    if action.isFake:
                        continue
                    sumOfActions += stepVar.actionVariables[action] * action.linearizationTimes
            return sumOfActions < metricBound

    def getDeltaStepRules(self, prevVars: TransitionVariables, stepVars: TransitionVariables) -> List[SMTExpression]:
        rules: List[SMTExpression] = []

        prevAction: Action or None = None
        for action in self.pattern:
            if not prevAction:
                # First action in the order copies the value from previous step
                for v in self.domain.allAtoms:
                    stepVars.deltaVariables[action][v] = prevVars.valueVariables[v]
                prevAction = action
                continue

            # Case a) Not influenced
            notInfluenced = self.domain.allAtoms - (prevAction.getInfluencedAtoms())
            for v in notInfluenced:
                stepVars.deltaVariables[action][v] = stepVars.deltaVariables[prevAction][v]

            # Case b) Boolean
            for v in prevAction.getAddList() | prevAction.getDelList():
                d_bv = stepVars.deltaVariables[prevAction][v]
                s_bv = self.sign[prevAction][v]
                b_b = stepVars.boolActionVariables[prevAction]

                stepVars.deltaVariables[action][v] = d_bv + s_bv * b_b
            # Case c) Numeric increases or decreases
            if not prevAction.hasNonSimpleLinearIncrement():
                modifications = [(+1, prevAction.getIncreases()), (-1, prevAction.getDecreases())]
                for sign, modificationDict in modifications:
                    for v, funct in modificationDict.items():

                        d_bv = stepVars.deltaVariables[prevAction][v]
                        k = SMTNumericVariable.fromPddl(funct, stepVars.deltaVariables[prevAction])
                        b_n = stepVars.actionVariables[prevAction]
                        if sign > 0:
                            stepVars.deltaVariables[action][v] = d_bv + (k * b_n)
                        else:
                            stepVars.deltaVariables[action][v] = d_bv - (k * b_n)
            # Case d) Numeric assignments
            for v in prevAction.getAssList():
                stepVars.deltaVariables[action][v] = stepVars.auxVariables[prevAction][v]

            if prevAction.hasNonSimpleLinearIncrement():
                for eff in prevAction.effects:
                    if not eff.isLinearIncrement():
                        continue
                    v = eff.getAtom()
                    stepVars.deltaVariables[action][v] = stepVars.auxVariables[prevAction][v]

            prevAction = action

        return rules

    def getActStepRules(self, stepVars: TransitionVariables) -> List[SMTExpression]:
        rules: List[SMTExpression] = []

        for a in self.pattern:
            if a.isFake:
                continue
            a_n = stepVars.actionVariables[a]
            a_b = stepVars.boolActionVariables[a]
            b = BOUND if a.couldBeRepeated() and not a.hasNonSimpleLinearIncrement() else 1
            rules.append(a_n >= 0)
            rules.append(a_n <= b)
            if a.getPredicates():
                active = (a_n > 0).AND(a_b == 1)
                notActive = (a_n == 0).AND(a_b == 0)
                rules.append(active.OR(notActive))

        if len(self.domain.arpg.stateLevels) > 2:
            for (atom, interval) in self.domain.arpg.stateLevels[-1].intervals.items():
                if atom not in stepVars.valueVariables:
                    continue
                if interval.lb != float("-inf"):
                    rules.append(stepVars.valueVariables[atom] >= interval.lb)
                if interval.ub != float("+inf"):
                    rules.append(stepVars.valueVariables[atom] <= interval.ub)

        return rules

    def getPreStepRules(self, stepVars: TransitionVariables) -> List[SMTExpression]:
        rules: List[SMTExpression] = []

        for a in self.pattern:
            if a.isFake:
                continue
            # a_n > 0
            lhs = stepVars.actionVariables[a] > 0
            preconditions = None
            for pre in a.preconditions:
                if isinstance(pre, Literal):
                    v = pre.getAtom()
                    d_av = stepVars.deltaVariables[a][v]
                    rhs = d_av > 0 if pre.sign == "+" else d_av < 0
                    preconditions = preconditions.AND(rhs) if preconditions else rhs
                    continue

                function: BinaryPredicate = pre.lhs - pre.rhs

                subs: Dict[Atom, float] = dict()
                # Searching for decrease effects
                for eff in a.effects:
                    if not isinstance(eff, BinaryPredicate):
                        continue
                    if not isinstance(eff.rhs, Constant):
                        continue
                    if eff.operator == "assign":
                        continue

                    sign = +1 if eff.operator == "increase" else -1
                    subs[eff.lhs.getAtom()] = sign * eff.rhs.value

                subsFunction = function.substitute(subs, default=0)

                # Transformed precondition
                functSMT = SMTNumericVariable.fromPddl(function, stepVars.deltaVariables[a])
                w0 = function.getLinearIncrement()
                subsFunctSMT = SMTNumericVariable.fromPddl(subsFunction, dict())  # It should not contain literals
                subsFunctSTM_w0 = subsFunctSMT - w0
                prevTimes = (stepVars.actionVariables[a] - 1)

                # Controlliamo se f(k_1, ..., k_n) contribuisce ad avvicinarsi al vincolo, se non è cosi la togliamo
                aDecrease = 0 if Utilities.compare(pre.operator, subsFunctSTM_w0, 0) else subsFunctSTM_w0 * prevTimes

                # f(x_1, ..., x_p) + [f(k_1, ..., k_p) - w_0]*(a_n - 1) {op} 0
                condition = functSMT + aDecrease
                rhs = SMTNumericVariable.opByString(pre.operator, condition, 0)

                preconditions = preconditions.AND(rhs) if preconditions else rhs

            if preconditions:
                rules.append(lhs.implies(preconditions))
        return rules

    def getEffStepRules(self, stepVars: TransitionVariables) -> List[SMTExpression]:
        rules: List[SMTExpression] = []

        for a in self.pattern:
            for var, rhs in a.getAssignments().items():
                v_a = stepVars.auxVariables[a][var]
                a_n = stepVars.actionVariables[a]
                d_a_v = stepVars.deltaVariables[a][var]
                if not isinstance(rhs, Constant):
                    raise Exception("I cannot handle yet linear assignments")
                k = rhs.value
                rules.append((a_n > 0).implies(v_a == k))
                rules.append((a_n == 0).implies(v_a == d_a_v))

            if not a.hasNonSimpleLinearIncrement():
                continue

            for eff in a.effects:
                if not eff.isLinearIncrement():
                    continue
                var = eff.getAtom()
                v_a = stepVars.auxVariables[a][var]
                a_n = stepVars.actionVariables[a]
                d_a_v = stepVars.deltaVariables[a][var]
                d_a_phi = SMTNumericVariable.fromPddl(eff.rhs, stepVars.deltaVariables[a])
                if eff.operator == "increase":
                    rules.append((a_n > 0).implies(v_a == d_a_v + d_a_phi))
                else:
                    rules.append((a_n > 0).implies(v_a == d_a_v - d_a_phi))
                rules.append((a_n == 0).implies(v_a == d_a_v))

        return rules

    def getFrameStepRules(self, stepVars: TransitionVariables) -> List[SMTExpression]:
        rules: List[SMTExpression] = []

        for v in self.domain.functions:
            v_first = stepVars.valueVariables[v]
            delta_g_v = stepVars.deltaVariables[self.dummyAction][v]
            rules.append(v_first == delta_g_v)

        for v in self.domain.predicates:
            v_first = stepVars.valueVariables[v]
            delta_g_v = stepVars.deltaVariables[self.dummyAction][v]
            rules.append((delta_g_v > 0).implies(v_first == 1))
            rules.append((delta_g_v < 0).implies(v_first == -1))

        return rules

    def getStepRules(self, index: int) -> List[SMTExpression]:
        prevVars = self.transitionVariables[index - 1]
        stepVars = self.transitionVariables[index]

        rules: List[SMTExpression] = []
        rules += self.getDeltaStepRules(prevVars, stepVars)
        rules += self.getActStepRules(stepVars)
        rules += self.getPreStepRules(stepVars)
        rules += self.getEffStepRules(stepVars)
        rules += self.getFrameStepRules(stepVars)

        return rules

    def printRules(self):
        for rule in self.rules:
            print(rule)

    def getPlanFromSolution(self, solution: SMTSolution) -> NumericPlan:
        plan = NumericPlan()

        if not solution:
            return plan

        for i in range(1, self.horizon + 1):
            stepVar = self.transitionVariables[i]
            for a in self.pattern:
                if a.isFake:
                    continue
                repetitions = int(str(solution.getVariable(stepVar.actionVariables[a]))) * a.linearizationTimes
                if repetitions > 0:
                    plan.addRepeatedAction(a.linearizationOf, repetitions)

        return plan