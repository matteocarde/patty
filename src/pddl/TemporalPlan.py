from typing import List, Tuple, Set

from src.pddl.Action import Action
from src.pddl.DurativeAction import DurativeAction
from src.pddl.Plan import Plan
from src.pddl.Problem import Problem
from src.pddl.TemporalPlanAction import TemporalPlanAction
from src.utils.LogPrint import LogPrint


class TemporalPlan(Plan):
    quality: float

    def __init__(self):
        super().__init__()
        self.__plan: List[TemporalPlanAction] = list()
        self.quality: float
        self.optimal = False

    @property
    def rolledPlan(self):
        return sorted(self.__plan)

    def addAction(self, action: DurativeAction, time: float, duration: float):
        tpa = TemporalPlanAction(action, time, duration)
        self.__plan.append(tpa)

    def __str__(self):
        return "\n".join([f"{a}" for a in self.rolledPlan])

    def validate(self, problem: Problem, avoidRaising=False, logger: LogPrint = None) -> bool:
        return True

    def toValString(self):
        string = ""
        for tpa in self.rolledPlan:
            string += f"{tpa}\n"
        return string
