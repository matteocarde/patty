from __future__ import annotations

import copy
from typing import Dict, Set

from src.pattern.PatternAction import PatternAction
from src.pddl.Action import Action
from src.pddl.Atom import Atom
from src.pddl.BinaryPredicate import BinaryPredicate
from src.pddl.Constant import Constant
from src.pddl.Literal import Literal
from src.pddl.Operation import Operation
from src.pddl.SnapAction import SnapAction
from src.pddl.TimePredicate import TimePredicateType


class BooleanPatternAction:
    action: Action
    name: str
    prePos: Set[Atom]
    preNeg: Set[Atom]
    addedAtoms: Set[Atom]
    deletedAtoms: Set[Atom]
    __hash: int

    def __init__(self):
        super().__init__()

    @classmethod
    def fromAction(cls, action: Action) -> BooleanPatternAction:
        pa = cls()
        pa.action = action
        pa.name = action.name
        pa.__hash = hash(action.name)
        pa.prePos = action.prePos
        pa.preNeg = action.preNeg
        pa.addedAtoms = action.addedAtoms
        pa.deletedAtoms = action.deletedAtoms
        return pa

    def __hash__(self):
        return self.__hash

    def __lt__(self, other):
        return self.name < other.name

    def __repr__(self):
        return f"<pre+={self.prePos}, pre-={self.preNeg}, add={self.addedAtoms}, del={self.deletedAtoms}>"

    def compare(self, other) -> int:
        if not isinstance(other, BooleanPatternAction):
            return False
        a = self
        a_ = other

        if a.blocks(a_) and a_.blocks(a):
            return 0

        if a.blocks(a_):
            return +1
        if a_.blocks(a):
            return -1
        if a.supports(a_) and not a_.interferesWithExecutability(a):
            return -1
        if a_.supports(a) and not a.interferesWithExecutability(a_):
            return +1

        return 0

    def interferesWithExecutability(self, a_: BooleanPatternAction) -> bool:
        return bool((self.addedAtoms | self.deletedAtoms) & (a_.prePos | a_.preNeg))

    def blocks(self, a_: BooleanPatternAction) -> bool:
        return bool((self.addedAtoms & a_.preNeg)) or bool(self.deletedAtoms & a_.prePos)

    def supports(self, a_: BooleanPatternAction) -> bool:
        if not self.action.interferes(a_.action):
            return False
        # v = a_.prePos.issubset(self.addedAtoms) and a_.preNeg.issubset(self.deletedAtoms)
        v = bool(a_.prePos & self.addedAtoms) or bool(a_.preNeg & self.deletedAtoms)
        return v
