from typing import Tuple, Set

from src.smt.SMTExpression import SMTExpression
from src.smt.expressions.NaryExpression import NaryExpression


class BinaryExpression(NaryExpression):
    children: Tuple[SMTExpression]
    lhs: SMTExpression
    rhs: SMTExpression

    def __init__(self, *xs):
        if len(xs) != 2:
            raise Exception(f"Binary expression specified with {len(xs)} values: {xs}")
        super().__init__(*xs)
        self.lhs = xs[0]
        self.rhs = xs[1]

    def getVariables(self) -> Set:
        return self.lhs.getVariables() | self.rhs.getVariables()
