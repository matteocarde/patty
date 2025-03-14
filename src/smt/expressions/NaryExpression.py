from typing import List, Tuple, Dict, Set

from libs.pyeda.pyeda.boolalg.bdd import BDDVariable
from pysmt.fnode import FNode

from src.smt.SMTBoolVariable import SMTBoolVariable
from src.smt.SMTExpression import SMTExpression
from src.smt.SMTVariable import SMTVariable
from src.smt.expressions.ConstantExpression import ConstantExpression


class NaryExpression(SMTExpression):
    children: List[SMTExpression]

    def __init__(self, *xs):
        super().__init__()
        self.children = []
        for x in xs:
            if type(x) in {float, int}:
                self.children.append(ConstantExpression(x))
            else:
                self.children.append(x)

        self.variables = set()
        self.depth = (max([c.depth for c in self.children]) if self.children else 0) + 1
        self.size = sum([c.size for c in self.children]) if self.children else 0
        for c in self.children:
            self.variables |= c.getVariables()

    @classmethod
    def simplify(cls, *xs):
        raise NotImplementedError()

    def getVariables(self) -> Set:
        return self.variables

    def toBDDExpression(self, map: Dict[SMTBoolVariable, BDDVariable]):
        raise NotImplementedError()
