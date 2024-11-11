from __future__ import annotations

from typing import Set

from src.pddl.Atom import Atom
from src.pddl.Preconditions import Preconditions
from src.pddl.TimePredicate import TimePredicateType


class SupporterEffect:

    def __init__(self, atom: Atom, value: float):
        self.atom = atom
        self.value = value
        pass

    def __str__(self):
        return f"[{self.atom}, {self.value}]"

    def __repr__(self):
        return str(self)


class Supporter:
    preconditions: Preconditions
    effect: SupporterEffect
    originatingAction: 'Action'

    def __init__(self, originatingAction, preconditions: Preconditions, effect: SupporterEffect or None):
        self.preconditions = preconditions
        self.effect = effect
        self.originatingAction = originatingAction
        pass

    def isSatisfiedBy(self, state) -> bool:
        return state.satisfies(self.preconditions)

    def __str__(self):
        return f"<{self.preconditions}, {self.effect}, {self.originatingAction.name}>"

    def __repr__(self):
        return str(self)

    def respectsTemporal(self, usedActions: Set["Action"]):
        from src.pddl.SnapAction import SnapAction
        if not isinstance(self.originatingAction, SnapAction):
            return True
        if self.originatingAction.timeType == TimePredicateType.AT_START:
            return True
        if self.originatingAction.timeType == TimePredicateType.OVER_ALL:
            return False
        if self.originatingAction.timeType == TimePredicateType.AT_END:
            return self.originatingAction.durativeAction.start in usedActions
        raise Exception("This should not be reached")
