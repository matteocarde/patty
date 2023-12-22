from __future__ import annotations

import copy
from enum import Enum
from typing import Dict, Tuple, List, Set

from src.pddl.Atom import Atom
from src.pddl.BinaryPredicate import BinaryPredicate
from src.pddl.Literal import Literal
from src.pddl.Predicate import Predicate
from src.pddl.grammar.pddlParser import pddlParser as p


class TimePredicateType(Enum):
    AT_START = "at start"
    OVER_ALL = "over all"
    AT_END = "at end"


class TimePredicate(Predicate):
    type: TimePredicateType
    subPredicate: Predicate

    def __init__(self):
        super().__init__()

    def __deepcopy__(self, m=None) -> TimePredicate:
        m = {} if m is None else m
        tp = TimePredicate()
        tp.type = self.type
        tp.subPredicate = copy.deepcopy(self.subPredicate, m)
        return tp

    @classmethod
    def fromNode(cls, node: p.AtStartPreContext or p.OverAllPreContext or p.AtEndPreContext or p.AtStartEffectContext
                            or p.OverAllEffectContext or p.AtEndEffectContext) -> TimePredicate:

        tp = cls()
        if type(node) in {p.AtStartPreContext, p.AtStartEffectContext}:
            tp.type = TimePredicateType.AT_START

        if type(node) in {p.OverAllPreContext, p.OverAllEffectContext}:
            tp.type = TimePredicateType.OVER_ALL

        if type(node) in {p.AtEndPreContext, p.AtEndEffectContext}:
            tp.type = TimePredicateType.AT_END

        predicate = node.getChild(2)
        if isinstance(predicate, p.BooleanLiteralContext):
            tp.subPredicate = Literal.fromNode(predicate.getChild(0))
        else:
            tp.subPredicate = BinaryPredicate.fromNode(predicate)

        return tp

    def ground(self, subs: Dict[str, str], delta=1) -> TimePredicate:
        tp = TimePredicate()
        tp.type = self.type
        tp.subPredicate = self.subPredicate.ground(subs, delta)

        return tp

    def getPredicates(self) -> Set[Atom]:
        return self.subPredicate.getPredicates()

    def getFunctions(self) -> Set[Atom]:
        return self.subPredicate.getFunctions()

    def isDynamicLifted(self, problem) -> bool:
        return self.subPredicate.isDynamicLifted(problem)

    def canHappenLiftedPartial(self, item: Tuple, params: List[str], problem) -> bool:
        return self.subPredicate.canHappenLiftedPartial(item, params, problem)

    def __str__(self):
        return f"({self.type} {self.subPredicate})"

    def __repr__(self):
        return str(self)
