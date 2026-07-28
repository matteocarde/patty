import statistics
from typing import Dict

from pysmt.fnode import FNode
from pysmt.shortcuts import FALSE, TRUE
from z3 import RatNumRef, is_false, BoolRef, is_true

from src.sat.CNFVariable import CNFVariable
from src.smt.SMTBoolVariable import SMTBoolVariable
from src.smt.SMTNumericVariable import SMTNumericVariable, SMTIntVariable
from src.smt.SMTVariable import SMTVariable


class SATSolution:

    def __init__(self):
        self.__variables: Dict[CNFVariable, bool] = dict()

    def addVariable(self, var: CNFVariable, value: bool):
        self.__variables[var] = value

    def getVariable(self, var: CNFVariable) -> bool:
        return self.__variables[var]

    def __str__(self):
        return str(self.__variables)

    def prettyString(self):
        strings = [f"{v}: {self.getVariable(v)}" for (v, val) in self.__variables.items()]
        strings.sort()
        return '\n'.join(list(strings))
