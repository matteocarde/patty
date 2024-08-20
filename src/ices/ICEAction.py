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

    def __hash__(self):
        return hash(self.name)

    def __eq__(self, other):
        # In reality, for two actions to be equal they should also have the same icond and ieff. In the plan,
        # if they have the same name they are undistinguishable. Thus we check only the name.
        return isinstance(other, ICEAction) and self.name == other.name

    def __repr__(self):
        return str(self)

    def __str__(self):
        return self.name

    @classmethod
    def fromProperties(cls, name: str, duration: int) -> ICEAction:
        a = cls()
        a.name = name
        a.duration = duration
        return a
