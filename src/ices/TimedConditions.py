from typing import List

from src.ices.PlanIntermediateCondition import PlanIntermediateCondition


class TimedConditions:
    icond: List[PlanIntermediateCondition]

    def __init__(self):
        self.icond = list()
        pass

    def __len__(self):
        return len(self.icond)

    def __iter__(self):
        return iter(self.icond)

    def addPlanIntermediateCondition(self, ic: PlanIntermediateCondition):
        self.icond.append(ic)
