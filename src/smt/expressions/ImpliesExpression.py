from typing import Dict

from pyeda.boolalg.bdd import BDDVariable
from pysmt.shortcuts import Implies

from src.smt.SMTBoolVariable import SMTBoolVariable
from src.smt.SMTExpression import SMTExpression
from src.smt.expressions.BinaryExpression import BinaryExpression


class ImpliesExpression(BinaryExpression):

    def __init__(self, *xs: SMTExpression):
        super().__init__(*xs)
        self.expression = Implies(self.lhs.expression, self.rhs.expression)

    def toBDDExpression(self, map: Dict[SMTBoolVariable, BDDVariable]):
        return ~self.lhs.toBDDExpression(map) | self.rhs.toBDDExpression(map)