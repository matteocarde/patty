from __future__ import annotations

from typing import List, Set

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
