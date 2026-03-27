from typing import Dict

from libs.pyeda.pyeda.boolalg.bdd import BDDVariable
from libs.pyeda.pyeda.boolalg.expr import Not as BDDNot
from pysmt.fnode import FNode
from pysmt.shortcuts import Not as SMTNot

from src.smt.SMTBoolVariable import SMTBoolVariable
from src.smt.SMTExpression import SMTExpression, BOOLEAN
from pysmt.typing import BOOL

from src.smt.expressions.FalseExpression import FalseExpression
from src.smt.expressions.TrueExpression import TrueExpression
from src.smt.expressions.UnaryExpression import UnaryExpression

NOT_EXPRESSION_CACHE: Dict[SMTExpression, SMTExpression] = dict()


class NotExpression(UnaryExpression):

    def __init__(self, expr: SMTExpression):
        super().__init__(expr)
        self.positive = expr
        self.type = BOOLEAN

    def __hash__(self):
        return hash(-hash(self.positive))

    @classmethod
    def simplify(cls, pos):
        if isinstance(pos, TrueExpression):
            return FalseExpression()
        if isinstance(pos, FalseExpression):
            return TrueExpression()
        if pos in NOT_EXPRESSION_CACHE:
            return NOT_EXPRESSION_CACHE[pos]
        expr = cls(pos)
        NOT_EXPRESSION_CACHE[pos] = expr
        return expr

    def getExpression(self, memodict=dict()) -> FNode:
        if self in memodict:
            return memodict[self]
        expr = SMTNot(self.positive.getExpression(memodict=memodict))
        memodict[self] = expr
        return expr

    def toBDDExpression(self, map: Dict[SMTBoolVariable, BDDVariable]):
        x = self.positive.toBDDExpression(map)
        f = ~x
        return f

    def replace(self, sub):
        return ~self.positive.replace(sub)

    def evaluate(self, solution):
        if self.positive.evaluate(solution):
            return False
        return True
