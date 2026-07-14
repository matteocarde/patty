from typing import Dict

from pysmt.fnode import FNode
from pysmt.shortcuts import FALSE, TRUE
from z3 import RatNumRef, is_false

from src.smt.SMTBoolVariable import SMTBoolVariable
from src.smt.SMTNumericVariable import SMTNumericVariable, SMTIntVariable
from src.smt.SMTVariable import SMTVariable


class SMTSolution:

    def __init__(self):
        self.__variables: Dict[SMTVariable, float or bool] = dict()

    def addVariable(self, var: SMTVariable, value: float or bool):
        self.__variables[var] = value

    def getVariable(self, var: SMTVariable, dec: int = 3) -> float or int or bool:
        node: FNode = self.__variables[var]
        if isinstance(var, SMTNumericVariable):
            if isinstance(node, RatNumRef):
                return float(node.as_fraction())
            if isinstance(var, SMTIntVariable):
                return int(str(node))
            if "/" in str(node):
                n, d = str(node).split("/")
                return float(n) / float(d)
            return float(str(node))
        if isinstance(var, SMTBoolVariable):
            v = node.is_true()
            return v

    def __str__(self):
        return str(self.__variables)

    def prettyString(self):
        strings = [f"{v}: {self.getVariable(v)}" for (v, val) in self.__variables.items()]
        strings.sort()
        return '\n'.join(list(strings))
