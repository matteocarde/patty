import re
from typing import List, Set

from src.pddl.Domain import GroundedDomain
from src.pddl.Operation import Operation
from src.pddl.OperationType import OperationType


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


class Trace:

    def __init__(self):
        self.logs: List[Log] = list()

    def __len__(self):
        return len(self.logs)

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
