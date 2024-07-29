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
