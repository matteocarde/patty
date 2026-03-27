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
            elif type(x) in {bool}:
                from src.smt.expressions.TrueExpression import TrueExpression
                from src.smt.expressions.FalseExpression import FalseExpression
                self.children.append(TrueExpression() if x else FalseExpression())
            else:
                if not isinstance(x, SMTExpression):
                    raise Exception(f"Expected {x} to be SMTExpression, instead found {type(x)}")
                self.children.append(x)

        self.variables = set()
        for c in self.children:
            self.variables |= c.variables

    @classmethod
    def simplify(cls, *xs):
        raise NotImplementedError()

    def getVariables(self) -> Set:
        return self.variables

    def toBDDExpression(self, map: Dict[SMTBoolVariable, BDDVariable]):
        raise NotImplementedError()
