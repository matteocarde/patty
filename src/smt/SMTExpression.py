from __future__ import annotations

from src.pddl.Atom import Atom
from src.pddl.BinaryPredicate import BinaryPredicate
from src.pddl.Constant import Constant
from src.pddl.Formula import Formula
from src.pddl.Literal import Literal
from pysmt.fnode import FNode
from pysmt.shortcuts import And, Or, Equals, LE, LT, GE, GT, Implies, Real, Times, Minus, Plus, Div, TRUE, ToReal, Int, \
    NotEquals, Iff, FALSE
from pysmt.typing import REAL, INT, BOOL
from typing import Set, Dict


def toRHS(other):
    if isinstance(other, SMTExpression):
        return other.expression
    if type(other) == int or (type(other) == float and other.is_integer()):
        return Real(float(other))
    if type(other) == float:
        return Real(other)


def getVars(obj):
    from src.smt.SMTNegation import SMTNegation
    if isinstance(obj, SMTExpression):
        return obj.variables if obj.variables or obj.isConstant else {obj} if not isinstance(obj, SMTNegation) else {
            obj.positive}
    return set()


class SMTExpression:
    expression: FNode
    variables: Set
    lhs: SMTExpression
    rhs: SMTExpression
    isConstant: bool

    def __init__(self):
        self.variables = set()
        self.type = REAL
        self.lhs: SMTExpression
        self.rhs: SMTExpression
        self.expression = TRUE()
        self.isConstant = False

    def __str__(self):
        return str(self.expression.serialize())

    def __repr__(self):
        return str(self)

    def __binary(self, other: SMTExpression or float, operation, lhsExpression: FNode,
                 rhsExpression: FNode) -> SMTExpression:
        expr = SMTExpression()
        expr.lhs = self
        expr.variables = getVars(self) | getVars(other)

        if isinstance(other, SMTExpression):
            rhsType = other.type
        elif type(other) == int or (type(other) == float and other.is_integer()):
            other = float(other)
            rhsType = REAL
        else:
            rhsType = REAL

        expr.rhs = other

        if expr.lhs.type == BOOL or expr.lhs.type == rhsType:
            expr.type = expr.lhs.type
        else:
            expr.type = REAL
            lhsExpression = ToReal(lhsExpression) if expr.lhs.type == INT else lhsExpression
            rhsExpression = ToReal(rhsExpression) if rhsType == INT else rhsExpression

        expr.expression = operation(lhsExpression, rhsExpression)

        return expr

    def AND(self, other: SMTExpression):
        return self.__binary(other, And, self.expression, other.expression)

    def OR(self, other: SMTExpression):
        return self.__binary(other, Or, self.expression, other.expression)

    def NOT(self):
        from src.smt.SMTNegation import SMTNegation
        return SMTNegation(self)

    def __eq__(self, other: SMTExpression or int):
        if self.type == BOOL:
            return self.coimplies(other)
        expr = self.__binary(other, Equals, self.expression, toRHS(other))
        expr.type = BOOL
        return expr

    def __ne__(self, other: SMTExpression or int):
        expr = self.__binary(other, NotEquals, self.expression, toRHS(other))
        expr.type = BOOL
        return expr

    def __le__(self, other: SMTExpression or float):
        expr = self.__binary(other, LE, self.expression, toRHS(other))
        expr.type = BOOL
        return expr

    def __lt__(self, other: SMTExpression or float):
        expr = self.__binary(other, LT, self.expression, toRHS(other))
        expr.type = BOOL
        return expr

    def __ge__(self, other: SMTExpression or float):
        expr = self.__binary(other, GE, self.expression, toRHS(other))
        expr.type = BOOL
        return expr

    def __gt__(self, other: SMTExpression or float):
        expr = self.__binary(other, GT, self.expression, toRHS(other))
        expr.type = BOOL
        return expr

    def __sub__(self, other: SMTExpression or float):
        return self.__binary(other, Minus, self.expression, toRHS(other))

    def __rsub__(self, other: SMTExpression or float):
        return self.__binary(other, Minus, self.expression * -1, toRHS(other) * -1)

    def __add__(self, other: SMTExpression or float):
        return self.__binary(other, Plus, self.expression, toRHS(other))

    def __radd__(self, other: SMTExpression or float):
        if type(other) == float and other == 0:
            return self
        return self.__binary(other, Plus, self.expression, toRHS(other))

    def __mul__(self, other: SMTExpression or float):
        return self.__binary(other, Times, self.expression, toRHS(other))

    def __rmul__(self, other: SMTExpression or float):
        if type(other) == float and other == 1:
            return self
        return self.__binary(other, Times, self.expression, toRHS(other))

    def __truediv__(self, other: SMTExpression or float):
        return self.__binary(other, Div, self.expression, toRHS(other))

    def __rtruediv__(self, other: SMTExpression or float):
        return self.__binary(other, Div, toRHS(other), self.expression)

    def implies(self, other: SMTExpression):
        expr = self.__binary(other, Implies, self.expression, other.expression)
        expr.type = BOOL
        return expr

    def coimplies(self, other: SMTExpression):
        expr = self.__binary(other, Iff, self.expression, other.expression)
        expr.type = BOOL
        return expr

    def impliedBy(self, other: SMTExpression):
        expr = self.__binary(other, Implies, other.expression, self.expression)
        expr.type = BOOL
        return expr

    @staticmethod
    def opByString(op: str, left: SMTExpression or float, right: SMTExpression or float):
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
        if op == "!=":
            return left != right

    @classmethod
    def fromPddl(cls, predicate: BinaryPredicate or Literal or Constant,
                 variables: Dict[Atom, SMTExpression]) -> SMTExpression or float:
        if isinstance(predicate, BinaryPredicate):
            lhs = SMTExpression.fromPddl(predicate.lhs, variables)
            rhs = SMTExpression.fromPddl(predicate.rhs, variables)
            result = SMTExpression.opByString(predicate.operator, lhs, rhs)
            return result
        if isinstance(predicate, Literal):
            if predicate.sign == "+":
                return variables[predicate.getAtom()]
            else:
                return variables[predicate.getAtom()].NOT()
        if isinstance(predicate, Constant):
            return predicate.value

    @classmethod
    def fromFormula(cls, formula: Formula,
                    variables: Dict[Atom, SMTExpression]) -> SMTExpression or float:
        preRules = []
        for pre in formula:
            if isinstance(pre, Formula):
                preRules += [SMTExpression.fromFormula(pre, variables)]
            else:
                preRules += [SMTExpression.fromPddl(pre, variables)]
        if formula.type == "AND":
            return SMTExpression.andOfExpressionsList(preRules)
        else:
            return SMTExpression.andOfExpressionsList(preRules)

    @classmethod
    def __connectiveOfExpressionList(cls, rules: [SMTExpression], connective):
        if not rules:
            return SMTExpression.TRUE()
        e = cls()
        e.variables = set()
        expressions = list()
        r: SMTExpression
        for r in rules:
            e.variables |= getVars(r)
            expressions.append(r.expression)
        e.expression = connective(expressions)
        return e

    @classmethod
    def andOfExpressionsList(cls, rules: [SMTExpression]):
        return cls.__connectiveOfExpressionList(rules, And)

    @classmethod
    def orOfExpressionsList(cls, rules: [SMTExpression]):
        return cls.__connectiveOfExpressionList(rules, Or)

    @classmethod
    def FALSE(cls):
        exp = cls()
        exp.expression = FALSE()
        exp.isConstant = True
        return exp

    @classmethod
    def TRUE(cls):
        exp = cls()
        exp.expression = TRUE()
        exp.isConstant = True
        return exp
