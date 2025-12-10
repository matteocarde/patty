from __future__ import annotations
from typing import List

from src.ices.ActionRelativeTime import ActionRelativeTime
from src.ices.IntermediateEffect import IntermediateEffect
from src.pddl.BinaryPredicate import BinaryPredicate
from src.pddl.Effects import Effects
from src.pddl.Literal import Literal


class ActionIntermediateEffect(IntermediateEffect):
    time: ActionRelativeTime
    effects: Effects

    def __init__(self):
        super().__init__()

    def __repr__(self):
        return str(self)

    def __str__(self):
        return f"{self.time}: {self.effects}"

    def __lt__(self, other):
        if not isinstance(other, ActionIntermediateEffect):
            return False
        return self.time < other.time

    def __le__(self, other):
        if not isinstance(other, ActionIntermediateEffect):
            return False
        return self.time <= other.time

    def __sub__(self, other):
        if not isinstance(other, ActionIntermediateEffect):
            return False
        return self.time.k - other.time.k

    def __iter__(self):
        return iter(self.effects)

    @classmethod
    def fromProperties(cls, time: ActionRelativeTime) -> ActionIntermediateEffect:
        ie = cls()
        ie.time = time

        return ie

