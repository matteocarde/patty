from typing import Dict, List

from src.ices.Happening import HappeningActionStart, HappeningActionEnd, Happening, HappeningAction
from src.smt.SMTExpression import SMTExpression


class ICEActionStartEndPair:
    h_i: HappeningActionStart
    h_j: HappeningActionEnd
    i: int
    j: int

    def __init__(self, h_i: HappeningActionStart, i: int, h_j: HappeningActionEnd, j: int):
        self.h_i = h_i
        self.h_j = h_j
        self.i = i
        self.j = j

        assert self.h_i.action == self.h_j.action
        self.action = self.h_i.action

    def getPlaceholderBij(self, vars: Dict[Happening, SMTExpression], pattern) -> SMTExpression:
        h_i = vars[self.h_i]
        h_j = vars[self.h_j]
        andList: List[SMTExpression] = [vars[h].equal(0) for h in pattern[self.i + 1:self.j]
                                        if isinstance(h, HappeningAction) and h.action == self.action]
        return SMTExpression.bigand([h_i > 0, h_j > 0] + andList)
