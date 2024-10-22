from typing import Dict

from pyeda.boolalg.bdd import BDDVariable
from pysmt.shortcuts import TRUE, FALSE

from src.smt.SMTBoolVariable import SMTBoolVariable
from src.smt.SMTExpression import SMTExpression


class FalseExpression(SMTExpression):

    def __init__(self):
        super().__init__()
        self.expression = FALSE()
        self.isConstant = True

    def __hash__(self):
        return hash(self.expression)

    def toBDDExpression(self, map: Dict[SMTBoolVariable, BDDVariable]):
        return 0

    def evaluate(self, solution):
        return False