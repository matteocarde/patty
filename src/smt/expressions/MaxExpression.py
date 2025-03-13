from typing import Dict

from pyeda.boolalg.bdd import BDDVariable
from pyeda.boolalg.expr import AndOp, Variable, Complement, OrOp
from pysmt.fnode import FNode
from pysmt.shortcuts import Max as SMTMax

from src.smt.SMTBoolVariable import SMTBoolVariable
from src.smt.SMTExpression import SMTExpression, BOOLEAN
from src.smt.expressions.FalseExpression import FalseExpression
from src.smt.expressions.NaryExpression import NaryExpression
from src.smt.expressions.TrueExpression import TrueExpression


class MaxExpression(NaryExpression):

    def __init__(self, *xs: SMTExpression):
        super().__init__(*xs)
        self.type = BOOLEAN

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
