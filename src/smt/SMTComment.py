from typing import Set

from pysmt.fnode import FNode
from pysmt.shortcuts import TRUE

from src.smt.SMTExpression import SMTExpression
from src.smt.expressions.TrueExpression import TrueExpression


class SMTComment(SMTExpression):

    def __init__(self, comment: str):
        self.comment = comment
        self.depth = 0
        self.size = 0

    def __str__(self):
        return ";" + self.comment

    def getExpression(self) -> FNode:
        return TRUE()

    def getVariables(self) -> Set:
        return set()
