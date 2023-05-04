from typing import Dict, Tuple, Set, List

from Action import Action
from Atom import Atom
from Domain import GroundedDomain
from Operation import Operation
from Problem import Problem
from classes.plan.ActionOrder import ActionOrder
from classes.smt.SMTExpression import SMTExpression
from classes.smt.SMTNumericVariable import SMTNumericVariable, SMTRealVariable, SMTIntVariable
from classes.smt.SMTVariable import SMTVariable


class TransitionVariables:

    def __init__(self, allAtoms: Set[Atom], assList: Dict[Atom, Set[Operation]], order: List[Action], index: int):
        self.allAtoms: Set[Atom] = allAtoms
        self.assList: Dict[Atom, Set[Operation]] = assList
        self.order: List[Action] = order
        self.valueVariables: Dict[Atom, SMTVariable] = self.__computeValueVariables(index)
        self.deltaVariables: Dict[Action, Dict[Atom, SMTExpression]] = self.__computeDeltaVariables(index)
        if index > 0:
            self.actionVariables: Dict[Action, SMTVariable] = self.__computeActionVariables(index)
            self.boolActionVariables: Dict[Action, SMTVariable] = self.__computeBoolActionVariables(index)
            self.auxVariables: Dict[Action, Dict[Atom, SMTVariable]] = self.__computeAuxVariables(index)

    def __computeValueVariables(self, index: int) -> Dict[Atom, SMTVariable]:
        variables: Dict[Atom, SMTVariable] = dict()

        for atom in self.allAtoms:
            variables[atom] = SMTRealVariable(f"{atom}_{index}")

        return variables

    def __computeActionVariables(self, index: int) -> Dict[Action, SMTVariable]:
        variables: Dict[Action, SMTVariable] = dict()

        for action in self.order:
            if action.isFake:
                continue
            variables[action] = SMTIntVariable(f"{action.name}_{index}_n")

        return variables

    def __computeBoolActionVariables(self, index: int) -> Dict[Action, SMTVariable]:
        variables: Dict[Action, SMTVariable] = dict()

        for action in self.order:
            if action.isFake:
                continue
            # They should be Integer, but in order to avoid always casting them with ToReal we relax them to float,
            # since they are constrained in the encoding
            variables[action] = SMTRealVariable(f"{action.name}_{index}_b")

        return variables

    def __computeDeltaVariables(self, index: int) -> Dict[Action, Dict[Atom, SMTVariable]]:
        variables: Dict[Action, Dict[Atom, SMTVariable]] = dict()

        for action in self.order:
            variables[action] = dict()
            # for atom in self.allAtoms:
            #     variables[action][atom] = SMTRealVariable(f"d_{{{action}}}_{index}({atom})")

        return variables

    def __computeAuxVariables(self, index) -> Dict[Action, Dict[Atom, SMTVariable]]:
        variables: Dict[Action, Dict[Atom, SMTVariable]] = dict()
        for (var, actions) in self.assList.items():
            for a in actions:
                variables.setdefault(a, dict())
                variables[a][var] = SMTRealVariable(f"{var}_{a}_{index}")

        return variables
