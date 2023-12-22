from __future__ import annotations

from src.pddl.Action import Action
from src.pddl.TimePredicate import TimePredicateType


class SnapAction(Action):
    timeType: TimePredicateType

    def __init__(self):
        super().__init__()
