import itertools
from typing import Dict

import pyeda
from pyeda.boolalg.bdd import BDDVariable
from pyeda.boolalg.expr import And
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
