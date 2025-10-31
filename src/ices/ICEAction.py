from __future__ import annotations

from typing import List, Set, Tuple

from classes.utils.Constants import EPSILON
from src.ices.ActionIntermediateCondition import ActionIntermediateCondition
from src.ices.ActionIntermediateEffect import ActionIntermediateEffect
from src.ices.ActionRelativeTime import ActionRelativeTimeAnchor
from src.ices.IntermediateCondition import IntermediateCondition
from src.ices.IntermediateEffect import IntermediateEffect
from src.ices.PlanRelativeTime import PlanRelativeTimeAnchor
from src.pddl.Constant import Constant
from src.pddl.DurativeAction import DurativeAction
from src.pddl.TimePredicate import TimePredicate

START = ActionRelativeTimeAnchor.START
END = ActionRelativeTimeAnchor.END
BEGIN = PlanRelativeTimeAnchor.BEGIN
FINISH = PlanRelativeTimeAnchor.FINISH
ALPHA = PlanRelativeTimeAnchor.BEGIN
OMEGA = PlanRelativeTimeAnchor.FINISH


class ICEAction:
    name: str
    originalName: str
    icond: List[ActionIntermediateCondition]
    ieff: List[ActionIntermediateEffect]
    duration: float

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
        a.originalName = name
        a.duration = duration
        return a

    def isEligibleForRolling(self):
        return "uncap-cap" not in self.name  # TODO

    def isWellOrderable(self):
        return True  # TODO

    @classmethod
    def fromDurativeActionNOICEs(cls, action: DurativeAction):
        iceAction = cls()
        iceAction.name = action.name
        iceAction.originalName = action.originalName
        if not isinstance(action.duration, Constant):
            raise Exception("Cannot translate durative action w/o ICEs if duration is not constant")
        iceAction.duration = action.duration.value

        for type, pres in TimePredicate.group(action.preconditions.conditions):
            iceAction.icond.append(IntermediateCondition.fromTimePredicateSet(type, pres))

        for type, effs in TimePredicate.group(action.effects.assignments):
            iceAction.ieff.append(IntermediateEffect.fromTimePredicateSet(type, effs))

        return iceAction

    def getEpsilonB(self) -> float:
        start = ({c for c in self.icond if c.fromTime.anchor == START and c.fromTime.k == 0} |
                 {e for e in self.ieff if e.time.anchor == START and e.time.k == 0})
        end = ({c for c in self.icond if c.fromTime.anchor == END and c.fromTime.k == 0} |
               {e for e in self.ieff if e.time.anchor == END and e.time.k == 0})
        for s in start:
            for e in end:
                if s.inMutexWith(e):
                    return EPSILON
        return 0
