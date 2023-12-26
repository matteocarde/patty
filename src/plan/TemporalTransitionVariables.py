from typing import Dict, Set, List

from src.pddl.Action import Action
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
        self.sigmaVariables: Dict[Action, Dict[Atom, SMTExpression]] = self.__computeSigmaVariables()
        if index > 0:
            self.actionVariables: Dict[Action, SMTVariable] = self.__computeActionVariables(index)
            self.auxVariables: Dict[Action, Dict[Atom, SMTVariable]] = self.__computeAuxVariables(index)
            self.timeVariables: Dict[Action, SMTVariable] = self.__computeTimeVariables(index)
            self.durVariables: Dict[Action, SMTVariable] = self.__computeDurVariables(index)

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

    def __computeTimeVariables(self, index: int) -> Dict[Action, SMTVariable]:
        variables: Dict[Action, SMTVariable] = dict()

        for action in self.pattern:
            if action.isFake:
                continue
            variables[action] = SMTIntVariable(f"time_{action.name}_{index}")

        return variables

    def __computeDurVariables(self, index: int) -> Dict[Action, SMTVariable]:
        variables: Dict[Action, SMTVariable] = dict()

        for action in self.pattern:
            if action.isFake or not isinstance(action, SnapAction) or action.timeType != TimePredicateType.AT_START:
                continue
            variables[action] = SMTIntVariable(f"dur_{action.name}_{index}")

        return variables

    def __computeSigmaVariables(self) -> Dict[Action, Dict[Atom, SMTVariable]]:
        variables: Dict[Action, Dict[Atom, SMTVariable]] = dict([(action, dict()) for action in self.pattern])
        return variables

    def __computeAuxVariables(self, index) -> Dict[Action, Dict[Atom, SMTVariable]]:
        variables: Dict[Action, Dict[Atom, SMTVariable]] = dict()

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
