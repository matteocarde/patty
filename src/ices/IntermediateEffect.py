from __future__ import annotations

from typing import List

from src.ices.RelativeTime import RelativeTime
from src.pddl.BinaryPredicate import BinaryPredicate
from src.pddl.Literal import Literal


class IntermediateEffect:
    time: RelativeTime
    effects: List[Literal or BinaryPredicate]

    atomsAdded: set()
    atomsDeleted: set()
    atomsAssigned: set()

    def __init__(self):
        super().__init__()
        self.effects = list()
        self.atomsAdded = set()
        self.atomsDeleted = set()
        self.atomsAssigned = set()
        self.atomsNumeric = set()

    def __repr__(self):
        return str(self.effects)

    @classmethod
    def fromProperties(cls, time: RelativeTime) -> IntermediateEffect:
        raise NotImplementedError()

    def addEffect(self, eff: Literal or BinaryPredicate):
        self.effects.append(eff)
        if isinstance(eff, Literal) and eff.sign == "+":
            self.atomsAdded.add(eff.getAtom())
        if isinstance(eff, Literal) and eff.sign == "-":
            self.atomsDeleted.add(eff.getAtom())
        if isinstance(eff, BinaryPredicate):
            self.atomsAssigned.add(eff.getAtom())
            self.atomsNumeric.add(eff.getFunctions())

    @property
    def atomsTouched(self):
        return self.atomsAssigned | self.atomsAdded | self.atomsDeleted

    def interfere(self, effect: IntermediateEffect):
        if self.atomsAdded.intersection(effect.atomsDeleted):
            return True
        if self.atomsAssigned.intersection(effect.atomsAssigned):
            return True
        if self.atomsAssigned.intersection(effect.atomsNumeric):
            return True
        return False

    def inMutexWith(self, effect: IntermediateEffect):
        return self.interfere(effect) or effect.interfere(self)
