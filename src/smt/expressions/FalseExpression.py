from typing import Dict, Set

from pysmt.fnode import FNode
from pysmt.shortcuts import FALSE

from libs.pyeda.pyeda.boolalg.bdd import BDDVariable
from src.smt.SMTBoolVariable import SMTBoolVariable
from src.smt.SMTExpression import SMTExpression, BOOLEAN


class FalseExpression(SMTExpression):

    def __init__(self):
        super().__init__()
        self.type = BOOLEAN
        self.depth = 1
        self.size = 0

    def __hash__(self):
        return hash(True)

    def getExpression(self) -> FNode:
        return FALSE()

    def getVariables(self) -> Set:
        return set()

    def toBDDExpression(self, map: Dict[SMTBoolVariable, BDDVariable]):
        return 0

    def evaluate(self, solution):
        return False
