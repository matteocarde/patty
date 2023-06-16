from __future__ import annotations

from typing import Set, List

from Action import Operation
from Domain import GroundedDomain
from Problem import Problem
from RPG import RPG


class Pattern:
    __domain: GroundedDomain
    __problem: Problem

    def __init__(self):
        self.__actions: Set[Operation] = set()
        pass

    @classmethod
    def fromPlanningTask(cls, domain: GroundedDomain, problem: Problem) -> Pattern:
        p = cls()
        p.__actions = domain.actions
        p.__domain = domain
        p.__problem = problem

        return p

    def getPartialOrder(self) -> List[Set[Operation]]:
        rpg = RPG(self.__domain, self.__problem)

        return rpg.getPartialOrder()
