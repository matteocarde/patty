from typing import Dict

from libs.pyeda.pyeda.boolalg.bdd import BDDVariable
from pysmt.fnode import FNode
from pysmt.shortcuts import Times

from src.smt.SMTBoolVariable import SMTBoolVariable
from src.smt.SMTExpression import SMTExpression, NUMERIC
from src.smt.expressions.BinaryExpression import BinaryExpression
from src.smt.expressions.ConstantExpression import ConstantExpression


class MultiplyExpression(BinaryExpression):

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
            return ConstantExpression(0)
        if isinstance(rhs, ConstantExpression) and rhs.value == 1:
            return lhs
        if isinstance(lhs, ConstantExpression) and lhs.value == 1:
            return rhs
        if isinstance(lhs, ConstantExpression) and isinstance(rhs, ConstantExpression):
            return ConstantExpression(lhs.value * rhs.value)
        return cls(lhs, rhs)

    def toBDDExpression(self, map: Dict[SMTBoolVariable, BDDVariable]):
        raise NotImplementedError()

    def getExpression(self) -> FNode:
        return Times(self.lhs.getExpression(), self.rhs.getExpression())

    def evaluate(self, solution):
        return self.lhs.evaluate(solution) * self.rhs.evaluate(solution)

    def replace(self, sub):
        pass
