from typing import Dict

from libs.pyeda.pyeda.boolalg.bdd import BDDVariable
from pysmt.fnode import FNode
from pysmt.shortcuts import Implies

from src.smt.SMTBoolVariable import SMTBoolVariable
from src.smt.SMTExpression import SMTExpression, BOOLEAN
from src.smt.expressions.BinaryExpression import BinaryExpression
from src.smt.expressions.FalseExpression import FalseExpression
from src.smt.expressions.NotExpression import NotExpression
from src.smt.expressions.TrueExpression import TrueExpression


class ImpliesExpression(BinaryExpression):

    def __init__(self, *xs: SMTExpression):
        super().__init__(*xs)
        self.type = BOOLEAN

    @classmethod
    def simplify(cls, lhs, rhs):
        if isinstance(lhs, FalseExpression):
            return TrueExpression()
        if isinstance(lhs, TrueExpression):
            return rhs
        if isinstance(rhs, TrueExpression):
            return TrueExpression()
        if isinstance(rhs, FalseExpression):
            return NotExpression.simplify(lhs)
        return cls(lhs, rhs)

    def toBDDExpression(self, map: Dict[SMTBoolVariable, BDDVariable]):
        return ~self.lhs.toBDDExpression(map) | self.rhs.toBDDExpression(map)

    def getExpression(self) -> FNode:
        return Implies(self.lhs.getExpression(), self.rhs.getExpression())

    def evaluate(self, solution):
        if not self.lhs.evaluate(solution):
            return True
        return self.rhs.evaluate(solution)
