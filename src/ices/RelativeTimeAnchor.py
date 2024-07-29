from enum import Enum


class RelativeTimeAnchor(Enum):
    BEGIN = "BEGIN"
    FINISH = "FINISH"
    START = "START"
    END = "END"


class PlanRelativeTimeAnchor(Enum):
    BEGIN = "BEGIN"
    FINISH = "FINISH"


class ActionRelativeTimeAnchor(Enum):
    START = "START"
    END = "END"
