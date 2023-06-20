from __future__ import annotations

from typing import Set, List

from src.pddl.Action import Operation


class Pattern:
    __order: List[Operation]

    def __init__(self):
        self.__order: List[Operation] = list()
        pass

    @classmethod
    def fromOrder(cls, order: List[Operation]):
        p = cls()
        p.__order = order

        return p

    def __iter__(self):
        return iter(self.__order)

    def extendNonLinearities(self, nOfActions: int):

        newOrder = self.__order.copy()
        for operation in self.__order:
            if not operation.hasNonSimpleLinearIncrement():
                continue
            rolledActions = list()
            for i in range(1, nOfActions):
                a_i = operation.getBinaryOperation(i)
                rolledActions.append(a_i)
            index = newOrder.index(operation)
            newOrder = newOrder[:index] + rolledActions + newOrder[index + 1:]
