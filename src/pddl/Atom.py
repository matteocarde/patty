from __future__ import annotations

from typing import Dict

from sympy import Symbol, Expr

from src.pddl.Utilities import Utilities
from src.pddl.grammar.pddlParser import pddlParser as p


class Atom:
    name: str
    __string: str
    __hash: int
    __functionName: str
    __alphaFunctionName: str
    attributes: list[str]

    def __init__(self):
        self.attributes = []
        pass

    @classmethod
    def fromNode(cls, node: p.AtomContext) -> Atom:
        atom = cls()
        atom.name = node.getChild(0).getText()
        node: p.GroundAtomParameterContext or p.LiftedAtomParameterContext
        for attr in node.children[1:]:
            atom.attributes.append(attr.getText())

        atom.__setProperties()

        return atom

    def __setProperties(self):
        parts = [self.name] + [a for a in self.attributes]
        self.__string = " ".join(parts)
        self.__hash = hash(self.__string)
        parameters = ','.join([a for a in self.attributes])
        parenthesis = f"({parameters})" if self.attributes else ""
        name = self.name.replace("_", r"\_")
        self.__functionName = f"{name}{parenthesis}"
        self.__alphaFunctionName = f"\\alpha_{{{name + parenthesis}}}"

    def ground(self, subs: Dict[str, str]) -> Atom:
        atom = Atom()
        atom.name = self.name
        atom.attributes = [subs[attr] for attr in self.attributes]
        atom.__setProperties()
        return atom

    def __str__(self):
        return self.__string

    def __repr__(self):
        return str(self)

    def __hash__(self):
        return hash(str(self))

    def __eq__(self, other: Atom):
        if not isinstance(other, Atom):
            return False
        return self.__string == other.__string

    def toFunctionName(self):
        return self.__functionName

    def toAlphaFunctionName(self):
        return self.__alphaFunctionName

    def toExpression(self) -> Expr:
        return Symbol(self.__functionName)

    @classmethod
    def fromString(cls, string):
        return cls.fromNode(Utilities.getParseTree(string).atom())

    def toLatex(self):
        return f"\\operatorname{{{self.__functionName}}}"
