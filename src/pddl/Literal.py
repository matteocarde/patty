from __future__ import annotations

from sympy import Expr
from typing import Dict, Set

from src.pddl.Atom import Atom
from src.pddl.Constant import Constant
from src.pddl.Predicate import Predicate
from src.pddl.Utilities import Utilities
from src.pddl.grammar.pddlParser import pddlParser as p


class Literal(Predicate):
    sign: str
    atom: Atom
    funct: str

    def __init__(self):
        super().__init__()

    @classmethod
    def fromAtom(cls, atom: Atom, sign: str):
        lit = cls()
        lit.atom = atom
        lit.sign = sign
        return lit

    @classmethod
    def fromNode(cls, node: p.PositiveLiteralContext or p.NegativeLiteralContext) -> Literal:
        literal = cls()

        literal.sign = "+" if isinstance(node, p.PositiveLiteralContext) else "-"
        positiveLiteralNode = node.getChild(2) if literal.sign == "-" else node
        atomNode = positiveLiteralNode.getChild(1)

        literal.atom = Atom.fromNode(atomNode)
        literal.string = f"({literal.atom})"
        literal.funct = literal.atom.toFunctionName()
        literal.alphaFunct = literal.atom.toAlphaFunctionName()

        return literal

    def getPredicates(self) -> Set[Atom]:
        return {self.atom}

    def getFunctions(self) -> Set[Atom]:
        return {self.atom}

    def getAtom(self) -> Atom:
        return self.atom

    def ground(self, subs: Dict[str, str]) -> Literal:

        literal = Literal()
        literal.sign = self.sign

        literal.atom = self.atom.ground(subs)
        literal.funct = literal.atom.toFunctionName()
        literal.alphaFunct = literal.atom.toAlphaFunctionName()

        return literal

    def __str__(self):
        if self.sign == "+":
            return f"({self.atom})"
        else:
            return f"(not ({self.atom}))"

    def __repr__(self):
        return str(self)

    @classmethod
    def fromPositiveString(cls, string: str) -> Literal:
        return cls.fromNode(Utilities.getParseTree(string).positiveLiteral())

    @classmethod
    def fromNegativeString(cls, string: str) -> Literal:
        return cls.fromNode(Utilities.getParseTree(string).negativeLiteral())

    def toLatex(self) -> str:
        if self.sign == "+":
            return self.atom.toLatex()
        return f"(\\neg {self.atom.toLatex()})"

    def __hash__(self):
        return hash(self.sign + str(self.atom))

    def substitute(self, subs: Dict[Atom, float], default=None) -> Predicate:
        if self.atom not in subs and default is None:
            return self
        if self.atom not in subs and default is not None:
            return Constant(default)
        if self.atom in subs:
            return Constant(subs[self.atom])

    def getLinearIncrement(self) -> float:
        return 0

    def toExpression(self) -> Expr:
        return self.atom.toExpression()
