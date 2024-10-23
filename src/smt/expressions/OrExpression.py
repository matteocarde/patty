from typing import Dict

from pyeda.boolalg.bdd import BDDVariable
from pyeda.boolalg.expr import OrOp, Variable, Complement, AndOp
from pysmt.shortcuts import Or as SMTOr

from src.smt.SMTBoolVariable import SMTBoolVariable
from src.smt.SMTExpression import SMTExpression
from src.smt.expressions.NaryExpression import NaryExpression


class OrExpression(NaryExpression):

    def __init__(self, *xs: SMTExpression):
        super().__init__(*xs)
        self.expression = SMTOr([x.expression for x in xs])

    def toBDDExpression(self, map: Dict[SMTBoolVariable, BDDVariable]):
        exprs = [c.toBDDExpression(map) for c in self.children]
        f = exprs[0]
        for c in exprs[1:]:
            f = f | c
        return f

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
