from typing import Dict

from libs.pyeda.pyeda.boolalg.bdd import BDDVariable
from pysmt.fnode import FNode
from pysmt.operators import ITE
from pysmt.shortcuts import Iff
from libs.pyeda.pyeda.boolalg.expr import Or as BDDOr
from libs.pyeda.pyeda.boolalg.expr import And as BDDAnd

from src.smt.SMTBoolVariable import SMTBoolVariable
from src.smt.SMTExpression import SMTExpression, BOOLEAN
from src.smt.expressions.BinaryExpression import BinaryExpression
from src.smt.expressions.FalseExpression import FalseExpression
from src.smt.expressions.NaryExpression import NaryExpression
from src.smt.expressions.NotExpression import NotExpression
from src.smt.expressions.TrueExpression import TrueExpression


class ITEExpression(NaryExpression):

    def __init__(self, c: SMTExpression, t: SMTExpression, e: SMTExpression):
        super().__init__(c, t, e)
        self.type = BOOLEAN
        self.c = c
        self.t = t
        self.e = e

    @classmethod
    def simplify(cls, c, t, e):
        if isinstance(c, TrueExpression):
            return t
        if isinstance(c, FalseExpression):
            return e
        return cls(c, t, e)

    def toBDDExpression(self, map: Dict[SMTBoolVariable, BDDVariable]):
        raise NotImplemented()

    def getExpression(self) -> FNode:
        return ITE(self.c.getExpression(), self.t.getExpression(), self.e.getExpression())

    def evaluate(self, solution):
        if self.c.evaluate(solution):
            return self.t.evaluate(solution)
        else:
            return self.e.evaluate(solution)
