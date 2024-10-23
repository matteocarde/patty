from __future__ import annotations

from typing import Set, Dict

from pyeda.boolalg.bdd import BinaryDecisionDiagram, bdd2expr
from pyeda.boolalg.expr import OrOp, AndOp, Variable, Complement, OrAndOp
from pysmt.fnode import FNode
from pysmt.shortcuts import Equals, LE, LT, GE, GT, Real, Times, Minus, Plus, Div, TRUE, ToReal, \
    NotEquals
from pysmt.typing import REAL, INT, BOOL

from src.pddl.Atom import Atom
from src.pddl.BinaryPredicate import BinaryPredicate
from src.pddl.Constant import Constant
from src.pddl.Formula import Formula
from src.pddl.Literal import Literal


def toRHS(other):
    if isinstance(other, SMTExpression):
        return other.expression
    if type(other) == int or (type(other) == float and other.is_integer()):
        return Real(float(other))
    if type(other) == float:
        return Real(other)


def getVars(obj):
    from src.smt.expressions.NotExpression import NotExpression
    if isinstance(obj, SMTExpression):
        return obj.variables if obj.variables or obj.isConstant else {obj} if not isinstance(obj, NotExpression) else {
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
        self.operation = None
        self.lhs: SMTExpression
        self.rhs: SMTExpression
        self.expression = TRUE()
        self.isConstant = False

    def __str__(self):
        return str(self.expression.serialize())

    def __repr__(self):
        return str(self)

    def __hash__(self):
        return hash(str(self))

    def __binary(self, other: SMTExpression or float, operation, lhsExpression: FNode,
                 rhsExpression: FNode) -> SMTExpression:
        expr = SMTExpression()
        expr.lhs = self
        expr.operation = operation
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
        from src.smt.expressions.AndExpression import AndExpression
        return AndExpression(self, other)

    def __and__(self, other):
        from src.smt.expressions.AndExpression import AndExpression
        from src.smt.expressions.TrueExpression import TrueExpression
        from src.smt.expressions.FalseExpression import FalseExpression
        if isinstance(self, TrueExpression):
            return other
        if isinstance(other, TrueExpression):
            return self
        if isinstance(other, FalseExpression) or isinstance(self, FalseExpression):
            return FalseExpression()
        return AndExpression(self, other)

    def OR(self, other: SMTExpression):
        from src.smt.expressions.OrExpression import OrExpression
        return OrExpression(self, other)

    def __or__(self, other):
        from src.smt.expressions.OrExpression import OrExpression
        from src.smt.expressions.TrueExpression import TrueExpression
        from src.smt.expressions.FalseExpression import FalseExpression
        if isinstance(self, FalseExpression):
            return other
        if isinstance(other, FalseExpression):
            return self
        if isinstance(other, TrueExpression) or isinstance(self, TrueExpression):
            return TrueExpression()
        return OrExpression(self, other)

    def NOT(self):
        from src.smt.expressions.NotExpression import NotExpression
        from src.smt.expressions.TrueExpression import TrueExpression
        from src.smt.expressions.FalseExpression import FalseExpression
        if isinstance(self, TrueExpression):
            return FalseExpression()
        if isinstance(self, FalseExpression):
            return TrueExpression()
        return NotExpression(self)

    def implies(self, other: SMTExpression):
        from src.smt.expressions.ImpliesExpression import ImpliesExpression
        return ImpliesExpression(self, other)

    def coimplies(self, other: SMTExpression):
        from src.smt.expressions.IffExpression import IffExpression
        return IffExpression(self, other)

    def iff(self, other: SMTExpression):
        from src.smt.expressions.IffExpression import IffExpression
        return IffExpression(self, other)

    def impliedBy(self, other: SMTExpression):
        from src.smt.expressions.ImpliesExpression import ImpliesExpression
        return ImpliesExpression(other, self)

    def __eq__(self, other: SMTExpression or int):
        if self.type == BOOL:
            return self.coimplies(other)
        expr = self.__binary(other, Equals, self.expression, toRHS(other))
        expr.type = BOOL
        return expr

    def __invert__(self):
        return self.NOT()

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
                return ~variables[predicate.getAtom()]
        if isinstance(predicate, Constant):
            return predicate.value
        raise Exception(f"Don't know how to convert {predicate} to Expression")

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
        if len(rules) == 1:
            return rules[0]
        return connective(*rules)

    @classmethod
    def andOfExpressionsList(cls, rules: [SMTExpression]):
        from src.smt.expressions.AndExpression import AndExpression
        from src.smt.expressions.FalseExpression import FalseExpression
        from src.smt.expressions.TrueExpression import TrueExpression
        sRules = []
        for r in rules:
            if isinstance(r, FalseExpression):
                return FalseExpression()
            if isinstance(r, TrueExpression):
                continue
            sRules.append(r)
        if not rules:
            return TrueExpression()
        return SMTExpression.__connectiveOfExpressionList(sRules, AndExpression)

    @classmethod
    def bigand(cls, rules: [SMTExpression]):
        return SMTExpression.andOfExpressionsList(rules)

    @classmethod
    def orOfExpressionsList(cls, rules: [SMTExpression]):
        from src.smt.expressions.OrExpression import OrExpression
        from src.smt.expressions.FalseExpression import FalseExpression
        from src.smt.expressions.TrueExpression import TrueExpression
        sRules = []
        for r in rules:
            if isinstance(r, TrueExpression):
                return TrueExpression()
            if isinstance(r, FalseExpression):
                continue
            sRules.append(r)
        if not rules:
            return FalseExpression()
        return SMTExpression.__connectiveOfExpressionList(rules, OrExpression)

    @classmethod
    def bigor(cls, rules: [SMTExpression]):
        return SMTExpression.orOfExpressionsList(rules)

    def toBDDExpression(self, map):
        raise NotImplementedError()

    @classmethod
    def fromBDDExpression(cls, expr: OrAndOp, subs: Dict[str, SMTExpression]):
        from src.smt.expressions.OrExpression import OrExpression
        from src.smt.expressions.AndExpression import AndExpression
        if isinstance(expr, OrOp):
            return OrExpression.fromBDDExpression(expr, subs)
        if isinstance(expr, AndOp):
            return AndExpression.fromBDDExpression(expr, subs)
        if isinstance(expr, Variable):
            return subs[expr.name]
        if isinstance(expr, Complement):
            return ~subs[expr.top.name]

    def replace(self, sub):
        raise NotImplementedError()

    def evaluate(self, solution):
        raise NotImplementedError
