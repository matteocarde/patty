from __future__ import annotations

import copy
from sympy import Expr
from typing import Dict, Set

from src.pddl.Atom import Atom
from src.pddl.Predicate import Predicate
from src.pddl.grammar.pddlParser import pddlParser


class Constant(Predicate):
    value: float
    isDelta: bool

    def __init__(self, value=0):
        super().__init__()
        self.value = float(value)
        self.isDelta = False

    def __deepcopy__(self, m=None) -> Constant:
        m = {} if m is None else m
        c = Constant()
        c.value = self.value
        c.isDelta = self.isDelta
        return c

    @classmethod
    def fromValue(cls, value: float):
        c = cls()
        c.value = value
        return c

    @classmethod
    def fromNode(cls, node: pddlParser.ConstantContext or pddlParser.NumberContext) -> Constant:

        constant = cls()
        constant.isDelta = False
        if isinstance(node, pddlParser.NumberContext):
            constant.value = float(node.getText())
            return constant

        child = node.getChild(0)
        if isinstance(child, pddlParser.NumberContext):
            constant.value = float(child.getText())
        elif isinstance(child, pddlParser.DeltaContext):
            constant.isDelta = True

        return constant

    def ground(self, subs: Dict[str, str]) -> Constant:
        constant = Constant()
        constant.value = self.value
        constant.isDelta = self.isDelta

        return constant

    def __str__(self):
        return "#t" if self.isDelta else str(self.value)

    def __repr__(self):
        return str(self)

    def getPredicates(self) -> Set[Atom]:
        return set()

    def getFunctions(self) -> Set[Atom]:
        return set()

    def substitute(self, subs: Dict[Atom, float], default=None) -> Predicate:
        return self

    def isLinearIncrement(self):
        raise False

    def getLinearIncrement(self) -> float:
        return self.value

    def toExpression(self) -> Expr or float:
        return self.value

    def expressify(self, symbols: Dict[Atom, Expr]) -> Expr or float:
        return self.value

    def replace(self, atom: Atom, w):
        return copy.deepcopy(self)

    def toLatex(self) -> str:
        return r"\delta_e" if self.isDelta else str(self.value)
