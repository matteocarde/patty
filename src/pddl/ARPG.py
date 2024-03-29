from typing import Set, List, Dict

from src.pddl.Action import Action
from src.pddl.Atom import Atom
from src.pddl.Domain import Domain, GroundedDomain
from src.pddl.PDDLException import PDDLException
from src.pddl.Problem import Problem
from src.pddl.RelaxedIntervalState import RelaxedIntervalState
from src.pddl.Supporter import Supporter


class ARPG:
    supporterLevels: List[Set[Supporter]]
    stateLevels: List[RelaxedIntervalState]

    def __init__(self, actions: List[Action], problem: Problem, domain: GroundedDomain):
        self.supporterLevels = list()
        self.stateLevels = list()
        self.actions: List[Action] = actions

        self.originalOrder = dict([(action, i) for (i, action) in enumerate(self.actions)])

        supporters: Set[Supporter] = set()
        for a in actions:
            supporters |= a.getSupporters()

        state: RelaxedIntervalState = RelaxedIntervalState.fromInitialCondition(problem.init, domain.predicates)
        activeSupporters = {s for s in supporters if s.isSatisfiedBy(state)}

        self.supporterLevels.append(activeSupporters)
        self.stateLevels.append(state)

        fullBooleanGoal = len(problem.goal.getFunctions()) == 0

        isFixpoint = False
        while activeSupporters and not isFixpoint:  # (fullBooleanGoal or not state.satisfies(problem.goal)):
            supporters = supporters - activeSupporters
            newState = state.applySupporters(activeSupporters)
            activeSupporters = {s for s in supporters if s.isSatisfiedBy(newState)}

            self.supporterLevels.append(activeSupporters)
            self.stateLevels.append(newState)

            isFixpoint = state.coincide(newState)
            state = newState

        if not fullBooleanGoal and not state.satisfies(problem.goal):
            raise PDDLException.GoalNotReachable()

    def __getPurelyBoolean(self) -> List[Action]:
        order: List[Action] = list()
        for action in self.actions:
            if not action.getFunctions():
                order.append(action)
        return order

    def getActionsOrder(self) -> List[Action]:
        order: List[Action] = list()
        usedActions: Set[Action] = set(order)
        for supporters in self.supporterLevels:
            partialOrder = set()
            for supporter in supporters:
                if supporter.originatingAction not in usedActions:
                    partialOrder.add(supporter.originatingAction)
                usedActions.add(supporter.originatingAction)
            order += sorted(partialOrder, key=lambda x: self.originalOrder[x])
        leftActions = set(self.actions) - usedActions
        order += sorted(leftActions, key=lambda x: self.originalOrder[x])
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
