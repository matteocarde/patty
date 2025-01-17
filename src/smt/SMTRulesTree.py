from typing import List, Dict

from libs.pyeda.pyeda.boolalg.bdd import BDDVariable
from pysmt.shortcuts import TRUE, FALSE

from src.smt.SMTBoolVariable import SMTBoolVariable
from src.smt.SMTConjunction import SMTConjunction
from src.smt.SMTExpression import SMTExpression
from src.smt.expressions.FalseExpression import FalseExpression
from src.smt.expressions.TrueExpression import TrueExpression


class SMTRulesTree:

    def __init__(self):
        super().__init__()
        self.dict: Dict[str, Dict[int, List[SMTExpression]]] = dict()

    def append(self, name: str, index: int, rules: List[SMTExpression]):
        self.dict.setdefault(name, dict())
        self.dict[name].setdefault(index, list())
        self.dict[name][index] += rules

    def __repr__(self):
        return repr(self.dict)

    def __str__(self):
        return str(self.dict)

    def getConjunction(self) -> SMTConjunction:
        conj = SMTConjunction()
        for (name, dName) in self.dict.items():
            for (index, rules) in dName.items():
                conj += rules
        return conj

    def print(self):
        for (key, steps) in self.dict.items():
            for i, rules in steps.items():
                print(f"-- {key} {i} --")
                for r in rules:
                    print(r)
        pass
