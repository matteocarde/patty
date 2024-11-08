from typing import Dict

from pyeda.boolalg.bdd import BDDVariable
from pysmt.fnode import FNode
from pysmt.shortcuts import Plus, Equals

from src.smt.SMTBoolVariable import SMTBoolVariable
from src.smt.SMTExpression import SMTExpression, NUMERIC, BOOLEAN
from src.smt.expressions.BinaryExpression import BinaryExpression
from src.smt.expressions.ConstantExpression import ConstantExpression
from src.smt.expressions.FalseExpression import FalseExpression
from src.smt.expressions.IffExpression import IffExpression
from src.smt.expressions.TrueExpression import TrueExpression


class EqualExpression(BinaryExpression):

    def __init__(self, *xs: SMTExpression):
        super().__init__(*xs)
        self.type = NUMERIC

    @classmethod
    def simplify(cls, *xs):
        lhs = SMTExpression.numericConstant(xs[0])
        rhs = SMTExpression.numericConstant(xs[1])
        if lhs.type != rhs.type:
            raise Exception()
        if lhs.type == BOOLEAN:
            return IffExpression(lhs, rhs)
        if isinstance(lhs, ConstantExpression) and isinstance(rhs, ConstantExpression):
            return TrueExpression() if lhs.value == rhs.value else FalseExpression()
        return cls(lhs, rhs)

    def toBDDExpression(self, map: Dict[SMTBoolVariable, BDDVariable]):
        raise NotImplementedError()

    def getExpression(self) -> FNode:
        return Equals(self.lhs.getExpression(), self.rhs.getExpression())

    def evaluate(self, solution):
        return self.lhs.evaluate(solution) == self.rhs.evaluate(solution)

    def replace(self, sub):
        pass
