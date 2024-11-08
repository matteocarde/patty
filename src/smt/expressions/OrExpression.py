from typing import Dict

from pyeda.boolalg.bdd import BDDVariable
from pyeda.boolalg.expr import OrOp, Variable, Complement, AndOp
from pysmt.fnode import FNode
from pysmt.shortcuts import Or as SMTOr

from src.smt.SMTBoolVariable import SMTBoolVariable
from src.smt.SMTExpression import SMTExpression, BOOLEAN
from src.smt.expressions.FalseExpression import FalseExpression
from src.smt.expressions.NaryExpression import NaryExpression
from src.smt.expressions.TrueExpression import TrueExpression


class OrExpression(NaryExpression):

    def __init__(self, *xs: SMTExpression):
        super().__init__(*xs)
        self.type = BOOLEAN

    @classmethod
    def simplify(cls, lhs, rhs):
        if isinstance(rhs, TrueExpression) or isinstance(lhs, TrueExpression):
            return TrueExpression()
        if isinstance(lhs, FalseExpression):
            return rhs
        if isinstance(rhs, FalseExpression):
            return lhs
        return cls(lhs, rhs)

    def toBDDExpression(self, map: Dict[SMTBoolVariable, BDDVariable]):
        exprs = [c.toBDDExpression(map) for c in self.children]
        f = exprs[0]
        for c in exprs[1:]:
            f = f | c
        return f

    def getExpression(self) -> FNode:
        return SMTOr([x.getExpression() for x in self.children])

    @classmethod
    def fromBDDExpression(cls, bdd: OrOp, subs: Dict[str, SMTExpression]):
        from src.smt.expressions.AndExpression import AndExpression
        assert isinstance(bdd, OrOp)
        conjunction = []
        for x in bdd.xs:
            if isinstance(x, Variable):
                conjunction.append(subs[x.name])
            if isinstance(x, Complement):
                conjunction.append(~subs[x.top.name])
            if isinstance(x, AndOp):
                conjunction.append(AndExpression.fromBDDExpression(x, subs))
        return SMTExpression.bigor(conjunction)

    def replace(self, sub):
        return SMTExpression.bigor([c.replace(sub) for c in self.children])

    def evaluate(self, solution):
        for c in self.children:
            if c.evaluate(solution):
                return True
        return False
