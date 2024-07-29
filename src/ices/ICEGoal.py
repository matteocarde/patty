from typing import List

from src.ices.PlanIntermediateCondition import PlanIntermediateCondition


class ICEGoal:
    icond: List[PlanIntermediateCondition]

    def __init__(self):
        self.icond = list()
        pass

    def addPlanIntermediateCondition(self, ic: PlanIntermediateCondition):
        self.icond.append(ic)
