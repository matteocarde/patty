from __future__ import annotations
from typing import List

from src.ices.RelativeTime import RelativeTime
from src.pddl.BinaryPredicate import BinaryPredicate
from src.pddl.Literal import Literal


class IntermediateEffect:
    time: RelativeTime
    effects: List[Literal or BinaryPredicate]

    def __init__(self):
        self.effects = list()
        pass

    @classmethod
    def fromProperties(cls, time: RelativeTime) -> IntermediateEffect:
        raise NotImplementedError()
