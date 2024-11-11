from __future__ import annotations
from typing import List

from src.ices.IntermediateEffect import IntermediateEffect
from src.ices.PlanRelativeTime import PlanRelativeTime
from src.pddl.BinaryPredicate import BinaryPredicate
from src.pddl.Literal import Literal


class PlanIntermediateEffect(IntermediateEffect):
    time: PlanRelativeTime
    effects: List[Literal or BinaryPredicate]

    def __init__(self):
        super().__init__()

    @classmethod
    def fromProperties(cls, time: PlanRelativeTime) -> PlanIntermediateEffect:
        ie = cls()
        ie.time = time

        return ie
