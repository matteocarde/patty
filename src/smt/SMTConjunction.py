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

    def append(self, expr: SMTExpression) -> None:
        if isinstance(expr, TrueExpression):
            return
        if isinstance(expr, FalseExpression):
            raise Exception("Trying to append FALSE rule into conjunction")
        super().append(expr)

    def toBDDExpression(self, map: Dict[SMTBoolVariable, BDDVariable]):
        clauses = [e.toBDDExpression(map) for e in self]
        f = clauses[0]
        for c in clauses[1:]:
            f = f & c
        return f
