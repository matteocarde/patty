from __future__ import annotations

import copy
from typing import Dict, Set

from libs.pyeda.pyeda.boolalg.bdd import BDDVariable, BinaryDecisionDiagram
from sympy import Expr

from src.pddl.Atom import Atom
from src.pddl.Predicate import Predicate


class TruePredicate(Predicate):

    def __init__(self):
        super().__init__()

    def __deepcopy__(self, m=None) -> TruePredicate:
        return TruePredicate()

    def ground(self, subs: Dict[str, str], delta=1) -> TruePredicate:
        return self

    def __str__(self):
        return "TRUE"

    def __repr__(self):
        return str(self)

    def getPredicates(self) -> Set[Atom]:
        return set()

    def getFunctions(self) -> Set[Atom]:
        return set()

    def substitute(self, subs: Dict[Atom, float], default=None) -> Predicate:
        return self

    def isLinearIncrement(self):
        raise False

    def getLinearIncrement(self) -> float:
        return 0

    def canHappen(self, subs: Dict[Atom, float or bool], default=None) -> bool:
        return True

    def toExpression(self, onlyExpr=False) -> Expr or float:
        return True

    def replace(self, atom: Atom, w):
        return TruePredicate()

    def replaceDict(self, r: Dict[Atom, Predicate]):
        return copy.deepcopy(self)

    def toBDD(self, vars: Dict[Atom, BDDVariable]) -> BinaryDecisionDiagram:
        return 1
