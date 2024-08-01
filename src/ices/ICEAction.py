from __future__ import annotations
from typing import List

from src.ices.ActionIntermediateCondition import ActionIntermediateCondition
from src.ices.ActionIntermediateEffect import ActionIntermediateEffect
from src.ices.ActionRelativeTime import ActionRelativeTimeAnchor
from src.ices.PlanRelativeTime import PlanRelativeTimeAnchor

START = ActionRelativeTimeAnchor.START
END = ActionRelativeTimeAnchor.END
BEGIN = PlanRelativeTimeAnchor.BEGIN
FINISH = PlanRelativeTimeAnchor.FINISH

class ICEAction:
    name: str
    icond: List[ActionIntermediateCondition]
    ieff: List[ActionIntermediateEffect]
    duration: int

    def __init__(self):
        self.icond = list()
        self.ieff = list()

    @classmethod
    def fromProperties(cls, name: str, duration: int) -> ICEAction:
        a = cls()
        a.name = name
        a.duration = duration
        return a
