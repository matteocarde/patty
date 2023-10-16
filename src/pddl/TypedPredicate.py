from __future__ import annotations
from typing import Dict, Tuple, List

from src.pddl.Predicate import Predicate
from src.pddl.Type import Type

from src.pddl.grammar.pddlParser import pddlParser


class TypedPredicate(Predicate):
    name: str
    parameters: List[Tuple[str, Type]]

    def __init__(self):
        super().__init__()

    def __str__(self):
        paramString = ' '.join(f"{x} - {t}" for (x, t) in self.parameters)
        return f"{self.name} {paramString}"

    def __repr__(self):
        return str(self)

    @classmethod
    def fromNode(cls, node: pddlParser.TypedPositiveLiteralContext, types: Dict[str, Type]) -> TypedPredicate:
        typedPredicate = cls()

        atomNode: pddlParser.AtomContext = node.getChild(1)
        typedPredicate.name = atomNode.getChild(0).getText()
        typedPredicate.parameters = []

        for parameterNode in atomNode.children[1:]:
            paramNames = []
            paramType = None
            for c in parameterNode.children:
                if isinstance(c, pddlParser.LiftedAtomParameterContext):
                    paramNames.append(c.getText())
                if isinstance(c, pddlParser.TypeNameContext):
                    paramType = c.getText()
            for name in paramNames:
                typedPredicate.parameters.append((name, types[paramType]))

        return typedPredicate
