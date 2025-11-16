from __future__ import annotations

from enum import Enum

from unified_planning.model import Timing, TimepointKind

from src.ices.RelativeTime import RelativeTime
from src.ices.RelativeTimeAnchor import RelativeTimeAnchor


class ActionRelativeTime(RelativeTime):
    anchor: ActionRelativeTimeAnchor
    k: int

    def __init__(self):
        super().__init__()

    def __le__(self, other):
        if not isinstance(other, ActionRelativeTime):
            return False
        if self.anchor != other.anchor:
            return False
        return self.k <= other.k

    def __lt__(self, other):
        if not isinstance(other, ActionRelativeTime):
            return False
        if self.anchor != other.anchor:
            return False
        return self.k < other.k



class ActionRelativeTimeAnchor(RelativeTimeAnchor):
    START = "S"
    END = "E"

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
