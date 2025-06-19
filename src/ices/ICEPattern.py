from __future__ import annotations
import copy
from typing import List, Iterable

from src.ices.Happening import Happening, HappeningActionStart, HappeningActionEnd, HappeningConditionStart, \
    HappeningConditionEnd, HappeningEffect
from src.ices.ICEAction import BEGIN, ICEAction
from src.ices.ICEActionStartEndPair import ICEActionStartEndPair
from src.ices.ICEConditionStartEndPair import ICEConditionStartEndPair
from src.ices.PlanIntermediateEffect import PlanIntermediateEffect


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
        pt.pattern = self.pattern + other.pattern
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
            a = copy.deepcopy(item)

            a.name = f"{a.name}_{postfix}"
            order.append(a)
        self.pattern = order
        return self

    def multiply(self, times: int, addFake=True) -> ICEPattern:
        order = []
        for i in range(0, times):
            for item in self.pattern:
                a = copy.deepcopy(item)
                if hasattr(a, "action") and isinstance(a.action, ICEAction):
                    a.action.name = f"{a.action.name}_{i}"
                if hasattr(a, "parent") and isinstance(a.parent, ICEAction):
                    a.parent.name = f"{a.parent.name}_{i}"
                a.name = f"{a.name}_{i}" if times > 1 else f"{a.name}"
                order.append(a)

        return ICEPattern.fromOrder(order)

    def getActionsStartEndPairs(self) -> List[ICEActionStartEndPair]:
        pairs: List[ICEActionStartEndPair] = list()

        for i, h_i in enumerate(self.pattern):
            if not isinstance(h_i, HappeningActionStart):
                continue
            for j, h_j in enumerate(self.pattern):
                if j < i or not isinstance(h_j, HappeningActionEnd) or h_i.action != h_j.action:
                    continue
                pairs.append(ICEActionStartEndPair(h_i, i, h_j, j))

        return pairs

    def getConditionsStartEndPairs(self) -> List[ICEConditionStartEndPair]:
        pairs: List[ICEConditionStartEndPair] = list()

        for i, h_i in enumerate(self.pattern):
            if not isinstance(h_i, HappeningConditionStart):
                continue
            for j, h_j in enumerate(self.pattern):
                if j < i or not isinstance(h_j, HappeningConditionEnd) or h_i.condition != h_j.condition:
                    continue
                pairs.append(ICEConditionStartEndPair(h_i, i, h_j, j))

        return pairs

    def getFake(self) -> Happening:

        fakeEff = PlanIntermediateEffect.fromProperties(BEGIN + 0)
        return HappeningEffect(fakeEff, None, "FAKE")
