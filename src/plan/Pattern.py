from __future__ import annotations

import copy
import random
from typing import List, Dict, Tuple, Set, Type

from src.goalFunctions.GoalFunction import GoalFunction
from src.pddl.ARPG import ARPG
from src.pddl.ARPGJair import ARPGJair
from src.pddl.Action import Operation, Action
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
        arpg = Pattern.fromStateGreedy(state, goal, domain, lvl, Askip)
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
    def fromStateGreedy(cls, state: State, goal: Goal, domain: GroundedDomain, lvl: int, Askip: Set[Action]):
        arpg: ARPGJair = ARPGJair.compute(domain, state, goal)
        i = len(arpg.actionLevels) - 1
        if lvl >= 3:
            return arpg.getActionsOrder()

        gamma: Formula = goal
        newArpg = ARPGJair()
        while i > 0:
            Ag: Set[Action] = set()
            prevState: RelaxedIntervalState = arpg.stateLevels[i - 1]
            Ai: Set[Action] = arpg.actionLevels[i] - Askip
            nextState: RelaxedIntervalState = arpg.stateLevels[i]
            unsatGamma = gamma.getConditionsNotSatisfiedByRelaxedState(prevState)
            if not unsatGamma.conditions:
                i -= 1
                continue
            gamma = unsatGamma
            if lvl == 0:
                Ag = Pattern.greedy0(prevState, Ai, nextState, gamma)
                lvl = 1
            elif lvl == 1:
                Ag = Pattern.greedy1(prevState, Ai, nextState, gamma)
            elif lvl == 2:
                Ag = Pattern.greedy2(prevState, Ai, nextState, gamma)
            gamma = Formula.join([a.preconditions for a in Ag])
            newArpg.actionLevels = [Ag] + newArpg.actionLevels
            i -= 1

        return newArpg
        # order = newArpg.getActionsOrder()
        # return order and Pattern.fromOrder(order)

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
        self.__order = order

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
