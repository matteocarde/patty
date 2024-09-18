from typing import List, Dict

from pyeda.boolalg.bdd import BDDVariable
from pyeda.boolalg.expr import And as BDDAnd

from src.smt.SMTBoolVariable import SMTBoolVariable
from src.smt.SMTExpression import SMTExpression


class SMTConjunction(List[SMTExpression]):

    def __init__(self):
        super().__init__()

    def toBDDExpression(self, map: Dict[SMTBoolVariable, BDDVariable]):
        clauses = [e.toBDDExpression(map) for e in self]
        f = clauses[0]
        for c in clauses[1:]:
            f = f & c
        return f
