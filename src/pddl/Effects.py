from __future__ import annotations

import copy

from itertools import chain
from typing import Dict, List, cast, Iterable

from src.pddl.Atom import Atom
from src.pddl.BinaryPredicate import BinaryPredicate
from src.pddl.Literal import Literal
from src.pddl.grammar.pddlParser import pddlParser
from src.pddl.grammar.pddlParser import pddlParser as p


class Effects:
    assignments: List[Literal or BinaryPredicate]

    def __init__(self):
        self.assignments = []
        pass

    def __deepcopy__(self, m=None):
        m = {} if m is None else m
        eff = copy.deepcopy(super(), m)
        eff.__class__ = Effects
        return cast(Effects, eff)

    @classmethod
    def fromNode(cls, node: pddlParser.EffectsContext) -> Effects:

        effects = cls()
        nodes: [p.EffectContext] = []

        if isinstance(node.getChild(0), p.AndEffectContext):
            nodes.extend([n.getChild(0) for n in node.getChild(0).children[2:-1]])
        else:
            nodes.append(node.getChild(0))

        for n in nodes:
            if isinstance(n, p.BooleanLiteralContext):
                effects.assignments.append(Literal.fromNode(n.getChild(0)))
            else:
                effects.assignments.append(BinaryPredicate.fromNode(n))

        return effects

    def ground(self, sub: Dict[str, str]) -> Effects:
        e = Effects()
        e.assignments = [predicate.ground(sub) for predicate in self.assignments]
        return e

    def getFunctions(self):
        return set(chain.from_iterable([c.getFunctions() for c in self.assignments if isinstance(c, BinaryPredicate)]))

    def getPredicates(self):
        return set(chain.from_iterable([c.getPredicates() for c in self.assignments]))

    def substitute(self, sub: Dict[Atom, float], default=None):
        e = Effects()
        e.assignments = [predicate.substitute(sub, default) for predicate in self.assignments]
        return e

    def __iter__(self) -> Iterable[Literal or BinaryPredicate]:
        return iter(self.assignments)

    def __str__(self):
        return str(self.assignments)

    def __repr__(self):
        return str(self.assignments)

    def __len__(self):
        return len(self.assignments)

    def toLatex(self):
        return ",".join([a.toLatex() for a in self.assignments])
        pass

    def addEffect(self, ass: Literal or BinaryPredicate):
        self.assignments.append(ass)
