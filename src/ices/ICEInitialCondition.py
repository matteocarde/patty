from typing import List

from src.ices.ICEAction import BEGIN
from src.ices.PlanIntermediateEffect import PlanIntermediateEffect
from src.pddl.State import State


class ICEInitialCondition:
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

    def getInitialState(self) -> State:
        initialEff = [e for e in self.ieff if e.time == BEGIN + 0]
        if len(initialEff) != 1:
            raise Exception(
                f"The initial state must be specified by exactly one PlanIntermediateEffect. Found: {len(initialEff)}")

        return State.fromPlanIntermediateEffect(initialEff[0])
