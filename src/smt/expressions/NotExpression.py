from typing import Dict

from pyeda.boolalg.bdd import BDDVariable
from pyeda.boolalg.expr import Not as BDDNot
from pysmt.shortcuts import Not as SMTNot

from src.smt.SMTBoolVariable import SMTBoolVariable
from src.smt.SMTExpression import SMTExpression
from pysmt.typing import BOOL

from src.smt.expressions.UnaryExpression import UnaryExpression


class NotExpression(UnaryExpression):

    def __init__(self, expr: SMTExpression):
        super().__init__(expr)
        self.variables = expr.variables
        self.positive = expr
        self.type = BOOL
        self.expression = SMTNot(expr.expression)

    def __hash__(self):
        return hash(self.expression)

    def toBDDExpression(self, map: Dict[SMTBoolVariable, BDDVariable]):
        x = self.positive.toBDDExpression(map)
        f = ~x
        return f

    def replace(self, sub):
        return ~self.positive.replace(sub)
