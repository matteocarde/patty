from typing import List, Dict, Set, Tuple

import pysmt.smtlib.commands as smtcmd
import pysmt.smtlib.script
from prettytable import PrettyTable
from pysmt.environment import get_env
from pysmt.logics import QF_NRA

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
from src.smt.SMTSolution import SMTSolution

# BOUND = 1000
EXPLICIT_DELTA = False


class TemporalEncoding(Encoding):
    domain: GroundedDomain
    problem: Problem
    rules: List[SMTExpression]

    def __init__(self, domain: GroundedDomain, problem: Problem, pattern: Pattern, bound: int, epsilon=0.001,
                 constraints: str = "numerical", relaxGoal=False,
                 subgoalsAchieved: Set[Formula] = None):

        super().__init__(domain, problem, pattern, bound)
        self.domain = domain
        self.problem = problem
        self.bound = bound
        self.pattern = pattern
        self.epsilon = epsilon
        self.constraints = constraints
        self.relaxGoal = relaxGoal
        self.subgoalsAchieved = subgoalsAchieved

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
        self.dur2start: Dict[DurativeAction, List[SnapAction]] = dict()
        self.dur2end: Dict[DurativeAction, List[SnapAction]] = dict()
        self.action2index: Dict[SnapAction, int] = dict()
        self.k = len(pattern) - 1
        self.computeHelpers()

        for index in range(1, bound + 1):
            stepRules = self.getStepRules(index)
            self.transitions.extend(stepRules)

        self.rules = self.initial + self.transitions + [self.goal]

    def computeHelpers(self):

        originalToSnap: Dict[str, List[SnapAction]] = dict()
        action: SnapAction
        for i, action in enumerate(self.pattern):
            if action.isFake:
                continue
            originalToSnap[action.originalName] = originalToSnap.setdefault(action.originalName, [])
            originalToSnap[action.originalName].append(action)

            if not isinstance(action, SnapAction):
                continue

            self.dur2start[action.durativeAction] = self.dur2start.setdefault(action.durativeAction, [])
            self.dur2end[action.durativeAction] = self.dur2end.setdefault(action.durativeAction, [])
            self.action2index[action] = i

            if action.timeType == TimePredicateType.AT_START:
                self.dur2start[action.durativeAction].append(action)
                self.start2end[action] = []
            if action.timeType == TimePredicateType.AT_END:
                self.dur2end[action.durativeAction].append(action)
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
            rules.append(SMTExpression.andOfExpressionsList(andRules))
        if orRules:
            rules.append(SMTExpression.orOfExpressionsList(orRules))

        return SMTExpression.andOfExpressionsList(rules)

    def getGoalExpression(self) -> SMTExpression:
        return self.getGoalRuleFromFormula(self.problem.goal, 0)

    def getMetricExpression(self, metricBound: float) -> SMTExpression or None:

        if self.problem.metric:
            return SMTExpression.fromPddl(self.problem.metric,
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

        action: SnapAction

        # First action in the order copies the value from previous step
        for v in self.domain.allAtoms:
            stepVars.sigmaVariables[-1][v] = prevVars.valueVariables[v]

        for i, action in enumerate(self.pattern):

            j = i - 1
            action_i: SnapAction = self.pattern[i]
            sigma_i = stepVars.sigmaVariables[i]
            sigma_j = stepVars.sigmaVariables[j]
            a_i = stepVars.actionVariables[i]
            # Case a) Not influenced
            notInfluenced = self.domain.allAtoms - (action_i.getInfluencedAtoms())
            for v in notInfluenced:
                stepVars.sigmaVariables[i][v] = stepVars.sigmaVariables[j][v]

            # Case b) Boolean
            for v in action_i.getAddList() | action_i.getDelList():
                if v in action_i.getAddList():
                    sigma_i[v] = sigma_j[v].OR(a_i > 0)
                if v in action_i.getDelList():
                    sigma_i[v] = sigma_j[v].AND(a_i == 0)

            # Case c) Numeric increases or decreases
            modifications = [(+1, action_i.getIncreases()), (-1, action_i.getDecreases())]
            for sign, modificationDict in modifications:
                for v, funct in modificationDict.items():

                    k = SMTExpression.fromPddl(funct, sigma_j)
                    if sign > 0:
                        sigma_i[v] = sigma_j[v] + (k * a_i)
                    else:
                        sigma_i[v] = sigma_j[v] - (k * a_i)
            # Case d) Numeric assignments
            for v in action_i.getAssList():
                sigma_i[v] = stepVars.auxVariables[i][v]

            for eff in action_i.effects:
                if not eff.isLinearIncrement():
                    continue
                v = eff.getAtom()
                sigma_i[v] = stepVars.auxVariables[i][v]

    def getPreStepRules(self, stepVars: TemporalTransitionVariables) -> List[SMTExpression]:
        rules: List[SMTExpression] = []

        for i, a in enumerate(self.pattern):
            if a.isFake:
                continue

            a_i = stepVars.actionVariables[i]
            sigma_j = stepVars.sigmaVariables[i - 1]

            # 1) Snap action
            andPreconditions: [SMTExpression] = []
            for p in a.preconditions:
                if isinstance(p, Literal):
                    v = p.getAtom()
                    if p.sign == "+":
                        andPreconditions.append(sigma_j[v])
                    else:
                        andPreconditions.append(sigma_j[v].NOT())
                elif isinstance(p, BinaryPredicate):
                    andPreconditions.append(SMTExpression.fromPddl(p, sigma_j))

            if andPreconditions:
                lhs: SMTExpression = a_i > 0
                rhs: SMTExpression = SMTExpression.andOfExpressionsList(andPreconditions)
                rules.append(lhs.implies(rhs))

            # 2) Start or end action
            if isinstance(a, SnapAction):
                start = a.durativeAction.start
                end = a.durativeAction.end
                if not a.durativeAction.couldBeRepeated():
                    continue

                for pre in a.preconditions:
                    if not isinstance(pre, BinaryPredicate):
                        continue

                    lhs: SMTExpression = a_i > 1
                    if a.timeType == TimePredicateType.AT_START:
                        rhs: SMTExpression = TemporalEncoding.getSigmaPsi(pre, sigma_j, a_i - 1, start, a_i - 1, end)
                    elif a.timeType == TimePredicateType.AT_END:
                        rhs: SMTExpression = TemporalEncoding.getSigmaPsi(pre, sigma_j, 0, start, a_i - 1, end)
                    else:
                        raise Exception("This should not happen")
                    rules.append(lhs.implies(rhs))
            else:
                for pre in a.preconditions:
                    if not isinstance(pre, BinaryPredicate):
                        continue
                    lhs: SMTExpression = a_i > 1
                    rhs: SMTExpression = TemporalEncoding.getSigmaPsi(pre, sigma_j, a_i - 1, a, 0, a)
                    rules.append(lhs.implies(rhs))

        # print("\n".join([str(rule) for rule in rules]))
        return rules

    def getEpsilonB(self, b: DurativeAction) -> float:
        return self.epsilon if b.start.isMutex(b.end) else 0.0

    @staticmethod
    def getSigmaPsi(psi: BinaryPredicate, sigmas: Dict[Atom, SMTExpression],
                    p: SMTExpression or float, start: SnapAction,
                    q: SMTExpression or float, end: SnapAction) -> SMTExpression:

        replacements: Dict[Atom, SMTExpression] = dict()

        groups = [(p, start), (q, end)]
        for (times, action) in groups:
            if not times:
                continue
            for eff in action.effects:
                if isinstance(eff, BinaryPredicate):
                    atom = eff.lhs.getAtom()
                    x = replacements[atom] if atom in replacements else sigmas[atom]
                    if eff.operator == "assign":
                        replacements[atom] = SMTExpression.fromPddl(eff.rhs, sigmas)
                    elif eff.operator == "increase" and times:
                        replacements[atom] = x + times * SMTExpression.fromPddl(eff.rhs, sigmas)
                    elif eff.operator == "decrease" and times:
                        replacements[atom] = x - times * SMTExpression.fromPddl(eff.rhs, sigmas)

        for (atom, expr) in sigmas.items():
            if atom not in replacements:
                replacements[atom] = expr

        return SMTExpression.fromPddl(psi, replacements)

    def getEffStepRules(self, stepVars: TemporalTransitionVariables) -> List[SMTExpression]:

        rules: List[SMTExpression] = []

        for i, a in enumerate(self.pattern):
            a_i = stepVars.actionVariables[i]
            for v, rhs in a.getAssignments().items():
                v_i = stepVars.auxVariables[i][v]
                sigma_j = stepVars.sigmaVariables[i - 1]

                rules.append((a_i > 0).implies(v_i == SMTExpression.fromPddl(rhs, sigma_j)))
                rules.append((a_i == 0).implies(v_i == sigma_j[v]))

        return rules

    def getAmoStepRules(self, stepVars: TemporalTransitionVariables) -> List[SMTExpression]:
        rules: List[SMTExpression] = []

        for i, a in enumerate(self.pattern):

            a_i = stepVars.actionVariables[i]
            if not a.couldBeRepeated():
                rules.append((a_i >= 0).AND(a_i <= 1))
            else:
                rules.append(a_i >= 0)

        return rules

    def getFrameStepRules(self, stepVars: TemporalTransitionVariables) -> List[SMTExpression]:
        rules: List[SMTExpression] = []

        functions = self.domain.functions if self.bound > 1 else self.problem.goal.getFunctions()
        predicates = self.domain.predicates if self.bound > 1 else self.problem.goal.getPredicates()

        for v in functions:
            v_first = stepVars.valueVariables[v]
            delta_g_v = stepVars.sigmaVariables[self.k][v]
            rules.append(v_first == delta_g_v)

        for v in predicates:
            v_first = stepVars.valueVariables[v]
            delta_g_v = stepVars.sigmaVariables[self.k][v]
            rules.append(delta_g_v.coimplies(v_first))

        return rules

    def getDurationRules(self, stepVars: TemporalTransitionVariables) -> List[SMTExpression]:

        rules: List[SMTExpression] = []

        for i, a in enumerate(self.pattern):
            if not isinstance(a, SnapAction):
                a_i = stepVars.actionVariables[i]
                t_i = stepVars.timeVariables[i]
                rules.append((a_i == 0).implies((t_i == 0)))
                continue
            if not isinstance(a.durativeAction.duration, Constant):
                raise Exception("I cannot handle durations which are not constants yet... but it is easy to add")
            D = a.durativeAction.duration.value

            if a.timeType == TimePredicateType.AT_START:
                a_i = stepVars.actionVariables[i]
                t_i = stepVars.timeVariables[i]
                d_i = stepVars.durVariables[i]
                e_b = self.getEpsilonB(a.durativeAction)
                rules.append((a_i == 0).implies((t_i == 0).AND(d_i == 0)))
                if a.durativeAction.couldBeRepeated():
                    rhs = (a_i * (D + e_b) <= d_i + e_b).AND(d_i + e_b <= a_i * (D + e_b))
                    rules.append((a_i > 0).implies(rhs))
                else:
                    rules.append((a_i > 0).implies(d_i == D))
            elif a.timeType == TimePredicateType.AT_END:
                a_j = stepVars.actionVariables[i]
                t_j = stepVars.timeVariables[i]
                rules.append((a_j == 0).implies(t_j == 0))

        return rules

    def getStartEndLogicalRules(self, stepVars: TemporalTransitionVariables) -> List[SMTExpression]:

        rules: List[SMTExpression] = []

        for action in self.pattern:
            if not isinstance(action, SnapAction):
                continue

            if action.timeType == TimePredicateType.AT_START:
                i = self.action2index[action]
                a_i = stepVars.actionVariables[i]
                t_i = stepVars.timeVariables[i]
                d_i = stepVars.durVariables[i]
                rhsList = []

                for end in self.start2end[action]:
                    j = self.action2index[end]
                    a_j = stepVars.actionVariables[j]
                    t_j = stepVars.timeVariables[j]

                    rhsList.append((a_i == a_j).AND(t_j == t_i + d_i))
                    pass

                lhs = a_i > 0
                rhs = SMTExpression.orOfExpressionsList(rhsList)
                rules.append(lhs.implies(rhs))
            elif action.timeType == TimePredicateType.AT_END:
                j = self.action2index[action]
                a_j = stepVars.actionVariables[j]
                t_j = stepVars.timeVariables[j]
                rhsList = []

                for start in self.end2start[action]:
                    i = self.action2index[start]
                    a_i = stepVars.actionVariables[i]
                    t_i = stepVars.timeVariables[i]
                    d_i = stepVars.durVariables[i]

                    rhsList.append((a_i == a_j).AND(t_j == t_i + d_i))
                    pass

                lhs = a_j > 0
                rhs = SMTExpression.orOfExpressionsList(rhsList)
                rules.append(lhs.implies(rhs))

        return rules

    def getStartEndNumericalRules(self, stepVars: TemporalTransitionVariables) -> List[SMTExpression]:

        rules: List[SMTExpression] = []

        for action in self.pattern:
            if not isinstance(action, SnapAction):
                continue

            if action.timeType == TimePredicateType.AT_START:
                i = self.action2index[action]
                a_i = stepVars.actionVariables[i]

                S_i = [self.action2index[a] for a in self.end2start[self.start2end[action][-1]] if
                       self.action2index[a] >= i]
                E_i = [self.action2index[a] for a in self.start2end[action]]

                # print(
                #     f"i: {self.pattern[i]}, S_i = {[self.pattern[j] for j in S_i]}, E_i = {[self.pattern[j] for j in E_i]}")

                sumActionS_i = sum([stepVars.actionVariables[j] for j in S_i])
                sumActionE_i = sum([stepVars.actionVariables[j] for j in E_i])
                sumTimeS_i = sum([stepVars.timeVariables[j] + stepVars.durVariables[j] for j in S_i])
                sumTimeE_i = sum([stepVars.timeVariables[j] for j in E_i])

                lhs = a_i > 0
                rhs = (sumActionS_i == sumActionE_i).AND(sumTimeS_i == sumTimeE_i)
                rules.append(lhs.implies(rhs))
                # print(lhs.implies(rhs))
            elif action.timeType == TimePredicateType.AT_END:
                j = self.action2index[action]
                a_j = stepVars.actionVariables[j]

                S_j = [self.action2index[a] for a in self.end2start[action]]
                E_j = [self.action2index[a] for a in self.start2end[self.end2start[action][0]] if
                       self.action2index[a] <= j]

                # print(f"j: {self.pattern[j]}, S_j = {[self.pattern[i] for i in S_j]}, E_j = {[self.pattern[i] for i in E_j]}")

                sumActionS_j = sum([stepVars.actionVariables[i] for i in S_j])
                sumActionE_j = sum([stepVars.actionVariables[i] for i in E_j])
                rules.append((a_j > 0).implies(sumActionS_j == sumActionE_j))
                # print((a_j > 0).implies(sumActionS_j == sumActionE_j))

        return rules

    def getEpsilonNoOverlappingRules(self, stepVars: TemporalTransitionVariables) -> List[SMTExpression]:

        rules: List[SMTExpression] = []

        for i, action_i in enumerate(self.pattern):
            a_i = stepVars.actionVariables[i]
            t_i = stepVars.timeVariables[i]

            M_i = set()
            F_i = set()
            B_i = set()
            for j in range(0, i):
                action_j = self.pattern[j]
                if action_j.isMutex(action_i):
                    M_i.add(j)
                if action_i.isSame(action_j):
                    if not isinstance(action_i, SnapAction) or action_i.timeType == TimePredicateType.AT_START:
                        B_i.add(j)
                    if isinstance(action_i, SnapAction) and action_i.timeType == TimePredicateType.AT_END \
                            and self.constraints == "logical":
                        F_i.add(j)

            # print(f"i={self.pattern[i]}, B_i = {[self.pattern[j] for j in B_i]}")

            lhs = a_i > 0
            rhsList = [t_i >= self.epsilon]
            for j in M_i | F_i:
                t_j = stepVars.timeVariables[j]
                rhsList.append(t_i >= t_j + self.epsilon)
            for j in B_i:
                t_j = stepVars.timeVariables[j]
                d_j = stepVars.durVariables[j] if j in stepVars.durVariables else 0.0
                rhsList.append(t_i >= t_j + d_j)
            rules.append(lhs.implies(SMTExpression.andOfExpressionsList(rhsList)))

        return rules

    def getLastingActionsRules(self, stepVars: TemporalTransitionVariables) -> List[SMTExpression]:
        rules: [SMTExpression] = []
        for b in self.domain.durativeActions:
            lasting = b.overall
            lastingPre = lasting.preconditions
            if not lastingPre:
                continue

            lastingAdd = set()
            lastingDel = set()
            for pre in lastingPre:
                if isinstance(pre, Literal):
                    if pre.sign == "+":
                        lastingAdd.add(pre.getAtom())
                    else:
                        lastingDel.add(pre.getAtom())

            start: SnapAction
            for action_i in self.dur2start[b]:
                i = self.action2index[action_i]
                # Preconditions
                a_i = stepVars.actionVariables[i]
                t_i = stepVars.timeVariables[i]
                d_i = stepVars.durVariables[i]
                sigma_i = stepVars.sigmaVariables[i]
                sigma_im1 = stepVars.sigmaVariables[i - 1]
                preStartRules = []
                preEndRules = []
                for pre in lastingPre:
                    if isinstance(pre, Literal):
                        atom = pre.getAtom()
                        preStartRules += [sigma_i[atom]] if pre.sign == "+" else [sigma_i[atom].NOT()]
                    if isinstance(pre, BinaryPredicate):
                        preStartRules.append(self.getSigmaPsi(pre, sigma_im1, 1, b.start, 0, b.end))
                        if b.couldBeRepeated():
                            preEndRules.append(self.getSigmaPsi(pre, sigma_im1, a_i, b.start, a_i - 1, b.end))
                if preStartRules:
                    rules.append((a_i > 0).implies(SMTExpression.andOfExpressionsList(preStartRules)))
                if preEndRules:
                    rules.append((a_i > 1).implies(SMTExpression.andOfExpressionsList(preEndRules)))

                mutexWithLasting = set()
                for j, action_j in enumerate(self.pattern):
                    if j != i and action_i.isMutex(action_j):
                        mutexWithLasting.add(j)

                for j in range(0, i):
                    action_j = self.pattern[j]
                    t_j = stepVars.timeVariables[j]

                    # Case i)
                    if j in mutexWithLasting:
                        rules.append((a_i > 0).implies(t_j <= t_i))

                    # Case ii)
                    if (not isinstance(action_j, SnapAction) or action_j.timeType == TimePredicateType.AT_START) \
                            and j in mutexWithLasting and action_j.couldBeRepeated():
                        a_j = stepVars.actionVariables[j]
                        d_j = stepVars.durVariables[j]
                        lhs = (a_i > 0).AND(a_j > 1)
                        rhs = t_j + d_j <= t_i
                        rules.append(lhs.implies(rhs))

                # Case iii)
                for j in range(i + 1, self.k):
                    action_j = self.pattern[j]
                    if j in mutexWithLasting:
                        a_j = stepVars.actionVariables[j]
                        t_j = stepVars.timeVariables[j]
                        sigma_j = stepVars.sigmaVariables[j]
                        interval = (t_i <= t_j).AND(t_j < t_i + d_i)
                        rhsList = []
                        for pre in lastingPre:
                            if isinstance(pre, Literal):
                                v = pre.getAtom()
                                rhsList += [sigma_j[v]] if pre.sign == "+" else [sigma_j[v].NOT()]
                            if isinstance(pre, BinaryPredicate):
                                rhsList += [SMTExpression.fromPddl(pre, sigma_j)]

                        if rhsList:
                            rules.append(interval.implies(SMTExpression.andOfExpressionsList(rhsList)))

                        if action_j.couldBeRepeated() or action_i.couldBeRepeated():
                            rhs = (a_i <= 1).AND(a_j <= 1)
                            rules.append(interval.implies(rhs))
                            print(interval.implies(rhs))

        return rules

    def getStepRules(self, index: int) -> List[SMTExpression]:
        prevVars = self.transitionVariables[index - 1]
        stepVars = self.transitionVariables[index]

        rulesDict = dict()
        self.computeSigmas(prevVars, stepVars)
        # Pattern State Encoding
        rulesDict["pre"] = self.getPreStepRules(stepVars)
        rulesDict["eff"] = self.getEffStepRules(stepVars)
        rulesDict["amo"] = self.getAmoStepRules(stepVars)
        rulesDict["frame"] = self.getFrameStepRules(stepVars)
        # Pattern Time Encoding
        rulesDict["dur"] = self.getDurationRules(stepVars)
        if self.constraints == "logical":
            rulesDict["start-end"] = self.getStartEndLogicalRules(stepVars)
        elif self.constraints == "numerical":
            rulesDict["start-end"] = self.getStartEndNumericalRules(stepVars)
        else:
            raise Exception("Constraint type not specified for temporal planning")
        rulesDict["overlap-epsilon"] = self.getEpsilonNoOverlappingRules(stepVars)
        rulesDict["lasting"] = self.getLastingActionsRules(stepVars)

        rules: List[SMTExpression] = []
        for dRules in rulesDict.values():
            rules += dRules

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
        plan = TemporalPlan(self.epsilon)

        if not solution:
            return plan

        stepVar = self.transitionVariables[1]

        x = PrettyTable()
        x.field_names = ["i", "Action", "a_i", "t_i", "d_i"]
        for i, action in enumerate(self.pattern):
            a_i = int(str(solution.getVariable(stepVar.actionVariables[i])))
            t_i = round(solution.getVariable(stepVar.timeVariables[i]), 3)
            d_i = round(solution.getVariable(stepVar.durVariables[i]), 3) if i in stepVar.durVariables else 0.0

            x.add_row([i, action, a_i, t_i, d_i])
        # print(x)

        started: Dict[DurativeAction, List[SnapAction]] = dict()
        pairs: List[Tuple[SnapAction, SnapAction]] = list()
        for i, action in enumerate(self.pattern):

            a_i = int(str(solution.getVariable(stepVar.actionVariables[i])))
            t_i = round(solution.getVariable(stepVar.timeVariables[i]), 3)

            if a_i == 0:
                continue

            if not isinstance(action, SnapAction):
                plan.addUnrolledTimedAction(action, t_i)
                for p in range(0, a_i):
                    plan.addAction(action, t_i, 0)
                    plan.addTimedAction(action, t_i)
                continue

            b = action.durativeAction
            if action.timeType == TimePredicateType.AT_START:
                started.setdefault(b, [])
                started[b].append(action)
            elif action.timeType == TimePredicateType.AT_END:
                if not b in started or not started[b]:
                    raise Exception(f"Action {b} ends without starting")
                pairs.append((started[b][0], action))
                started[b].pop(0)

        for start, end in pairs:
            i = self.action2index[start]
            j = self.action2index[end]

            b = start.durativeAction
            a_i = int(str(solution.getVariable(stepVar.actionVariables[i])))
            a_j = int(str(solution.getVariable(stepVar.actionVariables[j])))
            t_i = round(solution.getVariable(stepVar.timeVariables[i]), 3)
            t_j = round(solution.getVariable(stepVar.timeVariables[j]), 3)
            d_i = round(solution.getVariable(stepVar.durVariables[i]), 3)
            e_b = self.getEpsilonB(b)

            if a_i != a_j:
                raise Exception(f"Action {b} has different executions for start and end: a_i={a_i}, a_j={a_j}")

            # if round(t_j, 3) != round(t_i + d_i, 3):
            #     raise Exception(
            #         f"Action {b} has wrong timings t_j: {t_j}, t_i: {t_i}, d_i = {d_i} -> {t_j} != {t_i} + {d_i}")

            d = round(((d_i + e_b) / a_i) - e_b, 3)

            if isinstance(b.duration, Constant) and round(d, 3) != round(b.duration.value, 3):
                raise Exception(
                    f"Action {b} has a different duration than the one specified in the domain: {d}!={b.duration.value}")

            plan.addUnrolledTimedAction(start, t_i)
            plan.addUnrolledTimedAction(end, t_j)
            for p in range(0, a_i):
                t = round(t_i + p * (d + e_b), 3)
                plan.addAction(b, t, d)
                plan.addTimedAction(start, t)
                plan.addTimedAction(end, round(t + d, 3))

        return plan
