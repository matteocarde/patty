from typing import Dict

from pyeda.boolalg.bdd import BDDVariable, BinaryDecisionDiagram
from pyeda.boolalg.expr import Or as BDDOr, OrOp
from pysmt.shortcuts import Or as SMTOr

from src.smt.SMTBoolVariable import SMTBoolVariable
from src.smt.SMTExpression import SMTExpression
from src.smt.expressions.FalseExpression import FalseExpression
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
    def fromBDDExpression(cls, bdd: BinaryDecisionDiagram, subs: Dict[str, SMTExpression]):
        assert isinstance(bdd, OrOp)
        from src.smt.expressions.AndExpression import AndExpression
        return SMTExpression.bigor([AndExpression.fromBDDExpression(x, subs) for x in bdd.xs])

    def replace(self, sub):
        return SMTExpression.bigor([c.replace(sub) for c in self.children])

    def evaluate(self, solution):
        for c in self.children:
            if c.evaluate(solution):
                return True
        return False
