from __future__ import annotations
from typing import List, Dict

from src.pddl.Type import Type
from src.pddl.Operation import Operation
from src.pddl.OperationType import OperationType

from src.pddl.grammar.pddlParser import pddlParser as p


class Event(Operation):

    def __init__(self):
        super().__init__()

    @classmethod
    def fromNode(cls, node: p.EventContext, types: Dict[str, Type]):
        return super().fromNode(node, types)

    @property
    def type(self):
        return OperationType.EVENT

    def ground(self, problem, delta=1) -> List[Event]:
        groundOps: List = []
        for op in self.getGroundedOperations(problem, delta=delta):
            event = Event()
            event.name = op.name
            event.preconditions = op.preconditions
            event.effects = op.effects
            event.planName = op.planName
            groundOps.append(event)
        return groundOps
