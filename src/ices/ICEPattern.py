from typing import List, Iterable

from src.ices.Happening import Happening


class ICEPattern:
    pattern: List[Happening]

    def __init__(self):
        self.pattern = list()

    def __iter__(self) -> Iterable[Happening]:
        return iter(self.pattern)

    def __getitem__(self, item):
        return self.pattern[item]

    def __computeHelpingStructs(self):
        pass
