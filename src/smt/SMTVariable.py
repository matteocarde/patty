from pysmt.fnode import FNode

from src.smt.SMTExpression import SMTExpression


class SMTVariable(SMTExpression):
    symbol: FNode
    name: str

    def __init__(self):
        super().__init__()
        self.depth = 1
        self.size = 1

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name

    def getSymbol(self) -> FNode:
        return self.symbol
