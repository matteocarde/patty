from typing import List, Dict, Set, Tuple

from classes.instradi.Instradi import Instradi
from classes.instradi.Train import Train
from classes.planning.actions.InstradiAction import InstradiAction
from src.ices.Happening import HappeningEffect, HappeningCondition, Happening
from src.ices.ICEAction import ICEAction
from src.ices.ICEActionStartEndPair import ICEActionStartEndPair
from src.ices.ICEPattern import ICEPattern
from src.ices.ICETask import ICETask
from src.ices.ICETransitionVariables import ICETransitionVariables
from src.ices.IntermediateCondition import IntermediateCondition
from src.ices.PlanIntermediateCondition import PlanIntermediateCondition
from src.ices.PlanIntermediateEffect import PlanIntermediateEffect
from src.ices.RelativeTime import RelativeTime
from src.pddl.Atom import Atom
from src.pddl.BinaryPredicate import BinaryPredicate
from src.pddl.Formula import Formula
from src.pddl.Predicate import Predicate
from src.pddl.State import State
from src.plan.Encoding import Encoding
from src.smt.SMTComment import SMTComment
from src.smt.SMTConjunction import SMTConjunction
from src.smt.SMTExpression import SMTExpression
from src.smt.SMTVariable import SMTVariable
from src.utils.Constants import EPSILON
from src.utils.TimeStat import TimeStat


