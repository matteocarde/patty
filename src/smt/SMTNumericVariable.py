from pysmt.shortcuts import Symbol
from pysmt.typing import REAL, INT

from src.smt.SMTExpression import NUMERIC
from src.smt.SMTVariable import SMTVariable


class SMTNumericVariable(SMTVariable):

    def __init__(self, name: str, varType):
        super().__init__()
        self.expression = Symbol(name, varType)
        self.type = NUMERIC

    def __hash__(self):
        return hash(self.expression)


class SMTIntVariable(SMTNumericVariable):
    def __init__(self, name: str):
        super().__init__(name, INT)


class SMTRealVariable(SMTNumericVariable):
    def __init__(self, name: str):
        super().__init__(name, REAL)
