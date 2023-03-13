from typing import Dict, Tuple

from Action import Action
from Atom import Atom
from Domain import GroundedDomain
from Problem import Problem
from classes.smt.SMTNumericVariable import SMTNumericVariable
from classes.smt.SMTVariable import SMTVariable


class TransitionVariables:

    def __init__(self, domain: GroundedDomain, problem: Problem, index: int):
        self.domain = domain
        self.problem = problem
        self.valueVariables: Dict[Atom, SMTVariable] = self.getValueVariables(index)
        self.actionVariables: Dict[Action, SMTVariable] = self.getActionVariables(index)
        self.deltaVariables: Dict[Action, Dict[Atom, SMTVariable]] = self.getDeltaVariables(index)
        self.auxVariables: Dict[Action, Dict[Atom, SMTVariable]] = dict()

    def getValueVariables(self, index: int) -> Dict[Atom, SMTVariable]:
        variables: Dict[Atom, SMTVariable] = dict()

        for assignment in self.problem.init:
            variables[assignment.getAtom()] = SMTNumericVariable(f"{assignment.getAtom()}_{index}")

        return variables

    def getActionVariables(self, index: int) -> Dict[Action, SMTVariable]:
        variables: Dict[Action, SMTVariable] = dict()

        for action in self.domain.actions:
            variables[action] = SMTNumericVariable(f"{action.name}_{index}")

        return variables

    def getDeltaVariables(self, index: int) -> Dict[Action, Dict[Atom, SMTVariable]]:
        variables: Dict[Action, Dict[Atom, SMTVariable]] = dict()

        for action in self.domain.actions:
            variables[action] = dict()
            for assignment in self.problem.init:
                atom = assignment.getAtom()
                variables[action][atom] = SMTNumericVariable(f"delta_{{{action}}}({atom})_{index}")

        return variables
