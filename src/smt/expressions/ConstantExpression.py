from typing import Dict, Set

from pyeda.boolalg.bdd import BDDVariable
from pysmt.fnode import FNode

from src.smt.SMTBoolVariable import SMTBoolVariable
from src.smt.SMTExpression import SMTExpression, NUMERIC


class ConstantExpression(SMTExpression):

    def __init__(self, value):
        super().__init__()
        self.value = value
        self.type = NUMERIC

    def toBDDExpression(self, map: Dict[SMTBoolVariable, BDDVariable]):
        raise NotImplementedError()

    def getExpression(self) -> FNode:
        return self.value

    def getVariables(self) -> Set:
        return set()

    def evaluate(self, solution):
        return self.value

    def replace(self, sub):
        pass
