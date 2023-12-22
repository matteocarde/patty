from __future__ import annotations

from typing import Dict, List

from src.pddl.Action import Action
from src.pddl.Atom import Atom
from src.pddl.DurativeAction import DurativeAction
from src.pddl.Effects import Effects
from src.pddl.Preconditions import Preconditions
from src.pddl.TimePredicate import TimePredicateType


class SnapAction(Action):
    timeType: TimePredicateType

    def __init__(self):
        super().__init__()

    @classmethod
    def fromDurativeAction(cls, dAction: DurativeAction, type: TimePredicateType) -> SnapAction:
        name = dAction.name + "_" + type.value.replace(" ", "_")
        pre = Preconditions()
        for p in dAction.timedPreconditions:
            if p.type == type:
                pre.addPrecondition(p.subPredicate)
        eff = Effects()
        for e in dAction.timedEffects:
            if e.type == type:
                eff.addEffect(e.subPredicate)
        a = cls.fromProperties(name, dAction.parameters, pre, eff, name)
        a.__class__ = SnapAction
        a.timeType = type
        return a

    def ground(self, problem, isPredicateStatic: Dict[str, bool], delta=1) -> List[Action]:
        groundOps = super().ground(problem, isPredicateStatic, delta)
        for op in groundOps:
            op.__class__ = SnapAction
            op.timeType = self.timeType

        return groundOps

    def substitute(self, sub: Dict[Atom, float], default=None) -> Action:
        action = super().substitute(sub, default)
        action.__class__ = SnapAction
        action.timeType = self.timeType
        return action
