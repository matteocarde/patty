from typing import Dict, Set, List

from src.pddl.Action import Action
from src.pddl.Atom import Atom
from src.pddl.Domain import GroundedDomain
from src.pddl.Literal import Literal
from src.plan.Pattern import Pattern
from src.smt.SMTBoolActionVariable import SMTBoolActionVariable
from src.smt.SMTBoolVariable import SMTBoolVariable
from src.smt.SMTExpression import SMTExpression
from src.smt.SMTVariable import SMTVariable
from src.utils.TimeStat import TimeStat


class ClassicEncodingVariables:
    action: Dict[Action, SMTBoolActionVariable]
    currentState: Dict[Atom, SMTVariable]
    sigma: Dict[int, Dict[Atom, SMTExpression]]
    addSequence: Dict[Atom, List[Set[SMTBoolActionVariable]]]
    deleteSequence: Dict[Atom, List[Set[SMTBoolActionVariable]]]
    PI2I: Dict[Atom, Dict[int, int]]

    def __init__(self, domain: GroundedDomain, pattern: Pattern):

        self.atoms: Set[Atom] = domain.predicates
        self.domain = domain
        self.pattern: Pattern = pattern
        self.__actionToIndexPattern: Dict[Action, int] = dict([(a, i) for (i, a) in self.pattern.enumerate()])
        self.action: Dict[Action, SMTBoolActionVariable] = self.__computeActionVariables()
        self.currentState: Dict[Atom, SMTBoolVariable] = self.__computeValueVariables()
        # self.sigma: Dict[int, Dict[Atom, SMTExpression]] = self.__computeSigmaVariables()

        t = TimeStat.startHolder("Computing Add-Delete Sequences")
        self.__computeAddDeleteSequences()
        t.endHolderMilliseconds()

    def __computeValueVariables(self) -> Dict[Atom, SMTBoolVariable]:
        variables: Dict[Atom, SMTBoolVariable] = dict()

        for atom in self.atoms:
            variables[atom] = SMTBoolVariable(f"{atom}")

        return variables

    def __computeActionVariables(self) -> Dict[Action, SMTBoolActionVariable]:
        variables: Dict[Action, SMTBoolActionVariable] = dict()

        for i, action in self.pattern.enumerate():
            variables[action] = SMTBoolActionVariable(f"{action.name}", action)

        return variables

    def __computeAddDeleteSequences(self):

        j = 1
        currentSign: Dict[Atom, str] = dict()
        lastAdd: Dict[Atom, Set[SMTBoolActionVariable]] = dict()
        lastDelete: Dict[Atom, Set[SMTBoolActionVariable]] = dict()
        addSequence: Dict[Atom, List[Set[SMTBoolActionVariable]]] = dict()
        deleteSequence: Dict[Atom, List[Set[SMTBoolActionVariable]]] = dict()
        PI2SI: Dict[Atom, Dict[int, int]] = dict()
        cnfPosVars: Dict[Atom, Dict[int, SMTBoolVariable]] = dict()
        cnfNegVars: Dict[Atom, Dict[int, SMTBoolVariable]] = dict()
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

        for i, a in self.pattern.enumerate():
            for eff in a.effects:
                assert isinstance(eff, Literal)
                v = eff.atom
                cs = currentSign[v]
                if eff.sign == "+":
                    lastAdd[v].add(self.action[a])
                    PI2SI[v][i] = len(addSequence)
                    if cs != eff.sign:
                        deleteSequence[v].append(lastDelete[v])
                        lastDelete[v] = set()
                else:
                    lastDelete[v].add(self.action[a])
                    PI2SI[v][i] = len(deleteSequence)
                    if cs != eff.sign:
                        addSequence[v].append(lastAdd[v])
                        lastAdd[v] = set()
                currentSign[v] = eff.sign

        for v in self.domain.predicates:
            if lastAdd[v]:
                addSequence[v].append(lastAdd[v])
            deleteSequence[v].append(lastDelete[v])
            assert len(addSequence[v]) == len(deleteSequence[v])
            m[v] = len(addSequence[v])
            for i in range(-1, len(addSequence[v]) + 1):
                cnfPosVars[v][i] = SMTBoolVariable(f"cnfpos({v},{i})")
                cnfNegVars[v][i] = SMTBoolVariable(f"cnfneg({v},{i})")

        self.addSequence = addSequence
        self.deleteSequence = deleteSequence
        self.PI2SI = PI2SI
        self.cnfPosVars = cnfPosVars
        self.cnfNegVars = cnfNegVars
        self.m = m

    def getBoolActionsBeforeIndex(self, boolActions: Set[SMTBoolActionVariable], i: int) -> Set[SMTBoolActionVariable]:
        return {a for a in boolActions if self.__actionToIndexPattern[a.action] < i}
