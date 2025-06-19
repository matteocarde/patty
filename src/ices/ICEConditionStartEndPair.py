from src.ices.Happening import HappeningConditionStart, HappeningConditionEnd
from src.ices.ICEAction import ICEAction
from src.ices.TimedConditions import TimedConditions
from src.ices.IntermediateCondition import IntermediateCondition


class ICEConditionStartEndPair:
    h_i: HappeningConditionStart
    h_j: HappeningConditionEnd
    i: int
    j: int
    parent: ICEAction or TimedConditions
    condition: IntermediateCondition

    def __init__(self, h_i: HappeningConditionStart, i: int, h_j: HappeningConditionEnd, j: int):
        self.h_i = h_i
        self.h_j = h_j
        self.i = i
        self.j = j

        # assert self.h_i.parent == self.h_j.parent
        assert self.h_i.condition == self.h_j.condition
        self.parent = self.h_i.parent
        self.condition = self.h_i.condition

    def __repr__(self):
        return str((self.h_i, self.h_j))

    def __str__(self):
        return str((self.h_i, self.h_j))
