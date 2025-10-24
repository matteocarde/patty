from typing import List, Set

from src.ices.PlanIntermediateEffect import PlanIntermediateEffect


class TimedEffects:
    ieff: Set[PlanIntermediateEffect]

    def __init__(self):
        self.ieff = set()
        pass

    def __len__(self):
        return len(self.ieff)

    def __str__(self):
        return str(self.ieff)

    def __iter__(self):
        return iter(self.ieff)

    def addPlanIntermediateEffect(self, ie: PlanIntermediateEffect):
        self.ieff.add(ie)
