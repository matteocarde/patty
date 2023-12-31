from typing import List, Dict, Set, Tuple

import pysmt.smtlib.commands as smtcmd
import pysmt.smtlib.script
from pysmt.environment import get_env
from pysmt.logics import QF_NRA

from src.pddl.Action import Action
from src.pddl.Atom import Atom
from src.pddl.BinaryPredicate import BinaryPredicate
from src.pddl.Constant import Constant
from src.pddl.Domain import GroundedDomain
from src.pddl.DurativeAction import DurativeAction
from src.pddl.Formula import Formula
from src.pddl.Literal import Literal
from src.pddl.Problem import Problem
from src.pddl.SnapAction import SnapAction
from src.pddl.TemporalPlan import TemporalPlan
from src.pddl.TimePredicate import TimePredicateType
from src.plan.Encoding import Encoding
from src.plan.Pattern import Pattern
from src.plan.TemporalTransitionVariables import TemporalTransitionVariables
from src.smt.SMTExpression import SMTExpression
from src.smt.SMTNumericVariable import SMTNumericVariable
from src.smt.SMTSolution import SMTSolution
from src.smt.SMTVariable import SMTVariable

# BOUND = 1000
EXPLICIT_DELTA = False


class TemporalEncoding(Encoding):
    domain: GroundedDomain
    problem: Problem
    rules: List[SMTExpression]

    def __init__(self, domain: GroundedDomain, problem: Problem, pattern: Pattern, bound: int, epsilon=0.001):

        super().__init__(domain, problem, pattern, bound)
        self.domain = domain
        self.problem = problem
        self.bound = bound
        self.pattern = pattern
        self.epsilon = epsilon

        self.transitionVariables: [TemporalTransitionVariables] = list()

        self.transitions: [SMTExpression] = []

        for index in range(0, bound + 1):
            var = TemporalTransitionVariables(self.domain.predicates, self.domain.functions, self.domain.assList,
                                              self.pattern, index)
            self.transitionVariables.append(var)

        self.softRules = []
        self.initial: [SMTExpression] = self.getInitialExpression()
        self.goal: [SMTExpression] = self.getGoalExpression()

        self.start2end: Dict[SnapAction, List[SnapAction]] = dict()
        self.end2start: Dict[SnapAction, List[SnapAction]] = dict()
        self.computeHelpers()

        for index in range(1, bound + 1):
            stepRules = self.getStepRules(index)
            self.transitions.extend(stepRules)

        self.rules = self.initial + self.transitions + [self.goal]

    def computeHelpers(self):

        originalToSnap: Dict[str, List[SnapAction]] = dict()
        action: SnapAction
        for action in self.pattern:
            if action.isFake:
                continue
            originalToSnap[action.originalName] = originalToSnap.setdefault(action.originalName, [])
            originalToSnap[action.originalName].append(action)

            if action.timeType == TimePredicateType.AT_START:
                self.start2end[action] = []
            if action.timeType == TimePredicateType.AT_END:
                self.end2start[action] = self.end2start.setdefault(action, [])
                for start in originalToSnap[action.durativeAction.start.originalName]:
                    self.start2end[start].append(action)
                    self.end2start[action].append(start)

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
                rules.append(tVars.valueVariables[assignment.getAtom()])
                trueAtoms.add(assignment.getAtom())
            else:
                raise NotImplemented("Shouldn't go here")

        for v in self.domain.predicates - trueAtoms:
            rules.append(tVars.valueVariables[v].NOT())

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
                    rule = tVars.valueVariables[condition.getAtom()].NOT()
            elif isinstance(condition, Formula):
                rule = self.getGoalRuleFromFormula(condition, level + 1)
            else:
                raise NotImplemented("Shouldn't go here")

            # if level == 0 and self.relaxGoal:
            #     if condition in self.subgoalsAchieved:
            #         andRules.append(rule)
            #     else:
            #         self.softRules.append(rule)
            #         orRules.append(rule)
            # else:
            if f.type == "AND":
                andRules.append(rule)
            elif f.type == "OR":
                orRules.append(rule)

        rules = []
        if andRules:
            rules.append(SMTExpression.andOfExpressionsList(andRules))
        if orRules:
            rules.append(SMTExpression.orOfExpressionsList(orRules))

        return SMTExpression.andOfExpressionsList(rules)

    def getGoalExpression(self) -> SMTExpression:
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

    def computeSigmas(self, prevVars: TemporalTransitionVariables, stepVars: TemporalTransitionVariables):

        prevAction: Action or None = None
        for action in self.pattern:
            if not prevAction:
                # First action in the order copies the value from previous step
                for v in self.domain.allAtoms:
                    stepVars.sigmaVariables[action][v] = prevVars.valueVariables[v]
                prevAction = action
                continue

            # Case a) Not influenced
            notInfluenced = self.domain.allAtoms - (prevAction.getInfluencedAtoms())
            for v in notInfluenced:
                stepVars.sigmaVariables[action][v] = stepVars.sigmaVariables[prevAction][v]

            # Case b) Boolean
            for v in prevAction.getAddList() | prevAction.getDelList():
                d_bv = stepVars.sigmaVariables[prevAction][v]
                b_n = stepVars.actionVariables[prevAction]

                if v in prevAction.getAddList():
                    stepVars.sigmaVariables[action][v] = d_bv.OR(b_n > 0)

                if v in prevAction.getDelList():
                    stepVars.sigmaVariables[action][v] = d_bv.AND(b_n == 0)

            # Case c) Numeric increases or decreases
            modifications = [(+1, prevAction.getIncreases()), (-1, prevAction.getDecreases())]
            for sign, modificationDict in modifications:
                for v, funct in modificationDict.items():

                    d_bv = stepVars.sigmaVariables[prevAction][v]
                    k = SMTNumericVariable.fromPddl(funct, stepVars.sigmaVariables[prevAction])
                    b_n = stepVars.actionVariables[prevAction]
                    if sign > 0:
                        stepVars.sigmaVariables[action][v] = d_bv + (k * b_n)
                    else:
                        stepVars.sigmaVariables[action][v] = d_bv - (k * b_n)
            # Case d) Numeric assignments
            for v in prevAction.getAssList():
                stepVars.sigmaVariables[action][v] = stepVars.auxVariables[prevAction][v]

            for eff in prevAction.effects:
                if not eff.isLinearIncrement():
                    continue
                v = eff.getAtom()
                stepVars.sigmaVariables[action][v] = stepVars.auxVariables[prevAction][v]

            prevAction = action

    def getPreStepRules(self, stepVars: TemporalTransitionVariables) -> List[SMTExpression]:
        rules: List[SMTExpression] = []
        sigmas = stepVars.sigmaVariables

        for a in self.pattern:
            if a.isFake:
                continue

            aVar: SMTVariable = stepVars.actionVariables[a]

            # 1) Snap action
            andPreconditions: [SMTExpression] = []
            for p in a.preconditions:
                if isinstance(p, Literal):
                    v = p.getAtom()
                    if p.sign == "+":
                        andPreconditions.append(stepVars.sigmaVariables[a][v])
                    else:
                        andPreconditions.append(stepVars.sigmaVariables[a][v].NOT())
                elif isinstance(p, BinaryPredicate):
                    andPreconditions.append(SMTNumericVariable.fromPddl(p, stepVars.sigmaVariables[a]))

            if andPreconditions:
                lhs: SMTExpression = aVar > 0
                rhs: SMTExpression = SMTNumericVariable.andOfExpressionsList(andPreconditions)
                rules.append(lhs.implies(rhs))

            # 2) Start or end action
            if not isinstance(a, SnapAction) or a.timeType == TimePredicateType.OVER_ALL:
                continue

            start = a.durativeAction.start
            end = a.durativeAction.end

            for pre in a.preconditions:
                if not isinstance(pre, BinaryPredicate):
                    continue

                lhs: SMTExpression = stepVars.actionVariables[a] > 1
                if a.timeType == TimePredicateType.AT_START:
                    rhs: SMTExpression = TemporalEncoding.getSigmaPsi(pre, sigmas[a], aVar - 1, start, aVar - 1, end)
                elif a.timeType == TimePredicateType.AT_END:
                    rhs: SMTExpression = TemporalEncoding.getSigmaPsi(pre, sigmas[a], 0, start, aVar - 1, end)
                else:
                    raise Exception("This should not happen")
                rules.append(lhs.implies(rhs))

        return rules

    @staticmethod
    def getSigmaPsi(psi: BinaryPredicate, sigmas: Dict[Atom, SMTExpression],
                    p: SMTExpression or float, start: SnapAction,
                    q: SMTExpression or float, end: SnapAction) -> SMTExpression:

        replacements: Dict[Atom, SMTExpression] = dict()

        groups = [(p, start), (q, end)]
        for (times, action) in groups:
            for eff in action.effects:
                if isinstance(eff, BinaryPredicate):
                    atom = eff.lhs.getAtom()
                    if atom in replacements:
                        raise Exception(f"{atom} is already replaced in psi")
                    if eff.operator == "assign":
                        replacements[atom] = SMTExpression.fromPddl(eff.rhs, sigmas)
                    elif eff.operator == "increase":
                        replacements[atom] = sigmas[atom] + times * SMTExpression.fromPddl(eff.rhs, sigmas)
                    elif eff.operator == "decrease":
                        replacements[atom] = sigmas[atom] - times * SMTExpression.fromPddl(eff.rhs, sigmas)

        for (atom, expr) in sigmas.items():
            if atom not in replacements:
                replacements[atom] = expr

        return SMTNumericVariable.fromPddl(psi, replacements)

    def getEffStepRules(self, stepVars: TemporalTransitionVariables) -> List[SMTExpression]:

        rules: List[SMTExpression] = []

        for a in self.pattern:
            if a.isFake:
                continue
            actionVar = stepVars.actionVariables[a]
            for var, rhs in a.getAssignments().items():
                v_a = stepVars.auxVariables[a][var]
                sigmaVar = stepVars.sigmaVariables[a][var]
                if not isinstance(rhs, Constant):
                    raise Exception("I cannot handle yet linear assignments")
                k = rhs.value
                rules.append((actionVar > 0).implies(v_a == k))
                rules.append((actionVar == 0).implies(v_a == sigmaVar))

        return rules

    def getAmoStepRules(self, stepVars: TemporalTransitionVariables) -> List[SMTExpression]:
        rules: List[SMTExpression] = []

        for a in self.pattern:
            if a.isFake:
                continue
            a_n = stepVars.actionVariables[a]
            rules.append(a_n >= 0)
            if not a.couldBeRepeated():
                rules.append(a_n <= 1)

        # if len(self.domain.arpg.stateLevels) > 2:
        #     for (atom, interval) in self.domain.arpg.stateLevels[-1].intervals.items():
        #         if atom not in stepVars.valueVariables:
        #             continue
        #         if interval.lb != float("-inf"):
        #             rules.append(stepVars.valueVariables[atom] >= interval.lb)
        #         if interval.ub != float("+inf"):
        #             rules.append(stepVars.valueVariables[atom] <= interval.ub)

        return rules

    def getFrameStepRules(self, stepVars: TemporalTransitionVariables) -> List[SMTExpression]:
        rules: List[SMTExpression] = []

        functions = self.domain.functions if self.bound > 1 else self.problem.goal.getFunctions()
        predicates = self.domain.predicates if self.bound > 1 else self.problem.goal.getPredicates()

        for v in functions:
            v_first = stepVars.valueVariables[v]
            delta_g_v = stepVars.sigmaVariables[self.pattern.dummyAction][v]
            rules.append(v_first == delta_g_v)

        for v in predicates:
            v_first = stepVars.valueVariables[v]
            delta_g_v = stepVars.sigmaVariables[self.pattern.dummyAction][v]
            rules.append(delta_g_v.coimplies(v_first))

        return rules

    def getDurationRules(self, stepVars: TemporalTransitionVariables) -> List[SMTExpression]:

        rules: List[SMTExpression] = []

        for a in self.pattern:
            if not isinstance(a, SnapAction) or a.timeType != TimePredicateType.AT_START:
                continue
            if not isinstance(a.durativeAction.duration, Constant):
                raise Exception("I cannot handle durations which are not constants yet... but it is easy to add")
            dur = a.durativeAction.duration.value
            rules.append(stepVars.durVariables[a] == dur)

        return rules

    def getDelta(self, a_i: SMTVariable or float, d_i: SMTVariable or float, b: DurativeAction) -> SMTExpression:
        if b.areStartAndEndInMutex():
            return a_i * d_i + (a_i - 1) * self.epsilon
        else:
            return a_i * d_i

    def getStartConnectionRules(self, stepVars: TemporalTransitionVariables) -> List[SMTExpression]:

        rules: List[SMTExpression] = []

        for start in self.pattern:
            if not isinstance(start, SnapAction) or start.timeType != TimePredicateType.AT_START:
                continue
            a_i = stepVars.actionVariables[start]
            t_i = stepVars.timeVariables[start]
            d_i = stepVars.durVariables[start]
            b = start.durativeAction
            rhsList = []

            for end in self.start2end[start]:
                a_j = stepVars.actionVariables[end]
                t_j = stepVars.timeVariables[end]

                rhsList.append((a_i == a_j).AND(t_j == t_i + self.getDelta(a_i, d_i, b)))

            lhs = a_i > 0
            rhs = SMTExpression.orOfExpressionsList(rhsList)
            rules.append(lhs.implies(rhs))

        return rules

    def getEndConnectionRules(self, stepVars: TemporalTransitionVariables) -> List[SMTExpression]:

        rules: List[SMTExpression] = []

        for end in self.pattern:
            if not isinstance(end, SnapAction) or end.timeType != TimePredicateType.AT_END:
                continue
            a_i = stepVars.actionVariables[end]
            t_i = stepVars.timeVariables[end]
            b = end.durativeAction
            rhsList = []

            for start in self.end2start[end]:
                a_j = stepVars.actionVariables[start]
                t_j = stepVars.timeVariables[start]
                d_j = stepVars.durVariables[start]

                # rhsList.append((a_i == a_j).AND(t_i == t_j + self.getDelta(a_j, d_j, b)))
                rhsList.append((a_i == a_j))

            lhs = a_i > 0
            rhs = SMTExpression.orOfExpressionsList(rhsList)
            rules.append(lhs.implies(rhs))

        return rules

    def getNoOverlappingRules(self, stepVars: TemporalTransitionVariables) -> List[SMTExpression]:

        rules: List[SMTExpression] = []

        isOk = lambda a: isinstance(a, SnapAction) and a.timeType in {TimePredicateType.AT_START,
                                                                      TimePredicateType.AT_END}
        startPairs: List[Tuple[SnapAction, SnapAction]] = []
        endPairs: List[Tuple[SnapAction, SnapAction]] = []
        action_i: SnapAction
        action_j: SnapAction

        action: SnapAction
        for action in self.pattern:
            if action.isFake:
                continue
            if action.timeType == TimePredicateType.AT_START:
                for end in self.start2end[action]:
                    startPairs.append((action, end))

            if action.timeType == TimePredicateType.AT_END:
                for start in self.end2start[action]:
                    startPairs.append((start, action))

        for (action_i, action_j) in startPairs:
            a_i = stepVars.actionVariables[action_i]
            a_j = stepVars.actionVariables[action_j]
            t_i = stepVars.timeVariables[action_i]
            t_j = stepVars.timeVariables[action_j]
            d_i = stepVars.durVariables[action_i]
            b = action_i.durativeAction

            lhs = (a_i > 0).AND(a_j > 0)
            rhs = (t_j >= t_i + self.getDelta(a_i, d_i, b))
            rules.append(lhs.implies(rhs))

        for (action_i, action_j) in endPairs:
            a_i = stepVars.actionVariables[action_i]
            a_j = stepVars.actionVariables[action_j]
            t_i = stepVars.timeVariables[action_i]
            t_j = stepVars.timeVariables[action_j]

            lhs = (a_i > 0).AND(a_j > 0)
            rhs = (t_j > t_i)
            rules.append(lhs.implies(rhs))

        return rules

    def getEpsilonSeparationRules(self, stepVars: TemporalTransitionVariables) -> List[SMTExpression]:

        rules: List[SMTExpression] = []

        action_i: SnapAction
        action_j: SnapAction
        for j, action_j in enumerate(self.pattern):
            if action_j.isFake:
                continue
            a_j = stepVars.actionVariables[action_j]
            t_j = stepVars.timeVariables[action_j]
            rules.append((a_j == 0).implies(t_j == 0))
            mutexes = [t_j >= self.epsilon]
            for i, action_i in enumerate(self.pattern):
                if i < j:
                    t_i = stepVars.timeVariables[action_i]
                    epsilon = self.epsilon if action_i.isMutex(action_j) else 0
                    mutexes.append(t_j >= t_i + self.epsilon)

            rules.append((a_j > 0).implies(SMTExpression.andOfExpressionsList(mutexes)))

        return rules

    def getLastingActionsRules(self, stepVars: TemporalTransitionVariables) -> List[SMTExpression]:

        k = len(self.pattern)
        rules: List[SMTExpression] = []
        pairs: List[Tuple[SnapAction, SnapAction]] = []

        action_i: SnapAction
        action_j: SnapAction
        for action_i in self.pattern[:-1]:
            if action_i.timeType != TimePredicateType.AT_START:
                continue
            for action_j in self.start2end[action_i]:
                pairs.append((action_i, action_j))

        for (action_i, action_j) in pairs:

            a_i = stepVars.actionVariables[action_i]
            t_i = stepVars.timeVariables[action_i]
            t_j = stepVars.timeVariables[action_j]
            d_i = stepVars.durVariables[action_i]
            b = action_i.durativeAction
            sigma_i = stepVars.sigmaVariables[action_i]

            preAnd = []
            lasting = action_i.durativeAction.overall
            if not lasting:
                continue
            for pre in lasting.preconditions:
                if isinstance(pre, Literal):
                    v = pre.getAtom()
                    if pre.sign == "+":
                        preAnd.append(sigma_i[v])
                    elif pre.sign == "-":
                        preAnd.append(sigma_i[v].NOT())
                if isinstance(pre, BinaryPredicate):
                    preAnd.append(self.getSigmaPsi(pre, sigma_i, 1, action_i, 0, action_j))

            if preAnd:
                rules.append((a_i > 0).implies(SMTExpression.andOfExpressionsList(preAnd)))

            isMutex = lambda l: self.pattern[l].isMutex(action_i) \
                                or self.pattern[l].isMutex(action_j) \
                                or self.pattern[l].isMutex(lasting)

            i = self.pattern.index(action_i)
            L_i = [self.pattern[l] for l in range(i + 1, k) if isMutex(l)]
            print(f"{action_i.durativeAction} is in mutex with {L_i}")

            times = []
            for action_l in L_i:
                t_l = stepVars.timeVariables[action_l]
                times.append((t_l < t_i).OR(t_l >= t_j))

            lhs1 = (t_j == t_i + self.getDelta(a_i, d_i, b)).AND(SMTExpression.andOfExpressionsList(times))

            preLasting = []
            for pre in lasting.preconditions:
                if not isinstance(pre, BinaryPredicate):
                    continue
                preLasting.append(self.getSigmaPsi(pre, sigma_i, a_i, action_i, a_i - 1, action_j))

            if preLasting:
                rhs1 = SMTExpression.andOfExpressionsList(preLasting)
                rules.append(lhs1.implies(rhs1))

            for action_l in L_i:
                t_l = stepVars.timeVariables[action_l]
                sigma_l = stepVars.sigmaVariables[action_l]
                lhs2 = SMTExpression.andOfExpressionsList(
                    [t_j == t_i + self.getDelta(a_i, d_i, b), t_l >= t_i, t_l < t_j])
                rhs2And = [a_i <= 1]
                for pre in lasting.preconditions:
                    if isinstance(pre, Literal):
                        v = pre.getAtom()
                        if pre.sign == "+":
                            rhs2And.append(sigma_l[v])
                        else:
                            rhs2And.append(sigma_l[v].NOT())
                    if isinstance(pre, BinaryPredicate):
                        rhs2And.append(SMTExpression.fromPddl(pre, sigma_l))
                rule2 = lhs2.implies(SMTExpression.andOfExpressionsList(rhs2And))
                rules.append(rule2)

        return rules

    def getStepRules(self, index: int) -> List[SMTExpression]:
        prevVars = self.transitionVariables[index - 1]
        stepVars = self.transitionVariables[index]

        rules: List[SMTExpression] = []
        self.computeSigmas(prevVars, stepVars)
        # Pattern State Encoding
        # rules += self.getPreStepRules(stepVars)
        rules += self.getEffStepRules(stepVars)
        rules += self.getAmoStepRules(stepVars)
        rules += self.getFrameStepRules(stepVars)
        # Pattern Time Encoding
        rules += self.getDurationRules(stepVars)
        rules += self.getStartConnectionRules(stepVars)
        rules += self.getEndConnectionRules(stepVars)
        rules += self.getNoOverlappingRules(stepVars)
        rules += self.getEpsilonSeparationRules(stepVars)
        rules += self.getLastingActionsRules(stepVars)

        return rules

    def printRules(self):
        for rule in self.rules:
            print(rule)

    def writeSMTLIB(self, filename: str):
        formula = SMTExpression.andOfExpressionsList(self.rules).expression
        with open(filename, "w") as fout:
            script = pysmt.smtlib.script.SmtLibScript()

            script.add(name=smtcmd.SET_LOGIC,
                       args=[QF_NRA])

            # Declare all types
            types = get_env().typeso.get_types(formula, custom_only=True)
            for type_ in types:
                script.add(name=smtcmd.DECLARE_SORT, args=[type_.decl])

            deps = formula.get_free_variables()
            # Declare all variables
            for symbol in deps:
                assert symbol.is_symbol()
                script.add(name=smtcmd.DECLARE_FUN, args=[symbol])

            for r in self.rules:
                # Assert formula
                script.add_command(pysmt.smtlib.script.SmtLibCommand(name=smtcmd.ASSERT,
                                                                     args=[r.expression]))
            # check-sat
            script.add_command(pysmt.smtlib.script.SmtLibCommand(name=smtcmd.CHECK_SAT,
                                                                 args=[]))
            script.serialize(fout, daggify=False)

    def getPlanFromSolution(self, solution: SMTSolution) -> TemporalPlan:
        plan = TemporalPlan()

        if not solution:
            return plan

        for i in range(1, self.bound + 1):
            stepVar = self.transitionVariables[i]
            for a in self.pattern:
                if a.isFake or not isinstance(a, SnapAction) or a.timeType != TimePredicateType.AT_START:
                    continue

                b = a.durativeAction
                repetitions = int(str(solution.getVariable(stepVar.actionVariables[a])))
                time = solution.getVariable(stepVar.timeVariables[a])
                duration = solution.getVariable(stepVar.durVariables[a])

                for i in range(0, repetitions):
                    t = time + self.getDelta(i, duration, b)
                    plan.addAction(b, t, duration)

        return plan
