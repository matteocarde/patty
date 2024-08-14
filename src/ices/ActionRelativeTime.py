from __future__ import annotations

from enum import Enum

from src.ices.RelativeTime import RelativeTime
from src.ices.RelativeTimeAnchor import RelativeTimeAnchor


class ActionRelativeTime(RelativeTime):
    anchor: ActionRelativeTimeAnchor
    k: int

    def __init__(self):
        super().__init__()



class ActionRelativeTimeAnchor(RelativeTimeAnchor, Enum):
    START = "START"
    END = "END"

    def __add__(self, other) -> ActionRelativeTime:
        if not isinstance(other, int) and not isinstance(other, float):
            raise Exception()

        rt = ActionRelativeTime()
        rt.anchor = self
        rt.k = other
        return rt

    def __sub__(self, other) -> ActionRelativeTime:
        if not isinstance(other, int) and not isinstance(other, float):
            raise Exception()

        rt = ActionRelativeTime()
        rt.anchor = self
        rt.k = - other
        return rt
