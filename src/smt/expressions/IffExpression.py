from typing import Dict

from pyeda.boolalg.bdd import BDDVariable
from pysmt.fnode import FNode
from pysmt.shortcuts import Iff
from pyeda.boolalg.expr import Or as BDDOr
from pyeda.boolalg.expr import And as BDDAnd

from src.smt.SMTBoolVariable import SMTBoolVariable
from src.smt.SMTExpression import SMTExpression, BOOLEAN
from src.smt.expressions.BinaryExpression import BinaryExpression
from src.smt.expressions.FalseExpression import FalseExpression
from src.smt.expressions.NotExpression import NotExpression
from src.smt.expressions.TrueExpression import TrueExpression


class IffExpression(BinaryExpression):

    def __init__(self, *xs: SMTExpression):
        super().__init__(*xs)
        self.type = BOOLEAN

    @classmethod
    def simplify(cls, lhs, rhs):
        if isinstance(rhs, FalseExpression) and isinstance(lhs, FalseExpression):
            return TrueExpression()
        if isinstance(rhs, TrueExpression) and isinstance(lhs, TrueExpression):
            return TrueExpression()
        if isinstance(lhs, FalseExpression):
            return NotExpression.simplify(rhs)
        if isinstance(rhs, FalseExpression):
            return NotExpression.simplify(lhs)
        if isinstance(lhs, TrueExpression):
            return rhs
        if isinstance(rhs, TrueExpression):
            return lhs
        return cls(lhs, rhs)

    def toBDDExpression(self, map: Dict[SMTBoolVariable, BDDVariable]):
        lhs = self.lhs.toBDDExpression(map)
        rhs = self.rhs.toBDDExpression(map)
        return (lhs & rhs) | (~lhs & ~rhs)

    def getExpression(self) -> FNode:
        return Iff(self.lhs.getExpression(), self.rhs.getExpression())

    def evaluate(self, solution):
        return self.lhs.evaluate(solution) == self.rhs.evaluate(solution)
