from __future__ import annotations

import copy
import time
from typing import Dict, List, Tuple, Set

from pyeda.boolalg.bdd import BDDVariable, BinaryDecisionDiagram, bdd2expr, bddvar
from pyeda.boolalg.expr import OrAndOp

from src.ces.ActionStateTransitionFunction import ActionStateTransitionFunction
from src.pddl.Action import Action
from src.pddl.Atom import Atom
from src.pddl.Domain import GroundedDomain
from src.pddl.FalsePredicate import FalsePredicate
from src.pddl.Formula import Formula
from src.pddl.State import State
from src.pddl.TruePredicate import TruePredicate
from src.smt.SMTBoolVariable import SMTBoolVariable
from src.smt.SMTExpression import SMTExpression
from src.smt.expressions.FalseExpression import FalseExpression
from src.smt.expressions.TrueExpression import TrueExpression


def Iff(a, b):
    return ~a ^ b


class TransitionFunctionBDD:
    transitionFunction: ActionStateTransitionFunction
    atoms: List[Atom]
    staticAtoms: Set[Atom]
    staticVars: Set[BDDVariable]
    action: Action
    m: int
    currentState: Dict[Atom, SMTBoolVariable]
    nextState: Dict[Atom, SMTBoolVariable]
    Xs: Dict[int, Dict[SMTBoolVariable, BDDVariable]]
    atomsOrder: List[Atom]
    bdd: BinaryDecisionDiagram
    expr: OrAndOp
    atom2var: Dict[Atom, Dict[int, BDDVariable]]
    var2atom: Dict[str, Atom]
    constraints: Formula
    expr: SMTExpression
    smt2bdd: Dict[SMTBoolVariable, BDDVariable]
    bdd2smt: Dict[str, SMTBoolVariable]
    C0: BinaryDecisionDiagram
    C1: BinaryDecisionDiagram
    C2: BinaryDecisionDiagram
    CLHS: BinaryDecisionDiagram

    def __init__(self):
        pass

    @classmethod
    def fromProperties(cls,
                       t: ActionStateTransitionFunction,
                       atomsOrder: List[Atom],
                       variables: Dict[Atom, Dict[int, BDDVariable]]):
        tf = cls()
        tf.transitionFunction = t
        tf.action = tf.transitionFunction.action
        tf.m = tf.transitionFunction.m
        tf.atoms = list(tf.action.predicates)
        tf.staticAtoms = tf.action.predicates - (tf.action.addedAtoms | tf.action.deletedAtoms)
        tf.currentState = tf.transitionFunction.current
        tf.nextState = tf.transitionFunction.next
        tf.staticVars = {tf.currentState[v] for v in tf.staticAtoms} | {tf.nextState[v] for v in tf.staticAtoms}
        tf.atomsOrder = atomsOrder
        tf.atom2var: Dict[Atom, Dict[int, BDDVariable]] = variables
        tf.constraints = tf.computeConstraints(t.domain.constraints)

        tf.C0, tf.C1, tf.C2 = tf.getConstraints()
        tf.CLHS = tf.C0 & tf.C2

        tf.Xs: Dict[int, Dict[SMTBoolVariable, BDDVariable]] = tf.getXs(0, 2)
        tf.smt2bdd: Dict[SMTBoolVariable, BDDVariable] = dict()
        tf.bdd2smt: Dict[str, SMTBoolVariable] = dict()
        for smt, bdd in tf.Xs[0].items():
            tf.smt2bdd[smt] = bdd
            tf.bdd2smt[bdd.name] = smt
        for smt, bdd in tf.Xs[2].items():
            tf.smt2bdd[smt] = bdd
            tf.bdd2smt[bdd.name] = smt

        return tf

    def __copy__(self):
        tf = TransitionFunctionBDD()
        tf.transitionFunction = self.transitionFunction
        tf.action = self.action
        tf.m = self.m
        tf.atoms = self.atoms
        tf.staticAtoms = self.staticAtoms
        tf.currentState = self.currentState
        tf.nextState = self.nextState
        tf.staticVars = self.staticVars
        tf.atomsOrder = self.atomsOrder
        tf.atom2var = self.atom2var
        tf.smt2bdd = self.smt2bdd
        tf.bdd2smt = self.bdd2smt
        tf.constraints = self.constraints
        tf.Xs = self.Xs
        tf.C0, tf.C1, tf.C2 = self.C0, self.C1, self.C2
        tf.CLHS = self.CLHS
        return tf

    def computeConstraints(self, c: Formula) -> Formula:

        if isinstance(c, TruePredicate) or isinstance(c, FalsePredicate):
            return c

        if not c.conditions:
            return c

        atom2var: Dict[Atom, BDDVariable] = dict()
        var2atom: Dict[str, Atom] = dict()
        for atom in c.getPredicates():
            name = f"c_{self.action}_{atom}"
            atom2var[atom] = bddvar(name)
            var2atom[name] = atom
        nonInAction: List[BDDVariable] = [atom2var[v] for v in c.getPredicates() - self.action.predicates]
        cBDD: BinaryDecisionDiagram = c.toBDD(atom2var)
        cBDDRemoved = cBDD.smoothing(nonInAction)
        return Formula.fromBDD(cBDDRemoved, var2atom)

    @classmethod
    def fromActionStateTransitionFunction(cls,
                                          t: ActionStateTransitionFunction,
                                          atomsOrder: List[Atom],
                                          variables: Dict[Atom, Dict[int, BDDVariable]]):

        tf = TransitionFunctionBDD.fromProperties(t, atomsOrder, variables)
        bdd = tf.CLHS >> t.clauses.toBDDExpression({**tf.Xs[0], **tf.Xs[2]})
        tf.bdd = bdd
        tf.expr = SMTExpression.fromBDDExpression(bdd2expr(tf.bdd), tf.bdd2smt)
        return tf

    def getVarFromAtom(self, v, i):
        return self.atom2var[v][i] if v not in self.staticAtoms else self.atom2var[v][0]

    def getXs(self, a: int, b: int) -> Dict[int, Dict[SMTBoolVariable, BDDVariable]]:
        Xs: Dict[int, Dict[SMTBoolVariable, BDDVariable]] = dict()
        Xs[a] = dict()
        Xs[b] = dict()
        for v in self.atomsOrder:
            Xs[a][self.currentState[v]] = self.getVarFromAtom(v, a)
            Xs[b][self.nextState[v]] = self.getVarFromAtom(v, b)
        return Xs

    def getConstraints(self) -> Tuple[BinaryDecisionDiagram, BinaryDecisionDiagram, BinaryDecisionDiagram]:
        X = dict()
        for i in range(0, 3):
            X[i] = dict()
            for v in self.atoms:
                X[i][v] = self.getVarFromAtom(v, i)

        C0 = self.constraints.toBDD(X[0])
        C1 = self.constraints.toBDD(X[1])
        C2 = self.constraints.toBDD(X[2])
        return C0, C1, C2

    def computeTransition(self, reflexive=True, relaxed=True) -> TransitionFunctionBDD:
        ith = copy.copy(self)

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

        CLHS = self.CLHS if relaxed else 1
        C1 = self.C1 if relaxed else 1
        toBeSmoothed: BinaryDecisionDiagram = bdd1 & C1 & bdd2

        smoothVariables = [Xs2[1][self.currentState[v]] for v in reversed(self.atomsOrder) if v not in self.staticAtoms]

        smoothed = toBeSmoothed.smoothing(smoothVariables)

        if reflexive:
            ith.bdd = CLHS >> (smoothed | self.bdd)
        else:
            ith.bdd = CLHS & smoothed

        ith.expr = SMTExpression.fromBDDExpression(bdd2expr(ith.bdd), ith.bdd2smt)

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

        if self.bdd.is_one():
            return TrueExpression()
        if self.bdd.is_zero():
            return FalseExpression()

        groundAtom2StateVariable: Dict[SMTBoolVariable, SMTExpression] = dict()
        for (groundAtom, groundVar) in self.currentState.items():
            groundAtom2StateVariable[groundVar] = current[groundAtom]
        for (groundAtom, groundVar) in self.nextState.items():
            groundAtom2StateVariable[groundVar] = next[groundAtom]

        bddVar2StateVariable: Dict[str, SMTExpression] = dict()
        for smtvar, bddvar in {**self.Xs[2], **self.Xs[0]}.items():
            bddVar2StateVariable[bddvar.name] = groundAtom2StateVariable[smtvar]

        groundExpr = SMTExpression.fromBDDExpression(bdd2expr(self.bdd), bddVar2StateVariable)
        return groundExpr

    def getRestriction(self, a: Action, s: State, Xs, vars) -> Dict[BDDVariable, bool]:
        restrict = dict()
        for atom in a.getPredicates():
            # for atom, ass in s.assignments.items():
            if atom not in vars or vars[atom] not in Xs:
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
