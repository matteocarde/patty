from pysmt.fnode import FNode

from src.smt.SMTExpression import SMTExpression


class SMTVariable(SMTExpression):
    expression: FNode

    def __init__(self):
        super().__init__()
