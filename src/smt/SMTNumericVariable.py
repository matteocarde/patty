from typing import Set

from pysmt.fnode import FNode
from pysmt.shortcuts import Symbol, ToReal
from pysmt.typing import REAL, INT

from src.smt.SMTExpression import NUMERIC
from src.smt.SMTVariable import SMTVariable


class SMTNumericVariable(SMTVariable):

    def __init__(self, name: str, varType):
        super().__init__()
        self.name = name
        self.varType = varType
        self.symbol = Symbol(self.name, self.varType)
        self.type = NUMERIC

    def getVariables(self) -> Set:
        return {self}

    def getExpression(self) -> FNode:
        return self.symbol

    def __hash__(self):
        return hash(self.name)


class SMTIntVariable(SMTNumericVariable):
    def __init__(self, name: str):
        super().__init__(name, INT)

    def getExpression(self) -> FNode:
        return ToReal(super().getExpression())


class SMTRealVariable(SMTNumericVariable):
    def __init__(self, name: str):
        super().__init__(name, REAL)
