from typing import Dict, Set, List

from src.pddl.Action import Action
from src.pddl.Atom import Atom
from src.pddl.Operation import Operation
from src.plan.Pattern import Pattern
from src.smt.SMTBoolVariable import SMTBoolVariable

from src.smt.SMTExpression import SMTExpression
from src.smt.SMTNumericVariable import SMTRealVariable, SMTIntVariable
from src.smt.SMTVariable import SMTVariable


class NumericTransitionVariables:

    def __init__(self, predicates: Set[Atom], functions: Set[Atom], assList: Dict[Atom, Set[Operation]],
                 pattern: Pattern, index: int, hasPlaceholders: bool, realActionVariables=False):
        self.functions: Set[Atom] = functions
        self.predicates: Set[Atom] = predicates
        self.assList: Dict[Atom, Set[Operation]] = assList
        self.pattern: Pattern = pattern
        self.realActionVariables = realActionVariables
        self.valueVariables: Dict[Atom, SMTVariable] = self.__computeValueVariables(index)
        self.sigmaVariables: Dict[int, Dict[Atom, SMTExpression]] = self.__computeSigmaVariables(index,
                                                                                                 hasPlaceholders)
        if index > 0:
            self.actionVariables: Dict[int, SMTVariable] = self.__computeActionVariables(index)
            # self.boolActionVariables: Dict[Action, SMTVariable] = self.__computeBoolActionVariables(index)
            self.auxVariables: Dict[int, Dict[Atom, SMTVariable]] = self.__computeAuxVariables(index)

    def __computeValueVariables(self, index: int) -> Dict[Atom, SMTVariable]:
        variables: Dict[Atom, SMTVariable] = dict()

        for atom in self.functions:
            variables[atom] = SMTRealVariable(f"{atom}_{index}")
        for atom in self.predicates:
            variables[atom] = SMTBoolVariable(f"{atom}_{index}")

        return variables

    def __computeActionVariables(self, index: int) -> Dict[int, SMTVariable]:
        variables: Dict[int, SMTVariable] = dict()

        for i, action in self.pattern.enumerate():
            if not self.realActionVariables:
                variables[i] = SMTIntVariable(f"{action.name}_{index}_int")
            else:
                variables[i] = SMTRealVariable(f"{action.name}_{index}_real")

        return variables

    def __computeBoolActionVariables(self, index: int) -> Dict[int, SMTVariable]:
        variables: Dict[int, SMTVariable] = dict()

        for i, action in self.pattern.enumerate():
            # They should be Integer, but in pattern to avoid always casting them with ToReal we relax them to float,
            # since they are constrained in the encoding
            variables[i] = SMTRealVariable(f"{action.name}_{index}_b")

        return variables

    def __computeSigmaVariables(self, index: int, hasPlaceholders: bool) -> Dict[int, Dict[Atom, SMTVariable]]:
        variables: Dict[int, Dict[Atom, SMTVariable]] = dict()

        variables[0] = dict()
        if hasPlaceholders:
            for atom in self.functions:
                variables[0][atom] = SMTRealVariable(f"d_0_{index}({atom})")
            for atom in self.predicates:
                variables[0][atom] = SMTBoolVariable(f"d_0_{index}({atom})")

        for i, action in self.pattern.enumerate():
            variables[i] = dict()
            if hasPlaceholders:
                for atom in self.functions:
                    variables[i][atom] = SMTRealVariable(f"d_{{{action}}}_{index}({atom})")
                for atom in self.predicates:
                    variables[i][atom] = SMTBoolVariable(f"d_{{{action}}}_{index}({atom})")

        return variables

    def __computeAuxVariables(self, index) -> Dict[int, Dict[Atom, SMTVariable]]:
        variables: Dict[int, Dict[Atom, SMTVariable]] = dict()

        for i, a in self.pattern.enumerate():
            variables.setdefault(i, dict())
            for var in a.assList:
                variables[i][var] = SMTRealVariable(f"{var}_{a}_{index}")
            if not a.hasNonSimpleLinearIncrement():
                continue
            for eff in a.effects:
                if not eff.isLinearIncrement():
                    continue
                var = eff.getAtom()
                variables.setdefault(i, dict())
                variables[i][var] = SMTRealVariable(f"{var}_{a}_{index}")

        return variables
