from __future__ import annotations

from typing import Set

from src.ices.IntermediateEffect import IntermediateEffect
from src.ices.RelativeTime import RelativeTime
from src.pddl.Atom import Atom
from src.pddl.Formula import Formula
from src.pddl.Predicate import Predicate


class IntermediateCondition:
    fromTime: RelativeTime
    toTime: RelativeTime
    conditions: Formula

    atomsInConditions: Set[Atom]

    def __init__(self):
        super().__init__()
        self.conditions = Formula()
        self.atomsInConditions = set()

    def __repr__(self):
        return str(self.conditions)

    @classmethod
    def fromProperties(cls, fromTime: RelativeTime, toTime: RelativeTime) -> IntermediateCondition:
        raise NotImplementedError()

    def addCondition(self, clause: Formula or Predicate):
        self.conditions.addClause(clause)
        self.atomsInConditions.update(clause.getPredicates() | clause.getFunctions())

    def inMutexWith(self, effect: IntermediateEffect):
        return True if self.atomsInConditions.intersection(effect.atomsTouched) else False
