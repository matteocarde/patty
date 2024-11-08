from typing import Dict

from pyeda.boolalg.bdd import BDDVariable
from pysmt.fnode import FNode
from pysmt.shortcuts import TRUE

from src.smt.SMTBoolVariable import SMTBoolVariable
from src.smt.SMTExpression import BOOLEAN
from src.smt.expressions.NaryExpression import NaryExpression


class TrueExpression(NaryExpression):

    def __init__(self):
        super().__init__()
        self.isConstant = True
        self.type = BOOLEAN

    def __hash__(self):
        return hash(True)

    def getExpression(self) -> FNode:
        return TRUE()

    def toBDDExpression(self, map: Dict[SMTBoolVariable, BDDVariable]):
        return 1

    def evaluate(self, solution):
        return True
