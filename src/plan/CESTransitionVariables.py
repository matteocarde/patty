from typing import Dict, Tuple

from src.pddl.Atom import Atom
from src.pddl.Domain import GroundedDomain
from src.plan.Pattern import Pattern
from src.plan.TransitionRelations import TransitionRelations
from src.smt.SMTBoolVariable import SMTBoolVariable
from src.smt.SMTExpression import SMTExpression
from src.smt.SMTVariable import SMTVariable


class CESTransitionVariables:
    currentState: Dict[Atom, SMTVariable]
    nextState: Dict[Atom, SMTVariable]
    sigma: Dict[int, Dict[Atom, SMTExpression]]
    actionVariables: Dict[int, SMTExpression]
    auxVariables: Dict[int, Dict[Atom, SMTExpression]]

    def __init__(self, gDomain: GroundedDomain, pattern: Pattern, transitions: TransitionRelations):
        self.domain = gDomain
        self.pattern = pattern
        self.transition = transitions
        self.predicates = self.domain.predicates

        self.currentState, self.nextState = self.__getValueVariables()
        self.actionVariables = self.__getActionVariables()
        self.auxVariables = self.__getAuxVariables()
        self.sigma = self.__getSigmaVariables()
        pass

    def __getValueVariables(self) -> Tuple[Dict[Atom, SMTVariable], Dict[Atom, SMTVariable]]:
        current: Dict[Atom, SMTVariable] = dict()
        next: Dict[Atom, SMTVariable] = dict()
        for v in self.predicates:
            current[v] = SMTBoolVariable(f"{v}_0")
            next[v] = SMTBoolVariable(f"{v}_1")

        return current, next

    def __getActionVariables(self) -> Dict[int, SMTVariable]:
        actionVariables: Dict[int, SMTVariable] = dict()
        for i, a in self.pattern.enumerate():
            actionVariables[i] = SMTBoolVariable(f"{a.name}")
        return actionVariables

    def __getAuxVariables(self) -> Dict[int, Dict[Atom, SMTVariable]]:
        auxVariables: Dict[int, Dict[Atom, SMTVariable]] = dict()
        for i, a in self.pattern.enumerate():
            if a.isIdempotent():
                continue
            auxVariables[i] = dict()
            for v in a.addedAtoms | a.deletedAtoms:
                auxVariables[i][v] = SMTBoolVariable(f"{v}_{a}")
        return auxVariables

    def __getSigmaVariables(self) -> Dict[int, Dict[Atom, SMTExpression]]:
        sigmas: Dict[int, Dict[Atom, SMTExpression]] = dict()
        sigmas[0] = dict()
        for v in self.predicates:
            sigmas[0][v] = self.currentState[v]

        for i, a in self.pattern.enumerate():
            isIdempotent = a.isIdempotent()
            a_i = self.actionVariables[i]
            sigmas[i] = dict()
            for v in self.predicates:
                if v not in a.addedAtoms | a.deletedAtoms:
                    sigmas[i][v] = sigmas[i - 1][v]
                    continue
                if isIdempotent:
                    andMinus = SMTExpression.bigand(
                        [~SMTExpression.fromFormula(ce.conditions, sigmas[i - 1]) for ce in a.deltaMinus[v]])
                    orPlus = SMTExpression.bigor(
                        [SMTExpression.fromFormula(ce.conditions, sigmas[i - 1]) for ce in a.deltaPlus[v]])
                    sigmas[i][v] = (sigmas[i - 1][v] & (~a_i | andMinus)) | (a_i & orPlus)
                if not isIdempotent:
                    sigmas[i][v] = (a_i & self.auxVariables[i][v]) | (~a_i & sigmas[i - 1][v])

        return sigmas
