from typing import Tuple, Set

from src.smt.SMTExpression import SMTExpression
from src.smt.expressions.NaryExpression import NaryExpression


class UnaryExpression(NaryExpression):
    children: Tuple[SMTExpression]
    single: SMTExpression

    def __init__(self, *xs):
        if len(xs) != 1:
            raise Exception(f"Unary expression specified with {len(xs)} values: {xs}")
        self.single = xs[0]
        super().__init__(*xs)

    def getVariables(self) -> Set:
        return self.single.getVariables()
