from __future__ import annotations

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

    def substitute(self, sub: Dict[Atom, float], default=None) -> Action:
        name = self.name
        preconditions = self.preconditions.substitute(sub, default)
        effects = self.effects.substitute(sub, default)
        planName = self.planName
        sa = SnapAction.fromProperties(name, [], preconditions, effects, planName)
        sa.timeType = self.timeType
        sa.durativeAction = self.durativeAction
        return sa
