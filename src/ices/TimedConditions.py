from typing import List, Set

from src.ices.PlanIntermediateCondition import PlanIntermediateCondition


class TimedConditions:
    icond: Set[PlanIntermediateCondition]

    def __init__(self):
        self.icond = set()
        pass

    def __len__(self):
        return len(self.icond)

    def __iter__(self):
        return iter(self.icond)

    def addPlanIntermediateCondition(self, ic: PlanIntermediateCondition):
        self.icond.add(ic)
