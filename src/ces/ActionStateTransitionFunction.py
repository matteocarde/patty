import copy
from typing import Dict, List, Set

from src.pddl.Action import Action
from src.pddl.Atom import Atom
from src.pddl.ConditionalEffect import ConditionalEffect
from src.pddl.Literal import Literal
from src.smt.SMTBoolVariable import SMTBoolVariable
from src.smt.SMTExpression import SMTExpression


class ActionStateTransitionFunction:

    def __init__(self, a: Action, current: Dict[Atom, SMTBoolVariable], next: Dict[Atom, SMTExpression]):
        self.action = a.toFullCEAction()
        # TODO: Remember to join together CES with the same cond(e)
        self.m = len(a.effects)
        self.current = copy.copy(current)
        self.next = copy.copy(next)
        self.countingCurrent = [SMTBoolVariable(f"r_{a.name}_{i}") for i in range(0, self.m)]
        self.countingNext = [SMTBoolVariable(f"r_{a.name}_{i}'") for i in range(0, self.m)]

        self.__computingHelping()

        self.clauses: List[SMTExpression] = list()

        self.clauses += self.getPreconditionClauses()
        self.clauses += self.getEffectClauses()
        self.clauses += self.getAmoClauses()
        self.clauses += self.getConflictClauses()

    def __computingHelping(self):
        self.deltaPlus: Dict[Atom, List[ConditionalEffect]] = dict()
        self.deltaMinus: Dict[Atom, List[ConditionalEffect]] = dict()
        self.addedAtoms: Set[Atom] = set()
        self.deletedAtoms: Set[Atom] = set()
        for v in self.current.keys():
            self.deltaPlus.setdefault(v, list())
            self.deltaMinus.setdefault(v, list())

        for ce in self.action.effects:
            assert isinstance(ce, ConditionalEffect)
            for l in ce.effects:
                assert isinstance(l, Literal)
                v = l.getAtom()
                if l.sign == "+":
                    self.addedAtoms.add(v)
                    self.deltaPlus[v].append(ce)
                if l.sign == "-":
                    self.deletedAtoms.add(v)
                    self.deltaMinus[v].append(ce)

    def getPreconditionClauses(self) -> List[SMTExpression]:
        preFormula = SMTExpression.fromFormula(self.action.preconditions, self.current)
        clauses = [preFormula]
        for ce in self.action.effects:
            assert isinstance(ce, ConditionalEffect)
            clauses.append(SMTExpression.fromFormula(ce.conditions, self.current))

        return clauses

    def getEffectClauses(self) -> List[SMTExpression]:
        clauses = []
        for v in self.addedAtoms | self.deletedAtoms:
            vNext = self.next[v]
            vCurrent = self.current[v]
            andExpr = [vCurrent]
            for e in self.deltaMinus[v]:
                andExpr.append(SMTExpression.fromFormula(e.conditions, self.current).NOT())
            orExpr = [SMTExpression.andOfExpressionsList(andExpr)]
            for e in self.deltaPlus[v]:
                orExpr.append(SMTExpression.fromFormula(e.conditions, self.current))
            clauses.append(SMTExpression.orOfExpressionsList(orExpr).iff(vNext))
        return clauses

    def getDiffZero(self) -> SMTExpression:
        bits = []
        for i in range(0, self.m):
            bits.append(self.countingCurrent[i].iff(self.countingNext[i]))
        return SMTExpression.andOfExpressionsList(bits)

    def getDiffOne(self) -> SMTExpression:
        bits = []
        for i in range(0, self.m):
            bit = [self.countingNext[i].AND(self.countingCurrent[i].NOT())]
            for j in range(0, i):
                bit.append(self.countingNext[i].NOT().AND(self.countingCurrent[i]))
            for k in range(i + 1, self.m):
                bit.append(self.countingNext[i].iff(self.countingCurrent[i]))

            bits.append(SMTExpression.andOfExpressionsList(bit))
        return SMTExpression.orOfExpressionsList(bits)

    def getAmoClauses(self):
        return [self.getDiffZero().OR(self.getDiffOne())]

    def getConflictClauses(self) -> List[SMTExpression]:
        clauses = []
        for v in self.addedAtoms | self.deletedAtoms:
            cesAdding = []
            cesDeleting = []
            for e1 in self.deltaPlus[v]:
                cesAdding.append(SMTExpression.fromFormula(e1.conditions, self.current).NOT())
            for e2 in self.deltaMinus[v]:
                cesDeleting.append(SMTExpression.fromFormula(e2.conditions, self.current).NOT())
            fAdding = SMTExpression.andOfExpressionsList(cesAdding)
            fDeleting = SMTExpression.andOfExpressionsList(cesDeleting)
            clauses.append(fAdding.OR(fDeleting))
        return clauses
