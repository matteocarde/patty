from typing import List, Dict, Set
import time

from src.ices.Happening import HappeningActionStart, HappeningActionEnd, HappeningEffect, HappeningConditionStart, \
    HappeningConditionEnd, HappeningAction
from src.ices.ICEAction import ICEAction
from src.ices.ICEActionStartEndPair import ICEActionStartEndPair
from src.ices.ICEConditionStartEndPair import ICEConditionStartEndPair
from src.ices.TimedConditions import TimedConditions
from src.ices.TimedEffects import TimedEffects
from src.ices.ICEPattern import ICEPattern
from src.ices.ICEPatternPrecedenceGraph import ICEPatternPrecedenceGraph
from src.ices.ICETask import ICETask
from src.ices.ICETransitionVariables import ICETransitionVariables
from src.pddl.Atom import Atom
from src.pddl.BinaryPredicate import BinaryPredicate
from src.pddl.Formula import Formula
from src.pddl.Literal import Literal
from src.plan.Encoding import Encoding
from src.smt.SMTConjunction import SMTConjunction
from src.smt.SMTExpression import SMTExpression
from src.utils.TimeStat import TimeStat


class ICEEncoding(Encoding):
    task: ICETask
    pattern: ICEPattern
    ppg: ICEPatternPrecedenceGraph
    rulesBySet: Dict[str, List[SMTExpression]]
    rules: SMTConjunction
    actionsStartEndPairs: List[ICEActionStartEndPair]
    conditionsStartEndPairs: List[ICEConditionStartEndPair]

    def __init__(self, task: ICETask, pattern: ICEPattern):
        super().__init__()
        self.task: ICETask = task
        self.pattern: ICEPattern = pattern
        self.actionsStartEndPairs = self.pattern.getActionsStartEndPairs()
        self.conditionsStartEndPairs = self.pattern.getConditionsStartEndPairs()
        self.transVars = ICETransitionVariables(task, pattern)
        self.ppg = ICEPatternPrecedenceGraph(pattern, self.transVars)
        self.k = len(pattern) - 1
        self.rulesBySet = dict()

        # self.ppg.printDot()
        # exit()

        self.b_ij = dict()
        for pair in self.actionsStartEndPairs:
            self.b_ij[pair] = pair.getPlaceholderBij(self.transVars.happeningVariables, self.pattern)

        # self.rulesBySet["init"] = self.__getInitialRules()
        # self.rulesBySet["frame"] = self.__getFrameRules()
        self.rulesBySet["domain"] = TimeStat.timeCall(self.__getDomainRules)
        self.rulesBySet["dur"] = TimeStat.timeCall(self.__getDurRules)
        self.rulesBySet["make-span"] = TimeStat.timeCall(self.__getMakeSpanRules)
        self.rulesBySet["precedence"] = TimeStat.timeCall(self.__getPrecedenceRules)
        self.rulesBySet["plan-intermediate"] = TimeStat.timeCall(self.__getPlanIntermediateRules)
        self.rulesBySet["start-end"] = TimeStat.timeCall(self.__getStartEndRules)
        self.rulesBySet["action-intermediate"] = TimeStat.timeCall(self.__getActionIntermediateRules)
        self.rulesBySet["conditions"] = TimeStat.timeCall(self.__getConditionsRules)
        self.rulesBySet["goal"] = TimeStat.timeCall(self.__getGoalRules)

        print("INIT", self.task.init)
        print("GOAL", self.task.goal)
        # print(self.task.effects)

        self.rules = SMTConjunction()
        for (key, rules) in self.rulesBySet.items():
            print(f"{key}: {len(rules)}")
            # print(f"-----{key}-----")
            # print("\n".join([str(r) for r in rules]))
            self.rules += rules

    def __len__(self):
        return len(self.rules)

    def __getGoalRules(self) -> SMTConjunction:
        tVars = self.transVars
        rules = SMTConjunction()
        sigma = tVars.sigmaExpressions[self.k]

        if self.task.goal.type == "OR":
            raise Exception("I cannot and OR goals at the moment")

        for condition in self.task.goal.conditions:
            if isinstance(condition, BinaryPredicate):
                rule = SMTExpression.fromPddl(condition, sigma)
            elif isinstance(condition, Literal):
                if condition.sign == "+":
                    rule = sigma[condition.getAtom()]
                else:
                    rule = sigma[condition.getAtom()].NOT()
            else:
                raise NotImplemented("I cannot handle sub formulas in goal at the moment")

            rules.append(rule)

        return rules

    def __getDomainRules(self) -> SMTConjunction:
        rules: SMTConjunction = SMTConjunction()
        hVar = self.transVars.happeningVariables
        tVar = self.transVars.timeVariables

        for h in self.pattern:
            h_i = hVar[h]
            t_i = tVar[h]
            rules.append(h_i >= 0)
            rules.append(h_i <= 1)
            rules.append(t_i >= 0)

        return rules

    def __getFrameRules(self) -> SMTConjunction:
        rules: SMTConjunction = SMTConjunction()

        for v in self.task.propVariables:
            rules.append(self.transVars.nextVariables[v].iff(self.transVars.sigmaExpressions[self.k][v]))

        for x in self.task.numVariables:
            rules.append(self.transVars.nextVariables[x] == self.transVars.sigmaExpressions[self.k][x])

        return rules

    def __getDurRules(self) -> SMTConjunction:
        rules: SMTConjunction = SMTConjunction()
        tVars = self.transVars

        for i, h in enumerate(self.pattern):
            if not isinstance(h, HappeningActionStart):
                continue
            b = h.action
            h_i = tVars.happeningVariables[h]
            d_i = tVars.durVariables[h]
            t_i = tVars.timeVariables[h]

            rules.append((h_i == 0).implies((d_i == 0).AND(t_i == 0)))
            rules.append((h_i > 0).implies(d_i == b.duration))

        return rules

    def __getMakeSpanRules(self) -> SMTConjunction:
        rules: SMTConjunction = SMTConjunction()
        tVars = self.transVars

        endingTimes = [tVars.timeVariables[h] for h in self.pattern if isinstance(h, HappeningActionEnd)]
        M = self.transVars.makespan
        rules.append(SMTExpression.andOfExpressionsList([M >= t_i for t_i in endingTimes]))
        rules.append(SMTExpression.orOfExpressionsList([M == t_i for t_i in endingTimes]))

        return rules

    def __getPrecedenceRules(self) -> SMTConjunction:
        rules: SMTConjunction = SMTConjunction()
        hVars = self.transVars.happeningVariables
        tVars = self.transVars.timeVariables

        for ((happening_i, happening_j), delta) in self.ppg.delta.items():
            h_i = hVars[happening_i]
            h_j = hVars[happening_j]
            t_i = tVars[happening_i]
            t_j = tVars[happening_j]
            rules.append(((h_i > 0).AND(h_j > 0)).implies(t_j >= t_i + delta))

        return rules

    def __getPlanIntermediateRules(self) -> SMTConjunction:
        rules: SMTConjunction = SMTConjunction()
        hVars = self.transVars.happeningVariables
        tVars = self.transVars.timeVariables
        M = self.transVars.makespan

        piEff = []
        piCondStart = []
        piCondEnd = []

        for h in self.pattern:
            if isinstance(h, HappeningEffect) and isinstance(h.parent, TimedEffects):
                piEff.append(h)
            if isinstance(h, HappeningConditionStart) and isinstance(h.parent, TimedConditions):
                piCondStart.append(h)
            if isinstance(h, HappeningConditionEnd) and isinstance(h.parent, TimedConditions):
                piCondEnd.append(h)

        if piEff:
            effSum = sum([hVars[h] for h in piEff]) == len(self.task.effects)
            effAnd = SMTExpression.andOfExpressionsList([hVars[h] <= 1 for h in piEff])
            # 5.a
            rules.append(effSum.AND(effAnd))

        # 5.b
        for h in piEff:
            h_i = hVars[h]
            t_i = tVars[h]
            rules.append((h_i > 0).implies(t_i == h.effect.time.absolute(0, M)))

        # 5.c
        if piCondStart:
            condStartSum = sum([hVars[h] for h in piCondStart]) == len(self.task.conditions)
            condEndSum = sum([hVars[h] for h in piCondEnd]) == len(self.task.conditions)
            condStartAnd = SMTExpression.andOfExpressionsList([hVars[h] <= 1 for h in piCondStart])
            condEndAnd = SMTExpression.andOfExpressionsList([hVars[h] <= 1 for h in piCondEnd])
            rules.append(condStartSum.AND(condEndSum).AND(condStartAnd).AND(condEndAnd))

        # 5.d
        for h in piCondStart:
            h_i = hVars[h]
            t_i = tVars[h]
            rules.append((h_i > 0).implies(t_i == h.condition.fromTime.absolute(0, M)))

        for h in piCondEnd:
            h_j = hVars[h]
            t_j = tVars[h]
            rules.append((h_j > 0).implies(t_j == h.condition.toTime.absolute(0, M)))

        return rules

    def __getStartEndRules(self) -> SMTConjunction:
        rules: SMTConjunction = SMTConjunction()
        hVars = self.transVars.happeningVariables
        tVars = self.transVars.timeVariables
        dVars = self.transVars.durVariables

        for i, h in enumerate(self.pattern):

            # 6.a
            if isinstance(h, HappeningActionStart):
                h_i = hVars[h]
                t_i = tVars[h]
                d_i = dVars[h]

                ending = []
                for ha_j in self.pattern[i + 1:]:
                    if not isinstance(ha_j, HappeningActionEnd) or not h.action == ha_j.action:
                        continue
                    ending.append((hVars[ha_j], tVars[ha_j]))

                orSubFormulas = [(h_j == h_i).AND(t_j == t_i + d_i) for (h_j, t_j) in ending]
                rules.append((h_i > 0).implies(SMTExpression.orOfExpressionsList(orSubFormulas)))

            # 6.b
            if isinstance(h, HappeningActionEnd):
                h_j = hVars[h]
                t_j = tVars[h]
                starting = [(hVars[ha_i], tVars[ha_i], dVars[ha_i])
                            for ha_i in self.pattern[:i]
                            if isinstance(ha_i, HappeningActionStart) and h.action == ha_i.action]
                orSubFormulas = [(h_j == h_i).AND(t_j == t_i + d_i) for (h_i, t_i, d_i) in starting]
                rules.append((h_j > 0).implies(SMTExpression.orOfExpressionsList(orSubFormulas)))

            # 6.c
            if not isinstance(h, HappeningAction) and isinstance(h.parent, ICEAction):
                p = i
                h_p = hVars[h]
                startBeforeP = []
                endBeforeP = []
                startAfterP = []
                endAfterP = []
                for q, ha_q in enumerate(self.pattern):
                    if not isinstance(ha_q, HappeningAction) or ha_q.action != h.parent:
                        continue
                    h_q = hVars[ha_q]
                    if q < p and isinstance(ha_q, HappeningActionStart):
                        startBeforeP.append(h_q)
                    if q < p and isinstance(ha_q, HappeningActionEnd):
                        endBeforeP.append(h_q)
                    if q > p and isinstance(ha_q, HappeningActionStart):
                        startAfterP.append(h_q)
                    if q > p and isinstance(ha_q, HappeningActionEnd):
                        endAfterP.append(h_q)

                rules.append((h_p > 0)
                             .implies((sum(startBeforeP) - sum(endBeforeP) > 0)
                                      .AND(sum(endAfterP) - sum(startAfterP) > 0)))

        return rules

    def __getActionIntermediateRules(self) -> SMTConjunction:
        rules: SMTConjunction = SMTConjunction()
        hVars = self.transVars.happeningVariables
        tVars = self.transVars.timeVariables

        for pair in self.actionsStartEndPairs:
            b_ij: SMTExpression = self.b_ij[pair]
            h_i = hVars[pair.h_i]
            t_i = tVars[pair.h_i]
            t_j = tVars[pair.h_j]
            b = pair.action

            ## 7.a
            ieffs: List[HappeningEffect] = [h_p for h_p in self.pattern[pair.i + 1:pair.j]
                                            if isinstance(h_p, HappeningEffect) and h_p.parent == pair.action]

            effectsSum = sum([hVars[h_p] for h_p in ieffs]) == len(b.ieff)
            effectsAnd = SMTExpression.andOfExpressionsList([hVars[h_p] <= 1 for h_p in ieffs])
            rules.append(b_ij.implies(effectsSum.AND(effectsAnd)))

            ## 7.b
            for ha_p in ieffs:
                h_p = hVars[ha_p]
                t_p = tVars[ha_p]
                rules.append((b_ij.AND(h_p > 0)).implies(t_p == ha_p.effect.time.absolute(t_i, t_j)))

            ## 7.c
            icondsStart = [h_p for h_p in self.pattern[pair.i:pair.j]
                           if isinstance(h_p, HappeningConditionStart) and h_p.parent == pair.action]
            icondsEnd = [h_p for h_p in self.pattern[pair.i:pair.j]
                         if isinstance(h_p, HappeningConditionEnd) and h_p.parent == pair.action]

            condStartSum = sum([hVars[h_p] for h_p in icondsStart]) == len(b.icond)
            condEndSum = sum([hVars[h_p] for h_p in icondsEnd]) == len(b.icond)
            condAnd = SMTExpression.andOfExpressionsList([hVars[h_p] <= 1 for h_p in icondsStart + icondsEnd])
            rules.append(b_ij.implies(condStartSum.AND(condEndSum).AND(condAnd)))

            ## 7.d
            for ha_p in icondsStart + icondsEnd:
                h_p = hVars[ha_p]
                t_p = tVars[ha_p]
                if isinstance(ha_p, HappeningConditionStart):
                    rules.append(b_ij.AND(h_p > 0).implies(t_p == ha_p.condition.fromTime.absolute(t_i, t_j)))
                if isinstance(ha_p, HappeningConditionEnd):
                    rules.append(b_ij.AND(h_p > 0).implies(t_p == ha_p.condition.toTime.absolute(t_i, t_j)))

        return rules

    def __getConditionsRules(self) -> SMTConjunction:
        rules: SMTConjunction = SMTConjunction()
        hVars = self.transVars.happeningVariables
        sigma = self.transVars.sigmaExpressions

        for pair in self.conditionsStartEndPairs:
            # 8.a
            h_i = hVars[pair.h_i]
            h_j = hVars[pair.h_j]
            i = pair.i
            j = pair.j
            cond = pair.condition.conditions
            cond_i = SMTExpression.fromFormula(cond, sigma[i])
            # print((h_i > 0), sigma[i])
            rules.append((h_i > 0).implies(cond_i))

            conditions: Dict[str, SMTExpression] = dict()
            for p in range(i + 1, j):
                f = SMTExpression.fromFormula(cond, sigma[p])
                conditions[str(f)] = f
            cond_p = SMTExpression.andOfExpressionsList(list(conditions.values()))
            rules.append(((h_i > 0).AND(h_j > 0)).implies(cond_p))

        return rules
