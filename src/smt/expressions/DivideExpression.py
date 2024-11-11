from typing import Dict

from pyeda.boolalg.bdd import BDDVariable
from pysmt.fnode import FNode
from pysmt.shortcuts import Iff, Plus, Times, Div
from pyeda.boolalg.expr import Or as BDDOr
from pyeda.boolalg.expr import And as BDDAnd

from src.smt.SMTBoolVariable import SMTBoolVariable
from src.smt.SMTExpression import SMTExpression, NUMERIC
from src.smt.expressions.BinaryExpression import BinaryExpression
from src.smt.expressions.ConstantExpression import ConstantExpression


class DivideExpression(BinaryExpression):

    def __init__(self, *xs: SMTExpression):
        super().__init__(*xs)
        self.type = NUMERIC

    @classmethod
    def simplify(cls, *xs):
        lhs = SMTExpression.numericConstant(xs[0])
        rhs = SMTExpression.numericConstant(xs[1])
        if isinstance(lhs, ConstantExpression) and lhs.value == 0:
            return ConstantExpression(0)
        if isinstance(rhs, ConstantExpression) and rhs.value == 0:
            raise ZeroDivisionError()
        if isinstance(rhs, ConstantExpression) and rhs.value == 1:
            return lhs
        if isinstance(lhs, ConstantExpression) and lhs.value == 1:
            return rhs
        if isinstance(lhs, ConstantExpression) and isinstance(rhs, ConstantExpression):
            return ConstantExpression(lhs.value / rhs.value)
        return cls(lhs, rhs)

    def toBDDExpression(self, map: Dict[SMTBoolVariable, BDDVariable]):
        raise NotImplementedError()

    def getExpression(self) -> FNode:
        return Div(self.lhs.getExpression(), self.rhs.getExpression())

    def evaluate(self, solution):
        return self.lhs.evaluate(solution) / self.rhs.evaluate(solution)

    def replace(self, sub):
        pass
