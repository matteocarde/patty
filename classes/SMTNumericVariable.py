from pysmt.shortcuts import Symbol
from pysmt.typing import INT, REAL

from classes.SMTExpression import SMTExpression
from classes.SMTVariable import SMTVariable


class SMTNumericVariable(SMTVariable):

    def __init__(self, name: str):
        super().__init__()
        self.expression = Symbol(name, REAL)

    @property
    def variables(self):
        return {self}

    def __hash__(self):
        return hash(self.expression)
