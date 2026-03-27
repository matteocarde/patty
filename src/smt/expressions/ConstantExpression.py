from typing import Dict, Set

from libs.pyeda.pyeda.boolalg.bdd import BDDVariable
from pysmt.fnode import FNode
from pysmt.shortcuts import Real

from src.smt.SMTBoolVariable import SMTBoolVariable
from src.smt.SMTExpression import SMTExpression, NUMERIC

CONSTANT_CACHE: Dict[float, SMTExpression] = dict()


class ConstantExpression(SMTExpression):

    def __init__(self, value):
        super().__init__()
        self.value = value
        self.type = NUMERIC
        self.variables = set()

    def toBDDExpression(self, map: Dict[SMTBoolVariable, BDDVariable]):
        raise NotImplementedError()

    @classmethod
    def simplify(cls, value):
        if value in CONSTANT_CACHE:
            return CONSTANT_CACHE[value]
        CONSTANT_CACHE[value] = cls(value)
        return CONSTANT_CACHE[value]

    def getExpression(self, memodict=dict()) -> FNode:
        if self.value in memodict:
            return memodict[self.value]
        expr = Real(float(self.value))
        memodict[self.value] = expr
        return expr

    def getVariables(self) -> Set:
        return set()

    def evaluate(self, solution):
        return self.value

    def replace(self, sub):
        pass
