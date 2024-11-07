from typing import List

from pysmt.shortcuts import TRUE, FALSE

from src.smt.SMTExpression import SMTExpression


class SMTConjunction(List[SMTExpression]):

    def __init__(self):
        super().__init__()

    def append(self, expr: SMTExpression) -> None:
        if expr.expression == TRUE():
            return
        if expr.expression == FALSE():
            raise Exception("Trying to append FALSE rule into conjunction")
        super().append(expr)




