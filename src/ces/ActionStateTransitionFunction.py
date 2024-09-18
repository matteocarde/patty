import copy
import pyeda
from typing import Dict, List, Set

from pyeda.boolalg.bdd import bddvar, BDDVariable
from pyeda.boolalg.bfarray import bddvars
from pyeda.boolalg.expr import expr

from src.pddl.Action import Action
from src.pddl.Atom import Atom
from src.pddl.ConditionalEffect import ConditionalEffect
from src.pddl.Literal import Literal
from src.smt.SMTBoolVariable import SMTBoolVariable
from src.smt.SMTConjunction import SMTConjunction
from src.smt.SMTExpression import SMTExpression


class ActionStateTransitionFunction:

    def __init__(self, a: Action, current: Dict[Atom, SMTBoolVariable], next: Dict[Atom, SMTBoolVariable]):
        self.action = a.toFullCEAction()
        # TODO: Remember to join together CES with the same cond(e)
        self.m = len(a.effects)
        self.atoms = current.keys()
        self.current = copy.copy(current)
        self.next = copy.copy(next)
        self.countingCurrent = [SMTBoolVariable(f"r_{a.name}_{i}") for i in range(0, self.m)]
        self.countingNext = [SMTBoolVariable(f"r_{a.name}_{i}'") for i in range(0, self.m)]

        self.__computingHelping()

        self.clauses: SMTConjunction = SMTConjunction()

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
                andExpr.append(~SMTExpression.fromFormula(e.conditions, self.current))
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
            bit = [self.countingNext[i].AND(~self.countingCurrent[i])]
            for j in range(0, i):
                bit.append((~self.countingNext[i]).AND(self.countingCurrent[i]))
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
                cesAdding.append(~SMTExpression.fromFormula(e1.conditions, self.current))
            for e2 in self.deltaMinus[v]:
                cesDeleting.append(~SMTExpression.fromFormula(e2.conditions, self.current))
            fAdding = SMTExpression.andOfExpressionsList(cesAdding)
            fDeleting = SMTExpression.andOfExpressionsList(cesDeleting)
            clauses.append(fAdding.OR(fDeleting))
        return clauses

    def toBDD(self):

        varToBddVar: Dict[SMTBoolVariable, BDDVariable] = dict()
        for v in self.atoms:
            varToBddVar[self.current[v]] = bddvar(f"{v.name}")
            varToBddVar[self.next[v]] = bddvar(f"{v.name}'")
        for i in range(0, self.m):
            varToBddVar[self.countingCurrent[i]] = bddvar(f"r_{self.action.name}_{i}")
            varToBddVar[self.countingNext[i]] = bddvar(f"r_{self.action.name}_{i}'")

        expr = self.clauses.toBDDExpression(varToBddVar)
        pass
