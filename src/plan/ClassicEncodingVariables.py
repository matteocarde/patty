from typing import Dict, Set, List

from src.pddl.Action import Action
from src.pddl.Atom import Atom
from src.pddl.Domain import GroundedDomain
from src.plan.Pattern import Pattern
from src.sat.CNFVariable import CNFActionVariable
from src.sat.CNFVariable import CNFVariable
from src.smt.SMTExpression import SMTExpression
from src.smt.SMTVariable import SMTVariable
from src.utils.TimeStat import TimeStat


class ClassicEncodingVariables:
    action: Dict[Action, CNFActionVariable]
    currentState: Dict[Atom, SMTVariable]
    sigma: Dict[int, Dict[Atom, SMTExpression]]
    addSequence: Dict[Atom, List[List[CNFActionVariable]]]
    deleteSequence: Dict[Atom, List[List[CNFActionVariable]]]
    __PI2I: Dict[Atom, Dict[int, int]]

    def __init__(self, domain: GroundedDomain, pattern: Pattern):

        self.atoms: Set[Atom] = domain.predicates
        self.domain = domain
        self.pattern: Pattern = pattern
        self.__actionToIndexPattern: Dict[Action, int] = dict([(a, i) for (i, a) in self.pattern.enumerate()])
        self.action: Dict[Action, CNFActionVariable] = self.__computeActionVariables()
        self.currentState: Dict[Atom, CNFVariable] = self.__computeValueVariables()
        # self.sigma: Dict[int, Dict[Atom, SMTExpression]] = self.__computeSigmaVariables()

        t = TimeStat.startHolder("Computing Add-Delete Sequences")
        self.__computeAddDeleteSequences()
        t.endHolderMilliseconds(group="ADD-DELETE-SEQUENCE")

    def __computeValueVariables(self) -> Dict[Atom, CNFVariable]:
        variables: Dict[Atom, CNFVariable] = dict()

        for atom in self.atoms:
            variables[atom] = CNFVariable(f"{atom}")

        return variables

    def __computeActionVariables(self) -> Dict[Action, CNFActionVariable]:
        variables: Dict[Action, CNFActionVariable] = dict()

        for i, action in self.pattern.enumerate():
            variables[action] = CNFActionVariable(f"{action.name}", action)

        return variables

    def __computeAddDeleteSequences(self):

        m: Dict[Atom, int] = dict()

        currentSign: Dict[Atom, str] = {v: "+" for v in self.domain.predicates}
        lastAdd: Dict[Atom, List[CNFActionVariable]] = {v: list() for v in self.domain.predicates}
        lastDelete: Dict[Atom, List[CNFActionVariable]] = {v: list() for v in self.domain.predicates}
        addSequence: Dict[Atom, List[List[CNFActionVariable]]] = {v: [] for v in self.domain.predicates}
        deleteSequence: Dict[Atom, List[List[CNFActionVariable]]] = {v: [] for v in self.domain.predicates}
        PI2SI: Dict[Atom, Dict[int, int]] = {v: {} for v in self.domain.predicates}
        cnfPosVars: Dict[Atom, Dict[int, CNFVariable]] = {v: {} for v in self.domain.predicates}
        cnfNegVars: Dict[Atom, Dict[int, CNFVariable]] = {v: {} for v in self.domain.predicates}

        for i, a in self.pattern.enumerate():
            action = self.action[a]
            for eff in a.effects:
                v = eff.atom
                cs = currentSign[v]
                if cs == "-" and eff.sign == "+":
                    PI2SI[v][i] = len(deleteSequence[v]) + 1
                if eff.sign == "+":
                    lastAdd[v].append(action)
                    if cs != eff.sign:
                        deleteSequence[v].append(lastDelete[v])
                        lastDelete[v] = list()
                else:
                    lastDelete[v].append(action)
                    if cs != eff.sign:
                        addSequence[v].append(lastAdd[v])
                        lastAdd[v] = list()
                currentSign[v] = eff.sign

        for v in self.domain.predicates:
            PI2SI[v][len(self.pattern)] = len(deleteSequence[v]) + 1
            if lastAdd[v] or not lastDelete[v]:
                addSequence[v].append(lastAdd[v])
            deleteSequence[v].append(lastDelete[v])
            assert len(addSequence[v]) == len(deleteSequence[v])
            m[v] = len(addSequence[v])
            for i in range(-1, len(addSequence[v])):
                cnfPosVars[v][i] = CNFVariable(f"cnfpos({v},{i})")
                cnfNegVars[v][i] = CNFVariable(f"cnfneg({v},{i})")

        self.addSequence = addSequence
        self.deleteSequence = deleteSequence
        self.__PI2SI = PI2SI
        self.cnfPosVars = cnfPosVars
        self.cnfNegVars = cnfNegVars
        self.m = m

    def getPI2SI(self, v, i):
        for (pi, si) in self.__PI2SI[v].items():
            if i <= pi:
                return si

    def getBoolActionsBeforeIndex(self, boolActions: List[CNFActionVariable], i: int) -> List[CNFActionVariable]:
        left = 0
        right = len(boolActions)
        while left < right:
            middle = (left + right) // 2
            actionIndex = self.__actionToIndexPattern[boolActions[middle].action]
            if actionIndex < i:
                left = middle + 1
            else:
                right = middle

        return boolActions[:left]
