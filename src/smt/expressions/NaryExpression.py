from typing import List, Tuple, Dict

from pyeda.boolalg.bdd import BDDVariable
from pysmt.fnode import FNode

from src.smt.SMTBoolVariable import SMTBoolVariable
from src.smt.SMTExpression import SMTExpression


class NaryExpression(SMTExpression):
    children: Tuple[SMTExpression]

    def __init__(self, *xs):
        super().__init__()
        self.children = xs

    @classmethod
    def simplify(cls, *xs):
        raise NotImplementedError()

    def getVariables(self):
        variables = set()
        for c in self.children:
            variables |= c.getVariables()
        return variables

    def toBDDExpression(self, map: Dict[SMTBoolVariable, BDDVariable]):
        raise NotImplementedError()
