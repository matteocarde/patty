from typing import List, Tuple, Dict, Set

from pyeda.boolalg.bdd import BDDVariable
from pysmt.fnode import FNode

from src.smt.SMTBoolVariable import SMTBoolVariable
from src.smt.SMTExpression import SMTExpression
from src.smt.SMTVariable import SMTVariable


class NaryExpression(SMTExpression):
    children: List[SMTExpression]

    def __init__(self, *xs):
        super().__init__()
        self.children = list(xs)
        self.variables = set()
        self.depth = max([c.depth for c in self.children]) + 1
        for c in self.children:
            self.variables |= c.getVariables()

    @classmethod
    def simplify(cls, *xs):
        raise NotImplementedError()

    def getVariables(self) -> Set:
        return self.variables

    def toBDDExpression(self, map: Dict[SMTBoolVariable, BDDVariable]):
        raise NotImplementedError()
