import itertools
from typing import Set, List, Dict

from src.pattern.PatternAction import PatternAction
from src.pddl.Action import Action
from src.pddl.Atom import Atom
from src.pddl.Domain import GroundedDomain
from src.pddl.Goal import Goal
from src.pddl.PDDLException import PDDLException
from src.pddl.RelaxedIntervalState import RelaxedIntervalState
from src.pddl.SnapAction import SnapAction
from src.pddl.State import State
from src.pddl.Supporter import Supporter
from src.pddl.TimePredicate import TimePredicateType

SEED = 0


class ARPG:
    supporterLevels: List[Set[Supporter]]
    stateLevels: List[RelaxedIntervalState]

    def __init__(self, domain: GroundedDomain, state: State, goal: Goal, avoidRaising=False):
        self.goalNotReachable = False
        self.supporterLevels = list()
        self.stateLevels = list()
        self.actions: List[Action] = list(domain.actions)
        # self.affectedGraph: AffectedGraph = domain.affectedGraph

        self.originalOrder = dict([(action, i) for (i, action) in enumerate(self.actions)])

        supporters: Set[Supporter] = set()
        for a in self.actions:
            supporters |= a.getSupporters()

        usedActions = set()
        state: RelaxedIntervalState = RelaxedIntervalState.fromState(state, domain.predicates)
        activeSupporters = {s for s in supporters if s.isSatisfiedBy(state) and s.respectsTemporal(usedActions)}
        usedActions = usedActions | {s.originatingAction for s in activeSupporters}
        self.supporterLevels.append(activeSupporters)
        self.stateLevels.append(state)

        fullBooleanGoal = len(goal.getFunctions()) == 0

        isFixpoint = False
        while activeSupporters or not isFixpoint:
            supporters = supporters - activeSupporters
            newState = state.applySupporters(activeSupporters)
            activeSupporters = {s for s in supporters if
                                s.isSatisfiedBy(newState) and s.respectsTemporal(usedActions)}
            usedActions = usedActions | {s.originatingAction for s in activeSupporters}

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

    def getUsefulActions(self) -> Set[Action]:
        usefulActions: Set[Action] = set()
        for supporters in self.supporterLevels:
            for supporter in supporters:
                usefulActions.add(supporter.originatingAction)
        return usefulActions

    def getActionsOrder(self, enhanced=False) -> List[Action] or bool:

        usedActions: Set[Action] = set()

        layers: List[Set[Action]] = list()

        for supporters in self.supporterLevels:
            partialOrder = set()
            for supporter in supporters:
                if supporter.originatingAction not in usedActions:
                    partialOrder.add(supporter.originatingAction)
                usedActions.add(supporter.originatingAction)
            layers.append(partialOrder)

        leftActions = set(self.actions) - usedActions
        layerInstant = {a for a in leftActions if not isinstance(a, SnapAction)}
        layerSnap = {a for a in leftActions if isinstance(a, SnapAction) and a.timeType != TimePredicateType.OVER_ALL}
        layers.append(layerInstant)
        layers.append(layerSnap)

        order = list()
        for i, layer in enumerate(layers):
            if enhanced:
                sortedLayer = sorted([PatternAction.fromAction(a) for a in layer])
                print(f"----Layer {i}----")
                print("\n".join([str(a) for a in sortedLayer]))
                order += sortedLayer
            else:
                order += sorted(layer)

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
