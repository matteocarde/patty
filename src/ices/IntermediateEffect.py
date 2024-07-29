from typing import List

from src.ices.RelativeTime import RelativeTime
from src.pddl.BinaryPredicate import BinaryPredicate
from src.pddl.Literal import Literal


class IntermediateEffect:
    time: RelativeTime
    effects: List[Literal or BinaryPredicate]

    def __init__(self):
        pass
