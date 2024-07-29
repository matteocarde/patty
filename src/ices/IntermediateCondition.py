from __future__ import annotations

from src.ices.RelativeTime import RelativeTime
from src.pddl.Formula import Formula


class IntermediateCondition:
    fromTime: RelativeTime
    toTime: RelativeTime
    conditions: Formula

    def __init__(self):
        self.conditions = Formula()
        pass

    @classmethod
    def fromProperties(cls, fromTime: RelativeTime, toTime: RelativeTime) -> IntermediateCondition:
        raise NotImplementedError()
