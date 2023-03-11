from pysmt.fnode import FNode

from classes.SMTExpression import SMTExpression


class SMTVariable(SMTExpression):
    expression: FNode

    def __init__(self):
        super().__init__()
