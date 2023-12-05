from __future__ import annotations
from typing import Dict, Tuple, List

from src.pddl.PDDLWriter import PDDLWriter
from src.pddl.Predicate import Predicate
from src.pddl.Type import Type
from src.pddl.Utilities import Utilities

from src.pddl.grammar.pddlParser import pddlParser


class TypedPredicate(Predicate):
    name: str
    parameters: List[Tuple[str, Type]]

    def __init__(self):
        super().__init__()

    def __str__(self):
        strParameters = [f"{p} - {t.name}" for (p, t) in self.parameters]
        return f"{self.name}({','.join(strParameters)})"

    def __repr__(self):
        return str(self)

    @classmethod
    def fromNode(cls, node: pddlParser.TypedPositiveLiteralContext, types: Dict[str, Type]) -> TypedPredicate:
        typedPredicate = cls()

        atomNode: pddlParser.TypedAtomContext = node.getChild(1)
        typedPredicate.name = atomNode.getChild(0).getText()
        typedPredicate.parameters = []

        for parameterNode in atomNode.children[1:]:
            if not isinstance(parameterNode, pddlParser.TypedAtomParameterContext):
                raise Exception(f"Typed predicate {typedPredicate.name} is not types")
            paramName = parameterNode.getChild(0).getText()
            paramType = parameterNode.getChild(2).getText()
            if paramType not in types:
                raise Exception(f"{paramType} is not in types list")
            typedPredicate.parameters.append((paramName, types[paramType]))

        return typedPredicate

    @classmethod
    def fromString(cls, string: str, types: Dict[str, Type]):
        return cls.fromNode(Utilities.getParseTree(string).typedPositiveLiteral(), types)

    def toPDDL(self, pw: PDDLWriter = PDDLWriter()):
        parameters = " ".join([f"{p.name} - {p.type.name}" for p in self.parameters])
        pw.write(f"({self.name} {parameters})")
        pass
