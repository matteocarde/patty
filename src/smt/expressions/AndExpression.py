from typing import Dict

from pyeda.boolalg.bdd import BDDVariable
from pyeda.boolalg.expr import AndOp, Variable, Complement, OrOp
from pysmt.fnode import FNode
from pysmt.shortcuts import And as SMTAnd

from src.smt.SMTBoolVariable import SMTBoolVariable
from src.smt.SMTExpression import SMTExpression
from src.smt.expressions.NaryExpression import NaryExpression


class AndExpression(NaryExpression):

    def __init__(self, *xs: SMTExpression):
        super().__init__(*xs)

    def toBDDExpression(self, map: Dict[SMTBoolVariable, BDDVariable]):
        exprs = [c.toBDDExpression(map) for c in self.children]
        f = exprs[0]
        for c in exprs[1:]:
            f = f & c
        return f

    def getExpression(self) -> FNode:
        return SMTAnd([x.getExpression() for x in self.children])

    @classmethod
    def fromBDDExpression(cls, bdd: AndOp, subs: Dict[str, SMTExpression]):
        from src.smt.expressions.OrExpression import OrExpression
        assert isinstance(bdd, AndOp)
        conjunction = []
        for x in bdd.xs:
            if isinstance(x, Variable):
                conjunction.append(subs[x.name])
            if isinstance(x, Complement):
                conjunction.append(~subs[x.top.name])
            if isinstance(x, OrOp):
                conjunction.append(OrExpression.fromBDDExpression(x, subs))
        return SMTExpression.bigand(conjunction)

    def replace(self, sub):
        return SMTExpression.bigand([c.replace(sub) for c in self.children])

    def evaluate(self, solution):
        for c in self.children:
            if not c.evaluate(solution):
                return False
        return True
