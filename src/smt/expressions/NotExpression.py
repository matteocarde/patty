from typing import Dict

from pyeda.boolalg.bdd import BDDVariable
from pyeda.boolalg.expr import Not as BDDNot
from pysmt.fnode import FNode
from pysmt.shortcuts import Not as SMTNot

from src.smt.SMTBoolVariable import SMTBoolVariable
from src.smt.SMTExpression import SMTExpression, BOOLEAN
from pysmt.typing import BOOL

from src.smt.expressions.FalseExpression import FalseExpression
from src.smt.expressions.TrueExpression import TrueExpression
from src.smt.expressions.UnaryExpression import UnaryExpression


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
        return cls(pos)

    def getExpression(self) -> FNode:
        return SMTNot(self.positive.getExpression())

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
