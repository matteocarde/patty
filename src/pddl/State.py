from __future__ import annotations

import copy
from typing import Dict, Set

from src.ices.ParallelIntermediateEffects import ParallelIntermediateEffects
from src.ices.PlanIntermediateEffect import PlanIntermediateEffect
from src.pddl.Action import Action
from src.pddl.Atom import Atom
from src.pddl.BinaryPredicate import BinaryPredicate
from src.pddl.ConditionalEffect import ConditionalEffect
from src.pddl.Constant import Constant
from src.pddl.Formula import Formula
from src.pddl.InitialCondition import InitialCondition
from src.pddl.Literal import Literal
from src.pddl.Predicate import Predicate
from src.pddl.Utilities import Utilities


class State:
    assignments: Dict[Atom, bool or float]

    def __init__(self):
        self.assignments: Dict[Atom, bool or float] = dict()

    def __deepcopy__(self, m=None) -> State:
        m = {} if m is None else m
        s = State()
        s.__assignments = copy.deepcopy(self.assignments, m)
        return s

    @classmethod
    def fromInitialCondition(cls, init: InitialCondition):
        state = cls()

        assignment: Predicate
        for assignment in init.assignments:
            atom = assignment.getAtom()
            state.assignments[atom] = state.getRealization(assignment)

        return state

    def getAtom(self, atom: Atom) -> bool or float:
        if atom not in self.assignments:
            return False
        return self.assignments[atom]

    def setAtom(self, atom: Atom, assignment: bool or float):
        self.assignments[atom] = assignment

    def __repr__(self):
        return repr(self.assignments)

    def __str__(self):
        return str(self.toClosedWorldSet())

    def toClosedWorldSet(self) -> Set[Predicate]:

        cwset = set()
        for (atom, value) in self.assignments.items():
            if type(value) == bool and value:
                cwset.add(Literal.pos(atom))
            if type(value) != bool:
                cwset.add(BinaryPredicate.fromAssignment(atom, value))

        return cwset

    def asBooleanSet(self):
        return sorted({v for (v, a) in self.assignments.items() if a})

    def applyAction(self, action: Action):
        state = State()
        state.assignments = self.assignments.copy()

        if not state.satisfies(action.preconditions):
            raise Exception(
                f"Tried to apply action {action} to a state {state} in which its preconditions {action.preconditions} are not satisfied")

        effect: Predicate
        added: Set[Atom] = set()
        deleted: Set[Atom] = set()
        for effect in action.effects:
            if not isinstance(effect, ConditionalEffect):
                state.assignments[effect.getAtom()] = self.getRealization(effect)
                continue
            assert isinstance(effect, ConditionalEffect)
            if state.satisfies(effect.conditions):
                added |= effect.effects.getPositive()
                deleted |= effect.effects.getNegative()
        if added & deleted:
            raise Exception(f"Action {action} has conflicting CES in state {state}")
        for v in added:
            state.assignments[v] = True
        for v in deleted:
            state.assignments[v] = False

        return state

    def applyParallelIntermediateEffects(self, pieff: ParallelIntermediateEffects) -> State:

        state = State()
        state.assignments = self.assignments.copy()

        for eff in pieff:
            for effect in eff.effects:
                state.assignments[effect.getAtom()] = self.getRealization(effect)

        return state

    def applyPlan(self, plan):
        state = self
        for (i, action) in enumerate(plan):
            state = state.applyAction(action)
        return state

    def __satisfiesAnd(self, formula: Formula, tolerance=0.0):
        satisfied = True
        for c in formula.conditions:
            if isinstance(c, Predicate) and not self.satisfiesPredicate(c, tolerance=tolerance):
                return False
            if isinstance(c, Formula) and c.type == "AND" and not self.__satisfiesAnd(c, tolerance=tolerance):
                return False
            if isinstance(c, Formula) and c.type == "OR" and not self.__satisfiesOr(c, tolerance=tolerance):
                return False

        return satisfied

    def __satisfiesOr(self, formula: Formula, tolerance=0.0):
        satisfied = False
        for c in formula.conditions:
            if isinstance(c, Predicate) and self.satisfiesPredicate(c, tolerance=tolerance):
                return True
            if isinstance(c, Formula) and c.type == "AND" and self.__satisfiesAnd(c, tolerance=tolerance):
                return True
            if isinstance(c, Formula) and c.type == "OR" and self.__satisfiesOr(c, tolerance=tolerance):
                return True

        return satisfied

    def satisfies(self, c: Formula or Predicate, tolerance=0.0) -> bool:
        if isinstance(c, Predicate):
            return self.satisfiesPredicate(c)
        return self.__satisfiesAnd(c, tolerance) if c.type == "AND" else self.__satisfiesOr(c, tolerance)

    def satisfiesPredicate(self, p: Predicate, tolerance=0.0):
        if isinstance(p, Literal):
            atom = p.getAtom()
            if p.sign == "+":
                return atom in self.assignments and self.assignments[atom]
            else:
                return atom not in self.assignments or not self.assignments[atom]

        if not isinstance(p, BinaryPredicate):
            raise "Precondition can only be BinaryPredicate or Literal"

        if p.operator not in {">=", ">", "<=", "<", "=", "!="}:
            raise Exception(f"Cannot check satisfaction for precondition with operator '{p.operator}'")

        function: BinaryPredicate = p.lhs - p.rhs
        result = self.substituteInto(function)

        if tolerance:
            if p.operator == "=":
                return abs(result) <= tolerance
            if p.operator in {">", ">=", "!="}:
                return result >= - tolerance
            if p.operator in {"<", "<="}:
                return result <= tolerance

        return Utilities.compare(p.operator, result, 0)

    def getRealization(self, p: Predicate):
        if isinstance(p, Literal):
            return True if p.sign == "+" else False
        if isinstance(p, BinaryPredicate):
            if p.operator not in {"=", "assign", "increase", "decrease"}:
                raise Exception(f"Operator {p.operator} not allowed in effects")

            lhs = self.substituteInto(p.rhs)
            value = self.assignments[p.getAtom()] if p.getAtom() in self.assignments else 0
            if p.operator == "assign" or p.operator == "=":
                return lhs
            if p.operator == "increase":
                return value + lhs
            if p.operator == "decrease":
                return value - lhs

    def substituteInto(self, p: Predicate) -> bool or float:
        if isinstance(p, Constant):
            return p.value
        if isinstance(p, Literal):
            return self.assignments[p.getAtom()] if p.getAtom() in self.assignments else 0
        if isinstance(p, BinaryPredicate):
            lhs = self.substituteInto(p.lhs)
            rhs = self.substituteInto(p.rhs)
            return Utilities.op(p.operator, lhs, rhs)
