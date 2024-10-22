import itertools
from typing import Dict

import pyeda
from pyeda.boolalg.bdd import BDDVariable, BinaryDecisionDiagram
from pyeda.boolalg.expr import And, AndOp, Variable, Complement
from pysmt.shortcuts import And as SMTAnd

from src.smt.SMTBoolVariable import SMTBoolVariable
from src.smt.SMTExpression import SMTExpression
from src.smt.expressions.NaryExpression import NaryExpression


class AndExpression(NaryExpression):

    def __init__(self, *xs: SMTExpression):
        super().__init__(*xs)
        self.expression = SMTAnd([x.expression for x in xs])

    def toBDDExpression(self, map: Dict[SMTBoolVariable, BDDVariable]):
        exprs = [c.toBDDExpression(map) for c in self.children]
        f = exprs[0]
        for c in exprs[1:]:
            f = f & c
        return f

    @classmethod
    def fromBDDExpression(cls, bdd: BinaryDecisionDiagram, subs: Dict[str, SMTExpression]):
        assert isinstance(bdd, AndOp)
        conjunction = []
        for x in bdd.xs:
            if isinstance(x, Variable):
                conjunction.append(subs[x.name])
            if isinstance(x, Complement):
                conjunction.append(~subs[x.top.name])
        return SMTExpression.bigand(conjunction)

    def replace(self, sub):
        return SMTExpression.bigand([c.replace(sub) for c in self.children])
