from __future__ import annotations

import math
from typing import Dict, Set

from src.goalFunctions.GoalFunction import EPSILON
from src.pddl.Action import Action
from src.pddl.Atom import Atom
from src.pddl.BinaryPredicate import BinaryPredicate
from src.pddl.Formula import Formula
from src.pddl.Constant import Constant
from src.pddl.InitialCondition import InitialCondition
from src.pddl.Literal import Literal
from src.pddl.MooreInterval import MooreInterval
from src.pddl.Predicate import Predicate
from src.pddl.State import State
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

    def __str__(self):
        strSet = []
        for key, item in self.__intervals.items():
            strSet.append(f"{key} = {item}")
        for item in self.__boolean:
            strSet.append(("¬" if item.sign == "-" else "") + str(item.getAtom()))
        return "{" + ",".join(strSet) + "}"

    def __eq__(self, other):
        if not isinstance(other, RelaxedIntervalState):
            return False
        if self.__boolean != other.boolean:
            return False
        if self.__intervals.keys() != other.__intervals.keys():
            return False
        for v in self.__intervals.keys():
            if self.__intervals[v] != other.__intervals[v]:
                return False
        return True

    @property
    def intervals(self) -> Dict[Atom, MooreInterval]:
        return self.__intervals

    @property
    def boolean(self) -> Set[Literal]:
        return self.__boolean

    @classmethod
    def fromState(cls, state: State, atoms: Set[Atom]):
        ris = cls()
        for (atom, value) in state.assignments.items():
            if type(value) is not bool:
                ris.__intervals[atom] = MooreInterval(value, value)

        posLit = set()
        negLit = set()
        for (atom, value) in state.assignments.items():
            if type(value) is not bool:
                continue
            ris.__boolean.add(Literal.fromAtom(atom, "+" if value else "-"))
            if value:
                posLit.add(atom)
            else:
                negLit.add(atom)

        for a in atoms:
            if a in posLit or a in negLit:
                continue
            ris.__boolean.add(Literal.fromAtom(a, "-"))

        return ris

    # @classmethod
    # def fromInitialCondition(cls, init: InitialCondition, atoms: Set[Atom]):
    #     ris = cls()
    #     for (atom, value) in init.numericAssignments.items():
    #         ris.__intervals[atom] = MooreInterval(value, value)
    #
    #     posLit = set()
    #     negLit = set()
    #     for lit in init.assignments:
    #         if not isinstance(lit, Literal):
    #             continue
    #         ris.__boolean.add(lit)
    #         if lit.sign == "+":
    #             posLit.add(lit.getAtom())
    #         else:
    #             negLit.add(lit.getAtom())
    #
    #     for a in atoms:
    #         if a in posLit or a in negLit:
    #             continue
    #         ris.__boolean.add(Literal.fromAtom(a, "-"))
    #
    #     return ris

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

    def getMaxRepetitions(self, action: Action):

        rep = []
        for x in action.getFunctions():
            pre = action.getLinearPrecondition(x)
            eff = action.getConstantIncrement(x)
            if not pre or not eff:
                rep.append(float("+inf"))
                continue
            x_hat = self.__intervals[x]
            (m, q) = action.getLinearPreconditionCoefficients(x)
            k = eff.getNormalizedRhs().getLinearIncrement()
            e = EPSILON if pre.operator in {">", "<"} else 0
            v_ub = (m * (k - x_hat.ub) - q + e) / (m * k)
            v_lb = (m * (k - x_hat.lb) - q + e) / (m * k)
            r_ub = max(v_ub, v_lb)
            r = math.floor(r_ub) if r_ub > 0 else float("+inf")
            rep.append(r)

        return min(rep)

    def applyAction(self, action: Action) -> RelaxedIntervalState:
        s_ = RelaxedIntervalState()
        s_.__intervals = self.__intervals.copy()
        s_.__boolean = self.__boolean.copy()

        r = self.getMaxRepetitions(action)

        for eff in action.effects:
            if isinstance(eff, Literal):
                s_.__boolean.add(eff)
            if isinstance(eff, BinaryPredicate):
                x = eff.getAtom()
                nRHS = eff.getNormalizedRhs()
                psi = self.substituteInto(nRHS)
                x_hat = s_.__intervals[x]
                if eff.operator == "assign":
                    interval = psi
                elif not action.couldBeRepeated():
                    interval = x_hat + psi
                elif not eff.rhs.getFunctions():
                    k = eff.getNormalizedRhs().getLinearIncrement()
                    interval = x_hat + MooreInterval(0, r) * k
                    print(action, x, interval)
                else:
                    interval = s_.__intervals[x] + psi
                    if psi < 0:
                        interval.lb = -float("inf")
                    if psi > 0:
                        interval.ub = +float("inf")
                s_.__intervals[x] = s_.__intervals[x].convexUnion(interval)
        return s_

    def convexUnion(self, other: RelaxedIntervalState) -> RelaxedIntervalState:
        s_ = RelaxedIntervalState()
        s_.__boolean = self.__boolean.copy() | other.__boolean.copy()
        for v in self.__intervals.keys():
            s_.__intervals[v] = self.__intervals[v].convexUnion(other.__intervals[v])

        return s_

    def applyActions(self, actions: Set[Action]):

        s = self
        for action in actions:
            s = self.applyAction(action).convexUnion(s)
        return s

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

    def satisfies(self, c: Formula or Predicate) -> bool:
        if isinstance(c, Formula):
            return self.__satisfiesAnd(c) if c.type == "AND" else self.__satisfiesOr(c)
        if isinstance(c, Predicate):
            return self.satisfiesPredicate(c)

    def satisfiesOne(self, c: Formula):
        for cond in c.conditions:
            if self.satisfies(cond):
                return True
        return False

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
