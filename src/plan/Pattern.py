from __future__ import annotations

import copy
import random
from typing import List, Dict

from src.pddl.ARPG import ARPG
from src.pddl.Action import Operation, Action
from src.pddl.Goal import Goal
from src.pddl.GroundedDomain import GroundedDomain
from src.pddl.NumericPlan import NumericPlan
from src.pddl.State import State


class Pattern:
    __order: List[Operation]
    dummyAction: Action

    def __init__(self):
        self.__order: List[Operation] = list()
        pass

    def __deepcopy__(self, m=None) -> Pattern:
        m = {} if m is None else m
        p = Pattern()
        p.__order = copy.copy(self.__order)
        p.dummyAction = copy.copy(self.dummyAction)
        return p

    def __getitem__(self, item):
        return self.__order[item]

    def __len__(self):
        return len(self.__order)

    @property
    def order(self):
        return self.__order

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

    def __add__(self, other):
        if not isinstance(other, Pattern):
            raise Exception("Cannot concatenate Pattern with element not of type Pattern")
        catPattern: Pattern = Pattern()
        catPattern.__order = [a for a in self.__order if not a.isFake] + [b for b in other.__order if not b.isFake]
        catPattern.dummyAction = other.dummyAction
        catPattern.__order.append(catPattern.dummyAction)

        return catPattern

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
                a.name = f"{a.name}_{i}" if times > 1 else f"{a.name}"
                # a.name = f"{a.name}_{i}"
                order.append(a)

        return Pattern.fromOrder(order)

    @classmethod
    def fromARPG(cls, gDomain: GroundedDomain, useSCCs=False) -> Pattern:
        order = gDomain.getARPG().getActionsOrder(useSCCs)
        return Pattern.fromOrder(order)

    @classmethod
    def fromRandom(cls, gDomain: GroundedDomain) -> Pattern:
        order = list(gDomain.actions)
        random.shuffle(order)
        return Pattern.fromOrder(order)

    @classmethod
    def fromState(cls, state: State, goal: Goal, domain: GroundedDomain, useSCCs=False):
        arpg: ARPG = ARPG(domain, state, goal, avoidRaising=True)
        order = arpg.getActionsOrder(useSCCs)
        return order and Pattern.fromOrder(order)

    def addPostfix(self, postfix: int or str):
        order = []
        for item in self.__order[:-1]:
            a = copy.deepcopy(item)
            a.name = f"{a.name}_{postfix}"
            order.append(a)
        order.append(self.dummyAction)
        self.__order = order

    @classmethod
    def fromPlan(cls, plan: NumericPlan) -> Pattern:
        names: Dict[str, int] = dict()
        order = []
        for item in plan.unrolledPlan:
            a = copy.deepcopy(item)
            names[a.name] = names.setdefault(a.name, 0) + 1
            a.name = f"{a.name}_{names[a.name]}"
            order.append(a)

        return Pattern.fromOrder(order)
