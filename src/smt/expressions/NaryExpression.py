from typing import List, Tuple, Dict

from pyeda.boolalg.bdd import BDDVariable

from src.smt.SMTBoolVariable import SMTBoolVariable
from src.smt.SMTExpression import SMTExpression


class NaryExpression(SMTExpression):
    children: Tuple[SMTExpression]

    def __init__(self, *xs):
        super().__init__()
        self.children = xs
        self.variables = set()
        for x in xs:
            self.variables |= x.variables

    def toBDDExpression(self, map: Dict[SMTBoolVariable, BDDVariable]):
        raise NotImplementedError()
