from typing import List, Dict, Set, Type

from src.goalFunctions.GoalFunction import GoalFunction, EPSILON
from src.pddl.Action import Action
from src.pddl.Atom import Atom
from src.pddl.BinaryPredicate import BinaryPredicate
from src.pddl.Constant import Constant
from src.pddl.Domain import GroundedDomain
from src.pddl.Formula import Formula
from src.pddl.Literal import Literal
from src.pddl.NumericPlan import NumericPlan
from src.pddl.Problem import Problem
from src.pddl.State import State
from src.plan.Encoding import Encoding
from src.plan.NumericTransitionVariables import NumericTransitionVariables
from src.plan.Pattern import Pattern
from src.smt.SMTExpression import SMTExpression
from src.smt.SMTNumericVariable import SMTNumericVariable
from src.smt.SMTSolution import SMTSolution
from src.utils.Arguments import Arguments

# BOUND = 1000
EXPLICIT_DELTA = False


class NumericEncoding(Encoding):
    domain: GroundedDomain
    problem: Problem

    def __init__(self, domain: GroundedDomain, problem: Problem, pattern: Pattern, bound: int,
                 args: Arguments,
                 relaxGoal=False,
                 subgoalsAchieved=None,
                 minimizeQuality=False,
                 maxActionsRolling: Dict[int, Dict[Action, int]] = None,
                 goalFunction: Type[GoalFunction] = None,
                 goalFunctionValue: float = 0.0,
                 goalFunctionWithEpsilon: bool = False,
                 minimizeGoalFunction: float = False):

        super().__init__(domain, problem, pattern, bound)
        self.domain = domain
        self.problem = problem
        self.bound = bound

        self.relaxGoal = relaxGoal
        self.subgoalsAchieved = subgoalsAchieved
        self.encoding = args.encoding
        self.rollBound = args.rollBound
        self.minimizeQuality = minimizeQuality or args.quality == "shortest-step"
        self.binaryActions: int = args.binaryActions
        self.hasEffectAxioms = args.hasEffectAxioms
        self.maxActionsRolling = maxActionsRolling
        self.goalFunction = goalFunction
        self.goalFunctionValue = goalFunctionValue
        self.minimizeGoalFunction = minimizeGoalFunction
        self.goalFunctionWithEpsilon = goalFunctionWithEpsilon

        self.transitionVariables: [NumericTransitionVariables] = list()

        self.transitions: [SMTExpression] = []

        self.pattern = pattern
        if self.encoding == "binary":
            self.pattern.extendNonLinearities(self.binaryActions)

        for index in range(0, bound + 1):
            var = NumericTransitionVariables(self.domain.predicates, self.domain.functions, self.domain.assList,
                                             self.pattern, index, self.hasEffectAxioms)
            self.transitionVariables.append(var)
            if index > 0:
                self.actionVariables.update(var.actionVariables.values())
        self.k = len(self.pattern)

        self.softRules = []
        self.initial: [SMTExpression] = self.getInitialExpression()
        self.minimize: SMTExpression or None = self.getMinimize()
        self.goal: [SMTExpression] = self.getGoalExpression()

        for index in range(1, bound + 1):
            stepRules = self.getStepRules(index)
            self.transitions.extend(stepRules)

        self.rules = self.initial + self.transitions + [self.goal]

    def getMinimize(self):
        if self.minimizeQuality:
            return sum(self.actionVariables)
        if self.minimizeGoalFunction:
            vars = self.transitionVariables[-1].valueVariables
            init = State.fromInitialCondition(self.problem.init)
            return self.goalFunction.getExpression(vars, self.problem.goal, init)
        return None

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
                rules.append(tVars.valueVariables[assignment.getAtom()].equal(float(str(assignment.rhs))))
            elif isinstance(assignment, Literal):
                rules.append(tVars.valueVariables[assignment.getAtom()])
                trueAtoms.add(assignment.getAtom())
            else:
                raise NotImplemented("Shouldn't go here")

        for v in self.domain.predicates - trueAtoms:
            rules.append(~tVars.valueVariables[v])

        return rules

    def getGoalRuleFromFormula(self, f: Formula, level: int) -> SMTExpression:
        tVars = self.transitionVariables[-1]

        andRules: [SMTExpression] = []
        orRules: [SMTExpression] = []

        for condition in f.conditions:
            rule: SMTExpression

            if isinstance(condition, BinaryPredicate):
                rule = SMTExpression.fromPddl(condition, tVars.valueVariables)
            elif isinstance(condition, Literal):
                if condition.sign == "+":
                    rule = tVars.valueVariables[condition.getAtom()]
                else:
                    rule = ~tVars.valueVariables[condition.getAtom()]
            elif isinstance(condition, Formula):
                rule = self.getGoalRuleFromFormula(condition, level + 1)
            else:
                raise NotImplemented("Shouldn't go here")

            if level == 0 and self.relaxGoal:
                if condition in self.subgoalsAchieved:
                    andRules.append(rule)
                else:
                    self.softRules.append(rule)
                    orRules.append(rule)
            else:
                if f.type == "AND":
                    andRules.append(rule)
                elif f.type == "OR":
                    orRules.append(rule)

        rules = []
        if andRules:
            rules.append(SMTExpression.bigand(andRules))
        if orRules:
            rules.append(SMTExpression.bigor(orRules))

        return SMTExpression.bigand(rules)

    def getGoalExpression(self) -> SMTExpression:

        if self.relaxGoal and self.problem.goal.type != "AND":
            raise Exception("At the moment I cannot relax the goal if it is not expressed as a conjunction of formulas")

        if self.goalFunction:
            vars = self.transitionVariables[-1].valueVariables
            init = State.fromInitialCondition(self.problem.init)
            expr = self.goalFunction.getExpression(vars, self.problem.goal.normalize(), init)
            c = self.goalFunctionValue
            if self.goalFunctionWithEpsilon:
                return expr <= max(c - EPSILON, 0)
            else:
                return expr < EPSILON

        return self.getGoalRuleFromFormula(self.problem.goal, 0)

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

    def getDeltaStepRules(self, prevVars: NumericTransitionVariables, stepVars: NumericTransitionVariables) \
            -> List[SMTExpression]:
        rules: List[SMTExpression] = []

        for v in self.domain.allAtoms:
            stepVars.sigmaVariables[0][v] = prevVars.valueVariables[v]

        for i, action in self.pattern.enumerate():

            # Case a) Not influenced
            notInfluenced = self.domain.allAtoms - (action.getInfluencedAtoms())
            for v in notInfluenced:
                stepVars.sigmaVariables[i][v] = stepVars.sigmaVariables[i - 1][v]

            # Case b) Boolean
            for v in action.getAddList() | action.getDelList():
                d_bv = stepVars.sigmaVariables[i - 1][v]
                b_n = stepVars.actionVariables[i]

                if v in action.getAddList():
                    stepVars.sigmaVariables[i][v] = (d_bv | (b_n > 0))

                if v in action.getDelList():
                    stepVars.sigmaVariables[i][v] = (d_bv & (b_n.equal(0)))

            # Case c) Numeric increases or decreases
            if not action.hasNonSimpleLinearIncrement(self.encoding):
                modifications = [(+1, action.getIncreases()), (-1, action.getDecreases())]
                for sign, modificationDict in modifications:
                    for v, funct in modificationDict.items():
                        d_bv = stepVars.sigmaVariables[i - 1][v]
                        k = SMTNumericVariable.fromPddl(funct, stepVars.sigmaVariables[i - 1])
                        b_n = stepVars.actionVariables[i]
                        stepVars.sigmaVariables[i][v] = (d_bv + (k * b_n)) if sign > 0 else (d_bv - (k * b_n))

            # Case d) Numeric assignments
            for v in action.getAssList():
                stepVars.sigmaVariables[i][v] = stepVars.auxVariables[i][v]

            if action.hasNonSimpleLinearIncrement(self.encoding):
                for eff in action.effects:
                    if not eff.isLinearIncrement():
                        continue
                    v = eff.getAtom()
                    stepVars.sigmaVariables[i][v] = stepVars.auxVariables[i][v]

        return rules

    def getAmoStepRules(self, stepVars: NumericTransitionVariables, n: int) -> List[SMTExpression]:
        rules: List[SMTExpression] = []

        for i, a in self.pattern.enumerate():
            a_n = stepVars.actionVariables[i]
            rules.append(a_n >= 0)
            if self.rollBound:
                rules.append(a_n <= self.rollBound)
                continue
            if self.maxActionsRolling:
                rules.append(a_n <= self.maxActionsRolling[n][a])
                continue
            if not a.couldBeRepeated() or (a.hasNonSimpleLinearIncrement(self.encoding)):
                rules.append(a_n <= 1)
                continue

        if len(self.domain.arpg.stateLevels) > 2:
            for (atom, interval) in self.domain.arpg.stateLevels[-1].intervals.items():
                if atom not in stepVars.valueVariables:
                    continue
                if interval.lb != float("-inf"):
                    rules.append(stepVars.valueVariables[atom] >= interval.lb)
                if interval.ub != float("+inf"):
                    rules.append(stepVars.valueVariables[atom] <= interval.ub)

        return rules

    def getPreStepRules(self, stepVars: NumericTransitionVariables) -> List[SMTExpression]:
        rules: List[SMTExpression] = []

        for i, a in self.pattern.enumerate():

            lhs0 = stepVars.actionVariables[i] > 0
            lhs1 = stepVars.actionVariables[i] > 1
            preconditions0 = None
            preconditions1 = None
            isPre1Impossible = False
            for pre in a.preconditions:
                if isinstance(pre, Literal):
                    v = pre.getAtom()
                    d_av = stepVars.sigmaVariables[i - 1][v]
                    rhs = d_av if pre.sign == "+" else ~d_av
                    preconditions0 = preconditions0 & rhs if preconditions0 else rhs
                    preconditions1 = preconditions1 & rhs if preconditions1 else rhs
                    continue

                precondition0 = SMTNumericVariable.fromPddl(pre, stepVars.sigmaVariables[i - 1])
                preconditions0 = preconditions0 & precondition0 if preconditions0 else precondition0

                subs: Dict[Atom, SMTExpression] = dict()
                # Searching for decrease effects
                for eff in a.effects:
                    if not isinstance(eff, BinaryPredicate):
                        continue
                    v = eff.lhs.getAtom()
                    rhsExpr = SMTNumericVariable.fromPddl(eff.rhs, stepVars.sigmaVariables[i - 1])
                    if eff.operator == "assign":
                        subs[v] = rhsExpr
                        continue
                    if eff.operator == "increase":
                        subs[v] = stepVars.sigmaVariables[i - 1][v] + rhsExpr * (stepVars.actionVariables[i] - 1)
                        pass
                    else:
                        subs[v] = stepVars.sigmaVariables[i - 1][v] - rhsExpr * (stepVars.actionVariables[i] - 1)

                for v in stepVars.sigmaVariables[i - 1].keys():
                    subs[v] = subs[v] if v in subs else stepVars.sigmaVariables[i - 1][v]

                # Transformed precondition
                precondition1 = SMTNumericVariable.fromPddl(pre, subs)
                if not precondition1:
                    isPre1Impossible = True
                else:
                    preconditions1 = preconditions1 & precondition1 if preconditions1 else precondition1

            if preconditions0:
                rules.append(lhs0.implies(preconditions0))

            if preconditions1 and not isPre1Impossible:
                rules.append(lhs1.implies(preconditions1))

            if isPre1Impossible:
                rules.append(~lhs1)

        return rules

    def getEffStepRules(self, stepVars: NumericTransitionVariables) -> List[SMTExpression]:
        rules: List[SMTExpression] = []

        for i, a in self.pattern.enumerate():
            for var, rhs in a.getAssignments().items():
                v_a = stepVars.auxVariables[i][var]
                a_n = stepVars.actionVariables[i]
                d_a_v = stepVars.sigmaVariables[i - 1][var]
                d_psi = rhs.value if isinstance(rhs, Constant) else \
                    SMTNumericVariable.fromPddl(rhs, stepVars.sigmaVariables[i - 1])

                rules.append((a_n > 0).implies(v_a.equal(d_psi)))
                rules.append((a_n.equal(0)).implies(v_a.equal(d_a_v)))

            if not a.hasNonSimpleLinearIncrement(self.encoding):
                continue

            for eff in a.effects:
                if not eff.isLinearIncrement():
                    continue
                var = eff.getAtom()
                v_a = stepVars.auxVariables[i][var]
                a_n = stepVars.actionVariables[i]
                d_a_v = stepVars.sigmaVariables[i - 1][var]
                d_a_phi = SMTNumericVariable.fromPddl(eff.rhs, stepVars.sigmaVariables[i - 1])
                if eff.operator == "increase":
                    rules.append((a_n > 0).implies(v_a.equal(d_a_v + d_a_phi)))
                else:
                    rules.append((a_n > 0).implies(v_a.equal(d_a_v - d_a_phi)))
                rules.append((a_n.equal(0)).implies(v_a.equal(d_a_v)))

        return rules

    def getFrameStepRules(self, stepVars: NumericTransitionVariables) -> List[SMTExpression]:
        rules: List[SMTExpression] = []

        for v in self.domain.functions:
            v_first = stepVars.valueVariables[v]
            delta_g_v = stepVars.sigmaVariables[self.k][v]
            rules.append(v_first.equal(delta_g_v))

        for v in self.domain.predicates:
            v_first = stepVars.valueVariables[v]
            delta_g_v = stepVars.sigmaVariables[self.k][v]
            rules.append(v_first.equal(delta_g_v))

        return rules

    def getStepRules(self, index: int) -> List[SMTExpression]:
        prevVars = self.transitionVariables[index - 1]
        stepVars = self.transitionVariables[index]

        rules: List[SMTExpression] = []
        rules += self.getDeltaStepRules(prevVars, stepVars)
        rules += self.getAmoStepRules(stepVars, index)
        rules += self.getPreStepRules(stepVars)
        rules += self.getEffStepRules(stepVars)
        rules += self.getFrameStepRules(stepVars)

        return rules

    def getPlanFromSolution(self, solution: SMTSolution) -> NumericPlan:
        plan = NumericPlan()

        if not solution:
            return plan

        plan.actionRolling = dict()

        for n in range(1, self.bound + 1):
            plan.actionRolling.setdefault(n, dict())
            stepVar = self.transitionVariables[n]
            for i, a in self.pattern.enumerate():
                repetitions = int(str(solution.getVariable(stepVar.actionVariables[i]))) * a.linearizationTimes
                plan.actionRolling[n][a] = repetitions
                if repetitions > 0:
                    plan.addRepeatedAction(a.linearizationOf, repetitions)

        return plan
