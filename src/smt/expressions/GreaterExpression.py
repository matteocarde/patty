from typing import Dict, Tuple

from pysmt.fnode import FNode
from pysmt.shortcuts import GT

from libs.pyeda.pyeda.boolalg.bdd import BDDVariable
from src.smt.SMTBoolVariable import SMTBoolVariable
from src.smt.SMTExpression import SMTExpression, NUMERIC
from src.smt.expressions.BinaryExpression import BinaryExpression
from src.smt.expressions.ConstantExpression import ConstantExpression
from src.smt.expressions.FalseExpression import FalseExpression
from src.smt.expressions.NotExpression import NotExpression
from src.smt.expressions.TrueExpression import TrueExpression

GREATER_CACHE: Dict[Tuple[SMTExpression, SMTExpression], SMTExpression] = dict()


class GreaterExpression(BinaryExpression):

    def __init__(self, *xs: SMTExpression):
        super().__init__(*xs)
        self.type = NUMERIC

    @classmethod
    def simplify(cls, *xs):
        if isinstance(xs[0], SMTBoolVariable) and xs[1] == 0:
            # "b > 0", with b boolean becomes just "b"
            return xs[0]
        lhs = SMTExpression.numericConstant(xs[0])
        rhs = SMTExpression.numericConstant(xs[1])
        if isinstance(lhs, ConstantExpression) and isinstance(rhs, ConstantExpression):
            return TrueExpression() if lhs.value > rhs.value else FalseExpression()
        if (lhs, rhs) in GREATER_CACHE:
            return GREATER_CACHE[lhs, rhs]
        GREATER_CACHE[lhs, rhs] = cls(lhs, rhs)
        return GREATER_CACHE[lhs, rhs]

    def toBDDExpression(self, map: Dict[SMTBoolVariable, BDDVariable]):
        raise NotImplementedError()

    def getExpression(self, memodict=dict()) -> FNode:
        if self in memodict:
            return memodict[self]
        expr = GT(self.lhs.getExpression(memodict=memodict), self.rhs.getExpression(memodict=memodict))
        memodict[self] = expr
        return expr

    def evaluate(self, solution):
        return self.lhs.evaluate(solution) > self.rhs.evaluate(solution)

    def replace(self, sub):
        pass
