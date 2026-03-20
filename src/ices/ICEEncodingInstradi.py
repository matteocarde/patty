from typing import List, Dict, Set, Tuple

from classes.instradi.Instradi import Instradi
from classes.instradi.station.Route import Route
from src.ices.Happening import HappeningActionStart, HappeningActionEnd, HappeningEffect, HappeningConditionStart, \
    HappeningConditionEnd, Happening
from src.ices.ICEAction import ICEAction
from src.ices.ICEActionStartEndPair import ICEActionStartEndPair
from src.ices.ICEConditionStartEndPair import ICEConditionStartEndPair
from src.ices.ICEPattern import ICEPattern
from src.ices.ICEPatternPrecedenceGraphInstradi import ICEPatternPrecedenceGraphInstradi
from src.ices.ICETask import ICETask
from src.ices.ICETransitionVariablesInstradi import ICETransitionVariablesInstradi
from src.ices.PlanIntermediateEffect import PlanIntermediateEffect
from src.ices.TimedConditions import TimedConditions
from src.ices.TimedEffects import TimedEffects
from src.pddl.Atom import Atom
from src.pddl.BinaryPredicate import BinaryPredicate
from src.pddl.Literal import Literal
from src.plan.Encoding import Encoding
from src.smt.SMTConjunction import SMTConjunction
from src.smt.SMTExpression import SMTExpression
from src.utils.TimeStat import TimeStat


