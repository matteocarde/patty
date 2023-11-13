from __future__ import annotations

import copy
import itertools
from typing import Dict, Tuple, List

from src.pddl.Atom import Atom
from src.pddl.Literal import Literal
from src.pddl.Parameter import Parameter
from src.pddl.Predicate import Predicate
from src.pddl.Problem import Problem
from src.pddl.Type import Type

from src.pddl.grammar.pddlParser import pddlParser


class TypedPredicate(Predicate):
    name: str
    parameters: List[Parameter]
    atom: Atom

    def __init__(self):
        super().__init__()

    def __deepcopy__(self, m=None):
        c = TypedPredicate()
        c.name = self.name
        c.parameters = copy.deepcopy(self.parameters, m)
        c.atom = copy.deepcopy(self.atom, m)
        return c

    def __str__(self):
        paramString = ' '.join(f"{p}" for p in self.parameters)
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
                typedPredicate.parameters.append(Parameter(name, types[paramType]))

        atom = Atom.fromProperties(typedPredicate.name, [p.name for p in typedPredicate.parameters])
        typedPredicate.atom = atom

        return typedPredicate

    def getCombinations(self, problem: Problem) -> List[Tuple]:
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

    def ground(self, subs: Tuple) -> Literal:

        literal = Literal()
        literal.sign = "+"

        literal.atom = self.atom.ground(subs)
        literal.funct = literal.atom.toFunctionName()
        literal.alphaFunct = literal.atom.toAlphaFunctionName()

        return literal
