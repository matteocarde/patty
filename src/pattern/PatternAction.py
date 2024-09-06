from __future__ import annotations
import copy
from typing import Dict, Set

from src.pddl.Action import Action
from src.pddl.Atom import Atom
from src.pddl.BinaryPredicate import BinaryPredicate
from src.pddl.Constant import Constant
from src.pddl.Formula import Formula
from src.pddl.Literal import Literal


class PatternAction(Action):
    simpleAssignments: Dict[Atom, float or bool]
    assignments: Set[Atom]
    linearIncremented: Set[Atom]

    def __init__(self):
        super().__init__()

    @classmethod
    def fromAction(cls, action: Action) -> PatternAction:
        pa = copy.deepcopy(action)
        pa.__class__ = PatternAction
        assert isinstance(pa, PatternAction)

        pa.assignments = set()
        pa.linearIncremented = set()
        pa.simpleAssignments = dict()
        for e in pa.effects:
            if isinstance(e, BinaryPredicate):
                x = e.getAtom()
                pa.assignments.add(x)
                if e.isLinearIncrement():
                    pa.linearIncremented.add(x)
                if isinstance(e.rhs, Constant):
                    pa.simpleAssignments[x] = e.rhs.value
            elif isinstance(e, Literal):
                x = e.getAtom()
                pa.simpleAssignments[x] = True if e.sign == "+" else False
                pa.assignments.add(x)

        return pa

    def __lt__(self, other):
        if not isinstance(other, PatternAction):
            return False
        a = self
        a_ = other

        if a.interferesWithEffects(a_) or a_.interferesWithEffects(a):
            return a.name < a_.name
        if a.blocks(a_):
            return False
        if a_.blocks(a):
            return True
        if a.supports(a_) and not a_.interferes(a):
            return True
        if a_.supports(a) and not a.interferes(a_):
            return False

        return a.name < a_.name

    def interferesWithEffects(self, a_: PatternAction) -> bool:
        return not self.__notInterferesWithEffects(a_)

    def __notInterferesWithEffects(self, a_: PatternAction) -> bool:
        a = self
        for x in self.assignments:
            res = x not in a_.assignments or \
                  (x in a.linearIncremented and x in a_.linearIncremented) or \
                  (x in a.simpleAssignments and x in a_.simpleAssignments)
            if not res:
                return False
        return True

    def blocks(self, a_: PatternAction) -> bool:
        for pre in a_.preconditions:
            if not pre.canHappen(self.simpleAssignments):
                return True
        return False

    def supports(self, a_: PatternAction) -> bool:
        if not self.interferes(a_):
            return False
        for pre in a_.preconditions:
            if not pre.isValid(self.simpleAssignments):
                return False
        return True
