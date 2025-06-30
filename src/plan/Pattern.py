from __future__ import annotations

import copy
import random
from typing import List, Dict, Tuple, Set, Type

from src.goalFunctions.GoalFunction import GoalFunction
from src.pddl.ARPG import ARPG
from src.pddl.ARPGJair import ARPGJair
from src.pddl.Action import Operation, Action
from src.pddl.Constant import Constant
from src.pddl.Domain import GroundedDomain
from src.pddl.Formula import Formula
from src.pddl.Goal import Goal
from src.pddl.Plan import Plan
from src.pddl.RelaxedIntervalState import RelaxedIntervalState
from src.pddl.State import State


class Pattern:
    __order: List[Operation]
    dummyAction: Action or None

    def __init__(self):
        self.__order: List[Operation] = list()
        pass

    def __deepcopy__(self, m=None) -> Pattern:
        p = Pattern()
        p.__order = copy.copy(self.__order)
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
        p.dummyAction = None
        p.__order = order

        return p

    def __iter__(self):
        return iter(self.__order)

    def __add__(self, other):
        if not isinstance(other, Pattern):
            raise Exception("Cannot concatenate Pattern with element not of type Pattern")
        catPattern: Pattern = Pattern()
        catPattern.__order = [a for a in self.__order] + [b for b in other.__order]

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

    def multiply(self, times: int, addFake=True) -> Pattern:

        order = []
        for i in range(0, times):
            for item in self.__order:
                a = copy.deepcopy(item)
                a.name = f"{a.name}_{i}" if times > 1 else f"{a.name}"
                order.append(a)

        return Pattern.fromOrder(order)

    @classmethod
    def fromARPG(cls, gDomain: GroundedDomain) -> Pattern:
        order: List[Action] = gDomain.getARPG().getActionsOrder(enhanced=False)
        return Pattern.fromOrder(order)

    @classmethod
    def fromARPGEnhanced(cls, gDomain: GroundedDomain) -> Pattern:
        order: List[Action] = gDomain.getARPG().getActionsOrder(enhanced=True)
        return Pattern.fromOrder(order)

    @classmethod
    def fromRandom(cls, gDomain: GroundedDomain) -> Pattern:
        order = list(gDomain.actions)
        random.shuffle(order)
        return Pattern.fromOrder(order)

    @classmethod
    def fromState(cls, state: State, goal: Goal, domain: GroundedDomain, enhanced=False):
        arpg: ARPG = ARPG(domain, state, goal, avoidRaising=True)
        order = arpg.getActionsOrder(enhanced)
        return order and Pattern.fromOrder(order)

    @classmethod
    def fromStateGreedyGoalFunction(cls, state: State, goal: Goal, domain: GroundedDomain, lvl: int,
                                    GF: Type[GoalFunction], c: float):
        Askip = set()
        arpg: ARPG = Pattern.fromStateGreedy(state, goal, domain, lvl, Askip)
        # foundArpg = None
        # while len(Askip) < len(domain.actions):
        #     arpg = Pattern.fromStateGreedy(state, goal, domain, lvl, Askip)
        #     s0 = RelaxedIntervalState.fromState(state, domain.predicates)
        #     sk = RelaxedIntervalState.applyARPGToState(s0, arpg, conservative=False)
        #     goalFunctionRelaxed = GF.compute(sk, goal, state)
        #     if c - goalFunctionRelaxed > 0:
        #         foundArpg = arpg
        #         break

        # arpg = foundArpg if foundArpg else Pattern.fromStateGreedy(state, goal, domain, 3, set())
        order = arpg.getActionsOrder()
        return order and Pattern.fromOrder(order)

    @classmethod
    def fromStateGreedy(cls, state: State, goal: Goal, domain: GroundedDomain, p: int):
        arpg: ARPGJair = ARPGJair.compute(domain, state, goal)
        i = len(arpg.actionLevels) - 1

        gamma: Formula = goal
        newArpg = ARPGJair()
        # random.seed(20121996)
        while i > 0:
            s: RelaxedIntervalState = arpg.stateLevels[i - 1]
            Ai: List[Action] = arpg.getSortedActionLevel(i, goal)
            # random.shuffle(Ai)
            s_: RelaxedIntervalState = arpg.stateLevels[i]
            unsatGamma = gamma.getConditionsNotSatisfiedByRelaxedState(s)
            satGamma = gamma.getConditionsSatisfiedByRelaxedState(s)
            if not unsatGamma.conditions:
                i -= 1
                continue
            gamma = unsatGamma
            Agamma = set()
            for g in gamma:
                Ag = set()
                for a in Ai:
                    s_a = s.applyAction(a)
                    if s_a != s_ and s_a.satisfies(g):
                        Ag.add(a)
                    if len(Ag) >= p:
                        break
                Agamma |= Ag
            gamma = Formula.join([a.preconditions for a in Agamma] + [satGamma])
            newArpg.actionLevels = [Agamma] + newArpg.actionLevels
            i -= 1

        order = newArpg.getActionsOrder()
        return Pattern.fromOrder(order)

    @staticmethod
    def greedy0(s: RelaxedIntervalState, A: Set[Action], s_: RelaxedIntervalState, gamma: Formula) -> Set[Action]:
        for a in A:
            s_a = s.applyAction(a)
            if s_a != s_ and s_a.satisfiesOne(gamma):
                return {a}
        return set()

    @staticmethod
    def greedy1(s: RelaxedIntervalState, A: Set[Action], s_: RelaxedIntervalState, gamma: Formula) -> Set[Action]:
        Ag = set()
        for g in gamma.conditions:
            for a in A:
                s_a = s.applyAction(a)
                if s_a != s_ and s_a.satisfies(g):
                    Ag.add(a)
                    break
        return Ag

    @staticmethod
    def greedy2(s: RelaxedIntervalState, A: Set[Action], s_: RelaxedIntervalState, gamma: Formula) -> Set[Action]:
        Ag = set()
        for a in A:
            s_a = s.applyAction(a)
            if s_a != s_ and s_a.satisfiesOne(gamma):
                Ag.add(a)
        return Ag

    @classmethod
    def fromConeOfInfluence(cls, state: State, goal: Goal, domain: GroundedDomain):
        arpg: ARPG = ARPG(domain, state, goal, avoidRaising=True)
        order = arpg.getConeOfInfluence(goal)
        return order and Pattern.fromOrder(order)

    def addPostfix(self, postfix: int or str):
        order = []
        for item in self.__order:
            a = copy.deepcopy(item)
            a.name = f"{a.name}_{postfix}"
            order.append(a)
        p = Pattern()
        p.__order = order
        return p

    @classmethod
    def fromPlan(cls, plan: Plan, addFake=False) -> Pattern:
        names: Dict[str, int] = dict()
        order = []
        actionsList = plan.getActionsList()
        for item in actionsList:
            a = copy.deepcopy(item)
            names[a.name] = names.setdefault(a.name, 0) + 1
            a.name = f"{a.name}_{names[a.name]}"
            order.append(a)

        return Pattern.fromOrder(order)

    def index(self, a):
        return self.__order.index(a)

    @classmethod
    def fromAlphabetical(cls, domain: GroundedDomain):
        return cls.fromOrder(sorted(domain.actions))

    def getLength(self):
        return len(self)

    def enumerate(self) -> List[Tuple[int, Action]]:
        return [(i + 1, a) for (i, a) in enumerate(self.__order)]

    @classmethod
    def empty(cls):
        return Pattern.fromOrder([])
