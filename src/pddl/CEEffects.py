from __future__ import annotations

import copy
from typing import List, Set, Dict, cast

from src.pddl.Atom import Atom
from src.pddl.BinaryPredicate import BinaryPredicate
from src.pddl.Literal import Literal
from src.pddl.Effects import Effects
from src.pddl.grammar.pddlParser import pddlParser as p


class CEEffects(Effects):
    assignments: List[Literal or BinaryPredicate]

    def __init__(self):
        super().__init__()
        self.assignments = list()

    @classmethod
    def fromNode(cls, node: p.CeEffContext) -> CEEffects:

        effects = cls()
        nodes: [p.EffectContext] = []

        if type(node.getChild(0)) in {p.AndEffectNoCesContext}:
            nodes.extend([n.getChild(0) for n in node.getChild(0).children[2:-1]])
        else:
            nodes.append(node.getChild(0).getChild(0))

        for n in nodes:
            if isinstance(n, p.BooleanLiteralContext):
                effects.assignments.append(Literal.fromNode(n.getChild(0)))
            else:
                effects.assignments.append(BinaryPredicate.fromNode(n))

        return effects

    def getPositive(self) -> Set[Atom]:
        return {e for e in self.assignments if isinstance(e, Literal) and e.sign == "+"}

    def getNegative(self) -> Set[Atom]:
        return {e for e in self.assignments if isinstance(e, Literal) and e.sign == "-"}

    def ground(self, subs: Dict[str, str], delta=1) -> CEEffects:
        g = super().ground(subs, delta)
        g.__class__ = CEEffects
        return cast(CEEffects, g)

    def substitute(self, subs: Dict[Atom, float], default=None) -> CEEffects:
        s = super().substitute(subs, default)
        s.__class__ = CEEffects
        return cast(CEEffects, s)

    def __deepcopy__(self, m=None):
        m = {} if m is None else m
        eff = copy.deepcopy(super(), m)
        eff.__class__ = CEEffects
        return cast(CEEffects, eff)
