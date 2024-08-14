from __future__ import annotations

from typing import List

from src.ices.RelativeTime import RelativeTime
from src.pddl.BinaryPredicate import BinaryPredicate
from src.pddl.Literal import Literal


class IntermediateEffect:
    time: RelativeTime
    effects: List[Literal or BinaryPredicate]

    def __init__(self):
        super().__init__()
        self.effects = list()

    def __repr__(self):
        return str(self.effects)

    @classmethod
    def fromProperties(cls, time: RelativeTime) -> IntermediateEffect:
        raise NotImplementedError()
