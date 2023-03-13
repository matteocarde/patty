from __future__ import annotations

from typing import Set, Dict

from pysmt.fnode import FNode
from pysmt.shortcuts import And, Or, Equals, LE, LT, GE, GT, Implies, Real, Times, Minus, Plus, Div

from Atom import Atom
from BinaryPredicate import BinaryPredicate
from Constant import Constant
from Literal import Literal


def toRHS(other):
    return other.expression if isinstance(other, SMTExpression) else Real(other)


class SMTExpression:
    expression: FNode or bool
    vars: Set
    lhs: SMTExpression
    rhs: SMTExpression

    def __init__(self):
        self.vars = set()
        self.lhs: SMTExpression
        self.rhs: SMTExpression
        self.expression = True

    def __str__(self):
        return str(self.expression)

    def __repr__(self):
        return str(self)

    @property
    def variables(self) -> Set:
        variables = set()
        if isinstance(self.lhs, SMTExpression):
            variables = variables | self.lhs.variables
        if isinstance(self.rhs, SMTExpression):
            variables = variables | self.rhs.variables
        return variables

    def __binary(self, other: SMTExpression or float, symbol: FNode) -> SMTExpression:
        expr = SMTExpression()
        expr.lhs = self
        expr.rhs = other
        expr.expression = symbol

        return expr

    def AND(self, other: SMTExpression):
        return self.__binary(other, And(self.expression, other.expression))

    def OR(self, other: SMTExpression):
        return self.__binary(other, Or(self.expression, other.expression))

    def __eq__(self, other: SMTExpression or int):
        return self.__binary(other, Equals(self.expression, toRHS(other)))

    def __le__(self, other: SMTExpression or float):
        return self.__binary(other, LE(self.expression, toRHS(other)))

    def __lt__(self, other: SMTExpression or float):
        return self.__binary(other, LT(self.expression, toRHS(other)))

    def __ge__(self, other: SMTExpression or float):
        return self.__binary(other, GE(self.expression, toRHS(other)))

    def __gt__(self, other: SMTExpression or float):
        return self.__binary(other, GT(self.expression, toRHS(other)))

    def __sub__(self, other: SMTExpression or float):
        return self.__binary(other, Minus(self.expression, toRHS(other)))

    def __rsub__(self, other: SMTExpression or float):
        return self.__binary(other, Minus(self.expression, toRHS(other)))

    def __add__(self, other: SMTExpression or float):
        return self.__binary(other, Plus(self.expression, toRHS(other)))

    def __radd__(self, other: SMTExpression or float):
        return self.__binary(other, Plus(self.expression, toRHS(other)))

    def __mul__(self, other: SMTExpression or float):
        return self.__binary(other, Times(self.expression, toRHS(other)))

    def __rmul__(self, other: SMTExpression or float):
        return self.__binary(other, Times(self.expression, toRHS(other)))

    def __truediv__(self, other: SMTExpression or float):
        return self.__binary(other, Div(self.expression, toRHS(other)))

    def __rtruediv__(self, other: SMTExpression or float):
        return self.__binary(other, Div(self.expression, toRHS(other)))

    def implies(self, other: SMTExpression):
        return self.__binary(other, Implies(self.expression, other.expression))

    def impliedBy(self, other):
        return self.__binary(other, Implies(other.expression, self.expression))

    @staticmethod
    def opByString(op: str, left: SMTExpression, right: SMTExpression):
        if op == "and":
            return left.AND(right)
        if op == "or":
            return left.OR(right)
        if op == "+":
            return left + right
        if op == "-":
            return left - right
        if op == "*":
            return left * right
        if op == "/":
            return left / right
        if op == ">=":
            return left >= right
        if op == "<=":
            return left <= right
        if op == ">":
            return left > right
        if op == "<":
            return left < right
        if op == "=":
            return left == right

    @classmethod
    def fromPddl(cls, predicate: BinaryPredicate or Literal or Constant,
                 variables: Dict[Atom, SMTExpression]) -> SMTExpression or float:
        if isinstance(predicate, BinaryPredicate):
            lhs = SMTExpression.fromPddl(predicate.lhs, variables)
            rhs = SMTExpression.fromPddl(predicate.rhs, variables)
            return SMTExpression.opByString(predicate.operator, lhs, rhs)
        if isinstance(predicate, Literal):
            return variables[predicate.getAtom()]
        if isinstance(predicate, Constant):
            return predicate.value
