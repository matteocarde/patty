from typing import List

from src.ices.ActionRelativeTime import ActionRelativeTime
from src.ices.IntermediateEffect import IntermediateEffect
from src.pddl.BinaryPredicate import BinaryPredicate
from src.pddl.Literal import Literal


class ActionIntermediateEffect(IntermediateEffect):
    time: ActionRelativeTime
    effects: List[Literal or BinaryPredicate]

    def __init__(self):
        super().__init__()
