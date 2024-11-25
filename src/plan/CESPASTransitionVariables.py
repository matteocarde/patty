from typing import Dict, Tuple, List

from src.pddl.Action import Action
from src.pddl.Atom import Atom
from src.pddl.Domain import GroundedDomain
from src.plan.Pattern import Pattern
from src.plan.TransitionRelations import TransitionRelations
from src.smt.SMTBoolVariable import SMTBoolVariable
from src.smt.SMTExpression import SMTExpression
from src.smt.SMTVariable import SMTVariable


class CESPASTransitionVariables:
    stateVariables: List[Dict[Atom, SMTVariable]]
    actionVariables: List[Dict[Action, SMTVariable]]

    def __init__(self, gDomain: GroundedDomain, bound: int):
        self.domain = gDomain
        self.predicates = self.domain.predicates
        self.n = bound

        self.stateVariables = self.__getStateVariables()
        self.actionVariables = self.__getActionVariables()
        pass

    def __getStateVariables(self) -> List[Dict[Atom, SMTVariable]]:
        state: List[Dict[Atom, SMTVariable]] = list()
        for i in range(0, self.n + 1):
            stateI: Dict[Atom, SMTVariable] = dict()
            for v in self.predicates:
                stateI[v] = SMTBoolVariable(f"{v}_{i}")
            state.append(stateI)

        return state

    def __getActionVariables(self) -> List[Dict[Action, SMTVariable]]:
        action: List[Dict[Action, SMTVariable]] = list()
        for i in range(1, self.n + 1):
            actionI: Dict[Action, SMTVariable] = dict()
            for a in self.domain.actions:
                actionI[a] = SMTBoolVariable(f"{a.name}_{a}")
            action.append(actionI)
        return action
