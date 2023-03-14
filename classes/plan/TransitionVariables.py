from typing import Dict, Tuple, Set

from Action import Action
from Atom import Atom
from Domain import GroundedDomain
from Problem import Problem
from classes.plan.ActionOrder import ActionOrder
from classes.smt.SMTNumericVariable import SMTNumericVariable
from classes.smt.SMTVariable import SMTVariable


class TransitionVariables:

    def __init__(self, allAtoms: Set[Atom], order: ActionOrder, index: int):
        self.allAtoms: Set[Atom] = allAtoms
        self.order: ActionOrder = order
        self.valueVariables: Dict[Atom, SMTVariable] = self.__computeValueVariables(index)
        self.actionVariables: Dict[Action, SMTVariable] = self.__computeActionVariables(index)
        self.deltaVariables: Dict[Action, Dict[Atom, SMTVariable]] = self.__computeDeltaVariables(index)
        self.auxVariables: Dict[Action, Dict[Atom, SMTVariable]] = dict()

    def __computeValueVariables(self, index: int) -> Dict[Atom, SMTVariable]:
        variables: Dict[Atom, SMTVariable] = dict()

        for atom in self.allAtoms:
            variables[atom] = SMTNumericVariable(f"{atom}_{index}")

        return variables

    def __computeActionVariables(self, index: int) -> Dict[Action, SMTVariable]:
        variables: Dict[Action, SMTVariable] = dict()

        for action in self.order:
            variables[action] = SMTNumericVariable(f"{action.name}_{index}")

        return variables

    def __computeDeltaVariables(self, index: int) -> Dict[Action, Dict[Atom, SMTVariable]]:
        variables: Dict[Action, Dict[Atom, SMTVariable]] = dict()

        for action in self.order:
            variables[action] = dict()
            for atom in self.allAtoms:
                variables[action][atom] = SMTNumericVariable(f"delta_{{{action}}}({atom})_{index}")

        return variables
