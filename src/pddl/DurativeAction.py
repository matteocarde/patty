from __future__ import annotations

import copy
from typing import Dict, List

from src.pddl.BinaryPredicate import BinaryPredicate
from src.pddl.Constant import Constant
from src.pddl.Effects import Effects
from src.pddl.Literal import Literal
from src.pddl.Operation import Operation
from src.pddl.Preconditions import Preconditions
from src.pddl.Predicate import Predicate
from src.pddl.SnapAction import SnapAction
from src.pddl.TimePredicate import TimePredicate, TimePredicateType
from src.pddl.Type import Type
from src.pddl.grammar.pddlParser import pddlParser as p


class DurativeAction(Operation):
    name: str

    def __init__(self):
        super().__init__()
        self.duration: Predicate
        self.start: SnapAction
        self.overall: SnapAction
        self.end: SnapAction

    def __deepcopy__(self, m=None):
        if m is None:
            m = {}
        c = super().__deepcopy__(m)
        c.duration = copy.deepcopy(self.duration, m)
        m["durative"] = c
        c.start = copy.deepcopy(self.start, m)
        c.overall = copy.deepcopy(self.overall, m)
        c.end = copy.deepcopy(self.end, m)
        return c

    @classmethod
    def fromNode(cls, node: p.DurativeActionContext, types: Dict[str, Type]):
        da = cls()
        for child in node.children:
            if isinstance(child, p.OpNameContext):
                da.name = child.getText()
            elif isinstance(child, p.OpParametersContext):
                da.setParameters(child.getChild(1), types)
            elif isinstance(child, p.OpDurationContext):
                da.__setDuration(child.getChild(1))
            elif isinstance(child, p.OpDurativeConditionContext):
                da.addPreconditions(child)
            elif isinstance(child, p.OpDurativeEffectContext):
                da.addEffects(child)

        da.cacheLists()
        return da

    def getSnapAction(self, type: TimePredicateType) -> SnapAction:
        name = self.name + "_" + type.value.replace(" ", "_")
        parameters = self.parameters
        preconditions = Preconditions()
        effects = Effects()
        for p in self.preconditions:
            if not isinstance(p, TimePredicate):
                raise Exception("Durative actions should contain only TimePredicate")
            if p.type == type:
                preconditions.addPrecondition(p.subPredicate)
        for e in self.effects:
            if not isinstance(e, TimePredicate):
                raise Exception("Durative actions should contain only TimePredicate")
            if e.type == type:
                effects.addEffect(e.subPredicate)
        planName = self.planName
        sa = SnapAction.fromProperties(name, parameters, preconditions, effects, planName, duration=0)

        if type == TimePredicateType.AT_START:
            self.start = sa
        elif type == TimePredicateType.OVER_ALL:
            self.overall = sa
        elif type == TimePredicateType.AT_END:
            self.end = sa

        sa.durativeAction = self
        sa.timeType = type
        return sa

    def __setDuration(self, node: p.DurationAssignmentContext):
        op = node.op.getChild(0)
        if isinstance(op, p.OperationContext):
            self.duration = BinaryPredicate.fromNode(op)
        elif isinstance(op, p.PositiveLiteralContext):
            self.duration = Literal.fromNode(op)
        elif isinstance(op, p.ConstantContext):
            self.duration = Constant.fromNode(op)

    def ground(self, problem, delta=1) -> List[DurativeAction]:
        groundOps: List = []
        toGroundOps = self.getGroundedOperations(problem, delta=delta)
        for op in toGroundOps:
            op.__class__ = DurativeAction
            op.snapActions = dict()
            groundOps.append(op)
        return groundOps

    def areStartAndEndInMutex(self):
        return self.start.isMutex(self.end)
        pass

    @classmethod
    def fromAction(cls, action) -> DurativeAction:
        from src.pddl.Action import Action
        action: Action
        preconditions = action.preconditions.toTimePredicate(TimePredicateType.AT_START)
        effects = action.effects.toTimePredicate(TimePredicateType.AT_START)
        dAction = cls.fromProperties(action.name, action.parameters, preconditions, effects, action.planName)
        dAction.duration = Constant(0)
        return dAction
