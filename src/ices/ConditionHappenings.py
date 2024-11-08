from src.ices.Happening import HappeningConditionStart, HappeningConditionEnd
from src.ices.ICEAction import ICEAction
from src.ices.IntermediateCondition import IntermediateCondition


class ConditionHappenings:
    condition: IntermediateCondition
    start: HappeningConditionStart
    end: HappeningConditionEnd

    def __init__(self):
        pass

    @classmethod
    def fromCondition(cls, c: IntermediateCondition, parent: ICEAction or ICEGoal, index: int):
        ch = cls()
        ch.condition = c
        ch.start = HappeningConditionStart(c, parent, index)
        ch.end = HappeningConditionEnd(c, parent, index)

        return ch
