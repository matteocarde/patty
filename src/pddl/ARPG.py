import random
from typing import Set, List, Dict

from src.pddl.Action import Action
from src.pddl.Atom import Atom
from src.pddl.Goal import Goal
from src.pddl.GroundedDomain import GroundedDomain
from src.pddl.PDDLException import PDDLException
from src.pddl.RelaxedIntervalState import RelaxedIntervalState
from src.pddl.State import State
from src.pddl.Supporter import Supporter
from src.plan.AffectedGraph import AffectedGraph

SEED = 0


class ARPG:
    supporterLevels: List[Set[Supporter]]
    stateLevels: List[RelaxedIntervalState]

    def __init__(self, domain: GroundedDomain, state: State, goal: Goal, avoidRaising=False):
        self.goalNotReachable = False
        self.supporterLevels = list()
        self.stateLevels = list()
        self.actions: List[Action] = list(domain.actions)
        self.affectedGraph: AffectedGraph = domain.affectedGraph

        self.originalOrder = dict([(action, i) for (i, action) in enumerate(self.actions)])

        supporters: Set[Supporter] = set()
        for a in self.actions:
            supporters |= a.getSupporters()

        state: RelaxedIntervalState = RelaxedIntervalState.fromState(state, domain.predicates)
        activeSupporters = {s for s in supporters if s.isSatisfiedBy(state)}

        self.supporterLevels.append(activeSupporters)
        self.stateLevels.append(state)

        fullBooleanGoal = len(goal.getFunctions()) == 0

        isFixpoint = False
        while activeSupporters and not isFixpoint:
            supporters = supporters - activeSupporters
            newState = state.applySupporters(activeSupporters)
            activeSupporters = {s for s in supporters if s.isSatisfiedBy(newState)}

            self.supporterLevels.append(activeSupporters)
            self.stateLevels.append(newState)

            isFixpoint = state.coincide(newState)
            state = newState

        if not fullBooleanGoal and not state.satisfies(goal):
            self.goalNotReachable = True
            if not avoidRaising:
                raise PDDLException.GoalNotReachable()

    def __getPurelyBoolean(self) -> List[Action]:
        order: List[Action] = list()
        for action in self.actions:
            if not action.getFunctions():
                order.append(action)
        return order

    def getActionsOrder(self, useSCCs=False) -> List[Action] or bool:

        # if self.goalNotReachable:
        #     return False

        order: List[Action] = list()
        usedActions: Set[Action] = set(order)
        for supporters in self.supporterLevels:
            partialOrder = set()
            for supporter in supporters:
                if supporter.originatingAction not in usedActions:
                    partialOrder.add(supporter.originatingAction)
                usedActions.add(supporter.originatingAction)
            if not useSCCs:
                sortOrder = sorted(partialOrder, key=lambda a: a.name)
                order += sortOrder
            else:
                subGraph = self.affectedGraph.getSubGraph(partialOrder)
                graphOrder = subGraph.getOrderFromGraph()
                order += graphOrder
        leftActions = set(self.actions) - usedActions
        if not useSCCs:
            sortOrder = sorted(leftActions, key=lambda a: a.name)
            order += sortOrder
        else:
            graphOrder = self.affectedGraph.getSubGraph(leftActions).getOrderFromGraph()
            order += graphOrder
        return order

    def getConstantAtoms(self) -> Dict[Atom, float]:
        if len(self.stateLevels) < 2:
            return dict()
        lastLevel: RelaxedIntervalState = self.stateLevels[-1]
        subs: Dict[Atom, float] = dict()
        for (atom, interval) in lastLevel.intervals.items():
            if interval.lb == interval.ub:
                subs[atom] = interval.lb
        return subs

    def __str__(self):
        string = ""
        n = len(self.supporterLevels)
        prevActions = set()
        for layer in range(0, n):
            string += f"S_{layer} = {self.stateLevels[layer]}\n"
            actionLayer = {s.originatingAction for s in self.supporterLevels[layer]} - prevActions
            string += f"A_{layer} = {actionLayer}\n"

        return string
