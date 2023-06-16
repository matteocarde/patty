from pysmt.shortcuts import Symbol
from pysmt.typing import BOOL

from src.smt.SMTVariable import SMTVariable


class SMTBoolVariable(SMTVariable):

    def __init__(self, name: str):
        super().__init__()
        self.expression = Symbol(name)
        self.type = BOOL

    def variables(self):
        return {self}

    def __hash__(self):
        return hash(str(self.expression))
