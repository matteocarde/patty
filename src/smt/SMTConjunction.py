from typing import List, Dict

from pyeda.boolalg.bdd import BDDVariable
from pysmt.shortcuts import TRUE, FALSE

from src.smt.SMTBoolVariable import SMTBoolVariable
from src.smt.SMTExpression import SMTExpression
from src.smt.expressions.FalseExpression import FalseExpression
from src.smt.expressions.TrueExpression import TrueExpression


class SMTConjunction(List[SMTExpression]):

    def __init__(self):
        super().__init__()
        self.depth = max([c.depth for c in self]) + 1 if len(self) else 1
        self.variables = set()

    def append(self, expr: SMTExpression) -> None:
        if isinstance(expr, TrueExpression):
            return
        if isinstance(expr, FalseExpression):
            raise Exception("Trying to append FALSE rule into conjunction")
        super().append(expr)
        self.depth = max(expr.depth, self.depth) + 1
        self.variables |= expr.getVariables()

    def toBDDExpression(self, map: Dict[SMTBoolVariable, BDDVariable]):
        clauses = [e.toBDDExpression(map) for e in self]
        f = clauses[0]
        for c in clauses[1:]:
            f = f & c
        return f

    def getVariables(self):
        return self.variables
