from typing import Dict, Set, List

from src.pddl.Action import Action
from src.pddl.Atom import Atom
from src.pddl.Operation import Operation
from src.plan.Pattern import Pattern

from src.smt.SMTExpression import SMTExpression
from src.smt.SMTNumericVariable import SMTRealVariable, SMTIntVariable
from src.smt.SMTVariable import SMTVariable


class TransitionVariables:

    def __init__(self, allAtoms: Set[Atom], assList: Dict[Atom, Set[Operation]], pattern: Pattern, index: int):
        self.allAtoms: Set[Atom] = allAtoms
        self.assList: Dict[Atom, Set[Operation]] = assList
        self.pattern: Pattern = pattern
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

        for action in self.pattern:
            if action.isFake:
                continue
            variables[action] = SMTIntVariable(f"{action.name}_{index}_n")

        return variables

    def __computeBoolActionVariables(self, index: int) -> Dict[Action, SMTVariable]:
        variables: Dict[Action, SMTVariable] = dict()

        for action in self.pattern:
            if action.isFake:
                continue
            # They should be Integer, but in pattern to avoid always casting them with ToReal we relax them to float,
            # since they are constrained in the encoding
            variables[action] = SMTRealVariable(f"{action.name}_{index}_b")

        return variables

    def __computeDeltaVariables(self, index: int) -> Dict[Action, Dict[Atom, SMTVariable]]:
        variables: Dict[Action, Dict[Atom, SMTVariable]] = dict()

        for action in self.pattern:
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

        for a in self.pattern:
            if not a.hasNonSimpleLinearIncrement():
                continue
            for eff in a.effects:
                if not eff.isLinearIncrement():
                    continue
                var = eff.getAtom()
                variables.setdefault(a, dict())
                variables[a][var] = SMTRealVariable(f"{var}_{a}_{index}")

        return variables
