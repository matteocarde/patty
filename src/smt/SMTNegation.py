from pysmt.shortcuts import Not
from src.smt.SMTExpression import SMTExpression
from pysmt.typing import BOOL


class SMTNegation(SMTExpression):

    def __init__(self, expr: SMTExpression):
        super().__init__()
        self.variables = expr.variables
        self.positive = expr
        self.type = BOOL
        self.expression = Not(expr.expression)

    def __hash__(self):
        return hash(self.expression)
