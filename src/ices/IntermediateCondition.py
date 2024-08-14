from __future__ import annotations

from src.ices.RelativeTime import RelativeTime
from src.pddl.Formula import Formula


class IntermediateCondition:
    fromTime: RelativeTime
    toTime: RelativeTime
    conditions: Formula

    def __init__(self):
        super().__init__()
        self.conditions = Formula()

    def __repr__(self):
        return str(self.conditions)

    @classmethod
    def fromProperties(cls, fromTime: RelativeTime, toTime: RelativeTime) -> IntermediateCondition:
        raise NotImplementedError()
