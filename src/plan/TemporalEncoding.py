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

                    k = SMTNumericVariable.fromPddl(funct, sigma_j)
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

            if not isinstance(a, SnapAction) or a.timeType == TimePredicateType.OVER_ALL:
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
                    andPreconditions.append(SMTNumericVariable.fromPddl(p, sigma_j))

            if andPreconditions:
                lhs: SMTExpression = a_i > 0
                rhs: SMTExpression = SMTNumericVariable.andOfExpressionsList(andPreconditions)
                rules.append(lhs.implies(rhs))

            # 2) Start or end action

            start = a.durativeAction.start
            end = a.durativeAction.end

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

        # print("\n".join([str(rule) for rule in rules]))
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
                    elif eff.operator == "increase" and times:
                        replacements[atom] = sigmas[atom] + times * SMTExpression.fromPddl(eff.rhs, sigmas)
                    elif eff.operator == "decrease" and times:
                        replacements[atom] = sigmas[atom] - times * SMTExpression.fromPddl(eff.rhs, sigmas)
                    elif not times:
                        replacements[atom] = sigmas[atom]

        for (atom, expr) in sigmas.items():
            if atom not in replacements:
                replacements[atom] = expr

        return SMTNumericVariable.fromPddl(psi, replacements)

    def getEffStepRules(self, stepVars: TemporalTransitionVariables) -> List[SMTExpression]:

        rules: List[SMTExpression] = []

        for i, a in enumerate(self.pattern):
            if a.isFake:
                continue
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
            rules.append(a_i >= 0)
            if not a.couldBeRepeated():
                rules.append(a_i <= 1)

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
            if not isinstance(a, SnapAction) or a.timeType != TimePredicateType.AT_START:
                continue
            if not isinstance(a.durativeAction.duration, Constant):
                raise Exception("I cannot handle durations which are not constants yet... but it is easy to add")
            dur = a.durativeAction.duration.value
            rules.append(stepVars.durVariables[i] == dur)

        return rules

    def getDelta(self, a_i: SMTVariable or float, d_i: SMTVariable or float, b: DurativeAction) -> SMTExpression:
        if b.areStartAndEndInMutex():
            return a_i * d_i + (a_i - 1) * self.epsilon
        else:
            return a_i * d_i

    def getStartConnectionRules(self, stepVars: TemporalTransitionVariables) -> List[SMTExpression]:

        rules: List[SMTExpression] = []

        for i, start in enumerate(self.pattern):
            if not isinstance(start, SnapAction) or start.timeType != TimePredicateType.AT_START:
                continue
            a_i = stepVars.actionVariables[i]
            t_i = stepVars.timeVariables[i]
            d_i = stepVars.durVariables[i]
            b = start.durativeAction
            rhsList = []

            for end in self.start2end[start]:
                j = self.action2index[end]
                a_j = stepVars.actionVariables[j]
                t_j = stepVars.timeVariables[j]

                rhsList.append((a_i == a_j).AND(t_j == t_i + self.getDelta(a_i, d_i, b)))

            lhs = a_i > 0
            rhs = SMTExpression.orOfExpressionsList(rhsList)
            rules.append(lhs.implies(rhs))

        return rules

    def getEndConnectionRules(self, stepVars: TemporalTransitionVariables) -> List[SMTExpression]:

        rules: List[SMTExpression] = []

        for i, end in enumerate(self.pattern):
            if not isinstance(end, SnapAction) or end.timeType != TimePredicateType.AT_END:
                continue
            a_i = stepVars.actionVariables[i]
            t_i = stepVars.timeVariables[i]
            b = end.durativeAction
            rhsList = []

            for start in self.end2start[end]:
                j = self.action2index[start]
                a_j = stepVars.actionVariables[j]
                t_j = stepVars.timeVariables[j]
                d_j = stepVars.durVariables[j]

                rhsList.append((a_i == a_j).AND(t_i == t_j + self.getDelta(a_j, d_j, b)))

            lhs = a_i > 0
            rhs = SMTExpression.orOfExpressionsList(rhsList)
            rules.append(lhs.implies(rhs))

        return rules

    def getNoOverlappingRules(self, stepVars: TemporalTransitionVariables) -> List[SMTExpression]:

        rules: List[SMTExpression] = []

        # Pairs (start, start) and (end,end)

        dAction: DurativeAction
        for dAction in self.domain.durativeActions:
            startPairs = [(self.action2index[ai], self.action2index[aj]) for i, ai in enumerate(self.dur2start[dAction])
                          for j, aj in enumerate(self.dur2start[dAction]) if i < j]
            endPairs = [(self.action2index[ai], self.action2index[aj]) for i, ai in enumerate(self.dur2end[dAction])
                        for j, aj in enumerate(self.dur2start[dAction]) if i < j]
            for i, j in startPairs:
                a_i = stepVars.actionVariables[i]
                a_j = stepVars.actionVariables[j]
                t_i = stepVars.timeVariables[i]
                t_j = stepVars.timeVariables[j]
                d_i = stepVars.durVariables[i]
                b = self.pattern[i].durativeAction

                lhs = (a_i > 0).AND(a_j > 0)
                rhs = (t_j >= t_i + self.getDelta(a_i, d_i, b))
                rules.append(lhs.implies(rhs))

            for i, j in endPairs:
                a_i = stepVars.actionVariables[i]
                a_j = stepVars.actionVariables[j]
                t_i = stepVars.timeVariables[i]
                t_j = stepVars.timeVariables[j]

                lhs = (a_i > 0).AND(a_j > 0)
                rhs = (t_j > t_i)
                rules.append(lhs.implies(rhs))

        return rules

    def getEpsilonSeparationRules(self, stepVars: TemporalTransitionVariables) -> List[SMTExpression]:

        rules: List[SMTExpression] = []

        action_i: SnapAction
        action_j: SnapAction
        for i, action_i in enumerate(self.pattern):
            if action_i.isFake:
                continue
            a_i = stepVars.actionVariables[i]
            t_i = stepVars.timeVariables[i]
            rules.append((a_i == 0).implies(t_i == 0))
            mutexes = [t_i >= self.epsilon]
            for j in range(0, i):
                action_j = self.pattern[j]
                if not action_i.isMutex(action_j):
                    continue
                t_j = stepVars.timeVariables[j]
                mutexes.append(t_i >= t_j + self.epsilon)

            rules.append((a_i > 0).implies(SMTExpression.andOfExpressionsList(mutexes)))

        return rules

    def getLastingActionsRules(self, stepVars: TemporalTransitionVariables) -> List[SMTExpression]:
        rules: [SMTExpression] = []
        for b in self.domain.durativeActions:
            lastingPre = b.overall.preconditions
            if not lastingPre:
                continue

            start: SnapAction
            for start in self.dur2start[b]:
                i = self.action2index[start]
                # 1) Rolling
                a_i = stepVars.actionVariables[i]
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
                        preEndRules.append(self.getSigmaPsi(pre, sigma_im1, a_i, b.start, a_i - 1, b.end))
                if preStartRules:
                    rules.append((a_i > 0).implies(SMTExpression.andOfExpressionsList(preStartRules)))
                if preEndRules:
                    rules.append((a_i > 0).implies(SMTExpression.andOfExpressionsList(preEndRules)))

            # 2) Rolling end
            spanFrom = self.action2index[self.dur2start[b][0]]
            spanTo = self.action2index[self.dur2end[b][-1]]
            mutexWithAll: List[int] = list()
            mutexWithLasting: Set[int] = set()
            for l in range(spanFrom + 1, spanTo):
                action_l = self.pattern[l]
                if action_l.isMutex(b.overall):
                    mutexWithAll.append(l)
                    mutexWithLasting.add(l)
                    continue
                if action_l.isMutex(b.start) or action_l.isMutex(b.end):
                    mutexWithAll.append(l)

            action_i: SnapAction
            action_j: SnapAction
            action_l: SnapAction
            for action_i in self.dur2start[b]:
                i = self.action2index[action_i]
                a_i = stepVars.actionVariables[i]
                t_i = stepVars.timeVariables[i]
                d_i = stepVars.durVariables[i]
                for action_j in self.start2end[action_i]:
                    j = self.action2index[action_j]
                    t_j = stepVars.timeVariables[j]
                    for l in mutexWithAll:
                        if not i <= l <= j:
                            continue
                        action_l = self.pattern[l]
                        if action_i.isSame(action_l):
                            continue
                        a_l = stepVars.actionVariables[l]
                        t_l = stepVars.timeVariables[l]
                        lhs = (t_j == t_i + self.getDelta(a_i, d_i, b)).AND(t_i <= t_l).AND(t_l < t_j)
                        rhs = (a_i <= 1).AND(a_l <= 1)
                        rules.append(lhs.implies(rhs))
                        if l in mutexWithLasting:
                            sigma_l = stepVars.sigmaVariables[l]
                            rhs = SMTExpression.fromFormula(lastingPre, sigma_l)
                            rule = lhs.implies(rhs)
                            rules.append(rule)

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
        rulesDict["start"] = self.getStartConnectionRules(stepVars)
        rulesDict["end"] = self.getEndConnectionRules(stepVars)
        rulesDict["overlap"] = self.getNoOverlappingRules(stepVars)
        rulesDict["epsilon"] = self.getEpsilonSeparationRules(stepVars)
        rulesDict["lasting"] = self.getLastingActionsRules(stepVars)

        # for rule in rulesDict["lasting"]:
        #     print(rule)

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
        plan = TemporalPlan()

        if not solution:
            return plan

        for i in range(1, self.bound + 1):
            stepVar = self.transitionVariables[i]
            for i, a in enumerate(self.pattern):
                if a.isFake or not isinstance(a, SnapAction) or a.timeType != TimePredicateType.AT_START:
                    continue

                b = a.durativeAction
                repetitions = int(str(solution.getVariable(stepVar.actionVariables[i])))
                time = solution.getVariable(stepVar.timeVariables[i])
                duration = solution.getVariable(stepVar.durVariables[i])

                for i in range(0, repetitions):
                    t = time + self.getDelta(i, duration, b)
                    plan.addAction(b, t, duration)

        return plan
