import copy
from typing import Dict, List, Set

from pyeda.boolalg.bdd import bddvar, BDDVariable

from src.pddl.Action import Action
from src.pddl.Atom import Atom
from src.pddl.ConditionalEffect import ConditionalEffect
from src.pddl.Constraints import Constraints
from src.pddl.Domain import Domain, GroundedDomain
from src.pddl.Formula import Formula
from src.pddl.Literal import Literal
from src.smt.SMTBoolVariable import SMTBoolVariable
from src.smt.SMTConjunction import SMTConjunction
from src.smt.SMTExpression import SMTExpression
from src.smt.SMTVariable import SMTVariable
from src.smt.expressions.TrueExpression import TrueExpression


class ActionStateTransitionFunction:
    action: Action
    m: int
    atoms: Set[Atom]
    current: Dict[Atom, SMTBoolVariable]
    next: Dict[Atom, SMTBoolVariable]
    countingCurrent: List[SMTBoolVariable]
    countingNext: List[SMTBoolVariable]

    def __init__(self, action: Action, domain: GroundedDomain):
        self.m = len(action.effects)
        self.action = action
        self.domain = domain
        self.atoms = self.domain.predicates
        self.current = dict([(v, SMTBoolVariable(f"{v}")) for v in self.atoms])
        self.next = dict([(v, SMTBoolVariable(f"{v}'")) for v in self.atoms])

        self.clauses: SMTConjunction = SMTConjunction()

        self.clausesByName = dict()
        self.clausesByName["pre"] = self.getPreconditionClauses(self.action, self.current, self.next)
        self.clausesByName["eff"] = self.getEffectClauses(self.action, self.current, self.next)
        self.clausesByName["conflict"] = self.getConflictClauses(self.action, self.current, self.next)
        for name, clauses in self.clausesByName.items():
            self.clauses += clauses

        self.constraints: SMTExpression = SMTExpression.fromFormula(domain.constraints, self.current)
        print(self.constraints)
        pass

    @staticmethod
    def getPreconditionClauses(a: Action, X: Dict[Atom, SMTVariable], X_: Dict[Atom, SMTVariable]) -> List[
        SMTExpression]:
        preFormula = SMTExpression.fromFormula(a.preconditions, X)
        clauses = [preFormula]
        atLeastOneCe = []
        for ce in a.effects:
            if isinstance(ce, ConditionalEffect):
                atLeastOneCe.append(SMTExpression.fromFormula(ce.conditions, X))
            else:
                atLeastOneCe.append(TrueExpression())
        clauses.append(SMTExpression.bigor(atLeastOneCe))

        return clauses

    @staticmethod
    def getEffectClauses(a: Action, X: Dict[Atom, SMTVariable], X_: Dict[Atom, SMTVariable]) -> List[SMTExpression]:
        one = []
        for v in a.predicates:
            vNext = X_[v]
            vCurrent = X[v]
            andExpr = [vCurrent]
            for e in a.deltaMinus[v]:
                andExpr.append(~SMTExpression.fromFormula(e.conditions, X))
            orExpr = [SMTExpression.bigand(andExpr)]
            for e in a.deltaPlus[v]:
                orExpr.append(SMTExpression.fromFormula(e.conditions, X))
            one.append(vNext.equal(SMTExpression.bigor(orExpr)))
        zero = []
        for v in a.predicates:
            zero.append(X_[v].equal(X[v]))
        return one

    @staticmethod
    def getConflictClauses(a: Action, X: Dict[Atom, SMTVariable], X_: Dict[Atom, SMTVariable]) -> List[SMTExpression]:
        clauses = []
        for v in a.addedAtoms | a.deletedAtoms:
            cesAdding = []
            cesDeleting = []
            for e1 in a.deltaPlus[v]:
                cesAdding.append(~SMTExpression.fromFormula(e1.conditions, X))
            for e2 in a.deltaMinus[v]:
                cesDeleting.append(~SMTExpression.fromFormula(e2.conditions, X))
            fAdding = SMTExpression.bigand(cesAdding)
            fDeleting = SMTExpression.bigand(cesDeleting)
            clauses.append(fAdding | fDeleting)
        return clauses
