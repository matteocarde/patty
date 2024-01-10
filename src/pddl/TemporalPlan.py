from typing import List, Tuple, Set

from src.pddl.Action import Action
from src.pddl.DurativeAction import DurativeAction
from src.pddl.PDDLException import PDDLException
from src.pddl.Plan import Plan
from src.pddl.Problem import Problem
from src.pddl.State import State
from src.pddl.TemporalPlanAction import TemporalPlanAction
from src.pddl.TemporalPlanInstantAction import TemporalPlanInstantAction
from src.utils.LogPrint import LogPrint, LogPrintLevel


def validateError(message: str, avoidRaising=False, logger: LogPrint = None):
    if avoidRaising:
        if logger:
            logger.log(message, LogPrintLevel.PLAN)
    raise PDDLException.InvalidPlan(message)


class TemporalPlan(Plan):
    quality: float

    def __init__(self, epsilon: float):
        super().__init__()
        self.__plan: List[TemporalPlanAction] = list()
        self.__timedPlan: List[TemporalPlanInstantAction] = list()
        self.quality: float
        self.epsilon: float = epsilon
        self.optimal = False

    @property
    def rolledPlan(self):
        return sorted(self.__plan)

    def addAction(self, action: DurativeAction, time: float, duration: float):
        tpa = TemporalPlanAction(action, time, duration)
        self.__plan.append(tpa)

    def __str__(self):
        return "\n".join([f"{a}" for a in self.rolledPlan])

    def toValString(self):
        string = ""
        for tpa in self.rolledPlan:
            string += f"{tpa}\n"
        return string

    def addTimedAction(self, a: Action, t: float):
        tpia = TemporalPlanInstantAction(a, t)
        self.__timedPlan.append(tpia)

    def validate(self, problem: Problem, avoidRaising=False, logger: LogPrint = None) -> bool:
        timedPlan: List[TemporalPlanInstantAction] = sorted(self.__timedPlan)
        state = State.fromInitialCondition(problem.init)

        # Condition 1) The preconditions are respected
        for i, tpia in enumerate(timedPlan):
            action = tpia.action
            if not state.satisfies(action.preconditions):
                validateError(f"Plan doesn't satisfies preconditions of {action}@{i}. "
                              f"pre({action})={action.preconditions} at state {state}", avoidRaising, logger)
                return False
            state = state.applyAction(action)

        # Condition 2) Epsilon separation
        for tpia_i in timedPlan:
            for tpia_j in timedPlan:
                t_i = tpia_i.time
                t_j = tpia_j.time
                a_i = tpia_i.action
                a_j = tpia_j.action
                if a_i == a_j:
                    continue
                if a_i.isMutex(a_j) and round(abs(t_i - t_j), 3) < self.epsilon:
                    validateError(f"Actions {t_i}:{a_i} and {t_j}:{a_j} are in mutex and not epsilon separated",
                                  avoidRaising, logger)
                    return False

        # Condition 3) No self overlapping
        for tpa_1 in self.rolledPlan:
            for tpa_2 in self.rolledPlan:
                b_1: DurativeAction = tpa_1.action
                b_2: DurativeAction = tpa_2.action
                t_1 = tpa_1.time
                t_2 = tpa_2.time
                if b_1 != b_2 or tpa_1 == tpa_2:
                    continue
                d_1 = tpa_1.duration
                if round(t_1, 3) <= round(t_2, 3) < round(t_1 + d_1, 3):
                    validateError(f"Durative Actions {t_1}:{b_1} and {t_2}:{b_2} are self overlapping",
                                  avoidRaising, logger)
                    return False

        # Condition 4) The goal is satisfied
        if not state.satisfies(problem.goal):
            return False

        return True
