from __future__ import annotations

import copy
from typing import List, Iterable, Dict, Set, Tuple

from src.ices.Happening import Happening, HappeningActionStart, HappeningActionEnd, HappeningConditionStart, \
    HappeningConditionEnd, HappeningEffect, HappeningCondition
from src.ices.ICEAction import BEGIN, ICEAction
from src.ices.ICEActionStartEndPair import ICEActionStartEndPair
from src.ices.ICEConditionStartEndPair import ICEConditionStartEndPair
from src.ices.ICETask import ICETask
from src.ices.PlanIntermediateEffect import PlanIntermediateEffect
from src.ices.SnapHappeningAction import SnapHappeningAction

from src.ices.SnapTask import SnapTask
from src.pddl.ARPG import ARPG
from src.pddl.Action import Action
from src.pddl.Atom import Atom
from src.pddl.State import State


class ICEPattern:
    pattern: List[Happening]

    def __init__(self):
        self.pattern = list()

    def __iter__(self) -> Iterable[Happening]:
        return iter(self.pattern)

    def __len__(self):
        return len(self.pattern)

    def __getitem__(self, item):
        return self.pattern[item]

    def __add__(self, other):
        if not isinstance(other, ICEPattern):
            return self
        pt = ICEPattern()
        for item in self.pattern:
            a = copy.copy(item)
            pt.pattern.append(a)
        for item in other.pattern:
            a = copy.copy(item)
            pt.pattern.append(a)
        return pt

    def __str__(self):
        return str(self.pattern)

    @classmethod
    def fromOrder(cls, order: List[Happening]):
        p = cls()
        p.pattern = order

        return p

    def addPostfix(self, postfix: int or str):
        order = []
        for item in self.pattern:
            a = copy.copy(item)
            a.name = f"{a.name}_{postfix}"
            order.append(a)
        self.pattern = order
        return self

    def multiply(self, times: int, addFake=True) -> ICEPattern:
        order = []
        for i in range(0, times):
            for item in self.pattern:
                a = copy.copy(item)
                a.name = f"{a.name}_{i}" if times > 1 else f"{a.name}"
                order.append(a)

        return ICEPattern.fromOrder(order)

    def getActionsStartEndPairs(self) -> List[ICEActionStartEndPair]:
        pairs: List[ICEActionStartEndPair] = list()

        for i, h_i in enumerate(self.pattern):
            if not h_i.starting:
                continue
            for j, h_j in enumerate(self.pattern):
                if j < i or h_i.starting != h_j.ending:
                    continue
                pairs.append(ICEActionStartEndPair(h_i, i, h_j, j))

        return pairs

    def getConditionsStartEndPairs(self) -> List[ICEConditionStartEndPair]:
        pairs: List[ICEConditionStartEndPair] = list()

        for i, h_i in enumerate(self.pattern):
            if not isinstance(h_i, HappeningConditionStart):
                continue
            for j, h_j in enumerate(self.pattern[i + 1:]):
                if not isinstance(h_j, HappeningConditionEnd) or h_i.condition != h_j.condition:
                    continue
                pairs.append(ICEConditionStartEndPair(h_i, i, h_j, i + 1 + j))

        return pairs

    def getFake(self) -> Happening:

        fakeEff = PlanIntermediateEffect.fromProperties(BEGIN + 0)
        return HappeningEffect(fakeEff, None, "FAKE")

    def getTouchedAtomsIndexes(self) -> Dict[Atom, List[int]]:
        d: Dict[Atom, List[int]] = dict()
        for i, h_i in enumerate(self.pattern):
            if not isinstance(h_i, HappeningEffect):
                continue
            for e in h_i.effect.effects:
                v = e.getAtom()
                d.setdefault(v, [])
                d[v].append(i)

        return d

    def getTouchedByConditionStart(self) -> Dict[Atom, List[int]]:
        d: Dict[Atom, List[int]] = dict()
        for i, h_i in enumerate(self.pattern):
            if not isinstance(h_i, HappeningConditionStart):
                continue
            for c in h_i.condition.conditions:
                v = c.getAtom()
                d.setdefault(v, [])
                d[v].append(i)

        return d

    @staticmethod
    def getARPG(task: ICETask, state: State, avoidRaising=False):
        snapDomain = SnapTask(task)
        return ARPG(snapDomain, state, snapDomain.goal, avoidRaising=avoidRaising)

    @classmethod
    def fromSnap(cls, task: ICETask):

        arpg: ARPG = ICEPattern.getARPG(task, State.fromInitialCondition(task.init))
        snapOrder: List[SnapHappeningAction] = arpg.getActionsOrder(enhanced=True)
        pattern = ICEPattern.fromOrder([a.originatingHappening for a in snapOrder])

        ICEPattern.__setStartingAndEnding(pattern)
        return pattern

    @staticmethod
    def __setStartingAndEnding(pattern):
        starting: Dict[ICEAction, Happening] = dict()
        ending: Dict[ICEAction, Happening] = dict()

        h: Happening
        for h in pattern:
            if not isinstance(h.parent, ICEAction):
                continue
            b = h.parent
            h.starting = None
            h.ending = None
            ending[b] = h
            if b not in starting:
                starting[b] = h
                h.starting = b

        for (b, h) in ending.items():
            h.ending = b

        return

    @classmethod
    def fromState(cls, s: State, task: ICETask) -> ICEPattern:
        arpg: ARPG = ICEPattern.getARPG(task, s, avoidRaising=True)

        snapOrder: List[SnapHappeningAction] = arpg.getActionsOrderWithoutUnused(enhanced=False)
        left: Set[SnapHappeningAction] = arpg.getUnusedActions()

        leftHappenings = dict([(aLeft.originatingHappening, aLeft) for aLeft in left])
        actions: Set[ICEAction] = {aLeft.originatingHappening.parent for aLeft in left if aLeft.originatingHappening}
        added: Set[Happening] = set()

        for b in sorted(actions):
            if not isinstance(b, ICEAction):
                continue
            for H in Happening.AICEs(b):
                for h in H:
                    if h in leftHappenings:
                        snapOrder.append(leftHappenings[h])
                        del leftHappenings[h]

        snapOrder += [h for h in leftHappenings.values()]
        pattern: ICEPattern = ICEPattern.fromOrder([aLeft.originatingHappening for aLeft in snapOrder if aLeft.originatingHappening])

        ICEPattern.__setStartingAndEnding(pattern)

        return pattern

    def print(self):
        print("----- Pattern -----")
        for a in self.pattern:
            print(a)

    @classmethod
    def empty(cls):
        return ICEPattern.fromOrder([])

    def getLength(self):
        return len(self)

    @classmethod
    def fromPlan(cls, plan) -> ICEPattern:
        # print(plan.timedHappenings)
        pattern = ICEPattern.fromOrder([copy.copy(h) for (t, o, h, t_e) in sorted(plan.timedHappenings)])
        # ICEPattern.__setStartingAndEnding(pattern)
        return pattern
