from typing import Dict, Tuple, List

from src.pddl.Action import Action
from src.pddl.Atom import Atom
from src.pddl.Domain import GroundedDomain
from src.pddl.Problem import Problem
from src.plan.Pattern import Pattern
from src.plan.TransitionRelations import TransitionRelations
from src.smt.SMTBoolVariable import SMTBoolVariable
from src.smt.SMTExpression import SMTExpression
from src.smt.SMTVariable import SMTVariable


class PASTransitionVariables:
    stateVariables: Dict[int, Dict[Atom, SMTVariable]]
    actionVariables: Dict[int, Dict[Action, SMTVariable]]

    def __init__(self, gDomain: GroundedDomain, problem: Problem, bound: int):
        self.domain = gDomain
        self.problem = problem
        self.predicates = self.domain.predicates | self.problem.predicates
        self.n = bound

        self.stateVariables = self.__getStateVariables()
        self.actionVariables = self.__getActionVariables()
        pass

    def __getStateVariables(self) -> Dict[int, Dict[Atom, SMTVariable]]:
        state: Dict[int, Dict[Atom, SMTVariable]] = dict()
        for i in range(0, self.n + 1):
            stateI: Dict[Atom, SMTVariable] = dict()
            for v in self.predicates:
                stateI[v] = SMTBoolVariable(f"{v}_{i}")
            state[i] = stateI

        return state

    def __getActionVariables(self) -> Dict[int, Dict[Action, SMTVariable]]:
        action: Dict[int, Dict[Action, SMTVariable]] = dict()
        for i in range(1, self.n + 1):
            actionI: Dict[Action, SMTVariable] = dict()
            for a in self.domain.actions:
                actionI[a] = SMTBoolVariable(f"{a.name}_{i}")
            action[i] = actionI
        return action
