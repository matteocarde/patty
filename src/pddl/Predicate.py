from __future__ import annotations

from sympy import Expr
from typing import Dict, Set, Tuple

from src.pddl.Atom import Atom


class Predicate:

    def __init__(self):
        pass

    def ground(self, subs: Dict[str, str]) -> Predicate:
        raise NotImplemented()

    def getAtom(self) -> Atom:
        raise NotImplemented()

    def getPredicates(self) -> Set[Atom]:
        raise NotImplemented()

    def getFunctions(self) -> Set[Atom]:
        raise NotImplemented()

    def toLatex(self) -> str:
        raise NotImplemented

    def __eq__(self, other):
        if not isinstance(other, Predicate):
            return False
        return str(other) == str(self)

    def __hash__(self):
        return hash(str(self))

    def __operation(self, other, operator: str):
        from src.pddl.BinaryPredicate import BinaryPredicate, BinaryPredicateType
        from src.pddl.Constant import Constant
        op = BinaryPredicate()
        op.lhs = self
        op.rhs = Constant.fromValue(other) if isinstance(other, float) or isinstance(other, int) else other
        op.operator = operator
        if operator in {"+", "-", "*", "/"}:
            op.type = BinaryPredicateType.OPERATION
        if operator in {">", ">=", "<=", "<", "="}:
            op.type = BinaryPredicateType.COMPARATION
        return op

    def __sub__(self, other):
        return self.__operation(other, "-")

    def isLinearIncrement(self):
        raise NotImplemented

    def __add__(self, other):
        return self.__operation(other, "+")

    def __mul__(self, other):
        return self.__operation(other, "*")

    def __rmul__(self, other):
        return self.__operation(other, "*")

    def __gt__(self, other):
        return self.__operation(other, ">")

    def __lt__(self, other):
        return self.__operation(other, "<")

    def __deepcopy__(self, m=None):
        raise NotImplemented()

    def substitute(self, subs: Dict[Atom, float], default=None) -> Predicate:
        raise NotImplemented()

    def getLinearIncrement(self) -> float:
        raise NotImplemented()

    def toExpression(self) -> Expr or float:
        raise NotImplemented()
