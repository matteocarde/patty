from typing import List, Iterable

from src.ices.Happening import Happening, HappeningActionStart, HappeningActionEnd, HappeningConditionStart, \
    HappeningConditionEnd, HappeningEffect
from src.ices.ICEAction import BEGIN
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
