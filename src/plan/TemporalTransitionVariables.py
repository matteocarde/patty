from typing import Dict, Set

from src.pddl.Atom import Atom
from src.pddl.Operation import Operation
from src.pddl.SnapAction import SnapAction
from src.pddl.TimePredicate import TimePredicateType
from src.plan.Pattern import Pattern
from src.smt.SMTBoolVariable import SMTBoolVariable
from src.smt.SMTExpression import SMTExpression
from src.smt.SMTNumericVariable import SMTRealVariable, SMTIntVariable
from src.smt.SMTVariable import SMTVariable


class TemporalTransitionVariables:

    def __init__(self, predicates: Set[Atom], functions: Set[Atom], assList: Dict[Atom, Set[Operation]],
                 pattern: Pattern, index: int):
        self.functions: Set[Atom] = functions
        self.predicates: Set[Atom] = predicates
        self.assList: Dict[Atom, Set[Operation]] = assList
        self.pattern: Pattern = pattern
        self.valueVariables: Dict[Atom, SMTVariable] = self.__computeValueVariables(index)
        self.sigmaVariables: Dict[int, Dict[Atom, SMTExpression]] = self.__computeSigmaVariables()
        if index > 0:
            self.actionVariables: Dict[int, SMTVariable] = self.__computeActionVariables(index)
            self.auxVariables: Dict[int, Dict[Atom, SMTVariable]] = self.__computeAuxVariables(index)
            self.timeVariables: Dict[int, SMTVariable] = self.__computeTimeVariables(index)
            self.durVariables: Dict[int, SMTVariable] = self.__computeDurVariables(index)

    def __computeValueVariables(self, index: int) -> Dict[Atom, SMTVariable]:
        variables: Dict[Atom, SMTVariable] = dict()

        for atom in self.functions:
            variables[atom] = SMTRealVariable(f"{atom}_{index}")
        for atom in self.predicates:
            variables[atom] = SMTBoolVariable(f"{atom}_{index}")

        return variables

    def __computeActionVariables(self, index: int) -> Dict[int, SMTVariable]:
        variables: Dict[int, SMTVariable] = dict()

        for i, action in enumerate(self.pattern):
            variables[i] = SMTIntVariable(f"{action.name}")

        return variables

    def __computeTimeVariables(self, index: int) -> Dict[int, SMTVariable]:
        variables: Dict[int, SMTVariable] = dict()

        for i, action in enumerate(self.pattern):
            variables[i] = SMTRealVariable(f"time_{action.name}")

        return variables

    def __computeDurVariables(self, index: int) -> Dict[int, SMTVariable]:
        variables: Dict[int, SMTVariable] = dict()

        for i, action in enumerate(self.pattern):
            if not isinstance(action, SnapAction) or action.timeType != TimePredicateType.AT_START:
                continue
            variables[i] = SMTRealVariable(f"dur_{action.name}")

        return variables

    def __computeSigmaVariables(self) -> Dict[int, Dict[Atom, SMTVariable]]:
        variables: Dict[int, Dict[Atom, SMTVariable]] = dict([(i, dict()) for i, action in enumerate(self.pattern)])
        variables[-1] = dict()
        return variables

    def __computeAuxVariables(self, index) -> Dict[int, Dict[Atom, SMTVariable]]:
        variables: Dict[int, Dict[Atom, SMTVariable]] = dict()

        for i, a in enumerate(self.pattern):
            variables.setdefault(i, dict())
            for var in a.assList:
                variables[i][var] = SMTRealVariable(f"{var}_{a}")
            if not a.hasNonSimpleLinearIncrement():
                continue
            for eff in a.effects:
                if not eff.isLinearIncrement():
                    continue
                var = eff.getAtom()
                variables.setdefault(i, dict())
                variables[i][var] = SMTRealVariable(f"{var}_{a}")

        return variables
