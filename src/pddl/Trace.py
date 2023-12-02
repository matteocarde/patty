import re
from typing import List, Set

from src.pddl.Action import Action
from src.pddl.Domain import GroundedDomain
from src.pddl.Effects import Effects
from src.pddl.Event import Event
from src.pddl.Formula import Formula
from src.pddl.Operation import Operation
from src.pddl.OperationType import OperationType
from src.pddl.Preconditions import Preconditions
from src.pddl.Process import Process

classes = {
    OperationType.ACTION: Action,
    OperationType.EVENT: Event,
    OperationType.PROCESS: Process,
}


class Log:

    def __init__(self, time: float):
        self.time: float = time
        self.type: OperationType or None = None
        self.operations: Set[Operation] = set()

    def add(self, operation: Operation):
        self.operations.add(operation)
        self.type = operation.type

    def __str__(self):
        return f"{self.time} - {self.operations} - {self.type.value}"

    def __repr__(self):
        return str(self)

    def squash(self) -> Operation:
        if len(self.operations) == 1:
            return self.operations.pop()
        pass

        name = "_".join([op.name for op in self.operations])
        preconditions = Preconditions.join([op.preconditions for op in self.operations])
        effects = Effects.join([op.effects for op in self.operations])
        planName = "no"
        squashed = classes[self.type].fromProperties(name, preconditions, effects, planName)

        return squashed


class Trace:

    def __init__(self):
        self.logs: List[Log] = list()

    def __len__(self):
        return len(self.logs)

    def __iter__(self):
        return iter(self.logs)

    @classmethod
    def fromFile(cls, filename: str, domain: GroundedDomain):
        t = cls()

        f = open(filename, "r")
        stdout = f.read()
        f.close()

        lines = re.findall(r"^(.*?): (\(.*?\))$", stdout, re.MULTILINE)

        currentLog = None

        for (timeStr, action) in lines:
            time = float(timeStr)
            planName = action.replace(" ", "_")
            op: Operation = domain.getOperationByPlanName(planName)

            if not currentLog \
                    or currentLog.time != time \
                    or currentLog.type == OperationType.ACTION \
                    or currentLog.type != op.type:
                currentLog = Log(time)
                t.logs.append(currentLog)

            currentLog.add(op)

        return t

    def __str__(self):
        return str(self.logs)

    def __repr__(self):
        return str(self)

    @classmethod
    def squash(cls, operations):
        pass
