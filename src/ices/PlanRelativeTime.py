from __future__ import annotations

from enum import Enum

from src.ices.RelativeTime import RelativeTime
from src.ices.RelativeTimeAnchor import RelativeTimeAnchor


class PlanRelativeTime(RelativeTime):
    anchor: PlanRelativeTimeAnchor
    k: int

    def __init__(self):
        super().__init__()


class PlanRelativeTimeAnchor(RelativeTimeAnchor, Enum):
    BEGIN = "BEGIN"
    FINISH = "FINISH"

    def __add__(self, other) -> PlanRelativeTime:
        if not isinstance(other, int) and not isinstance(other, float):
            raise Exception()

        rt = PlanRelativeTime()
        rt.anchor = PlanRelativeTimeAnchor.BEGIN
        rt.k = other
        return rt

    def __sub__(self, other) -> PlanRelativeTime:
        if not isinstance(other, int) and not isinstance(other, float):
            raise Exception()

        rt = PlanRelativeTime()
        rt.anchor = PlanRelativeTimeAnchor.FINISH
        rt.k = - other
        return rt
