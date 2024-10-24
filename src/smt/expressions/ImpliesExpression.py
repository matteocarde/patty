from typing import Dict

from pyeda.boolalg.bdd import BDDVariable
from pysmt.fnode import FNode
from pysmt.shortcuts import Implies

from src.smt.SMTBoolVariable import SMTBoolVariable
from src.smt.SMTExpression import SMTExpression
from src.smt.expressions.BinaryExpression import BinaryExpression


class ImpliesExpression(BinaryExpression):

    def __init__(self, *xs: SMTExpression):
        super().__init__(*xs)

    def toBDDExpression(self, map: Dict[SMTBoolVariable, BDDVariable]):
        return ~self.lhs.toBDDExpression(map) | self.rhs.toBDDExpression(map)

    def getExpression(self) -> FNode:
        return Implies(self.lhs.getExpression(), self.rhs.getExpression())

    def evaluate(self, solution):
        if not self.lhs.evaluate(solution):
            return True
        return self.rhs.evaluate(solution)
