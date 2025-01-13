from typing import List, Dict

from pyeda.boolalg.bdd import BDDVariable, BinaryDecisionDiagram
from src.smt.SMTBoolVariable import SMTBoolVariable
from src.smt.SMTExpression import SMTExpression
from src.smt.expressions.FalseExpression import FalseExpression
from src.smt.expressions.TrueExpression import TrueExpression


class SMTConjunction(List[SMTExpression]):

    def __init__(self):
        super().__init__()
        self.depth = max([c.depth for c in self]) + 1 if len(self) else 1
        self.variables = set()

    def append(self, expr: SMTExpression) -> None:
        if isinstance(expr, TrueExpression):
            return
        if isinstance(expr, FalseExpression):
            raise Exception("Trying to append FALSE rule into conjunction")
        super().append(expr)
        self.depth = max(expr.depth, self.depth) + 1
        self.variables |= expr.getVariables()

    def __add__(self, other):
        if not type(other, list):
            raise Exception()
        for c in other:
            self.append(c)

    def __andOfSubClauses(self, clauses):
        if len(clauses) == 1:
            return clauses[0]
        elif len(clauses) == 0:
            return 1

        mid = len(clauses) // 2

        # Recursively compute the sum of each half
        left = self.__andOfSubClauses(clauses[:mid])
        right = self.__andOfSubClauses(clauses[mid:])

        # Combine the results
        return left & right

    def toBDDExpression(self, map: Dict[SMTBoolVariable, BDDVariable]):
        clauses: List[BinaryDecisionDiagram] = [e.toBDDExpression(map) for e in self]
        return self.__andOfSubClauses(clauses)
        # f: BinaryDecisionDiagram = clauses[0]
        # for i, c in enumerate(clauses[1:]):
        #     f = f & c
        # return f

    def getVariables(self):
        return self.variables
