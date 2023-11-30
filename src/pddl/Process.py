from __future__ import annotations
from typing import List, Dict

from src.pddl.Type import Type
from src.pddl.Operation import Operation
from src.pddl.OperationType import OperationType

from src.pddl.grammar.pddlParser import pddlParser as p


class Process(Operation):

    def __init__(self):
        super().__init__()

    @classmethod
    def fromNode(cls, node: p.ProcessContext, types: Dict[str, Type]):
        return super().fromNode(node, types)

    @property
    def type(self):
        return OperationType.PROCESS

    def ground(self, problem) -> List[Process]:
        groundOps: List = []
        for op in self.getGroundedOperations(problem):
            name = op.name
            preconditions = op.preconditions
            effects = op.effects
            planName = op.planName
            process = Process.fromProperties(name, preconditions, effects, planName)
            groundOps.append(process)
        return groundOps
