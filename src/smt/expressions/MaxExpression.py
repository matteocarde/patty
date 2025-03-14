from typing import Dict

from pysmt.fnode import FNode
from pysmt.shortcuts import Max as SMTMax

from pyeda.boolalg.bdd import BDDVariable
from pyeda.boolalg.expr import AndOp
from src.smt.SMTBoolVariable import SMTBoolVariable
from src.smt.SMTExpression import SMTExpression, NUMERIC
from src.smt.expressions.NaryExpression import NaryExpression


class MaxExpression(NaryExpression):

    def __init__(self, *xs: SMTExpression):
        super().__init__(*xs)
        self.type = NUMERIC

    @classmethod
    def simplify(cls, lhs, rhs):
        raise NotImplementedError()

    def toBDDExpression(self, map: Dict[SMTBoolVariable, BDDVariable]):
        raise NotImplementedError()

    def getExpression(self) -> FNode:
        return SMTMax([x.getExpression() for x in self.children])

    @classmethod
    def fromBDDExpression(cls, bdd: AndOp, subs: Dict[str, SMTExpression]):
        raise NotImplementedError()

    def replace(self, sub):
        raise NotImplementedError()

    def evaluate(self, solution):
        raise NotImplementedError()

    def __str__(self):
        return f"max({','.join([str(c) for c in self.children])})"
