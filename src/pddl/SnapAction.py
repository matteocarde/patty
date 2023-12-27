from __future__ import annotations

import copy

from src.pddl.Action import Action
from src.pddl.Atom import Atom
from src.pddl.TimePredicate import TimePredicateType
from typing import TYPE_CHECKING, Dict

if TYPE_CHECKING:
    from src.pddl.DurativeAction import DurativeAction


class SnapAction(Action):
    timeType: TimePredicateType
    durativeAction: DurativeAction

    def __init__(self):
        super().__init__()

    def __deepcopy__(self, m=None):
        m = {}
        c = super().__deepcopy__(m)
        c.__class__ = SnapAction
        c.timeType = self.timeType
        c.durativeAction = self.durativeAction
        return c

    def substitute(self, sub: Dict[Atom, float], default=None) -> Action:
        name = self.name
        preconditions = self.preconditions.substitute(sub, default)
        effects = self.effects.substitute(sub, default)
        planName = self.planName
        sa = SnapAction.fromProperties(name, [], preconditions, effects, planName)
        sa.timeType = self.timeType
        sa.durativeAction = self.durativeAction
        return sa

    def canHappen(self, sub: Dict[Atom, float], default=None) -> bool:
        if self.type in {TimePredicateType.OVER_ALL, TimePredicateType.AT_END}:
            return True
        return super().canHappen(sub, default=default)

    @classmethod
    def fromAction(cls, a: Action, type: TimePredicateType, dAction: DurativeAction):
        sa = cls.fromProperties(a.name, a.parameters, a.preconditions, a.effects, a.planName)
        sa.timeType = type
        sa.durativeAction = dAction
        return sa

    def isSame(self, end: SnapAction):
        return self.originalName == end.originalName
