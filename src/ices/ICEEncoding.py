import itertools
from typing import List, Dict, Tuple, Set

from pysmt.shortcuts import TRUE, FALSE

from src.ices.Happening import HappeningActionStart, HappeningActionEnd, HappeningEffect, HappeningCondition, \
    HappeningConditionStart, HappeningConditionEnd, HappeningAction
from src.ices.ICEActionStartEndPair import ICEActionStartEndPair
from src.ices.ICEConditionStartEndPair import ICEConditionStartEndPair
from src.ices.ICEGoal import ICEGoal
from src.ices.ICEInitialCondition import ICEInitialCondition
from src.ices.ICEPattern import ICEPattern
from src.ices.ICEPatternPrecedenceGraph import ICEPatternPrecedenceGraph
from src.ices.ICETask import ICETask
from src.ices.ICETransitionVariables import ICETransitionVariables
from src.smt.SMTConjunction import SMTConjunction
from src.smt.SMTExpression import SMTExpression


class ICEEncoding:
    task: ICETask
    pattern: ICEPattern
    ppg: ICEPatternPrecedenceGraph
    rulesBySet: Dict[str, List[SMTExpression]]
    rules: SMTConjunction
    actionsStartEndPairs: List[ICEActionStartEndPair]
    conditionsStartEndPairs: List[ICEConditionStartEndPair]

    def __init__(self, task: ICETask, pattern: ICEPattern):
        self.task: ICETask = task
        self.pattern: ICEPattern = pattern
        self.actionsStartEndPairs = self.pattern.getActionsStartEndPairs()
        self.conditionsStartEndPairs = self.pattern.getConditionsStartEndPairs()
        self.transVars = ICETransitionVariables(task, pattern)
        self.ppg = ICEPatternPrecedenceGraph(pattern, self.transVars)
        self.k = len(pattern) - 1
        self.rulesBySet = dict()

        self.b_ij = dict()
        for pair in self.actionsStartEndPairs:
            self.b_ij[pair] = pair.getPlaceholderBij(self.transVars.happeningVariables, self.pattern)

        # self.rulesBySet["frame"] = self.__getFrameRules()
        self.rulesBySet["dur"] = self.__getDurRules()
        self.rulesBySet["make-span"] = self.__getMakeSpanRules()
        self.rulesBySet["precedence"] = self.__getPrecedenceRules()
        self.rulesBySet["plan-intermediate"] = self.__getPlanIntermediateRules()
        self.rulesBySet["start-end"] = self.__getStartEndRules()
        self.rulesBySet["action-intermediate"] = self.__getActionIntermediateRules()
        self.rulesBySet["conditions"] = self.__getConditionsRules()

        self.rules = SMTConjunction()
        for (key, rules) in self.rulesBySet.items():
            print(f"-----{key}-----")
            print("\n".join([str(r) for r in rules]))
            self.rules += rules

        pass

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
        tVars = self.transVars
        M = tVars.makespan

        planEffects = []
        planConditionsStarts = []
        planConditionsEnds = []

        for h in self.pattern:
            if isinstance(h, HappeningEffect) and isinstance(h.parent, ICEInitialCondition):
                planEffects.append(h)
            if isinstance(h, HappeningConditionStart) and isinstance(h.parent, ICEGoal):
                planConditionsStarts.append(h)
            if isinstance(h, HappeningConditionEnd) and isinstance(h.parent, ICEGoal):
                planConditionsEnds.append(h)

        # 5.a
        rules.append(sum([tVars.happeningVariables[h] for h in planEffects]) == 1)

        # 5.b
        for h in planEffects:
            h_i = tVars.happeningVariables[h]
            t_i = tVars.timeVariables[h]
            rules.append((h_i > 0).implies(t_i == h.effect.time.absolute(0, M)))

        # 5.c
        rules.append(sum([tVars.happeningVariables[h] for h in planConditionsStarts]) == 1)
        rules.append(sum([tVars.happeningVariables[h] for h in planConditionsEnds]) == 1)

        # 5.d
        for h in planConditionsStarts:
            h_i = tVars.happeningVariables[h]
            t_i = tVars.timeVariables[h]
            rules.append((h_i > 0).implies(t_i == h.condition.fromTime.absolute(0, M)))

        for h in planConditionsEnds:
            h_j = tVars.happeningVariables[h]
            t_j = tVars.timeVariables[h]
            rules.append((h_j > 0).implies(t_j == h.condition.toTime.absolute(0, M)))

        return rules

    def __getStartEndRules(self) -> SMTConjunction:
        rules: SMTConjunction = SMTConjunction()
        tVars = self.transVars

        for i, h in enumerate(self.pattern):
            if not isinstance(h, HappeningAction):
                continue

            # 6.a
            if isinstance(h, HappeningActionStart):
                h_i = tVars.happeningVariables[h]
                t_i = tVars.timeVariables[h]
                d_i = tVars.durVariables[h]

                ending = []
                for ha_j in self.pattern[i + 1:]:
                    if not isinstance(ha_j, HappeningActionEnd) or not h.action == ha_j.action:
                        continue
                    ending.append((tVars.happeningVariables[ha_j], tVars.timeVariables[ha_j]))

                orSubFormulas = [(h_j == h_i).AND(t_j == t_i + d_i) for (h_j, t_j) in ending]
                rules.append((h_i > 0).implies(SMTExpression.orOfExpressionsList(orSubFormulas)))

            # 6.b
            if isinstance(h, HappeningActionEnd):
                h_j = tVars.happeningVariables[h]
                t_j = tVars.timeVariables[h]
                starting = [(tVars.happeningVariables[ha_i], tVars.timeVariables[ha_i], tVars.durVariables[ha_i])
                            for ha_i in self.pattern[:i]
                            if isinstance(ha_i, HappeningActionStart) and h.action == ha_i.action]
                orSubFormulas = [(h_j == h_i).AND(t_j == t_i + d_i) for (h_i, t_i, d_i) in starting]
                rules.append((h_j > 0).implies(SMTExpression.orOfExpressionsList(orSubFormulas)))

        return rules

    def __getActionIntermediateRules(self) -> SMTConjunction:
        rules: SMTConjunction = SMTConjunction()
        hVars = self.transVars.happeningVariables
        tVars = self.transVars.timeVariables

        for pair in self.actionsStartEndPairs:
            b_ij: SMTExpression = self.b_ij[pair]
            t_i = tVars[pair.h_i]
            t_j = tVars[pair.h_j]

            ## 7.a
            ieffs: List[HappeningEffect] = [h_p for h_p in self.pattern[pair.i:pair.j]
                                            if isinstance(h_p, HappeningEffect) and h_p.parent == pair.action]
            rules.append(b_ij.implies(sum([hVars[h_p] for h_p in ieffs]) == 1))

            ## 7.b
            for ha_p in ieffs:
                h_p = hVars[ha_p]
                t_p = tVars[ha_p]
                rules.append(b_ij.AND(h_p > 0).implies(t_p == ha_p.effect.time.absolute(t_i, t_j)))

            ## 7.c
            iconds: List[HappeningCondition] = [h_p for h_p in self.pattern[pair.i:pair.j]
                                                if isinstance(h_p, HappeningCondition) and h_p.parent == pair.action]

            rules.append(b_ij.implies(sum([hVars[h_p] for h_p in iconds]) == 1))

            ## 7.d
            for ha_p in iconds:
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
            rules.append((h_i > 0).implies(cond_i))

            for p in range(i + 1, j):
                cond_p = SMTExpression.fromFormula(cond, sigma[p])
                rules.append(((h_i > 0).AND(h_j > 0)).implies(cond_p))

        return rules
