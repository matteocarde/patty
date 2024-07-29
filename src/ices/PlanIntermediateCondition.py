from __future__ import annotations

from src.ices.IntermediateCondition import IntermediateCondition
from src.ices.PlanRelativeTime import PlanRelativeTime
from src.pddl.Formula import Formula


class PlanIntermediateCondition(IntermediateCondition):
    fromTime: PlanRelativeTime
    toTime: PlanRelativeTime
    conditions: Formula

    def __init__(self):
        super().__init__()

    @classmethod
    def fromProperties(cls, fromTime: PlanRelativeTime, toTime: PlanRelativeTime) -> PlanIntermediateCondition:
        ic = cls()
        ic.fromTime = fromTime
        ic.toTime = toTime
        return ic
