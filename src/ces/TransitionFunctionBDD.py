from __future__ import annotations

import copy
from typing import Dict, List, Tuple

from pyeda.boolalg.bdd import BDDVariable, bddvar, BinaryDecisionDiagram, bdd2expr
from pyeda.boolalg.expr import OrAndOp

from src.ces.ActionStateTransitionFunction import ActionStateTransitionFunction
from src.pddl.Action import Action
from src.pddl.Atom import Atom
from src.pddl.Domain import GroundedDomain
from src.pddl.Formula import Formula
from src.pddl.State import State
from src.smt.SMTBoolVariable import SMTBoolVariable
from src.smt.SMTExpression import SMTExpression
from src.smt.expressions.FalseExpression import FalseExpression
from src.smt.expressions.TrueExpression import TrueExpression
from src.utils.LogPrint import LogPrint, LogPrintLevel
from src.utils.TimeStat import TimeStat


def Iff(a, b):
    return ~a ^ b


class TransitionFunctionBDD:
    transitionFunction: ActionStateTransitionFunction
    atoms: List[Atom]
    action: Action
    m: int
    currentState: Dict[Atom, SMTBoolVariable]
    nextState: Dict[Atom, SMTBoolVariable]
    currentCounting: List[SMTBoolVariable]
    nextCounting: List[SMTBoolVariable]
    Xs: Dict[int, Dict[SMTBoolVariable, BDDVariable]]
    atomsOrder: List[Atom]
    bdd: BinaryDecisionDiagram
    expr: OrAndOp

    def __init__(self, t: ActionStateTransitionFunction):
        self.transitionFunction = t
        self.action = self.transitionFunction.action
        self.domain = self.transitionFunction.domain
        self.m = self.transitionFunction.m
        self.atoms = list(self.domain.predicates)
        self.staticAtoms = self.domain.predicates - (self.action.addedAtoms | self.action.deletedAtoms)
        self.currentState = self.transitionFunction.current
        self.nextState = self.transitionFunction.next
        self.staticVars = {self.currentState[v] for v in self.staticAtoms} | {self.nextState[v] for v in
                                                                              self.staticAtoms}
        self.clauses = self.transitionFunction.clauses

    @classmethod
    def fromActionStateTransitionFunction(cls, t: ActionStateTransitionFunction, atomsOrder: List[Atom]):
        tfbdd = cls(t)
        tfbdd.atomsOrder = atomsOrder
        tfbdd.Xs = tfbdd.getXs(0, 2)
        bdd = tfbdd.clauses.toBDDExpression({**tfbdd.Xs[0], **tfbdd.Xs[2]})
        tfbdd.bdd = bdd
        tfbdd.expr = bdd2expr(bdd)
        return tfbdd

    def getXs(self, a: int, b: int) -> Dict[int, Dict[SMTBoolVariable, BDDVariable]]:
        Xs: Dict[int, Dict[SMTBoolVariable, BDDVariable]] = dict()
        Xs[a] = dict()
        Xs[b] = dict()
        for v in self.atoms:
            Xs[a][self.currentState[v]] = bddvar(f"{self.action}_{v}_{a}")
            Xs[b][self.nextState[v]] = bddvar(f"{self.action}_{v}_{b}") if v not in self.staticAtoms else bddvar(
                f"{self.action}_{v}_0")
        return Xs

    def getConstraints(self) -> Tuple[BinaryDecisionDiagram, BinaryDecisionDiagram, BinaryDecisionDiagram]:
        X0 = dict()
        X1 = dict()
        X2 = dict()
        for v in self.atoms:
            v0 = bddvar(f"{self.action}_{v}_0")
            X0[self.currentState[v]] = v0
            X1[self.currentState[v]] = bddvar(f"{self.action}_{v}_1") if v not in self.staticAtoms else v0
            X2[self.currentState[v]] = bddvar(f"{self.action}_{v}_2") if v not in self.staticAtoms else v0

        C0 = self.transitionFunction.constraints.toBDDExpression(X0)
        C1 = self.transitionFunction.constraints.toBDDExpression(X1)
        C2 = self.transitionFunction.constraints.toBDDExpression(X2)
        return C0, C1, C2

    def smoothingSet(self, func: BinaryDecisionDiagram, vars: List[BDDVariable],
                     var: BDDVariable or None = None):
        if not var:
            return self.smoothingSet(func, vars[1:], vars[0])

        sFunc = self.smoothingSet(func, vars[1:], vars[0]) if vars else func
        left = sFunc.restrict({var: 0})
        right = sFunc.restrict({var: 1})
        join = left | right
        return join

    def computeTransition(self, reflexive=True, relaxed=True) -> TransitionFunctionBDD:
        ith = TransitionFunctionBDD(self.transitionFunction)
        ith.Xs = self.Xs
        ith.atomsOrder = self.atomsOrder

        Xs1 = ith.getXs(0, 1)
        Xs2 = ith.getXs(1, 2)

        rep1: Dict[BDDVariable, BDDVariable] = dict()
        rep2: Dict[BDDVariable, BDDVariable] = dict()
        for (smtVar, bddVar) in self.Xs[0].items():
            if smtVar not in self.staticVars:
                rep2[bddVar] = Xs2[1][smtVar]
        for (smtVar, bddVar) in self.Xs[2].items():
            if smtVar not in self.staticVars:
                rep1[bddVar] = Xs1[1][smtVar]

        bdd1 = self.bdd.compose(rep1)
        bdd2 = self.bdd.compose(rep2)

        C0, C1, C2 = self.getConstraints() if relaxed else (1, 1, 1)
        toBeSmoothed = bdd1 & C1 & bdd2

        smoothVariables = [Xs2[1][self.currentState[v]] for v in self.atomsOrder if v not in self.staticAtoms]

        smoothed = self.smoothingSet(toBeSmoothed, smoothVariables)

        if reflexive:
            ith.bdd = (C0 & C2) >> (smoothed | self.bdd)
        else:
            ith.bdd = C0 & smoothed & C2
        ith.expr = bdd2expr(ith.bdd)

        return ith

    def isEquivalent(self, nextBDD: TransitionFunctionBDD) -> bool:
        return self.bdd.equivalent(nextBDD.bdd)

    def toSMTExpression(self):

        subs: Dict[str, SMTBoolVariable] = dict()
        for smtvar, bddvar in {**self.Xs[0], **self.Xs[2]}.items():
            subs[bddvar.name] = smtvar

        return SMTExpression.fromBDDExpression(self.expr, subs)

    def toGroundSMTExpression(self,
                              groundAction: Action,
                              domain: GroundedDomain,
                              current: Dict[Atom, SMTExpression],
                              next: Dict[Atom, SMTExpression]):

        if self.expr.is_one():
            return TrueExpression()
        if self.expr.is_zero():
            return FalseExpression()

        liftedAtom2groundAtom: Dict[Atom, Atom] = dict()
        for groundAtom in domain.predicates:
            liftedAtom2groundAtom[groundAtom.lifted] = groundAtom

        liftedVar2sigma: Dict[SMTBoolVariable, SMTExpression] = dict()
        print(self.action, groundAction, groundAction.lifted, liftedAtom2groundAtom)
        for (groundAtom, groundVar) in self.currentState.items():
            liftedVar2sigma[groundVar] = current[liftedAtom2groundAtom[groundAtom.lifted]]
        for (groundAtom, groundVar) in self.nextState.items():
            liftedVar2sigma[groundVar] = next[liftedAtom2groundAtom[groundAtom.lifted]]

        bddVar2sigma: Dict[str, SMTExpression] = dict()
        for smtvar, bddvar in {**self.Xs[2], **self.Xs[0]}.items():
            bddVar2sigma[bddvar.name] = liftedVar2sigma[smtvar]

        groundExpr = SMTExpression.fromBDDExpression(self.expr, bddVar2sigma)
        return groundExpr

    def getRestriction(self, a: Action, s: State, Xs, vars) -> Dict[BDDVariable, bool]:
        restrict = dict()
        for atom in self.atoms:
            # for atom, ass in s.assignments.items():
            if atom not in vars:
                continue
            v0 = Xs[vars[atom]]
            restrict[v0] = bool(s.assignments[atom]) if atom in s.assignments else False
        return restrict

    def reachable(self, a: Action, s0: State, s2: State) -> bool:

        restrict0 = self.getRestriction(a, s0, self.Xs[0], self.currentState)
        restrict2 = self.getRestriction(a, s2, self.Xs[2], self.nextState)
        restrict = {**restrict0, **restrict2}

        assert restrict
        res = self.bdd.restrict(restrict)
        if res.is_one():
            return True
        if res.is_zero():
            return False
        print(a, res.to_dot())
        raise Exception("When computing reachability, there are some variables missing")

    def jumpState(self, a: Action, s0: State) -> State:
        restrict = {**self.getRestriction(a, s0, self.Xs[0], self.currentState)}
        res = self.bdd.restrict(restrict)
        sat = res.satisfy_one()

        s1 = copy.deepcopy(s0)
        for atom in a.predicates:
            if atom not in self.nextState:
                continue
            var = self.Xs[2][self.nextState[atom]]
            s1.setAtom(atom, sat[var] if var in sat else s0.getAtom(atom))
        return s1
