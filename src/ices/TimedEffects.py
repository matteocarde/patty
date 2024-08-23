from typing import List

from src.ices.PlanIntermediateEffect import PlanIntermediateEffect


class TimedEffects:
    ieff: List[PlanIntermediateEffect]

    def __init__(self):
        self.ieff = list()
        pass

    def __len__(self):
        return len(self.ieff)

    def __iter__(self):
        return iter(self.ieff)

    def addPlanIntermediateEffect(self, ie: PlanIntermediateEffect):
        self.ieff.append(ie)
