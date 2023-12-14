from typing import Dict, Set, List

from src.pddl.Action import Action
from src.pddl.Atom import Atom
from src.pddl.Operation import Operation
from src.plan.Pattern import Pattern
from src.smt.SMTBoolVariable import SMTBoolVariable

from src.smt.SMTExpression import SMTExpression
from src.smt.SMTNumericVariable import SMTRealVariable, SMTIntVariable
from src.smt.SMTVariable import SMTVariable


class TransitionVariables:

    def __init__(self, predicates: Set[Atom], functions: Set[Atom], assList: Dict[Atom, Set[Operation]],
                 pattern: Pattern, index: int,
                 hasPlaceholders: bool):
        self.functions: Set[Atom] = functions
        self.predicates: Set[Atom] = predicates
        self.assList: Dict[Atom, Set[Operation]] = assList
        self.pattern: Pattern = pattern
        self.valueVariables: Dict[Atom, SMTVariable] = self.__computeValueVariables(index)
        self.deltaVariables: Dict[Action, Dict[Atom, SMTExpression]] = self.__computeDeltaVariables(index,
                                                                                                    hasPlaceholders)
        if index > 0:
            self.actionVariables: Dict[Action, SMTVariable] = self.__computeActionVariables(index)
            # self.boolActionVariables: Dict[Action, SMTVariable] = self.__computeBoolActionVariables(index)
            self.auxVariables: Dict[Action, Dict[Atom, SMTVariable]] = self.__computeAuxVariables(index)

    def __computeValueVariables(self, index: int) -> Dict[Atom, SMTVariable]:
        variables: Dict[Atom, SMTVariable] = dict()

        for atom in self.functions:
            variables[atom] = SMTRealVariable(f"{atom}_{index}")
        for atom in self.predicates:
            variables[atom] = SMTBoolVariable(f"{atom}_{index}")

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

    def __computeDeltaVariables(self, index: int, hasPlaceholders: bool) -> Dict[Action, Dict[Atom, SMTVariable]]:
        variables: Dict[Action, Dict[Atom, SMTVariable]] = dict()

        for action in self.pattern:
            variables[action] = dict()
            if hasPlaceholders:
                for atom in self.functions:
                    variables[action][atom] = SMTRealVariable(f"d_{{{action}}}_{index}({atom})")
                for atom in self.predicates:
                    variables[action][atom] = SMTBoolVariable(f"d_{{{action}}}_{index}({atom})")

        return variables

    def __computeAuxVariables(self, index) -> Dict[Action, Dict[Atom, SMTVariable]]:
        variables: Dict[Action, Dict[Atom, SMTVariable]] = dict()
        # for (var, actions) in self.assList.items():
        #     for a in actions:
        #         variables.setdefault(a, dict())
        #         variables[a][var] = SMTRealVariable(f"{var}_{a}_{index}")

        for a in self.pattern:
            variables.setdefault(a, dict())
            for var in a.assList:
                variables[a][var] = SMTRealVariable(f"{var}_{a}_{index}")
            if not a.hasNonSimpleLinearIncrement():
                continue
            for eff in a.effects:
                if not eff.isLinearIncrement():
                    continue
                var = eff.getAtom()
                variables.setdefault(a, dict())
                variables[a][var] = SMTRealVariable(f"{var}_{a}_{index}")

        return variables
