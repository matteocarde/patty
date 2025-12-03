from __future__ import annotations

from typing import Set, List, Tuple

from typing import List, Dict

from pysmt.fnode import FNode
from unified_planning.model import TimeInterval

from src.ices.IntermediateEffect import IntermediateEffect
from src.ices.RelativeTime import RelativeTime
from src.pddl.Atom import Atom
from src.pddl.Formula import Formula
from src.pddl.Predicate import Predicate
from src.pddl.TimePredicate import TimePredicate, TimePredicateType
from src.utils.Constants import EPSILON
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

    def __lt__(self, other):
        from src.ices.IntermediateEffect import IntermediateEffect
        if isinstance(other, IntermediateCondition):
            return self.fromTime < other.fromTime
        if isinstance(other, IntermediateEffect):
            return self.fromTime < other.time
        return False

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

    def inMutexWith(self, other: IntermediateCondition or IntermediateEffect):
        if isinstance(other, IntermediateCondition):
            return False
        return True if self.atomsInConditions.intersection(other.atomsTouched) else False

    def toTuple(self) -> Tuple[RelativeTime or float, RelativeTime or float, Formula]:
        return self.fromTime, self.toTime, self.conditions

    @classmethod
    def fromTimePredicateSet(cls, type: TimePredicateType, tps: Set[TimePredicate]):
        from src.ices.ICEAction import START, END
        ic = cls()
        ic.fromTime = START + 0 if type in {TimePredicateType.AT_START, TimePredicateType.OVER_ALL} else END - 0
        if type == TimePredicateType.AT_END:
            ic.toTime = END - 0
        elif type == TimePredicateType.OVER_ALL:
            ic.toTime = END - EPSILON
        else:
            ic.toTime = START + 0
        # ic.toTime = END - 0 if type in {TimePredicateType.AT_END, TimePredicateType.OVER_ALL} else START + 0
        for tp in tps:
            ic.addCondition(tp.subPredicate)
        return ic

    @classmethod
    def fromUnifiedPlanning(cls, time: TimeInterval, cond: List[FNode], atomDict: Dict[str, Atom]):
        ic = cls()
        ic.fromTime = RelativeTime.fromUnifiedPlanning(time.lower)
        ic.toTime = RelativeTime.fromUnifiedPlanning(time.upper)
        ic.conditions = Formula.fromUnifiedPlanning(cond, atomDict)
        ic.atomsInConditions.update(ic.conditions.getPredicates() | ic.conditions.getFunctions())
        return ic

    def toANML(self) -> List[str]:
        lines = list()
        if self.conditions.type != "AND":
            raise NotImplementedError("I cannot deal with disjunctions when converting to ANML")
        c: Predicate
        for c in self.conditions:
            lines.append(f"[{self.fromTime.toANML()}, {self.toTime.toANML()}] {c.toANML('c')};")
        return lines
