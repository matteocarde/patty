from __future__ import annotations

import copy
from typing import Dict, Set, List, Tuple

from pyeda.boolalg.bdd import BDDVariable, bddvar, BinaryDecisionDiagram, _NODES, bdd2expr
from pyeda.boolalg.expr import And, Expression

from src.ces.ActionStateTransitionFunction import ActionStateTransitionFunction
from src.pddl.Action import Action
from src.pddl.Atom import Atom
from src.smt.SMTBoolVariable import SMTBoolVariable


def Iff(a, b):
    return ~a ^ b


class TransitionFunctionBDD:
    transitionFunction: ActionStateTransitionFunction
    atoms: List[Atom]
    action: Action
    m: int
    currentState: Dict[Atom, SMTBoolVariable]
    nextState: Dict[Atom, SMTBoolVariable]
    Xs: Dict[SMTBoolVariable, BDDVariable]
    Xs_: Dict[SMTBoolVariable, BDDVariable]
    XsFake: Dict[SMTBoolVariable, BDDVariable]
    currentToFake: Dict[BDDVariable, BDDVariable]
    fakeToCurrent: Dict[BDDVariable, BDDVariable]
    atomsOrder: List[Atom]
    varTransitionSteps: Dict[int, Dict[Atom, BinaryDecisionDiagram]]
    varTransitionFixpoint: Dict[Atom, bool]
    bdd: BinaryDecisionDiagram

    def __init__(self, t: ActionStateTransitionFunction):
        self.transitionFunction = t
        self.action = self.transitionFunction.action
        self.m = self.transitionFunction.m
        self.atoms = list(self.transitionFunction.atoms)
        self.currentState = self.transitionFunction.current
        self.nextState = self.transitionFunction.next
        self.clauses = self.transitionFunction.clauses
        self.varTransitionSteps = dict()
        self.varTransitionFixpoint = dict()
        self.step = 1

    @classmethod
    def fromActionStateTransitionFunction(cls, t: ActionStateTransitionFunction, atomsOrder: List[Atom]):
        tfbdd = cls(t)
        tfbdd.atomsOrder = atomsOrder
        tfbdd.setOrder()
        tfbdd.Xs, tfbdd.Xs_, tfbdd.XsFake = tfbdd.getOneStepXs()
        tfbdd.currentToFake = dict([(tfbdd.Xs[v], tfbdd.XsFake[v]) for v in tfbdd.Xs.keys()])
        tfbdd.fakeToCurrent = dict([(tfbdd.XsFake[v], tfbdd.Xs[v]) for v in tfbdd.Xs.keys()])
        tfbdd.varTransitionSteps[1] = dict()
        for v, cav in t.varTransitions.items():
            bdd = cav.toBDDExpression(tfbdd.Xs)
            tfbdd.varTransitionSteps[1][v] = bdd
            print(f"Step 1 of {v}: {bdd.to_dot()}")
            tfbdd.varTransitionFixpoint[v] = False
        tfbdd.bdd = tfbdd.getInitialBdd()
        return tfbdd

    def getOneStepXs(self) -> Tuple[
        Dict[SMTBoolVariable, BDDVariable], Dict[SMTBoolVariable, BDDVariable], Dict[SMTBoolVariable, BDDVariable]]:
        Xs = dict()
        Xs_ = dict()
        XsFake = dict()
        for v in self.atoms:
            Xs[self.currentState[v]] = bddvar(f"{v.name}")
            XsFake[self.currentState[v]] = bddvar(f"{v.name}_fake")
            Xs_[self.nextState[v]] = bddvar(f"{v.name}'")
        return Xs, Xs_, XsFake

    def setOrder(self):
        for v in self.atomsOrder:
            bddvar(f"{v.name}")
            bddvar(f"{v.name}_fake")
            bddvar(f"{v.name}'")

    def getMapping(self, i) -> Dict[BDDVariable, BinaryDecisionDiagram]:
        mapping = dict()
        for atom, cav_prev in self.varTransitionSteps[i].items():
            v = self.Xs[self.currentState[atom]]
            mapping[v] = cav_prev.compose(self.currentToFake)
        return mapping

    def replace(self, bdd: BinaryDecisionDiagram, i: int) -> BinaryDecisionDiagram:
        return bdd.compose(self.getMapping(i)).compose(self.fakeToCurrent)

    def computeNextVarTransitions(self):
        i = self.step
        self.varTransitionSteps[i] = dict()

        for v, cav_prev in self.varTransitionSteps[i - 1].items():
            if self.varTransitionFixpoint[v]:
                self.varTransitionSteps[i][v] = cav_prev
                continue

            cav_i = cav_prev
            for j in range(1, i):
                cav_i = cav_i | self.replace(cav_prev, j)

            # cav_i = self.replace(cav_prev, i - 1)
            self.varTransitionSteps[i][v] = cav_i
            print(f"Step {i} of {v}: {cav_i.to_dot()}")
            if cav_i is cav_prev:
                print(f"Found fixpoint of {v}")
                self.varTransitionFixpoint[v] = True
        pass

    def getInitialBdd(self):
        andBdd = 1
        for v, cav in self.varTransitionSteps[1].items():
            v_ = self.Xs_[self.nextState[v]]
            andBdd = andBdd & Iff(v_, cav)

        return andBdd

    def getBDDFromTransitions(self, previousBDD: BinaryDecisionDiagram) -> BinaryDecisionDiagram:
        i = self.step

        andBdd = 1
        for v, cav in self.varTransitionSteps[i].items():
            v_ = self.Xs_[self.nextState[v]]
            andBdd = andBdd & Iff(v_, cav)

        return andBdd

    def computeTransition(self) -> TransitionFunctionBDD:
        ith = TransitionFunctionBDD(self.transitionFunction)
        ith.Xs, ith.Xs_ = self.Xs, self.Xs_
        ith.currentToFake, ith.fakeToCurrent = self.currentToFake, self.fakeToCurrent
        ith.step = self.step + 1
        ith.varTransitionSteps = self.varTransitionSteps
        ith.varTransitionFixpoint = self.varTransitionFixpoint
        ith.computeNextVarTransitions()
        ith.bdd = ith.getBDDFromTransitions(copy.copy(self.bdd))

        return ith

    def isEquivalent(self, nextBDD: TransitionFunctionBDD) -> bool:
        return self.bdd.equivalent(nextBDD.bdd)
