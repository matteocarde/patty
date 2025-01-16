from __future__ import annotations

import copy
from typing import Set, Dict, List, Tuple

from src.pddl.Atom import Atom
from src.pddl.CEConditions import CEConditions
from src.pddl.CEEffects import CEEffects
from src.pddl.FalsePredicate import FalsePredicate
from src.pddl.Literal import Literal
from src.pddl.Parameters import Parameters
from src.pddl.Predicate import Predicate
from src.pddl.Problem import Problem
from src.pddl.TruePredicate import TruePredicate
from src.pddl.grammar.pddlParser import pddlParser as p


class ConditionalEffect(Predicate):
    from src.pddl.CEEffects import CEEffects
    conditions: CEConditions
    effects: CEEffects

    def __init__(self):
        super().__init__()
        self.conditions = CEConditions()
        self.effects = CEEffects()

    @classmethod
    def fromNode(cls, node: p.CeContext):
        ce = cls()
        ce.conditions = CEConditions.fromNode(node.cond.getChild(0))
        ce.effects = CEEffects.fromNode(node.eff)
        return ce

    def __str__(self):
        return f"{self.conditions} -> {self.effects}"

    def __repr__(self):
        return str(self)

    def __deepcopy__(self, m=None) -> ConditionalEffect:
        m = {} if m is None else m
        ce = ConditionalEffect()
        ce.conditions = copy.deepcopy(self.conditions, m)
        ce.effects = copy.deepcopy(self.effects, m)
        return ce

    def canHappenLifted(self, sub: Tuple, params: List[str], problem) -> bool:
        return self.conditions.canHappenLifted(sub, params, problem)

    def getPredicates(self) -> Set[Atom]:
        return self.conditions.getPredicates() | self.effects.getPredicates()

    def getFunctions(self) -> Set[Atom]:
        return self.conditions.getFunctions() | self.effects.getFunctions()

    def getDynamicAtoms(self) -> Set[Atom]:
        return self.effects.getDynamicAtoms()

    def ground(self, subs: Dict[str, str], problem) -> Predicate:
        ce = ConditionalEffect()
        ce.conditions = self.conditions.ground(subs, problem).simplify()
        from src.pddl.FalsePredicate import FalsePredicate
        if isinstance(ce.conditions, FalsePredicate):
            return FalsePredicate()
        ce.effects = self.effects.ground(subs, problem)

        return ce

    def blocks(self, other: ConditionalEffect) -> bool:
        if isinstance(other.conditions, TruePredicate):
            return False
        if isinstance(other.conditions, FalsePredicate):
            return False
        return bool(self.effects.getNegative() & other.conditions.getPositive()) or \
            bool(self.effects.getPositive() & other.conditions.getNegative())

    def allows(self, other: ConditionalEffect) -> bool:
        if isinstance(other.conditions, TruePredicate):
            return False
        if isinstance(other.conditions, FalsePredicate):
            return False
        return bool(self.effects.getNegative() & other.conditions.getNegative()) or \
            bool(self.effects.getPositive() & other.conditions.getPositive())

    def substitute(self, subs: Dict[Atom, float], default=None) -> ConditionalEffect:
        ce = ConditionalEffect()
        ce.conditions = self.conditions.substitute(subs, default)
        ce.effects = self.effects.substitute(subs, default)

        return ce

    def canHappen(self, sub: Dict[Atom, float or bool]):
        return self.conditions.canHappen(sub)
