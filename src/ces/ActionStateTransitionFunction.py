import copy
from typing import Dict, List, Set

from pyeda.boolalg.bdd import bddvar, BDDVariable

from src.pddl.Action import Action
from src.pddl.Atom import Atom
from src.pddl.ConditionalEffect import ConditionalEffect
from src.pddl.Literal import Literal
from src.smt.SMTBoolVariable import SMTBoolVariable
from src.smt.SMTConjunction import SMTConjunction
from src.smt.SMTExpression import SMTExpression


class ActionStateTransitionFunction:
    action: Action
    m: int
    atoms: Set[Atom]
    current: Dict[Atom, SMTBoolVariable]
    next: Dict[Atom, SMTBoolVariable]
    countingCurrent: List[SMTBoolVariable]
    countingNext: List[SMTBoolVariable]

    def __init__(self, action: Action):
        self.m = len(action.effects)
        self.action = action
        self.atoms = self.action.predicates
        self.current = dict([(v, SMTBoolVariable(f"{v}")) for v in self.atoms])
        self.next = dict([(v, SMTBoolVariable(f"{v}'")) for v in self.atoms])

        self.clauses: SMTConjunction = SMTConjunction()

        self.clausesByName = dict()
        self.clausesByName["pre"] = self.getPreconditionClauses()
        self.clausesByName["eff"] = self.getEffectClauses()
        self.clausesByName["conflict"] = self.getConflictClauses()
        for name, clauses in self.clausesByName.items():
            self.clauses += clauses

    def getPreconditionClauses(self) -> List[SMTExpression]:
        preFormula = SMTExpression.fromFormula(self.action.preconditions, self.current)
        clauses = [preFormula]
        atLeastOneCe = []
        for ce in self.action.effects:
            assert isinstance(ce, ConditionalEffect)
            atLeastOneCe.append(SMTExpression.fromFormula(ce.conditions, self.current))
        clauses.append(SMTExpression.orOfExpressionsList(atLeastOneCe))

        return clauses

    def getEffectClauses(self) -> List[SMTExpression]:
        one = []
        for v in self.atoms:
            vNext = self.next[v]
            vCurrent = self.current[v]
            andExpr = [vCurrent]
            for e in self.action.deltaMinus[v]:
                andExpr.append(~SMTExpression.fromFormula(e.conditions, self.current))
            orExpr = [SMTExpression.andOfExpressionsList(andExpr)]
            for e in self.action.deltaPlus[v]:
                orExpr.append(SMTExpression.fromFormula(e.conditions, self.current))
            one.append(SMTExpression.orOfExpressionsList(orExpr).iff(vNext))
        zero = []
        for v in self.atoms:
            vNext = self.next[v]
            vCurrent = self.current[v]
            zero.append(vNext.iff(vCurrent))
        return one

    def getConflictClauses(self) -> List[SMTExpression]:
        clauses = []
        for v in self.action.addedAtoms | self.action.deletedAtoms:
            cesAdding = []
            cesDeleting = []
            for e1 in self.action.deltaPlus[v]:
                cesAdding.append(~SMTExpression.fromFormula(e1.conditions, self.current))
            for e2 in self.action.deltaMinus[v]:
                cesDeleting.append(~SMTExpression.fromFormula(e2.conditions, self.current))
            fAdding = SMTExpression.andOfExpressionsList(cesAdding)
            fDeleting = SMTExpression.andOfExpressionsList(cesDeleting)
            clauses.append(fAdding.OR(fDeleting))
        return clauses
