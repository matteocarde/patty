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

    @staticmethod
    def order(type: TimePredicateType):
        if type == TimePredicateType.AT_START:
            return 1
        if type == TimePredicateType.OVER_ALL:
            return 2
        if type == TimePredicateType.AT_END:
            return 3


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
                            or p.OverAllEffectContext or p.AtEndEffectContext) -> [TimePredicate]:

        # tp = cls()
        tpType = TimePredicateType
        if type(node) in {p.AtStartPreContext, p.AtStartEffectContext}:
            tpType = TimePredicateType.AT_START

        if type(node) in {p.OverAllPreContext, p.OverAllEffectContext}:
            tpType = TimePredicateType.OVER_ALL

        if type(node) in {p.AtEndPreContext, p.AtEndEffectContext}:
            tpType = TimePredicateType.AT_END

        subPredicates = []
        predicate = node.getChild(2)
        if isinstance(predicate, p.BooleanLiteralContext):
            subPredicates.append(Literal.fromNode(predicate.getChild(0)))
        elif isinstance(predicate, p.AndClauseContext):
            from src.pddl.Formula import Formula
            f = Formula.fromNode(predicate)
            subPredicates += f.conditions
        elif isinstance(predicate, p.AndEffectContext):
            nodes = [n.getChild(0) for n in predicate.children[2:-1]]
            for n in nodes:
                if isinstance(n, p.BooleanLiteralContext):
                    subPredicates.append(Literal.fromNode(n.getChild(0)))
                else:
                    subPredicates.append(BinaryPredicate.fromNode(n))
        else:
            subPredicates.append(BinaryPredicate.fromNode(predicate))

        timePredicates = []
        for subP in subPredicates:
            tp = cls()
            tp.type = tpType
            tp.subPredicate = subP
            timePredicates.append(tp)

        return timePredicates

    @classmethod
    def multipleFromNode(cls,
                         node: p.AtStartPreContext or p.OverAllPreContext or p.AtEndPreContext or p.AtStartEffectContext
                               or p.OverAllEffectContext or p.AtEndEffectContext):
        pass

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
