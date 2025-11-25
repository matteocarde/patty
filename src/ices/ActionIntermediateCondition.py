from __future__ import annotations

from typing import List

from src.ices.ActionRelativeTime import ActionRelativeTime
from src.ices.IntermediateCondition import IntermediateCondition
from src.pddl.BinaryPredicate import BinaryPredicate
from src.pddl.Formula import Formula
from src.pddl.Predicate import Predicate


class ActionIntermediateCondition(IntermediateCondition):
    fromTime: ActionRelativeTime
    toTime: ActionRelativeTime
    conditions: Formula

    def __init__(self):
        super().__init__()

    @classmethod
    def fromProperties(cls, fromTime: ActionRelativeTime, toTime: ActionRelativeTime) -> ActionIntermediateCondition:
        ic = cls()
        ic.fromTime = fromTime
        ic.toTime = toTime
        return ic

    @classmethod
    def fake(cls, fromTime: ActionRelativeTime, toTime: ActionRelativeTime):
        ic = cls()
        ic.fromTime = fromTime
        ic.toTime = toTime
        ic.conditions = Formula()
        ic.conditions.addClause(BinaryPredicate.equality(0, 0))
        return ic
