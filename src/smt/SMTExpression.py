from __future__ import annotations

from typing import Set, Dict

from libs.pyeda.pyeda.boolalg.expr import OrOp, AndOp, Variable, Complement, OrAndOp
from pysmt.fnode import FNode

from src.pddl.Atom import Atom
from src.pddl.BinaryPredicate import BinaryPredicate
from src.pddl.Constant import Constant
from src.pddl.FalsePredicate import FalsePredicate
from src.pddl.Formula import Formula
from src.pddl.Literal import Literal
from src.pddl.TruePredicate import TruePredicate
from src.pddl.Predicate import Predicate

NUMERIC = "N"
BOOLEAN = "B"


class SMTExpression:
    type: str
    size: int
    variables: set
    depth: int

    def __str__(self):
        return str(self.getExpression().serialize())

    def __repr__(self):
        return str(self)

    def __hash__(self):
        return hash(str(self))

    def getExpression(self) -> FNode:
        raise NotImplementedError()

    def getVariables(self) -> Set:
        raise NotImplementedError()

    def __and__(self, other):
        from src.smt.expressions.AndExpression import AndExpression
        return AndExpression.simplify(self, other)

    def __or__(self, other):
        from src.smt.expressions.OrExpression import OrExpression
        return OrExpression.simplify(self, other)

    def implies(self, other: SMTExpression):
        from src.smt.expressions.ImpliesExpression import ImpliesExpression
        return ImpliesExpression.simplify(self, other)

    def impliedBy(self, other: SMTExpression):
        from src.smt.expressions.ImpliesExpression import ImpliesExpression
        return ImpliesExpression(other, self)

    # def __eq__(self, other: SMTExpression or int):
    #     from src.smt.expressions.EqualExpression import EqualExpression
    #     return EqualExpression.simplify(self, other)

    def equal(self, other: SMTExpression or int):
        from src.smt.expressions.EqualExpression import EqualExpression
        return EqualExpression.simplify(self, other)

    def __invert__(self):
        from src.smt.expressions.NotExpression import NotExpression
        return NotExpression.simplify(self)

    def __ne__(self, other: SMTExpression or int) -> SMTExpression:
        from src.smt.expressions.NotEqualExpression import NotEqualExpression
        return NotEqualExpression.simplify(self, other)

    def __le__(self, other: SMTExpression or float) -> SMTExpression:
        from src.smt.expressions.LessEqualExpression import LessEqualExpression
        return LessEqualExpression.simplify(self, other)

    def __lt__(self, other: SMTExpression or float) -> SMTExpression:
        from src.smt.expressions.LessExpression import LessExpression
        return LessExpression.simplify(self, other)

    def __ge__(self, other: SMTExpression or float) -> SMTExpression:
        from src.smt.expressions.GreaterEqualExpression import GreaterEqualExpression
        return GreaterEqualExpression.simplify(self, other)

    def __gt__(self, other: SMTExpression or float) -> SMTExpression:
        from src.smt.expressions.GreaterExpression import GreaterExpression
        return GreaterExpression.simplify(self, other)

    def __sub__(self, other: SMTExpression or float) -> SMTExpression:
        from src.smt.expressions.SubtractExpression import SubtractExpression
        return SubtractExpression.simplify(self, other)

    def __neg__(self):
        from src.smt.expressions.SubtractExpression import SubtractExpression
        from src.smt.expressions.ConstantExpression import ConstantExpression
        return SubtractExpression.simplify(ConstantExpression(0), self)

    def __rsub__(self, other: SMTExpression or float) -> SMTExpression:
        from src.smt.expressions.SubtractExpression import SubtractExpression
        return SubtractExpression.simplify(other, self)

    def __add__(self, other: SMTExpression or float):
        from src.smt.expressions.AddExpression import AddExpression
        return AddExpression.simplify(self, other)

    def __radd__(self, other: SMTExpression or float):
        from src.smt.expressions.AddExpression import AddExpression
        return AddExpression.simplify(other, self)

    def __mul__(self, other: SMTExpression or float):
        from src.smt.expressions.MultiplyExpression import MultiplyExpression
        return MultiplyExpression.simplify(self, other)

    def __rmul__(self, other: SMTExpression or float):
        from src.smt.expressions.MultiplyExpression import MultiplyExpression
        return MultiplyExpression.simplify(other, self)

    def __truediv__(self, other: SMTExpression or float):
        from src.smt.expressions.DivideExpression import DivideExpression
        return DivideExpression.simplify(self, other)

    def __rtruediv__(self, other: SMTExpression or float):
        from src.smt.expressions.DivideExpression import DivideExpression
        return DivideExpression.simplify(other, self)

    @staticmethod
    def opByString(op: str, left: SMTExpression or float, right: SMTExpression or float):
        if op == "and":
            return left & right
        if op == "or":
            return left | right
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
            from src.smt.expressions.EqualExpression import EqualExpression
            return EqualExpression(left, right)
        if op == "!=":
            return left != right

    @classmethod
    def fromPddl(cls, predicate: BinaryPredicate or Literal or Constant,
                 variables: Dict[Atom, SMTExpression]) -> SMTExpression or float:

        from src.pddl.TruePredicate import TruePredicate
        from src.smt.expressions.TrueExpression import TrueExpression
        from src.pddl.FalsePredicate import FalsePredicate
        from src.smt.expressions.FalseExpression import FalseExpression
        from src.smt.expressions.ConstantExpression import ConstantExpression

        if isinstance(predicate, BinaryPredicate):
            lhs = SMTExpression.fromPddl(predicate.lhs, variables)
            rhs = SMTExpression.fromPddl(predicate.rhs, variables)
            result = SMTExpression.opByString(predicate.operator, lhs, rhs)
            return result
        if isinstance(predicate, Literal):
            atom = predicate.getAtom()
            if predicate.sign == "+":
                return variables[atom]
            else:
                return ~variables[atom]
        if isinstance(predicate, Constant):
            return ConstantExpression(predicate.value)
        if isinstance(predicate, TruePredicate):
            return TrueExpression()
        if isinstance(predicate, FalsePredicate):
            return FalseExpression()
        if isinstance(predicate, Formula):
            return SMTExpression.fromFormula(predicate, variables)
        raise Exception(f"Don't know how to convert {predicate} to Expression")

    @classmethod
    def fromFormula(cls, formula: Formula or Predicate,
                    variables: Dict[Atom, SMTExpression]) -> SMTExpression or float:

        from src.smt.expressions.TrueExpression import TrueExpression
        from src.smt.expressions.FalseExpression import FalseExpression

        if isinstance(formula, TruePredicate):
            return TrueExpression()
        if isinstance(formula, FalsePredicate):
            return FalseExpression()

        preRules = []
        if isinstance(formula, Predicate):
            return SMTExpression.fromPddl(formula, variables)

        for pre in formula:
            if isinstance(pre, Formula):
                preRules += [SMTExpression.fromFormula(pre, variables)]
            else:
                preRules += [SMTExpression.fromPddl(pre, variables)]
        if formula.type == "AND":
            return SMTExpression.andOfExpressionsList(preRules)
        else:
            return SMTExpression.orOfExpressionsList(preRules)

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

    @staticmethod
    def numericConstant(el):
        if type(el) == float or type(el) == int:
            from src.smt.expressions.ConstantExpression import ConstantExpression
            return ConstantExpression(el)
        return el
