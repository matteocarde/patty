from __future__ import annotations

import copy
import random
from typing import List

from src.pddl.Action import Operation, Action
from src.pddl.Domain import GroundedDomain


class Pattern:
    __order: List[Operation]
    dummyAction: Action

    def __init__(self):
        self.__order: List[Operation] = list()
        pass

    def __getitem__(self, item):
        return self.__order[item]

    @classmethod
    def fromOrder(cls, order: List[Operation]):
        p = cls()
        p.dummyAction = Action()
        p.dummyAction.isFake = True
        p.dummyAction.name = "final_dummy_g"

        order.append(p.dummyAction)
        p.__order = order

        return p

    def __iter__(self):
        return iter(self.__order)

    def __str__(self):
        return "\n".join([str(x) for x in self.__order if not x.isFake])

    def extendNonLinearities(self, nOfActions: int):

        newOrder = self.__order.copy()
        for operation in self.__order:
            if not operation.hasNonSimpleLinearIncrement():
                continue
            rolledActions = list()
            for i in range(0, nOfActions):
                a_i = operation.getBinaryOperation(i)
                a_i.linearizationOf = operation
                a_i.linearizationTimes = 2 ** i
                rolledActions.append(a_i)
            index = newOrder.index(operation)
            newOrder = newOrder[:index] + rolledActions + newOrder[index + 1:]

        self.__order = newOrder

    def multiply(self, times: int) -> Pattern:

        order = []
        for i in range(0, times):
            for item in self.__order[:-1]:
                a = copy.deepcopy(item)
                a.name = f"{a.name}_{i}"
                order.append(a)

        return Pattern.fromOrder(order)

    @classmethod
    def fromARPG(cls, gDomain: GroundedDomain) -> Pattern:
        order = gDomain.getARPG().getActionsOrder()
        return Pattern.fromOrder(order)

    @classmethod
    def fromRandom(cls, gDomain: GroundedDomain) -> Pattern:
        order = list(gDomain.actions)
        random.shuffle(order)
        return Pattern.fromOrder(order)
