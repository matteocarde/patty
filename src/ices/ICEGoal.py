from typing import List

from src.ices.PlanIntermediateCondition import PlanIntermediateCondition


class ICEGoal:
    icond: List[PlanIntermediateCondition]

    def __init__(self):
        self.icond = list()
        pass

    def __iter__(self):
        return iter(self.icond)

    def addPlanIntermediateCondition(self, ic: PlanIntermediateCondition):
        self.icond.append(ic)
