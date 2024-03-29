from __future__ import annotations

from typing import Set, List

from src.pddl.Action import Operation, Action


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
        return "; ".join([str(x) for x in self.__order if not x.isFake])

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
