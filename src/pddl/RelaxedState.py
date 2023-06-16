from typing import Dict, Set

from Action import Action
from Atom import Atom
from BinaryPredicate import BinaryPredicate
from Constant import Constant
from Formula import Formula
from Literal import Literal
from MooreInterval import MooreInterval
from Predicate import Predicate
from Supporter import Supporter
from Utilities import Utilities


class RelaxedState:
    __intervals: Dict[Atom, MooreInterval]
    __assignments: Set[Literal]

    def __init__(self):
        self.__intervals = dict()

    def __repr__(self):
        return repr(self.__intervals)

    def __iter__(self):
        return iter(self.__intervals)

    @property
    def intervals(self) -> Dict[Atom, MooreInterval]:
        return self.__intervals

    @classmethod
    def fromInitialCondition(cls, init):
        ris = cls()
        for (atom, value) in init.numericAssignments.items():
            ris.__intervals[atom] = MooreInterval(value, value)

        for lit in init.assignments:
            if not isinstance(lit, Literal):
                continue
            ris.__assignments.add(lit)

        return ris

    def getAtom(self, atom: Atom) -> MooreInterval:
        return self.__intervals[atom]

    def applySupporters(self, activeSupporters: Set[Supporter]):

        state = RelaxedState()
        state.__intervals = self.__intervals.copy()
        state.__assignments = self.__assignments.copy()

        for supporter in activeSupporters:
            atom = supporter.effect.atom
            state.__intervals[atom] = state.__intervals[atom].getExtended(supporter.effect)
            state.applyAction(supporter.originatingAction)

        return state

    def applyAction(self, action: Action):

        state = RelaxedState()
        state.__intervals = self.__intervals.copy()
        state.__assignments = self.__assignments.copy()

        for eff in action.effects:
            if isinstance(eff, Literal):
                state.__assignments.add(eff)

        return state

    def __satisfiesAnd(self, formula: Formula):
        satisfied = True
        for c in formula.conditions:
            if isinstance(c, Predicate) and not self.satisfiesPredicate(c):
                return False
            if isinstance(c, Formula) and c.type == "AND" and not self.__satisfiesAnd(c):
                return False
            if isinstance(c, Formula) and c.type == "OR" and not self.__satisfiesOr(c):
                return False

        return satisfied

    def __satisfiesOr(self, formula: Formula):
        satisfied = False
        for c in formula.conditions:
            if isinstance(c, Predicate) and self.satisfiesPredicate(c):
                return True
            if isinstance(c, Formula) and c.type == "AND" and self.__satisfiesAnd(c):
                return True
            if isinstance(c, Formula) and c.type == "OR" and self.__satisfiesOr(c):
                return True

        return satisfied

    def satisfies(self, c: Formula) -> bool:
        return self.__satisfiesAnd(c) if c.type == "AND" else self.__satisfiesOr(c)

    def satisfiesPredicate(self, p: Predicate):

        if isinstance(p, Literal) or not isinstance(p, BinaryPredicate):
            return p in self.__assignments

        if p.operator == "!=":
            return True

        if p.operator not in {">=", ">", "<=", "<", "="}:
            raise Exception(f"Cannot check satisfaction for precondition with operator '{p.operator}'")

        function: BinaryPredicate = p.lhs - p.rhs
        interval: MooreInterval = self.substituteInto(function)

        return interval.exists(p.operator, 0)

    def substituteInto(self, p: Predicate) -> MooreInterval:
        if isinstance(p, Constant):
            return MooreInterval(p.value, p.value)
        if isinstance(p, Literal):
            return self.getAtom(p.getAtom())
        if isinstance(p, BinaryPredicate):
            lhs = self.substituteInto(p.lhs)
            rhs = self.substituteInto(p.rhs)
            return Utilities.op(p.operator, lhs, rhs)
