from typing import Dict, Set

from libs.pyeda.pyeda.boolalg.bdd import BDDVariable
from pysmt.fnode import FNode
from pysmt.shortcuts import Real

from src.smt.SMTBoolVariable import SMTBoolVariable
from src.smt.SMTExpression import SMTExpression, NUMERIC


class ConstantExpression(SMTExpression):

    def __init__(self, value):
        super().__init__()
        self.value = value
        self.type = NUMERIC
        self.depth = 1
        self.size = 1

    def toBDDExpression(self, map: Dict[SMTBoolVariable, BDDVariable]):
        raise NotImplementedError()

    def getExpression(self) -> FNode:
        return Real(float(self.value))

    def getVariables(self) -> Set:
        return set()

    def evaluate(self, solution):
        return self.value

    def replace(self, sub):
        pass
