from typing import Dict, Tuple

from libs.pyeda.pyeda.boolalg.bdd import BDDVariable
from pysmt.fnode import FNode
from pysmt.shortcuts import Iff, Plus, Minus
from libs.pyeda.pyeda.boolalg.expr import Or as BDDOr
from libs.pyeda.pyeda.boolalg.expr import And as BDDAnd

from src.smt.SMTBoolVariable import SMTBoolVariable
from src.smt.SMTExpression import SMTExpression, NUMERIC
from src.smt.expressions.BinaryExpression import BinaryExpression
from src.smt.expressions.ConstantExpression import ConstantExpression

SUBTRACT_CACHE: Dict[Tuple[SMTExpression, SMTExpression], SMTExpression] = dict()


class SubtractExpression(BinaryExpression):

    def __init__(self, *xs: SMTExpression):
        super().__init__(*xs)
        self.type = NUMERIC

    @classmethod
    def simplify(cls, *xs):
        lhs = SMTExpression.numericConstant(xs[0])
        rhs = SMTExpression.numericConstant(xs[1])
        if isinstance(rhs, ConstantExpression) and rhs.value == 0:
            return lhs
        if isinstance(lhs, ConstantExpression) and isinstance(rhs, ConstantExpression):
            return ConstantExpression.simplify(lhs.value - rhs.value)
        if (lhs, rhs) in SUBTRACT_CACHE:
            return SUBTRACT_CACHE[lhs, rhs]
        SUBTRACT_CACHE[lhs, rhs] = cls(lhs, rhs)
        return SUBTRACT_CACHE[lhs, rhs]

    def toBDDExpression(self, map: Dict[SMTBoolVariable, BDDVariable]):
        raise NotImplementedError()

    def getExpression(self, memodict=dict()) -> FNode:
        if self in memodict:
            return memodict[self]
        expr = Minus(*[c.getExpression(memodict=memodict) for c in self.children])
        memodict[self] = expr
        return expr

    def evaluate(self, solution):
        return self.lhs.evaluate(solution) - self.rhs.evaluate(solution)

    def replace(self, sub):
        pass
