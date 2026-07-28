from typing import Dict, Set, List

from src.pddl.Action import Action
from src.pddl.Atom import Atom
from src.pddl.Domain import GroundedDomain
from src.pddl.Literal import Literal
from src.plan.Pattern import Pattern
from src.sat.CNFVariable import CNFActionVariable
from src.sat.CNFVariable import CNFVariable

from src.sat.CNFVariable import CNFActionVariable
from src.smt.SMTExpression import SMTExpression
from src.smt.SMTVariable import SMTVariable
from src.utils.TimeStat import TimeStat


class ClassicEncodingVariables:
    action: Dict[Action, CNFActionVariable]
    currentState: Dict[Atom, SMTVariable]
    sigma: Dict[int, Dict[Atom, SMTExpression]]
    addSequence: Dict[Atom, List[Set[CNFActionVariable]]]
    deleteSequence: Dict[Atom, List[Set[CNFActionVariable]]]
    PI2I: Dict[Atom, Dict[int, int]]

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
        t.endHolderMilliseconds()

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

        currentSign: Dict[Atom, str] = dict()
        lastAdd: Dict[Atom, Set[CNFActionVariable]] = dict()
        lastDelete: Dict[Atom, Set[CNFActionVariable]] = dict()
        addSequence: Dict[Atom, List[Set[CNFActionVariable]]] = dict()
        deleteSequence: Dict[Atom, List[Set[CNFActionVariable]]] = dict()
        PI2SI: Dict[Atom, Dict[int, int]] = dict()
        cnfPosVars: Dict[Atom, Dict[int, CNFVariable]] = dict()
        cnfNegVars: Dict[Atom, Dict[int, CNFVariable]] = dict()
        lastIndex: Dict[Atom, int] = dict()
        m: Dict[Atom, int] = dict()
        for v in self.domain.predicates:
            currentSign[v] = "+"
            lastAdd[v] = set()
            lastDelete[v] = set()
            addSequence[v] = list()
            deleteSequence[v] = list()
            PI2SI[v] = dict()
            cnfPosVars[v] = dict()
            cnfNegVars[v] = dict()
            lastIndex[v] = 0

        for i, a in self.pattern.enumerate():
            for eff in a.effects:
                assert isinstance(eff, Literal)
                v = eff.atom
                cs = currentSign[v]
                nowIndex = len(deleteSequence[v]) + 1
                PI2SI[v].update({index: nowIndex for index in range(lastIndex[v], i + 1)})
                lastIndex[v] = i + 1
                if eff.sign == "+":
                    lastAdd[v].add(self.action[a])
                    if cs != eff.sign:
                        deleteSequence[v].append(lastDelete[v])
                        lastDelete[v] = set()
                else:
                    lastDelete[v].add(self.action[a])
                    if cs != eff.sign:
                        addSequence[v].append(lastAdd[v])
                        lastAdd[v] = set()
                currentSign[v] = eff.sign

        for v in self.domain.predicates:
            PI2SI[v].update({index: len(deleteSequence[v]) + 1 for index in range(lastIndex[v], len(self.pattern) + 1)})
            if lastAdd[v]:
                addSequence[v].append(lastAdd[v])
            deleteSequence[v].append(lastDelete[v])
            assert len(addSequence[v]) == len(deleteSequence[v])
            m[v] = len(addSequence[v])
            for i in range(-1, len(addSequence[v])):
                cnfPosVars[v][i] = CNFVariable(f"cnfpos({v},{i})")
                cnfNegVars[v][i] = CNFVariable(f"cnfneg({v},{i})")

        self.addSequence = addSequence
        self.deleteSequence = deleteSequence
        self.PI2SI = PI2SI
        self.cnfPosVars = cnfPosVars
        self.cnfNegVars = cnfNegVars
        self.m = m

    def getBoolActionsBeforeIndex(self, boolActions: Set[CNFActionVariable], i: int) -> Set[CNFActionVariable]:
        return {a for a in boolActions if self.__actionToIndexPattern[a.action] < i}
