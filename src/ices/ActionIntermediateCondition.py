from __future__ import annotations

from src.ices.ActionRelativeTime import ActionRelativeTime
from src.ices.IntermediateCondition import IntermediateCondition
from src.pddl.Formula import Formula


class ActionIntermediateCondition(IntermediateCondition):
    fromTime: ActionRelativeTime
    toTime: ActionRelativeTime
    conditions: Formula

    def __init__(self):
        super().__init__()

    @classmethod
    def fromProperties(cls, fromTime: ActionRelativeTime, toTime: ActionRelativeTime) -> ActionIntermediateCondition:
        ic = cls()
        ic.fromTime = fromTime
        ic.toTime = toTime
        return ic
