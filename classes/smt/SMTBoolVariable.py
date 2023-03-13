from pysmt.shortcuts import Symbol

from classes.smt.SMTVariable import SMTVariable


class SMTBoolVariable(SMTVariable):

    def __init__(self, name: str):
        super().__init__()
        self.expression = Symbol(name)

    def variables(self):
        return {self}

    def __hash__(self):
        return hash(str(self.expression))
