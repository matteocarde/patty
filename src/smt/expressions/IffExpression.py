from typing import Dict

from pyeda.boolalg.bdd import BDDVariable
from pysmt.shortcuts import Iff
from pyeda.boolalg.expr import Or as BDDOr
from pyeda.boolalg.expr import And as BDDAnd

from src.smt.SMTBoolVariable import SMTBoolVariable
from src.smt.SMTExpression import SMTExpression
from src.smt.expressions.BinaryExpression import BinaryExpression


class IffExpression(BinaryExpression):

    def __init__(self, *xs: SMTExpression):
        super().__init__(*xs)
        self.expression = Iff(self.lhs.expression, self.rhs.expression)

    def toBDDExpression(self, map: Dict[SMTBoolVariable, BDDVariable]):
        lhs = self.lhs.toBDDExpression(map)
        rhs = self.rhs.toBDDExpression(map)
        return (lhs & rhs) | (~lhs & ~rhs)

    def evaluate(self, solution):
        return self.lhs.evaluate(solution) == self.rhs.evaluate(solution)