class ICEEncodingInstradi(Encoding):
    task: ICETask
    pattern: ICEPattern
    ppg: ICEPatternPrecedenceGraphInstradi
    rulesBySet: Dict[str, List[SMTExpression]]
    rules: SMTConjunction
    actionsStartEndPairs: List[ICEActionStartEndPair]
    conditionsStartEndPairs: List[ICEConditionStartEndPair]

    def __init__(self, task: ICETask, pattern: ICEPattern, instradi: Instradi):
        super().__init__()
        self.task: ICETask = task
        self.pattern: ICEPattern = pattern
        self.instradi: Instradi = instradi
        t = TimeStat.startHolder("Getting actions start and end pairs ")
        self.actionsStartEndPairs = self.pattern.getActionsStartEndPairs(True)
        t.endHolder()
        t = TimeStat.startHolder("Getting condition start and end pairs ")
        self.conditionsStartEndPairs = self.pattern.getConditionsStartEndPairs(True)
        t.endHolder()
        t = TimeStat.startHolder("Getting ICE transition variables")
        self.transVars = ICETransitionVariablesInstradi(task, pattern)
        t.endHolder()
        t = TimeStat.startHolder("Computing Pattern Precedence Graph")
        self.ppg = ICEPatternPrecedenceGraphInstradi(pattern, self.transVars, instradi)
        t.endHolder()
        self.k = len(pattern) - 1
        self.rulesBySet = dict()

        t = TimeStat.startHolder("Getting touched atoms")
        self.touchedAtomsIndexes: Dict[Atom, List[int]] = self.pattern.getTouchedAtomsIndexes()
        t.endHolder()

        # self.ppg.printDot()
        # exit()

        t = TimeStat.startHolder("Getting placeholders bij")
        self.b_ij = dict()
        for pair in self.actionsStartEndPairs:
            self.b_ij[pair] = pair.getPlaceholderBij(self.transVars.happeningVariables, self.pattern)
        t.endHolder()

        # self.rulesBySet["init"] = self.__getInitialRules()
        # self.rulesBySet["frame"] = self.__getFrameRules()
        self.rulesBySet["domain"] = TimeStat.timeCall(self.__getDomainRules)
        self.rulesBySet["dur"] = TimeStat.timeCall(self.__getDurRules)
        self.rulesBySet["make-span"] = TimeStat.timeCall(self.__getMakeSpanRules)
        self.rulesBySet["precedence"] = TimeStat.timeCall(self.__getPrecedenceRules)
        self.rulesBySet["mutex"] = TimeStat.timeCall(self.__getMutexRules)
        self.rulesBySet["plan-intermediate"] = TimeStat.timeCall(self.__getPlanIntermediateRules)
        self.rulesBySet["start-end"] = TimeStat.timeCall(self.__getStartEndRules)
        self.rulesBySet["action-intermediate"] = TimeStat.timeCall(self.__getActionIntermediateRules)
        self.rulesBySet["conditions"] = TimeStat.timeCall(self.__getConditionsRules)
        self.rulesBySet["goal"] = TimeStat.timeCall(self.__getGoalRules)

        self.rules = SMTConjunction()
        for (key, rules) in self.rulesBySet.items():
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
                    rule = ~sigma[condition.getAtom()]
            else:
                raise NotImplemented("I cannot handle sub formulas in goal at the moment")

            rules.append(rule)

        return rules

    def __getDomainRules(self) -> SMTConjunction:
        rules: SMTConjunction = SMTConjunction()
        hVar = self.transVars.happeningVariables
        tVar = self.transVars.timeVariables

        used = set()

        for h in self.pattern:
            # h_i = hVar[h]
            # if h_i not in used:
            #     rules.append(h_i.equal(0) | h_i.equal(1))
            t_i = tVar[h]
            if t_i not in used:
                rules.append(t_i >= 0)
            # used.add(h_i)
            used.add(t_i)

        return rules

    def __getFrameRules(self) -> SMTConjunction:
        rules: SMTConjunction = SMTConjunction()

        for v in self.task.propVariables:
            rules.append(self.transVars.nextVariables[v] == self.transVars.sigmaExpressions[self.k][v])

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

            rules.append((~h_i).implies((t_i.equal(0))))
            # rules.append((h_i > 0).implies(d_i.equal(b.duration)))

        return rules

    def __getMakeSpanRules(self) -> SMTConjunction:
        rules: SMTConjunction = SMTConjunction()
        # tVars = self.transVars
        #
        # endingTimes = [tVars.timeVariables[h] for h in self.pattern if isinstance(h, HappeningActionEnd)]
        # M = self.transVars.makespan
        # rules.append(SMTExpression.bigand([M >= t_i for t_i in endingTimes]))
        # rules.append(SMTExpression.bigor([M.equal(t_i) for t_i in endingTimes]))

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

            rules.append((h_i & h_j).implies(t_j >= t_i + delta))

        return rules

    def __getPlanIntermediateRules(self) -> SMTConjunction:
        rules: SMTConjunction = SMTConjunction()
        hVars = self.transVars.happeningVariables
        tVars = self.transVars.timeVariables

        piEff = []
        piCondStart = []
        piCondEnd = []

        parentEffects: Dict[PlanIntermediateEffect, Set[HappeningEffect]] = dict()

        for h in self.pattern:
            if isinstance(h, HappeningEffect) and isinstance(h.parent, TimedEffects):
                piEff.append(h)
                parentEffects.setdefault(h.effect, set())
                parentEffects[h.effect].add(h)
            if isinstance(h, HappeningConditionStart) and isinstance(h.parent, TimedConditions):
                piCondStart.append(h)
            if isinstance(h, HappeningConditionEnd) and isinstance(h.parent, TimedConditions):
                piCondEnd.append(h)

        if piEff:
            # effAnd = SMTExpression.bigand([hVars[h] <= 1 for h in piEff])
            # 5.a
            for (parent, effs) in parentEffects.items():
                rules.append(SMTExpression.bigor([hVars[h] for h in effs]))

        # 5.b
        for h in piEff:
            h_i = hVars[h]
            t_i = tVars[h]
            M = self.transVars.makespan
            rules.append(h_i.implies(t_i.equal(h.effect.time.absolute(0, M))))

        # 5.c
        # if piCondStart:
        #     condStartSum = sum([hVars[h] for h in piCondStart]).equal(len(self.task.conditions))
        #     condEndSum = sum([hVars[h] for h in piCondEnd]).equal(len(self.task.conditions))
        #     condStartAnd = SMTExpression.bigand([hVars[h] <= 1 for h in piCondStart])
        #     condEndAnd = SMTExpression.bigand([hVars[h] <= 1 for h in piCondEnd])
        #     rules.append(SMTExpression.bigand([condStartSum, condEndSum, condStartAnd, condEndAnd]))
        #
        # # 5.d
        # for h in piCondStart:
        #     h_i = hVars[h]
        #     t_i = tVars[h]
        #     rules.append((h_i > 0).implies(t_i.equal(h.condition.fromTime.absolute(0, M))))
        #
        # for h in piCondEnd:
        #     h_j = hVars[h]
        #     t_j = tVars[h]
        #     rules.append((h_j > 0).implies(t_j.equal(h.condition.toTime.absolute(0, M))))

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

                orSubFormulas = [(h_j) & (t_j.equal(t_i + d_i)) for (h_j, t_j) in ending]
                rules.append((h_i).implies(SMTExpression.bigor(orSubFormulas)))

            # 6.b
            if isinstance(h, HappeningActionEnd):
                h_j = hVars[h]
                t_j = tVars[h]
                starting = [(hVars[ha_i], tVars[ha_i], dVars[ha_i])
                            for ha_i in self.pattern[:i]
                            if isinstance(ha_i, HappeningActionStart) and h.action == ha_i.action]
                orSubFormulas = [(h_i) & (t_j.equal(t_i + d_i)) for (h_i, t_i, d_i) in starting]
                rules.append((h_j).implies(SMTExpression.bigor(orSubFormulas)))

            # 6.c
            # if not isinstance(h, HappeningAction) and isinstance(h.parent, ICEAction):
            #     p = i
            #     h_p = hVars[h]
            #     startBeforeP: List[SMTExpression] = []
            #     endBeforeP: List[SMTExpression] = []
            #     startAfterP: List[SMTExpression] = []
            #     endAfterP: List[SMTExpression] = []
            #     for q, ha_q in enumerate(self.pattern):
            #         if not isinstance(ha_q, HappeningAction) or ha_q.action != h.parent:
            #             continue
            #         h_q = hVars[ha_q]
            #         if q < p and isinstance(ha_q, HappeningActionStart):
            #             startBeforeP.append(h_q)
            #         if q < p and isinstance(ha_q, HappeningActionEnd):
            #             endBeforeP.append(h_q)
            #         if q > p and isinstance(ha_q, HappeningActionStart):
            #             startAfterP.append(h_q)
            #         if q > p and isinstance(ha_q, HappeningActionEnd):
            #             endAfterP.append(h_q)
            #     # print(sum(startBeforeP) - sum(endBeforeP), sum(endAfterP) - sum(startAfterP))
            #     implicand = FalseExpression()
            #     if (sum(startBeforeP) - sum(endBeforeP) > 0) and (sum(endAfterP) - sum(startAfterP) > 0):
            #         implicand = (sum(startBeforeP) - sum(endBeforeP) > 0) & (sum(endAfterP) - sum(startAfterP) > 0)
            #     rules.append((h_p > 0).implies(implicand))

        return rules

    def __getActionIntermediateRules(self) -> SMTConjunction:
        rules: SMTConjunction = SMTConjunction()
        hVars = self.transVars.happeningVariables
        tVars = self.transVars.timeVariables

        # for pair in self.actionsStartEndPairs:
        #     b_ij: SMTExpression = self.b_ij[pair]
        #     h_i = hVars[pair.h_i]
        #     t_i = tVars[pair.h_i]
        #     t_j = tVars[pair.h_j]
        #     b = pair.action
        #
        #     ## 7.a
        #     ieffs: List[HappeningEffect] = [h_p for h_p in self.pattern[pair.i + 1:pair.j]
        #                                     if isinstance(h_p, HappeningEffect) and h_p.parent == pair.action]
        #
        #     effectsSum = sum([hVars[h_p] for h_p in ieffs]).equal(len(b.ieff))
        #     effectsAnd = SMTExpression.bigand([hVars[h_p] <= 1 for h_p in ieffs])
        #     rules.append(b_ij.implies(effectsSum & effectsAnd))
        #
        #     ## 7.b
        #     for ha_p in ieffs:
        #         h_p = hVars[ha_p]
        #         t_p = tVars[ha_p]
        #         rules.append((b_ij & (h_p > 0)).implies(t_p.equal(ha_p.effect.time.absolute(t_i, t_j))))
        #
        #     ## 7.c
        #     icondsStart = [h_p for h_p in self.pattern[pair.i:pair.j]
        #                    if isinstance(h_p, HappeningConditionStart) and h_p.parent == pair.action]
        #     icondsEnd = [h_p for h_p in self.pattern[pair.i:pair.j]
        #                  if isinstance(h_p, HappeningConditionEnd) and h_p.parent == pair.action]
        #
        #     condStartSum = sum([hVars[h_p] for h_p in icondsStart]).equal(len(b.icond))
        #     condEndSum = sum([hVars[h_p] for h_p in icondsEnd]).equal(len(b.icond))
        #     condAnd = SMTExpression.bigand([hVars[h_p] <= 1 for h_p in icondsStart + icondsEnd])
        #     rules.append(b_ij.implies(condStartSum & condEndSum & condAnd))
        #
        #     ## 7.d
        #     for ha_p in icondsStart + icondsEnd:
        #         h_p = hVars[ha_p]
        #         t_p = tVars[ha_p]
        #         if isinstance(ha_p, HappeningConditionStart):
        #             rules.append((b_ij & (h_p > 0)).implies(t_p.equal(ha_p.condition.fromTime.absolute(t_i, t_j))))
        #         if isinstance(ha_p, HappeningConditionEnd):
        #             rules.append((b_ij & (h_p > 0)).implies(t_p.equal(ha_p.condition.toTime.absolute(t_i, t_j))))

        return rules

    def __getMutexes(self) -> List[Tuple[Happening, Happening]]:
        mutexes = []
        for i, h_i in enumerate(self.pattern):
            for h_j in self.pattern[i + 1:]:

                if not (hasattr(h_i, "parent") and hasattr(h_j, "parent")):
                    continue

                if not isinstance(h_i.parent, ICEAction) or not isinstance(h_j.parent, ICEAction):
                    continue

                a_i: ICEAction = h_i.parent
                a_j: ICEAction = h_j.parent

                if a_i.originalName == a_j.originalName:
                    continue

                if type(a_i) == type(a_j):
                    continue

                if hasattr(a_i, "train") and hasattr(a_j, "train"):
                    t_i = a_i.train
                    t_j = a_j.train

                    if t_i != t_j:
                        continue

                    if hasattr(a_i, "route") and hasattr(a_j, "route"):
                        r_i: Route = a_i.route
                        r_j: Route = a_j.route

                        if r_i == r_j:
                            continue

                        if not self.instradi.stationGraph.areConnected(r_i, r_j):
                            # print("Is useless to constrain", h_i, h_j)
                            mutexes.append((h_i, h_j))

        return mutexes

    def __getMutexRules(self) -> SMTConjunction:
        rules: SMTConjunction = SMTConjunction()
        hVars = self.transVars.happeningVariables

        for happening_i, happening_j in self.ppg.useless:
            h_i = hVars[happening_i]
            h_j = hVars[happening_j]
            rules.append(~(h_i & h_j))

        return rules

    def __getConditionsRules(self) -> SMTConjunction:
        rules: SMTConjunction = SMTConjunction()
        hVars = self.transVars.happeningVariables
        sigma = self.transVars.sigmaExpressions

        for pair in self.conditionsStartEndPairs:
            # 8.a
            if pair.start.parent != pair.end.parent:
                continue

            h_i = hVars[pair.start]
            # h_j = hVars[pair.h_j]
            i = pair.startIndex
            j = pair.endIndex
            cond = pair.condition.conditions
            cond_i = SMTExpression.fromFormula(cond, sigma[i - 1])
            rule = (h_i).implies(cond_i)
            rules.append(rule)

            ps = set()
            for atom in cond.atoms:
                if atom not in self.touchedAtomsIndexes:
                    continue
                for p in self.touchedAtomsIndexes[atom]:
                    if i < p < j:
                        ps.add(p - 1)

            cond_p = SMTExpression.bigand([SMTExpression.fromFormula(cond, sigma[p]) for p in ps])

            rule = (h_i).implies(cond_p)
            rules.append(rule)

        return rules
