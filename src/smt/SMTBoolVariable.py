from __future__ import annotations

from typing import Dict

from pysat.formula import Atom, Formula

from libs.pyeda.pyeda.boolalg.bdd import BDDVariable
from pysmt.fnode import FNode
from pysmt.shortcuts import Symbol

from src.smt.SMTExpression import BOOLEAN
from src.smt.SMTVariable import SMTVariable


class SMTBoolVariable(SMTVariable):

    def __init__(self, name: str):
        super().__init__()
        self.name = name
        self.type = BOOLEAN
        self.symbol = Symbol(self.name)
        self.atom = Atom(self.name)
        self.variables = {self}

    def __hash__(self):
        return hash(self.name)

    def getExpression(self, memodict=dict()) -> FNode:
        return self.symbol

    def getPropositionalFormula(self, memodict=dict()) -> Formula:
        return self.atom

    def getVariables(self):
        return {self}

    def toBDDExpression(self, map: Dict[SMTBoolVariable, BDDVariable]):
        return map[self]

    def replace(self, sub):
        if self not in sub:
            raise Exception(f"Dictionary {sub} doesn't contain {self} for replacement")
        return sub[self]

    def evaluate(self, solution):
        from src.smt.SMTSolution import SMTSolution
        solution: SMTSolution
        return solution.getVariable(self)