class ICEEncodingInstradi(Encoding):
    task: ICETask
    pattern: ICEPattern
    instradi: Instradi

    rulesBySet: Dict[str, List[SMTExpression]]
    rules: SMTConjunction
    actionsStartEndPairs: List[ICEActionStartEndPair]

    def __init__(self, task: ICETask, pattern: ICEPattern, instradi: Instradi,
                 subgoalsAchieved: Set[Formula or Predicate] = None,
                 unrepeatableActions=False):
        super().__init__()
        self.task: ICETask = task
        self.pattern: ICEPattern = pattern
        self.instradi = instradi
        self.subgoalsAchieved: Set[
            Formula or Predicate] = subgoalsAchieved if subgoalsAchieved is not None else set(self.task.goal.conditions)
        self.unrepeatableActions = unrepeatableActions

        t = TimeStat.startHolder("Getting actions start and end pairs ")
        self.actionsStartEndPairs = self.pattern.getActionsStartEndPairs(unrepeatableActions)
        t.endHolder()
        t = TimeStat.startHolder("Getting ICE transition variables")
        self.transVars = ICETransitionVariables(task, pattern, unrepeatableActions)
        t.endHolder()

        self.k = len(pattern)
        self.softRules: [SMTExpression] = []
        self.rulesBySet = dict()

        self.__computeHelpers()

        self.rulesBySet["init"] = TimeStat.timeCall(self.__getInitRules)
        self.rulesBySet["goal"] = TimeStat.timeCall(self.__getGoalRules)

        self.rulesBySet["domain"] = TimeStat.timeCall(self.__getDomainRules)
        self.rulesBySet["frame"] = self.__getFrameRules()
        self.rulesBySet["plan-intermediate-causal"] = TimeStat.timeCall(self.__getPlanIntermediateCausalRules)
        self.rulesBySet["action-intermediate-causal"] = TimeStat.timeCall(self.__getActionIntermediateCausalRules)
        self.rulesBySet["amo"] = TimeStat.timeCall(self.__getAMORules)
        self.rulesBySet["conditions"] = TimeStat.timeCall(self.__getConditionsRules)
        self.rulesBySet["dur"] = TimeStat.timeCall(self.__getDurRules)
        self.rulesBySet["plan-intermediate-temporal"] = TimeStat.timeCall(self.__getPlanIntermediateTemporalRules)
        self.rulesBySet["action-intermediate-temporal"] = TimeStat.timeCall(self.__getActionIntermediateTemporalRules)
        self.rulesBySet["epsilon-separation"] = TimeStat.timeCall(self.__getEpsilonSeparationRules)
        self.rulesBySet["no-overlap"] = TimeStat.timeCall(self.__getNoOverlapRules)

        self.rules = SMTConjunction()
        for (key, rules) in self.rulesBySet.items():
            rules.insert(0, SMTComment(key))
            self.rules += rules

    def __len__(self):
        return len(self.rules)

    def __computeHelpers(self):

        t = TimeStat.startHolder("Getting touched atoms")
        self.touchedAtomsIndexes: Dict[Atom, Set[int]] = self.pattern.getTouchedAtomsIndexes()
        t.endHolder()

        self.parents: Dict[ICEAction, Set[Happening]] = dict()
        self.originals: Dict[ICEAction, Set[Happening]] = dict()

        for h in self.pattern:
            self.parents.setdefault(h.parent, set())
            self.parents[h.parent].add(h)

            self.originals.setdefault(h.original, set())
            self.originals[h.original].add(h)

    def __getInitRules(self) -> SMTConjunction:
        tVars = self.transVars
        rules = SMTConjunction()
        current = tVars.currentVariables

        s = State.fromInitialCondition(self.task.init)
        rules.append(SMTExpression.fromState(s, current))

        return rules

    def __getGoalRules(self) -> SMTConjunction:
        tVars = self.transVars
        rules = SMTConjunction()
        next = tVars.nextVariables

        for goal in self.subgoalsAchieved:
            rules.append(SMTExpression.fromFormula(goal, next))

        orGoals = []
        for g in self.task.goal:
            if g in self.subgoalsAchieved:
                continue
            gf = SMTExpression.fromFormula(g, next)
            orGoals.append(gf)
            self.softRules.append(gf)

        if orGoals:
            rules.append(SMTExpression.bigor(orGoals))

        return rules

    def __getDomainRules(self) -> SMTConjunction:
        rules: SMTConjunction = SMTConjunction()
        hVar = self.transVars.happeningVariables
        tVar = self.transVars.timeVariables
        tEndVar = self.transVars.timeEndVariables
        dVar = self.transVars.durVariables

        for h in self.pattern:
            h_i = hVar[h]
            t_i = tVar[h]
            rules.append(h_i >= 0)
            rules.append(t_i >= 0)

            if h.starting:
                d_i = dVar[h]
                rules.append(d_i >= 0)

            if isinstance(h, HappeningCondition):
                t_i_end = tEndVar[h]
                rules.append(t_i_end >= 0)

        return rules

    def __getFrameRules(self) -> SMTConjunction:
        rules: SMTConjunction = SMTConjunction()

        for v in self.task.propVariables:
            rules.append(self.transVars.nextVariables[v].equal(self.transVars.sigmaExpressions[self.k][v]))

        for x in self.task.numVariables:
            rules.append(self.transVars.nextVariables[x].equal(self.transVars.sigmaExpressions[self.k][x]))

        return rules

    def __getPlanIntermediateCausalRules(self) -> SMTConjunction:
        rules: SMTConjunction = SMTConjunction()
        hVars = self.transVars.happeningVariables

        piEff: List[SMTVariable] = []
        piCond: List[SMTVariable] = []

        for h in self.pattern:
            if isinstance(h, HappeningEffect) and isinstance(h.parent, PlanIntermediateEffect):
                piEff.append(hVars[h])
            if isinstance(h, HappeningCondition) and isinstance(h.parent, PlanIntermediateCondition):
                piCond.append(hVars[h])

        for h_i in piCond:
            rules.append(h_i <= 1)

        for h_i in piEff:
            rules.append(h_i <= 1)

        if piCond:
            rules.append(sum(piCond).equal(len(self.task.conditions)))

        if piEff:
            rules.append(sum(piEff).equal(len(self.task.effects)))

        return rules

    def __getActionIntermediateCausalRules(self) -> SMTConjunction:
        rules: SMTConjunction = SMTConjunction()
        hVars = self.transVars.happeningVariables

        t = TimeStat.startHolder("__getActionIntermediateCausalRules 1)")

        for b in self.task.actions:

            parents = self.parents[b]

            if b.isSnap:
                continue

            for a in parents:

                h_i = hVars[a]
                andRules = []
                for b in parents:
                    orRules = []
                    for c in self.originals[b.original]:
                        h_j = hVars[c]
                        orRules.append(h_i.equal(h_j))
                    andRules.append(SMTExpression.bigor(orRules))
                rules.append(SMTExpression.bigand(andRules))
        t.endHolder()

        t = TimeStat.startHolder("__getActionIntermediateCausalRules 2)")
        for pair in self.actionsStartEndPairs:
            b = pair.action
            h_p = hVars[pair.start]
            h_q = hVars[pair.end]
            p = pair.startIndex
            q = pair.endIndex

            if b.isSnap:
                continue

            starting = []
            ices = []
            nOfICES = len(b.icond) + len(b.ieff)

            for h in self.pattern[p:q + 1]:
                if h.starting == b:
                    starting.append(hVars[h])
                if h.parent == b:
                    ices.append(hVars[h])

            rules.append(
                (h_p.equal(h_q)).implies(
                    (sum(starting) * nOfICES).equal(sum(ices))
                )
            )
        t.endHolder()

        t = TimeStat.startHolder("__getActionIntermediateCausalRules 3)")
        for i, h_a in enumerate(self.pattern):
            h_i = hVars[h_a]
            bigor = []
            if h_a.starting:
                for j, h_b in enumerate(self.pattern[i + 1:]):
                    if h_b.ending != h_a.starting:
                        continue
                    h_j = hVars[h_b]
                    bigor.append(h_j.equal(h_i))
                    if self.unrepeatableActions:
                        break

            if h_a.ending:
                for j, h_b in enumerate(self.pattern[:i]):
                    if h_b.starting != h_a.ending:
                        continue
                    h_j = hVars[h_b]
                    bigor.append(h_j.equal(h_i))
                    if self.unrepeatableActions:
                        break

            if bigor:
                rules.append((h_i > 0).implies(SMTExpression.bigor(bigor)))
        t.endHolder()

        return rules

    def __getAMORules(self) -> SMTConjunction:
        rules: SMTConjunction = SMTConjunction()
        hVars = self.transVars.happeningVariables

        for h in self.pattern:
            h_i = hVars[h]
            if isinstance(h.starting, ICEAction) and (
                    not h.starting.isEligibleForRolling() or not h.starting.isWellOrderable()):
                rules.append(h_i <= 1)

        return rules

    def __getConditionsRules(self) -> SMTConjunction:
        rules: SMTConjunction = SMTConjunction()
        hVars = self.transVars.happeningVariables
        sigma = self.transVars.sigmaExpressions

        for j, h in enumerate(self.pattern):
            i = j + 1
            h_i = hVars[h]
            sigma_im1 = sigma[i - 1]

            if not isinstance(h, HappeningCondition):
                continue

            # if "clear-platform" not in h.name:
            rules.append((h_i > 0).implies(SMTExpression.fromPddl(h.condition.conditions, sigma_im1)))

            if not isinstance(h.parent, ICEAction) or not h.parent.isWellOrderable():
                continue

            rollingPsi = []
            for pre in h.condition.conditions:
                if not isinstance(pre, BinaryPredicate):
                    continue
                rollingPsi.append(ICEEncodingInstradi.getSigmaPsi(sigma_im1, pre, h_i, h))

            if rollingPsi:
                rules.append((h_i > 1).implies(SMTExpression.bigand(rollingPsi)))

        return rules

    def __getMakeSpanRules(self) -> SMTConjunction:
        rules: SMTConjunction = SMTConjunction()
        tVars = self.transVars

        endingTimes = [tVars.timeVariables[h] for h in self.pattern if h.ending]
        M = self.transVars.makespan
        rules.append(SMTExpression.bigand([M >= t_i for t_i in endingTimes]))
        rules.append(SMTExpression.bigor([M.equal(t_i) for t_i in endingTimes]))

        return rules

    def __getPlanIntermediateTemporalRules(self) -> SMTConjunction:
        rules: SMTConjunction = SMTConjunction()
        hVars = self.transVars.happeningVariables
        tVars = self.transVars.timeVariables
        tEndVars = self.transVars.timeEndVariables

        piEff: List[HappeningEffect] = []
        piCond: List[HappeningCondition] = []

        for h in self.pattern:

            if isinstance(h.parent, ICEAction) and h.parent.isSnap:
                continue

            if isinstance(h, HappeningEffect) and isinstance(h.parent, PlanIntermediateEffect):
                piEff.append(h)
            if isinstance(h, HappeningCondition) and isinstance(h.parent, PlanIntermediateCondition):
                piCond.append(h)

        for h in piCond:
            h_i = hVars[h]
            t_i = tVars[h]
            t_i_end = tEndVars[h]
            M = self.transVars.makespan
            rules.append((h_i > 0).implies(t_i.equal(h.condition.fromTime.absolute(0, M))))
            rules.append((h_i > 0).implies(t_i_end.equal(h.condition.toTime.absolute(0, M))))

        for h in piEff:
            h_i = hVars[h]
            t_i = tVars[h]
            M = self.transVars.makespan
            rules.append((h_i > 0).implies(t_i.equal(h.effect.time.absolute(0, M))))

        return rules

    def __getActionIntermediateTemporalRules(self) -> SMTConjunction:
        rules: SMTConjunction = SMTConjunction()
        hVars = self.transVars.happeningVariables
        tVars = self.transVars.timeVariables
        tEndVars = self.transVars.timeEndVariables

        def hstr(h: Happening):
            return str(h.parent) + "-" + str(h.original)

        def hbstr(ice, b: ICEAction):
            return str(b) + "-" + str(ice)

        for pair in self.actionsStartEndPairs:
            b = pair.action
            h_p = hVars[pair.start]
            t_p = tVars[pair.start]
            h_q = hVars[pair.end]
            t_q = tVars[pair.end]
            p = pair.startIndex
            q = pair.endIndex

            ors = dict([(hbstr(h, b), set()) for h in b.icond + b.ieff])
            orsEnd = dict([(hbstr(h, b), set()) for h in b.icond + b.ieff])
            for h in self.pattern[p:q + 1]:
                if h.parent != b:
                    continue
                t_i = tVars[h]
                if isinstance(h, HappeningCondition):
                    assert isinstance(h.original.fromTime, RelativeTime)
                    assert isinstance(h.original.toTime, RelativeTime)
                    t_i_end = tEndVars[h]
                    ors[hstr(h)].add(t_i.equal(h.original.fromTime.absolute(t_p, t_q)))
                    orsEnd[hstr(h)].add(t_i_end.equal(h.original.toTime.absolute(t_p, t_q)))
                if isinstance(h, HappeningEffect):
                    assert isinstance(h.original.time, RelativeTime)
                    ors[hstr(h)].add(t_i.equal(h.original.time.absolute(t_p, t_q)))

            ices = []
            for ice in b.icond + b.ieff:
                if ors[hbstr(ice, b)]:
                    if isinstance(ice, IntermediateCondition):
                        ices.append(
                            SMTExpression.bigor(ors[hbstr(ice, b)]) & SMTExpression.bigor(orsEnd[hbstr(ice, b)]))
                    else:
                        ices.append(SMTExpression.bigor(ors[hbstr(ice, b)]))
            rules.append(((h_p > 0) & (h_q > 0)).implies(SMTExpression.bigand(ices)))

        return rules

    def __getDurRules(self) -> SMTConjunction:
        rules: SMTConjunction = SMTConjunction()
        tVars = self.transVars.timeVariables
        tEndVars = self.transVars.timeEndVariables
        hVars = self.transVars.happeningVariables
        dVars = self.transVars.durVariables

        for i, h in enumerate(self.pattern):
            h_i = hVars[h]
            t_i = tVars[h]

            rules.append((t_i > 0).iff(h_i > 0))
            if isinstance(h, HappeningCondition):
                t_i_end = tEndVars[h]
                rules.append((t_i_end > 0).iff(h_i > 0))

            if not h.starting:
                continue
            b = h.parent
            d_i = dVars[h]

            rules.append((h_i.equal(0)).implies((d_i.equal(0)) & (t_i.equal(0))))
            rules.append((h_i > 0).implies(d_i.equal(b.duration)))

            if isinstance(h.parent, ICEAction) and h.parent.isSnap:
                continue

            ending = []
            for end in self.pattern[i + 1:]:
                if end.ending == h.starting:
                    ending.append(tVars[end].equal(t_i + d_i))
                    if self.unrepeatableActions:
                        break
            rules.append((h_i > 0).implies(SMTExpression.bigor(ending)))

        return rules

    def __getPossiblyInMutex(self, h_a: Happening, i: int) -> List[int]:
        touchedAtoms = set()
        if isinstance(h_a, HappeningCondition):
            touchedAtoms = h_a.condition.conditions.getFunctions() | h_a.condition.conditions.getPredicates()
        if isinstance(h_a, HappeningEffect):
            touchedAtoms = h_a.effect.effects.getFunctions() | h_a.effect.effects.getPredicates()

        possiblyInMutex = set()
        for v in touchedAtoms:
            possiblyInMutex |= {j for j in self.touchedAtomsIndexes.get(v, set()) if j > i}
        return sorted(possiblyInMutex)

    def __getMutexRulesByHappeningPair(self, h_a: Happening, i: int, h_b: Happening, j: int):
        tVars = self.transVars.timeVariables
        tEndVars = self.transVars.timeEndVariables
        hVars = self.transVars.happeningVariables
        deltas = self.transVars.deltaExpressions
        sigmas = self.transVars.sigmaExpressions

        rules = SMTConjunction()

        if h_a.parent == h_b.parent or not h_a.original.inMutexWith(h_b.original):
            return rules

        h_i = hVars[h_a]
        h_j = hVars[h_b]
        sigmas_im1 = sigmas[i]
        t_i = tVars[h_a]
        t_j = tVars[h_b]

        if isinstance(h_a, HappeningCondition):
            t_i_end = tEndVars[h_a]
            rules.append(((h_i > 0) & (h_j > 0)).implies(t_j >= t_i_end))
            pass
        if isinstance(h_a, HappeningEffect) and isinstance(h_b, HappeningEffect):
            rules.append(((h_i > 0) & (h_j > 0)).implies(t_j >= t_i + EPSILON))
            pass
        if isinstance(h_a, HappeningEffect) and isinstance(h_b, HappeningCondition):
            cond = h_b.condition.conditions
            r = ((h_i > 0) & (h_j > 0) & ~SMTExpression.fromFormula(cond, sigmas_im1)).implies(
                t_j >= t_i + EPSILON)
            rules.append(r)

        return rules

    def __getEpsilonSeparationRules(self) -> SMTConjunction:
        rules: SMTConjunction = SMTConjunction()
        tVars = self.transVars.timeVariables
        tEndVars = self.transVars.timeEndVariables
        hVars = self.transVars.happeningVariables
        deltas = self.transVars.deltaExpressions
        sigmas = self.transVars.sigmaExpressions

        for i, h_a in enumerate(self.pattern):
            i = i + 1

            touchedAtoms = set()
            if isinstance(h_a, HappeningCondition):
                touchedAtoms = h_a.condition.conditions.getFunctions() | h_a.condition.conditions.getPredicates()
            if isinstance(h_a, HappeningEffect):
                touchedAtoms = h_a.effect.effects.getFunctions() | h_a.effect.effects.getPredicates()

            possiblyInMutex = set()
            for v in touchedAtoms:
                possiblyInMutex |= self.touchedAtomsIndexes.get(v, set())
            # print(i - 1, h_a, touchedAtoms, possiblyInMutex)

            for j in possiblyInMutex:

                if j < i:
                    continue

                h_b = self.pattern[j]
                if not h_a.original.inMutexWith(h_b.original):
                    continue

                if h_a.parent == h_b.parent:
                    continue

                h_i = hVars[h_a]
                h_j = hVars[h_b]
                sigmas_im1 = sigmas[i - 1]
                t_i = tVars[h_a]
                t_j = tVars[h_b]

                if isinstance(h_a, HappeningCondition):
                    t_i_end = tEndVars[h_a]
                    rules.append(((h_i > 0) & (h_j > 0)).implies(t_j >= t_i_end))
                    pass
                if isinstance(h_a, HappeningEffect) and isinstance(h_b, HappeningEffect):
                    rules.append(((h_i > 0) & (h_j > 0)).implies(t_j >= t_i + EPSILON))
                    pass
                if isinstance(h_a, HappeningEffect) and isinstance(h_b, HappeningCondition):
                    cond = h_b.condition.conditions
                    r = ((h_i > 0) & (h_j > 0) & ~SMTExpression.fromFormula(cond, sigmas_im1)).implies(
                        t_j >= t_i + EPSILON)
                    rules.append(r)
        return rules

    # def __getEpsilonSeparationRules(self) -> SMTConjunction:
    #     rules: SMTConjunction = SMTConjunction()
    #
    #     def isInMutex(h_a: Happening, h_b: Happening):
    #         return h_a.parent != h_b.parent and h_a.original.inMutexWith(h_b.original)
    #
    #     pairsConsidererd: Set[Tuple[int, int]] = set()
    #
    #     for i, h_a in enumerate(self.pattern):
    #         for j in self.__getPossiblyInMutex(h_a, i):
    #             h_b = self.pattern[j]
    #
    #             if (i, j) in pairsConsidererd or not isInMutex(h_a, h_b):
    #                 continue
    #
    #             pairsConsidererd.add((i, j))
    #             rules += self.__getMutexRulesByHappeningPair(h_a, i, h_b, j)
    #
    #             for k in self.__getPossiblyInMutex(h_b, j):
    #                 h_c = self.pattern[k]
    #
    #                 if (j, k) in pairsConsidererd or not isInMutex(h_b, h_c):
    #                     continue
    #
    #                 pairsConsidererd.add((j, k))
    #                 pairsConsidererd.add((i, k))
    #                 rules += self.__getMutexRulesByHappeningPair(h_b, j, h_c, k)
    #
    #     return rules

    def __getNoOverlapRules(self) -> SMTConjunction:
        rules: SMTConjunction = SMTConjunction()
        hVars = self.transVars.happeningVariables
        tVars = self.transVars.timeVariables
        dVars = self.transVars.durVariables

        for i, a in enumerate(self.pattern):
            for b in self.pattern[i + 1:]:
                if isinstance(a.starting, ICEAction) and a != b and a.starting == b.starting:
                    h_i = hVars[a]
                    t_i = tVars[a]
                    d_i = dVars[a]
                    h_j = hVars[b]
                    t_j = tVars[b]
                    e_b = a.starting.getEpsilonB()
                    if not self.unrepeatableActions:
                        rules.append(((h_i > 0) & (h_j > 0)).implies(t_j >= t_i + (d_i + e_b) * h_i))
                    else:
                        rules.append((h_i > 0).implies(h_j.equal(0)))

        return rules

    @staticmethod
    def getSigmaPsi(sigmas: Dict[Atom, SMTExpression], pre: BinaryPredicate,
                    r: SMTExpression or float, happening: Happening) -> SMTExpression:

        replacements: Dict[Atom, SMTExpression] = dict()

        assert isinstance(happening.parent, ICEAction)
        b = happening.parent

        AICEs = Happening.AICEs(b)

        psi = pre.lhs - pre.rhs

        for x in psi.getFunctions():

            asgnx = None
            deltax = []
            for H in AICEs:
                for h in H:
                    incrs = h.getPost().getIncreases()
                    decrs = h.getPost().getDecreases()
                    asgns = h.getPost().getAssignments()
                    if x in incrs:
                        deltax.append(SMTExpression.fromPddl(incrs[x], sigmas))
                    if x in decrs:
                        deltax.append(-SMTExpression.fromPddl(decrs[x], sigmas))
                    deltax.append(0)
                    if x in asgns:
                        asgnx = SMTExpression.fromPddl(asgns[x], sigmas)

            if asgnx:
                replacements[x] = asgnx
            else:
                replacements[x] = sigmas[x] + (r - 1) * sum(deltax)

        for (atom, expr) in sigmas.items():
            if atom not in replacements:
                replacements[atom] = expr

        return SMTExpression.fromPddl(pre, replacements)
