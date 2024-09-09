from __future__ import annotations

import copy
from typing import Dict, Set

from src.pddl.Action import Action
from src.pddl.Atom import Atom
from src.pddl.BinaryPredicate import BinaryPredicate
from src.pddl.Constant import Constant
from src.pddl.Literal import Literal


class PatternAction(Action):
    simpleAssignedAtoms: Set[Atom]
    assignedAtoms: Set[Atom]
    linearlyIncrementedAtoms: Set[Atom]
    constantAssignments: Dict[Atom, float or bool]

    def __init__(self):
        super().__init__()

    @classmethod
    def fromAction(cls, action: Action) -> PatternAction:
        pa = copy.deepcopy(action)
        pa.__class__ = PatternAction
        assert isinstance(pa, PatternAction)

        pa.assignedAtoms = set()
        pa.linearlyIncrementedAtoms = set()
        pa.simpleAssignedAtoms = set()
        pa.constantAssignments = dict()
        for e in pa.effects:
            if isinstance(e, BinaryPredicate):
                x = e.getAtom()
                pa.assignedAtoms.add(x)
                if e.isLinearIncrement():
                    pa.linearlyIncrementedAtoms.add(x)
                if not e.rhs.getFunctions().intersection(action.influencedAtoms):
                    pa.simpleAssignedAtoms.add(x)
                if isinstance(e.rhs, Constant) and e.operator == "assign":
                    pa.constantAssignments[x] = e.rhs.value
            elif isinstance(e, Literal):
                x = e.getAtom()
                pa.simpleAssignedAtoms.add(x)
                pa.constantAssignments[x] = True if e.sign == "+" else False
                pa.assignedAtoms.add(x)

        return pa

    def compare(self, other) -> int:
        if not isinstance(other, PatternAction):
            return False
        a = self
        a_ = other

        if a.interferesWithEffects(a_) and a_.interferesWithEffects(a):
            return 0
        if a.blocks(a_) and a_.blocks(a):
            return 0

        if a.blocks(a_):
            return +1
        if a_.blocks(a):
            return -1
        if a.supports(a_) and not a_.interferes(a):
            return -1
        if a_.supports(a) and not a.interferes(a_):
            return +1

        return 0

    def interferesWithEffects(self, a_: PatternAction) -> bool:
        return not self.__notInterferesWithEffects(a_)

    def __notInterferesWithEffects(self, a_: PatternAction) -> bool:
        a: PatternAction = self
        for x in self.assignedAtoms:
            res = x not in a_.assignedAtoms or \
                  (x in a.linearlyIncrementedAtoms and x in a_.linearlyIncrementedAtoms) or \
                  (x in a.simpleAssignedAtoms and x in a_.simpleAssignedAtoms)
            if not res:
                return False
        return True

    def blocks(self, a_: PatternAction) -> bool:
        for pre in a_.preconditions:
            if not pre.canHappen(self.constantAssignments):
                return True
        return False

    def supports(self, a_: PatternAction) -> bool:
        if not self.interferes(a_):
            return False
        for pre in a_.preconditions:
            if not pre.isValid(self.constantAssignments):
                return False
        return True
