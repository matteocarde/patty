from __future__ import annotations

from libs.pyeda.pyeda.boolalg.bdd import BinaryDecisionDiagram, BDDVariable
from sympy import Expr
from typing import Dict, Set, Tuple, List

from src.pddl.Atom import Atom
from src.pddl.PDDLWriter import PDDLWriter


class Predicate:

    def __init__(self):
        pass

    def ground(self, subs: Dict[str, str], problem) -> Predicate:
        raise NotImplemented()

    def getAtom(self) -> Atom:
        raise NotImplemented()

    def getPredicates(self) -> Set[Atom]:
        raise NotImplemented()

    def getFunctions(self) -> Set[Atom]:
        raise NotImplemented()

    def toLatex(self) -> str:
        raise NotImplemented

    def expressify(self, symbols: Dict[Atom, Expr]) -> Expr:
        raise NotImplemented

    def isDynamicLifted(self, problem) -> bool:
        raise NotImplemented

    def toTimePredicate(self, t):
        from src.pddl.TimePredicate import TimePredicate
        tp = TimePredicate()
        tp.type = t
        tp.subPredicate = self
        return tp

    def canHappenLiftedPartial(self, item: Tuple, params: List[str], problem) -> bool:
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

    def __ge__(self, other):
        return self.__operation(other, ">=")

    def __le__(self, other):
        return self.__operation(other, "<=")

    def __deepcopy__(self, m=None):
        raise NotImplemented()

    def substitute(self, subs: Dict[Atom, float], default=None) -> Predicate:
        raise NotImplemented()

    def getLinearIncrement(self) -> float:
        raise NotImplemented()

    def toExpression(self) -> Expr or float:
        raise NotImplemented()

    def toPDDL(self, pw: PDDLWriter = PDDLWriter()):
        pw.write(str(self))

    def toBDD(self, vars: Dict[Atom, BDDVariable]) -> BinaryDecisionDiagram:
        raise NotImplementedError()

    def isAtomic(self):
        return True
