from typing import List, Iterable

from src.ices.Happening import Happening, HappeningActionStart, HappeningActionEnd
from src.ices.ICEActionStartEndPair import ICEActionStartEndPair


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

    def getStartEndPairs(self) -> List[ICEActionStartEndPair]:
        pairs: List[ICEActionStartEndPair] = list()

        for i, h_i in enumerate(self.pattern):
            if not isinstance(h_i, HappeningActionStart):
                continue
            for j, h_j in enumerate(self.pattern):
                if j < i or not isinstance(h_j, HappeningActionEnd) or h_i.action != h_j.action:
                    continue
                pairs.append(ICEActionStartEndPair(h_i, i, h_j, j))

        return pairs
