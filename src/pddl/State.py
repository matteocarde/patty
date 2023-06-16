from typing import Dict

from src.pddl.Action import Action
from src.pddl.Atom import Atom
from src.pddl.BinaryPredicate import BinaryPredicate
from src.pddl.Formula import Formula
from src.pddl.Constant import Constant
from src.pddl.InitialCondition import InitialCondition
from src.pddl.Literal import Literal
from src.pddl.Predicate import Predicate
from src.pddl.Utilities import Utilities


class State:
    __assignments: Dict[Atom, bool or float]

    def __init__(self):
        self.__assignments: Dict[Atom, bool or float] = dict()

    @classmethod
    def fromInitialCondition(cls, init: InitialCondition):
        state = cls()

        assignment: Predicate
        for assignment in init.assignments:
            atom = assignment.getAtom()
            state.__assignments[atom] = state.getRealization(assignment)

        return state

    def getAtom(self, atom: Atom) -> bool or float:
        if atom not in self.__assignments:
            return False
        return self.__assignments[atom]

    def __repr__(self):
        return repr(self.__assignments)

    def applyAction(self, action: Action):

        state = State()
        state.__assignments = self.__assignments.copy()

        if not state.satisfies(action.preconditions):
            raise Exception(f"Tried to apply action {action} to a state in which its preconditions are note satisfied")

        effect: Predicate
        for effect in action.effects:
            state.__assignments[effect.getAtom()] = self.getRealization(effect)

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
            atom = p.getAtom()
            if p.sign == "+":
                return atom in self.__assignments and self.__assignments[atom]
            else:
                return atom not in self.__assignments or not self.__assignments[atom]

        if not isinstance(p, BinaryPredicate):
            raise "Precondition can only be BinaryPredicate or Literal"

        if p.operator not in {">=", ">", "<=", "<", "=", "!="}:
            raise Exception(f"Cannot check satisfaction for precondition with operator '{p.operator}'")

        function: BinaryPredicate = p.lhs - p.rhs
        result = self.substituteInto(function)

        return Utilities.compare(p.operator, result, 0)

    def getRealization(self, p: Predicate):
        if isinstance(p, Literal):
            return True if p.sign == "+" else False
        if isinstance(p, BinaryPredicate):
            if p.operator not in {"=", "assign", "increase", "decrease"}:
                raise Exception(f"Operator {p.operator} not allowed in effects")

            lhs = self.substituteInto(p.rhs)
            if p.operator == "assign" or p.operator == "=":
                return lhs
            if p.operator == "increase":
                return self.__assignments[p.getAtom()] + lhs
            if p.operator == "decrease":
                return self.__assignments[p.getAtom()] - lhs

    def substituteInto(self, p: Predicate) -> bool or float:
        if isinstance(p, Constant):
            return p.value
        if isinstance(p, Literal):
            return self.__assignments[p.getAtom()]
        if isinstance(p, BinaryPredicate):
            lhs = self.substituteInto(p.lhs)
            rhs = self.substituteInto(p.rhs)
            return Utilities.op(p.operator, lhs, rhs)
