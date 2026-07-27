from __future__ import annotations

from typing import Dict

from pysat.formula import Atom, Formula

from libs.pyeda.pyeda.boolalg.bdd import BDDVariable
from pysmt.fnode import FNode
from pysmt.shortcuts import Symbol

from src.pddl.Action import Action
from src.smt.SMTBoolVariable import SMTBoolVariable
from src.smt.SMTExpression import BOOLEAN
from src.smt.SMTVariable import SMTVariable


class SMTBoolActionVariable(SMTBoolVariable):
    action: Action

    def __init__(self, name: str, action: Action):
        super().__init__(name)
        self.action = action
