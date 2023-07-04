from __future__ import annotations
from typing import Dict, Set

from src.pddl.Action import Action
from src.pddl.Atom import Atom
from src.pddl.BinaryPredicate import BinaryPredicate
from src.pddl.Formula import Formula
from src.pddl.Constant import Constant
from src.pddl.InitialCondition import InitialCondition
from src.pddl.Literal import Literal
from src.pddl.MooreInterval import MooreInterval
from src.pddl.Predicate import Predicate
from src.pddl.Supporter import Supporter
from src.pddl.Utilities import Utilities


class RelaxedIntervalState:
    __intervals: Dict[Atom, MooreInterval]
    __boolean: Set[Literal]

    def __init__(self):
        self.__intervals = dict()
        self.__boolean = set()

    def __repr__(self):
        return repr(self.__intervals)

    @property
    def intervals(self) -> Dict[Atom, MooreInterval]:
        return self.__intervals

    @property
    def boolean(self) -> Set[Literal]:
        return self.__boolean

    @classmethod
    def fromInitialCondition(cls, init: InitialCondition, atoms: Set[Atom]):
        ris = cls()
        for (atom, value) in init.numericAssignments.items():
            ris.__intervals[atom] = MooreInterval(value, value)

        posLit = set()
        negLit = set()
        for lit in init.assignments:
            if not isinstance(lit, Literal):
                continue
            ris.__boolean.add(lit)
            if lit.sign == "+":
                posLit.add(lit.getAtom())
            else:
                negLit.add(lit.getAtom())

        for a in atoms:
            if a in posLit or a in negLit:
                continue
            ris.__boolean.add(Literal.fromAtom(a, "-"))

        return ris

    def getAtom(self, atom: Atom) -> MooreInterval:
        if not atom in self.__intervals:
            return MooreInterval(0, 0)
        return self.__intervals[atom]

    def applySupporters(self, activeSupporters: Set[Supporter]):

        state = RelaxedIntervalState()
        state.__intervals = self.__intervals.copy()
        state.__boolean = self.__boolean.copy()

        for supporter in activeSupporters:
            if supporter.effect:
                atom = supporter.effect.atom
                state.__intervals[atom] = state.getAtom(atom).getExtended(supporter.effect)
            og: Action = supporter.originatingAction
            for add in og.addList:
                state.__boolean.add(Literal.fromAtom(add, "+"))
            for d in og.delList:
                state.__boolean.add(Literal.fromAtom(d, "-"))

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

        if isinstance(p, Literal):
            return p in self.__boolean

        if not isinstance(p, BinaryPredicate):
            return True

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

    def coincide(self, newState: RelaxedIntervalState):
        for (atom, interval) in self.__intervals.items():
            if atom not in newState.__intervals:
                return False

            if newState.__intervals[atom] != self.__intervals[atom]:
                return False

        return len(newState.__boolean.difference(self.__boolean)) == 0
