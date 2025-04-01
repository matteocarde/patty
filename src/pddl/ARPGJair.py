import copy
import itertools
from typing import Set, List, Dict

from src.pattern.PatternActionGraph import PatternActionGraph
from src.pddl.Action import Action
from src.pddl.Atom import Atom
from src.pddl.Domain import GroundedDomain
from src.pddl.Formula import Formula
from src.pddl.Goal import Goal
from src.pddl.PDDLException import PDDLException
from src.pddl.RelaxedIntervalState import RelaxedIntervalState
from src.pddl.SnapAction import SnapAction
from src.pddl.State import State
from src.pddl.Supporter import Supporter
from src.pddl.TimePredicate import TimePredicateType

SEED = 0


class ARPGJair:
    actionLevels: List[Set[Action]]
    stateLevels: List[RelaxedIntervalState]

    def __init__(self, domain: GroundedDomain, state: State, goal: Goal, avoidRaising=False):
        self.goalNotReachable = False
        self.actionLevels = list()
        self.stateLevels = list()
        actionsLeft: Set[Action] = domain.actions
        s: RelaxedIntervalState = RelaxedIntervalState.fromState(state, domain.predicates)

        while True:
            actions: Set[Action] = set()
            rhs: Set[Atom] = set()
            for a in sorted(actionsLeft):
                if s.satisfies(a.preconditions) and not a.numEffList & rhs:
                    actions.add(a)
                    rhs |= a.effRhs
            if not actions:
                break
            s = s.applyActions(actions)
            actionsLeft = actionsLeft - actionsLeft
            self.actionLevels.append(actions)
            self.stateLevels.append(s)

        if not s.satisfies(goal):
            self.goalNotReachable = True
            if not avoidRaising:
                raise PDDLException.GoalNotReachable()

