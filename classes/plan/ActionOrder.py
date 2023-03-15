from typing import List, Set

from ARPG import ARPG
from Action import Action
from Domain import GroundedDomain
from Problem import Problem
from RelaxedIntervalState import RelaxedIntervalState
from Supporter import Supporter


class ActionOrder:

    def __init__(self, domain: GroundedDomain, problem: Problem, dummyAction: Action):
        self.domain = domain
        self.problem = problem

        self.__order: List[Action] = self.__computeOrder()
        self.__order.append(dummyAction)

    def __computeOrder(self) -> List[Action]:
        arpg = ARPG(self.domain, self.problem)
        return arpg.getActionsOrder()

    def __iter__(self):
        return iter(self.__order)

    def __str__(self):
        return str(self.__order)

    def __repr__(self):
        return str(self)
