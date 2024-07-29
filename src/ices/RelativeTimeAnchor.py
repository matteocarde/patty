from enum import Enum


class RelativeTimeAnchor(Enum):
    BEGIN = "BEGIN"
    FINISH = "FINISH"
    START = "START"
    END = "END"

    def __add__(self, other):
        raise NotImplementedError

    def __sub__(self, other):
        raise NotImplementedError

