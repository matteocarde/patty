from __future__ import annotations

from typing import Set, List

from src.pddl.Action import Action
from src.pddl.Atom import Atom
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
    def compute(cls, domain: GroundedDomain, state: State, goal: Goal, conservative=True) -> ARPGJair:
        arpg = cls()
        actionsLeft: Set[Action] = domain.actions
        s: RelaxedIntervalState = RelaxedIntervalState.fromState(state, domain.predicates)
        arpg.stateLevels.append(s)
        arpg.actionLevels.append(set())

        while True:
            actions: Set[Action] = set()
            rhs: Set[Atom] = set()
            for a in sorted(actionsLeft):
                if s.satisfies(a.preconditions) and not a.numEffList & rhs:
                    actions.add(a)
                    rhs |= a.effRhs
            if not actions:
                break
            s = s.applyActions(actions, conservative=conservative)
            actionsLeft = actionsLeft - actions
            arpg.actionLevels.append(actions)
            arpg.stateLevels.append(s)
            if s.satisfies(goal):
                break

        if not s.satisfies(goal):
            arpg.goalNotReachable = True
            # if not avoidRaising:
            #     raise PDDLException.GoalNotReachable()

        return arpg

    def getActionsOrder(self) -> List[Action]:
        order = []
        for actionSet in self.actionLevels:
            order += sorted(actionSet)
        return order
