from __future__ import annotations

import itertools
from typing import Dict, Tuple, List

from src.pddl.Atom import Atom
from src.pddl.Parameter import Parameter
from src.pddl.PDDLWriter import PDDLWriter
from src.pddl.Predicate import Predicate
from src.pddl.Type import Type
from src.pddl.Utilities import Utilities

from src.pddl.grammar.pddlParser import pddlParser


class TypedPredicate(Predicate):
    name: str
    parameters: List[Parameter]
    atom: Atom

    def __init__(self):
        super().__init__()

    def __str__(self):
        strParameters = [f"{p.name} - {p.type.name}" for p in self.parameters]
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
            paramNames = []
            paramType = None
            for c in parameterNode.children:
                if isinstance(c, pddlParser.LiftedAtomParameterContext):
                    paramNames.append(c.getText().lower())
                if isinstance(c, pddlParser.TypeNameContext):
                    paramType = c.getText().lower()
            for name in paramNames:
                typedPredicate.parameters.append(Parameter(name, types[paramType]))

        atom = Atom.fromProperties(typedPredicate.name, [p.name for p in typedPredicate.parameters])
        typedPredicate.atom = atom

        return typedPredicate

    def getCombinations(self, problem) -> List[Tuple]:
        subs: List[List[str]] = list()
        for parameter in self.parameters:
            pSubs = list()
            for childType in parameter.type.getMeAndMyChildren():
                if childType.name not in problem.objectsByType:
                    continue
                pSubs += problem.objectsByType[childType.name]
            subs.append(pSubs)

        combinations = list(itertools.product(*subs))

        return combinations

    def ground(self, subs: Dict[Atom, float], delta=1):

        from src.pddl.Literal import Literal
        literal = Literal()
        literal.sign = "+"

        literal.atom = self.atom.ground(subs)
        literal.funct = literal.atom.toFunctionName()
        literal.alphaFunct = literal.atom.toAlphaFunctionName()

        return literal

    @classmethod
    def fromString(cls, string: str, types: Dict[str, Type]):
        return cls.fromNode(Utilities.getParseTree(string).typedPositiveLiteral(), types)

    def toPDDL(self, pw: PDDLWriter = PDDLWriter()):
        parameters = " ".join([f"{p.name} - {p.type.name}" for p in self.parameters])
        pw.write(f"({self.name} {parameters})")
        pass
