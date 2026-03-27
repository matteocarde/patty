from typing import Dict

from pyeda.boolalg.bdd import BDDVariable
from pyeda.boolalg.expr import AndOp, Variable, Complement, OrOp
from pysmt.fnode import FNode
from pysmt.shortcuts import Min as SMTMin

from src.smt.SMTBoolVariable import SMTBoolVariable
from src.smt.SMTExpression import SMTExpression, BOOLEAN, NUMERIC
from src.smt.expressions.FalseExpression import FalseExpression
from src.smt.expressions.NaryExpression import NaryExpression
from src.smt.expressions.TrueExpression import TrueExpression


class MinExpression(NaryExpression):

    def __init__(self, *xs: SMTExpression or float):
        super().__init__(*xs)
        self.type = NUMERIC

    @classmethod
    def simplify(cls, lhs, rhs):
        raise NotImplementedError()

    def toBDDExpression(self, map: Dict[SMTBoolVariable, BDDVariable]):
        raise NotImplementedError()

    def getExpression(self, memodict=dict()) -> FNode:
        if self in memodict:
            return memodict[self]
        expr = SMTMin([x.getExpression(memodict=memodict) for x in self.children])
        memodict[self] = expr
        return expr

    @classmethod
    def fromBDDExpression(cls, bdd: AndOp, subs: Dict[str, SMTExpression]):
        raise NotImplementedError()

    def replace(self, sub):
        raise NotImplementedError()

    def evaluate(self, solution):
        raise NotImplementedError()
