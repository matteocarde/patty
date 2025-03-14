from typing import Dict

from pysmt.fnode import FNode
from pysmt.shortcuts import Ite

from libs.pyeda.pyeda.boolalg.bdd import BDDVariable
from src.smt.SMTBoolVariable import SMTBoolVariable
from src.smt.SMTExpression import SMTExpression, BOOLEAN
from src.smt.expressions.FalseExpression import FalseExpression
from src.smt.expressions.NaryExpression import NaryExpression
from src.smt.expressions.TrueExpression import TrueExpression


class ITEExpression(NaryExpression):

    def __init__(self, c: SMTExpression, t: SMTExpression or float, e: SMTExpression or float):
        super().__init__(c, t, e)
        self.type = BOOLEAN
        self.c = self.children[0]
        self.t = self.children[1]
        self.e = self.children[2]

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
        return Ite(self.c.getExpression(), self.t.getExpression(), self.e.getExpression())

    def evaluate(self, solution):
        if self.c.evaluate(solution):
            return self.t.evaluate(solution)
        else:
            return self.e.evaluate(solution)
