from __future__ import annotations

from typing import List, Set, Dict, Tuple

from src.ices.RelativeTime import RelativeTime
from src.pddl.Atom import Atom
from src.pddl.BinaryPredicate import BinaryPredicate, BinaryPredicateType
from src.pddl.Constant import Constant
from src.pddl.Effects import Effects
from src.pddl.Literal import Literal
from src.utils.Tuplable import Tuplable


class IntermediateEffect(Tuplable):
    time: RelativeTime or float
    effects: Effects

    atoms: Set[Atom]
    atomsAdded: Set[Atom]
    atomsDeleted: Set[Atom]
    atomsAssigned: Set[Atom]
    atomsNumeric: Set[Atom]
    atomToConstant: Dict[Atom, float]
    atomToEffect: Dict[Atom, BinaryPredicate]

    def __init__(self):
        super().__init__()
        self.atomToEffect = dict()
        self.atomToConstant = dict()
        self.effects = Effects()
        self.atoms = set()
        self.atomsAdded = set()
        self.atomsDeleted = set()
        self.atomsAssigned = set()
        self.atomsNumeric = set()

    def __repr__(self):
        return str(self.effects)

    def __str__(self):
        return f"<{self.time}, {self.effects}>"

    def toTuple(self) -> Tuple:
        return self.time, self.effects

    @classmethod
    def fromProperties(cls, time: RelativeTime) -> IntermediateEffect:
        raise NotImplementedError()

    def addEffect(self, eff: Literal or BinaryPredicate):
        self.effects.addEffect(eff)
        if isinstance(eff, Literal) and eff.sign == "+":
            self.atomsAdded.add(eff.getAtom())
            self.atoms.add(eff.getAtom())
        if isinstance(eff, Literal) and eff.sign == "-":
            self.atomsDeleted.add(eff.getAtom())
            self.atoms.add(eff.getAtom())
        if isinstance(eff, BinaryPredicate):
            self.atomsAssigned.add(eff.getAtom())
            self.atoms.add(eff.getAtom())
            self.atomToEffect[eff.getAtom()] = eff
            self.atomsNumeric.update(eff.getFunctions())
            self.atoms.update(eff.getFunctions())
            if eff.type == BinaryPredicateType.MODIFICATION and isinstance(eff.rhs, Constant):
                self.atomToConstant[eff.getAtom()] = eff.rhs.value

    def toAbsolute(self, a: float, b: float) -> IntermediateEffect:
        ie = self.__class__()
        ie.time = self.time.absolute(a, b)
        ie.effects = self.effects

        ie.atomsAdded = self.atomsAdded
        ie.atomsDeleted = self.atomsDeleted
        ie.atomsAssigned = self.atomsAssigned
        ie.atomsNumeric = self.atomsNumeric

        return ie

    @property
    def atomsTouched(self):
        return self.atomsAssigned | self.atomsAdded | self.atomsDeleted

    def interfere(self, effect: IntermediateEffect):
        if self.atomsAdded.intersection(effect.atomsDeleted):
            return True
        if self.atomsAdded.intersection(effect.atomsAdded):
            return True
        if self.atomsDeleted.intersection(effect.atomsDeleted):
            return True
        if self.atomsAssigned.intersection(effect.atomsAssigned):
            return True
        if self.atomsAssigned.intersection(effect.atomsNumeric):
            return True
        return False

    def inMutexWith(self, other):
        from src.ices.IntermediateCondition import IntermediateCondition
        if isinstance(other, IntermediateCondition):
            return other.inMutexWith(self)
        return self.interfere(other) or other.interfere(self)
