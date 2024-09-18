from typing import Tuple

from src.smt.SMTExpression import SMTExpression
from src.smt.expressions.NaryExpression import NaryExpression


class UnaryExpression(NaryExpression):
    children: Tuple[SMTExpression]

    def __init__(self, *xs):
        if len(xs) != 1:
            raise Exception(f"Unary expression specified with {len(xs)} values: {xs}")
        super().__init__(*xs)
