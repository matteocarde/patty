from __future__ import annotations
from typing import Dict, Set, List

from pyeda.boolalg.bdd import BDDVariable, bddvar, BinaryDecisionDiagram, _NODES
from pyeda.boolalg.expr import And

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
    currentCounting: List[SMTBoolVariable]
    nextCounting: List[SMTBoolVariable]
    Xs: Dict[int, Dict[SMTBoolVariable, BDDVariable]]
    bdd: BinaryDecisionDiagram

    def __init__(self, t: ActionStateTransitionFunction):
        self.transitionFunction = t
        self.action = self.transitionFunction.action
        self.m = self.transitionFunction.m
        self.atoms = list(self.transitionFunction.atoms)
        self.currentState = self.transitionFunction.current
        self.nextState = self.transitionFunction.next
        self.currentCounting = self.transitionFunction.countingCurrent
        self.nextCounting = self.transitionFunction.countingNext
        self.clauses = self.transitionFunction.clauses

    @classmethod
    def fromActionStateTransitionFunction(cls, t: ActionStateTransitionFunction):
        tfbdd = cls(t)
        tfbdd.setOrderForOneStep()
        tfbdd.Xs = tfbdd.getOneStepXs()
        tfbdd.bdd = tfbdd.clauses.toBDDExpression({**tfbdd.Xs[0], **tfbdd.Xs[1]})
        return tfbdd

    def setOrderForOneStep(self):
        for v in self.atoms:
            bddvar(f"{v.name}")
            bddvar(f"{v.name}'")
        for k in range(0, self.transitionFunction.m):
            bddvar(f"r_{self.action.name}_{k}")
            bddvar(f"r_{self.action.name}_{k}'")

    def getOneStepXs(self) -> Dict[int, Dict[SMTBoolVariable, BDDVariable]]:
        Xs: Dict[int, Dict[SMTBoolVariable, BDDVariable]] = dict()
        Xs[0] = dict()
        Xs[1] = dict()
        for v in self.atoms:
            Xs[0][self.currentState[v]] = bddvar(f"{v.name}")
            Xs[1][self.nextState[v]] = bddvar(f"{v.name}'")
        for k in range(0, self.transitionFunction.m):
            Xs[0][self.currentCounting[k]] = bddvar(f"r_{self.action.name}_{k}")
            Xs[1][self.nextCounting[k]] = bddvar(f"r_{self.action.name}_{k}'")
        return Xs

    def setOrderForTwoStep(self):
        for v in self.atoms:
            for i in [0, 1, 2]:
                bddvar(f"{v.name}_{i}")
        for k in range(0, self.transitionFunction.m):
            for i in [0, 1, 2]:
                bddvar(f"r_{self.action.name}_{k}_{i}")

    def getTwoStepXs(self, a: int, b: int) -> Dict[int, Dict[SMTBoolVariable, BDDVariable]]:
        Xs: Dict[int, Dict[SMTBoolVariable, BDDVariable]] = dict()
        Xs[a] = dict()
        Xs[b] = dict()
        for v in self.atoms:
            Xs[a][self.currentState[v]] = bddvar(f"{v.name}_{a}")
            Xs[b][self.nextState[v]] = bddvar(f"{v.name}_{b}")
        for k in range(0, self.transitionFunction.m):
            Xs[a][self.currentCounting[k]] = bddvar(f"r_{self.action.name}_{k}_{a}")
            Xs[b][self.nextCounting[k]] = bddvar(f"r_{self.action.name}_{k}_{b}")
        return Xs

    def smoothingSet(self, func: BinaryDecisionDiagram, vars: List[BDDVariable], var: BDDVariable or None = None):
        if not var:
            return self.smoothingSet(func, vars[1:], vars[0])
        # if not vars:
        #     return func.restrict({var: 0}) | func.restrict({var: 1})

        sFunc = self.smoothingSet(func, vars[1:], vars[0]) if vars else func
        print(f"Smoothing away {var}")
        return sFunc.restrict({var: 0}) | sFunc.restrict({var: 1})

    def computeTransition(self) -> TransitionFunctionBDD:
        ith = TransitionFunctionBDD(self.transitionFunction)
        ith.Xs = self.Xs

        ith.setOrderForTwoStep()

        Xs1 = ith.getTwoStepXs(0, 1)
        Xs2 = ith.getTwoStepXs(1, 2)

        rep1: Dict[BDDVariable, BDDVariable] = dict()
        rep2: Dict[BDDVariable, BDDVariable] = dict()
        repBack: Dict[BDDVariable, BDDVariable] = dict()
        for (smtVar, bddVar) in self.Xs[0].items():
            rep1[bddVar] = Xs1[0][smtVar]
            rep2[bddVar] = Xs2[1][smtVar]
            repBack[Xs1[0][smtVar]] = bddVar
        for (smtVar, bddVar) in self.Xs[1].items():
            rep1[bddVar] = Xs1[1][smtVar]
            rep2[bddVar] = Xs2[2][smtVar]
            repBack[Xs2[2][smtVar]] = bddVar

        print("Compose")
        bdd1 = self.bdd.compose(rep1)
        bdd2 = self.bdd.compose(rep2)
        print("Equiv")
        equiv = 1
        for atom in self.atoms:
            v = self.currentState[atom]
            v_ = self.nextState[atom]
            equiv = equiv & Iff(Xs2[1][v], Xs2[2][v_])
        for k in range(1, self.m):
            r = self.currentCounting[k]
            r_ = self.nextCounting[k]
            equiv = equiv & Iff(Xs2[1][r], Xs2[2][r_])

        print(equiv.to_dot())
        print("Smoothing")
        print("bdd1", bdd1.to_dot())
        print("bbb2", bdd2.to_dot())
        print("equiv", equiv.to_dot())
        print("bdd1 | equiv", (bdd2 | equiv).to_dot())
        print("bdd1 & (bdd2 | equiv)", (bdd1 & (bdd2 | equiv)).to_dot())
        ith.bdd = self.smoothingSet(bdd1 & (bdd2 | equiv), list(Xs2[1].values())).compose(repBack)

        del bdd1
        del bdd2
        del equiv

        print("Iteration:", ith.bdd.to_dot())

        return ith

    def isEquivalent(self, nextBDD: TransitionFunctionBDD) -> bool:
        return self.bdd.equivalent(nextBDD.bdd)
