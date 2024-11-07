from typing import List, Set

from src.pddl.Operation import Operation
from src.pddl.Problem import Problem
from src.utils.LogPrint import LogPrint


class Plan:

    def __init__(self):
        self.__plan: List = list()
        self.__rolledPlan: List = list()
        self.quality: float
        self.optimal = False

    def __len__(self):
        return len(self.__rolledPlan)

    @property
    def rolledPlan(self):
        return self.__rolledPlan

    @property
    def unrolledPlan(self):
        return [a for (a, i) in self.__plan]

    def __str__(self):
        return "\n".join([f"{a[0]} (x{a[1]})" for a in self.__plan])

    def __repr__(self):
        return str(self)

    def __iter__(self):
        return iter(self.__rolledPlan)

    def print(self):
        print(str(self))

    def validate(self, problem: Problem, avoidRaising=False, logger: LogPrint = None) -> bool:
        raise NotImplementedError()

    def toValString(self):
        raise NotImplementedError()

    def getMetric(self, problem: Problem):
        if not problem.metric:
            return len(self.__rolledPlan)

        raise Exception("Not yet implemented")

    def getActionsList(self):
        raise NotImplementedError()

    def getMaxRolling(self) -> int:
        raise NotImplementedError()

    def getDistinctActions(self) -> List[Operation]:
        raise NotImplementedError

    def getRolledActions(self) -> List[Operation]:
        raise NotImplementedError

    def toValString(self):
        raise NotImplementedError
