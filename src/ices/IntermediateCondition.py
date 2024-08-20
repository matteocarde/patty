from __future__ import annotations

from typing import Set, List, Tuple

from src.ices.IntermediateEffect import IntermediateEffect
from src.ices.RelativeTime import RelativeTime
from src.pddl.Atom import Atom
from src.pddl.Formula import Formula
from src.pddl.Predicate import Predicate
from src.utils.Tuplable import Tuplable


class IntermediateCondition(Tuplable):
    fromTime: RelativeTime or float
    toTime: RelativeTime or float
    conditions: Formula

    atomsInConditions: Set[Atom]

    def __init__(self):
        super().__init__()
        self.conditions = Formula()
        self.atomsInConditions = set()

    def __repr__(self):
        return str(self.conditions)

    def __str__(self):
        return f"<{self.fromTime}, {self.toTime}, {self.conditions}>"

    def toAbsolute(self, a: float, b: float) -> IntermediateCondition:
        ic = self.__class__()
        ic.fromTime = self.fromTime.absolute(a, b)
        ic.toTime = self.toTime.absolute(a, b)
        ic.conditions = self.conditions
        ic.atomsInConditions = self.atomsInConditions

        return ic

    @classmethod
    def fromProperties(cls, fromTime: RelativeTime, toTime: RelativeTime) -> IntermediateCondition:
        raise NotImplementedError()

    def addCondition(self, clause: Formula or Predicate):
        self.conditions.addClause(clause)
        self.atomsInConditions.update(clause.getPredicates() | clause.getFunctions())

    def inMutexWith(self, effect: IntermediateEffect):
        return True if self.atomsInConditions.intersection(effect.atomsTouched) else False

    def toTuple(self) -> Tuple[RelativeTime or float, RelativeTime or float, Formula]:
        return self.fromTime, self.toTime, self.conditions
