from typing import Dict

from pyeda.boolalg.bdd import BDDVariable
from pysmt.fnode import FNode
from pysmt.shortcuts import Iff, Plus
from pyeda.boolalg.expr import Or as BDDOr
from pyeda.boolalg.expr import And as BDDAnd

from src.smt.SMTBoolVariable import SMTBoolVariable
from src.smt.SMTExpression import SMTExpression, NUMERIC
from src.smt.expressions.BinaryExpression import BinaryExpression
from src.smt.expressions.ConstantExpression import ConstantExpression
from src.smt.expressions.NaryExpression import NaryExpression


class AddExpression(NaryExpression):

    def __init__(self, *xs: SMTExpression):
        super().__init__(*xs)
        self.type = NUMERIC

    @classmethod
    def simplify(cls, lhs, rhs):
        lhs = SMTExpression.numericConstant(lhs)
        rhs = SMTExpression.numericConstant(rhs)
        if isinstance(lhs, ConstantExpression) and lhs.value == 0:
            return rhs
        if isinstance(rhs, ConstantExpression) and rhs.value == 0:
            return lhs
        if isinstance(lhs, ConstantExpression) and isinstance(rhs, ConstantExpression):
            return ConstantExpression(lhs.value + rhs.value)
        if isinstance(lhs, AddExpression):
            lhs.children.append(rhs)
            return lhs
        if isinstance(rhs, AddExpression):
            rhs.children.append(lhs)
            return rhs
        return cls(lhs, rhs)

    def toBDDExpression(self, map: Dict[SMTBoolVariable, BDDVariable]):
        raise NotImplementedError()

    def getExpression(self) -> FNode:
        return Plus(*[c.getExpression() for c in self.children])

    def evaluate(self, solution):
        return self.lhs.evaluate(solution) + self.rhs.evaluate(solution)

    def replace(self, sub):
        pass
