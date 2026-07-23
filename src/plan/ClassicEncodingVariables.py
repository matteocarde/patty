from typing import Dict, Set, List

from src.pddl.Action import Action
from src.pddl.Atom import Atom
from src.pddl.Domain import GroundedDomain
from src.pddl.Operation import Operation
from src.plan.Pattern import Pattern
from src.smt.SMTBoolVariable import SMTBoolVariable

from src.smt.SMTExpression import SMTExpression
from src.smt.SMTNumericVariable import SMTRealVariable, SMTIntVariable
from src.smt.SMTVariable import SMTVariable


class ClassicEncodingVariables:

    def __init__(self, domain: GroundedDomain, pattern: Pattern):

        self.atoms: Set[Atom] = domain.predicates
        self.domain = domain
        self.pattern: Pattern = pattern
        self.action: Dict[int, SMTVariable] = self.__computeActionVariables()
        self.currentState: Dict[Atom, SMTVariable] = self.__computeValueVariables()
        self.sigma: Dict[int, Dict[Atom, SMTExpression]] = self.__computeSigmaVariables()

    def __computeValueVariables(self) -> Dict[Atom, SMTVariable]:
        variables: Dict[Atom, SMTVariable] = dict()

        for atom in self.atoms:
            variables[atom] = SMTBoolVariable(f"{atom}")

        return variables

    def __computeActionVariables(self) -> Dict[int, SMTVariable]:
        variables: Dict[int, SMTVariable] = dict()

        for i, action in self.pattern.enumerate():
            variables[i] = SMTBoolVariable(f"{action.name}")

        return variables

    def __computeSigmaVariables(self) -> Dict[int, Dict[Atom, SMTVariable]]:
        sigma: Dict[int, Dict[Atom, SMTVariable]] = dict()
        state = self.currentState
        avar = self.action

        sigma[0] = dict()

        for v in self.domain.allAtoms:
            sigma[0][v] = state[v]

        for i, action in self.pattern.enumerate():

            sigma[i] = dict()

            # Case a) Not influenced
            notInfluenced = self.domain.allAtoms - (action.getInfluencedAtoms())
            for v in notInfluenced:
                sigma[i][v] = sigma[i - 1][v]

            # Case b) Boolean
            for v in action.getAddList() | action.getDelList():

                if v in action.getAddList():
                    sigma[i][v] = sigma[i - 1][v] | avar[i]

                if v in action.getDelList():
                    sigma[i][v] = sigma[i - 1][v] & ~avar[i]

        return sigma
