from typing import Set

from pysat.formula import PYSAT_TRUE
from pysmt.fnode import FNode
from pysmt.shortcuts import TRUE

from src.smt.SMTExpression import SMTExpression


class SMTComment(SMTExpression):

    def __init__(self, comment: str):
        self.comment = comment
        self.depth = 0
        self.size = 0

    def __str__(self):
        return ";" + self.comment

    def getExpression(self, memodict=dict()) -> FNode:
        return TRUE()

    def getPropositionalFormula(self, memodict=dict()):
        return PYSAT_TRUE

    def getVariables(self) -> Set:
        return set()
