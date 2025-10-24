from src.ices.Happening import HappeningConditionStart, HappeningConditionEnd
from src.ices.ICEAction import ICEAction
from src.ices.TimedConditions import TimedConditions
from src.ices.IntermediateCondition import IntermediateCondition


class ICEConditionStartEndPair:
    start: HappeningConditionStart
    end: HappeningConditionEnd
    startIndex: int
    endIndex: int
    parent: ICEAction or TimedConditions
    condition: IntermediateCondition

    def __init__(self, start: HappeningConditionStart, i: int, end: HappeningConditionEnd, j: int):
        self.start = start
        self.end = end
        self.startIndex = i
        self.endIndex = j

        # assert self.h_i.parent == self.h_j.parent
        assert self.start.condition == self.end.condition
        self.parent = self.start.parent
        self.condition = self.start.condition

    def __repr__(self):
        return str((self.start, self.end))

    def __str__(self):
        return str((self.start, self.end))
