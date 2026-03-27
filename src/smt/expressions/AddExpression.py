from typing import Dict, Tuple

from libs.pyeda.pyeda.boolalg.bdd import BDDVariable
from pysmt.fnode import FNode
from pysmt.shortcuts import Iff, Plus
from libs.pyeda.pyeda.boolalg.expr import Or as BDDOr
from libs.pyeda.pyeda.boolalg.expr import And as BDDAnd

from src.smt.SMTBoolVariable import SMTBoolVariable
from src.smt.SMTExpression import SMTExpression, NUMERIC
from src.smt.expressions.BinaryExpression import BinaryExpression
from src.smt.expressions.ConstantExpression import ConstantExpression
from src.smt.expressions.NaryExpression import NaryExpression

ADD_CACHE: Dict[Tuple[SMTExpression, SMTExpression], SMTExpression] = dict()


class AddExpression(NaryExpression):

    def __init__(self, *xs: SMTExpression):
        super().__init__(*xs)
        self.type = NUMERIC

    @classmethod
    def simplify(cls, lhs, rhs):
        lhs = SMTExpression.numericConstant(lhs)
        rhs = SMTExpression.numericConstant(rhs)
        if isinstance(lhs, ConstantExpression) and lhs.value == 0:
            return rhs
        if isinstance(rhs, ConstantExpression) and rhs.value == 0:
            return lhs
        if isinstance(lhs, ConstantExpression) and isinstance(rhs, ConstantExpression):
            return ConstantExpression.simplify(lhs.value + rhs.value)
        if isinstance(lhs, AddExpression):
            children = lhs.children + [rhs]
            return AddExpression(*children)
        if isinstance(rhs, AddExpression):
            children = rhs.children + [lhs]
            return AddExpression(*children)
        if (lhs, rhs) in ADD_CACHE:
            return ADD_CACHE[lhs, rhs]
        ADD_CACHE[lhs, rhs] = cls(lhs, rhs)
        return ADD_CACHE[lhs, rhs]

    def toBDDExpression(self, map: Dict[SMTBoolVariable, BDDVariable]):
        raise NotImplementedError()

    def getExpression(self, memodict=dict()) -> FNode:
        if self in memodict:
            return memodict[self]
        expr = Plus(*[c.getExpression(memodict=memodict) for c in self.children])
        memodict[self] = expr
        return expr

    def evaluate(self, solution):
        return self.lhs.evaluate(solution) + self.rhs.evaluate(solution)

    def replace(self, sub):
        pass
