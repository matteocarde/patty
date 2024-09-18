from __future__ import annotations
from typing import Dict

from pyeda.boolalg.bdd import BDDVariable
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

    def toBDDExpression(self, map: Dict[SMTBoolVariable, BDDVariable]):
        return map[self]
