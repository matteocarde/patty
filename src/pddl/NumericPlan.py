from typing import List, Tuple, Set

from src.pddl.Action import Action
from src.pddl.Operation import Operation
from src.pddl.PDDLException import PDDLException
from src.pddl.Plan import Plan
from src.pddl.Problem import Problem
from src.pddl.State import State
from src.utils.LogPrint import LogPrint, LogPrintLevel


class NumericPlan(Plan):
    quality: float

    def __init__(self):
        super().__init__()
        self.__plan: List[Tuple[Action, int]] = list()
        self.__rolledPlan: List[Action] = list()
        self.quality: float
        self.optimal = False

    def __len__(self):
        return len(self.__rolledPlan)

    def getActionsList(self):
        return self.unrolledPlan

    @property
    def rolledPlan(self):
        return self.__rolledPlan

    @property
    def unrolledPlan(self):
        return [a for (a, i) in self.__plan]

    def addRepeatedAction(self, action: Action, repetitions: int):
        self.__plan.append((action, repetitions))
        for i in range(0, repetitions):
            self.__rolledPlan.append(action)

    def validate(self, problem: Problem, avoidRaising=False, logger: LogPrint = None) -> bool:

        state = State.fromInitialCondition(problem.init)
        for i, action in enumerate(self.__rolledPlan):
            if not state.satisfies(action.preconditions):
                if avoidRaising:
                    if logger:
                        logger.log(
                            f"Plan doesn't satisfies preconditions of {action}@{i}. pre({action})={action.preconditions} at state {state}",
                            LogPrintLevel.PLAN)
                    return False
                raise PDDLException.InvalidPlan(f"Plan doesn't satisfies action {action}")
            state = state.applyAction(action)

        if not state.satisfies(problem.goal):
            if avoidRaising:
                if logger:
                    logger.log(f"Plan doesn't satisfies goal", LogPrintLevel.PLAN)
                return False
            raise PDDLException.InvalidPlan(f"Plan doesn't satisfies goal")

        return True

    def __str__(self):
        return "\n".join([f"{a[0]} x{a[1]}" for a in self.__plan])

    def __repr__(self):
        return str(self)

    def __iter__(self):
        return iter(self.__rolledPlan)

    def print(self):
        print(str(self))

    def toValString(self):
        string = ""
        t = 0
        for a in self.__plan:
            for i in range(0, a[1]):
                string += f"{t}: ({a[0]})\n"
                t += 1
        return string

    def printWithRepetitions(self):
        print(self.toValString())

    def getMaxRolling(self) -> int:
        return max([i for (a, i) in self.__plan])

    def getDistinctActions(self) -> Set[Operation]:
        return {a for a in self.__rolledPlan}

    def getRolledActions(self) -> Set[Operation]:
        return {a for (a, i) in self.__plan if i > 1}

    def getMetric(self, problem: Problem):
        if not problem.metric:
            return len(self.__rolledPlan)

        raise Exception("Not yet implemented")
