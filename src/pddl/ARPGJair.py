from __future__ import annotations

from typing import Set, List, Tuple

from src.pddl.Action import Action
from src.pddl.Atom import Atom
from src.pddl.BinaryPredicate import BinaryPredicate
from src.pddl.Domain import GroundedDomain
from src.pddl.Goal import Goal
from src.pddl.PDDLException import PDDLException
from src.pddl.RelaxedIntervalState import RelaxedIntervalState
from src.pddl.State import State

SEED = 0


class ARPGJair:
    actionLevels: List[Set[Action]]
    stateLevels: List[RelaxedIntervalState]

    def __init__(self):
        self.goalNotReachable = False
        self.actionLevels = list()
        self.stateLevels = list()

    @classmethod
    def compute(cls, domain: GroundedDomain, state: State, goal: Goal, avoidRaising=True) -> ARPGJair:
        arpg = cls()
        actionsLeft: Set[Action] = domain.actions
        s: RelaxedIntervalState = RelaxedIntervalState.fromState(state, domain.predicates)
        arpg.stateLevels.append(s)
        arpg.actionLevels.append(set())

        while True:
            actions: Set[Action] = set()
            rhs: Set[Atom] = set()
            for a in actionsLeft:
                if s.satisfies(a.preconditions) and not a.numEffList & rhs:
                    actions.add(a)
                    rhs |= a.effRhs
            if not actions:
                break
            s = s.applyActions(actions)
            actionsLeft = actionsLeft - actions
            arpg.actionLevels.append(actions)
            arpg.stateLevels.append(s)
            if s.satisfies(goal):
                break

        if not s.satisfies(goal):
            arpg.goalNotReachable = True
            if not avoidRaising:
                raise PDDLException.GoalNotReachable()

        return arpg

    def getActionsOrder(self) -> List[Action]:
        order = []
        for actionSet in self.actionLevels:
            order += sorted(actionSet)
        return order

    def getSortedActionLevel(self, i: int, goal: Goal):
        state: RelaxedIntervalState = self.stateLevels[i - 1]
        actions: Set[Action] = self.actionLevels[i]

        numericGoals = [g for g in goal.normalize() if isinstance(g, BinaryPredicate)]
        actionWithValues: List[Tuple[float, Action]] = list()

        if not numericGoals:
            return list(actions)

        for a in actions:
            s_ = state.applyAction(a, forceSingleRepetition=True)
            goalValues = [s_.substituteInto(g.lhs).ub for g in numericGoals]
            actionWithValues.append((max(goalValues), a))

        sortedActionLevel = [a for (v, a) in sorted(actionWithValues, reverse=True)]
        return sortedActionLevel
