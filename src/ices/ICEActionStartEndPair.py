from typing import Dict, List

from src.ices.Happening import HappeningActionStart, HappeningActionEnd, Happening, HappeningAction
from src.smt.SMTExpression import SMTExpression


class ICEActionStartEndPair:
    start: Happening
    end: Happening
    startIndex: int
    endIndex: int

    def __init__(self, start: Happening, i: int, end: Happening, j: int):
        self.start = start
        self.end = end
        self.startIndex = i
        self.endIndex = j

        assert self.start.starting == self.end.ending
        self.action = self.start.starting

    def __repr__(self):
        return str(self)

    def __str__(self):
        return f"<{self.start}@{self.startIndex}, {self.end}@{self.endIndex}>"

    def getPlaceholderBij(self, vars: Dict[Happening, SMTExpression], pattern) -> SMTExpression:
        h_i = vars[self.start]
        h_j = vars[self.end]
        andList: List[SMTExpression] = [vars[h].equal(0) for h in pattern[self.i + 1:self.j]
                                        if isinstance(h, HappeningAction) and h.action == self.action]
        return SMTExpression.bigand([h_i > 0, h_j > 0] + andList)
