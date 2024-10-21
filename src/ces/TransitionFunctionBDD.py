from __future__ import annotations

from typing import Dict, List

from pyeda.boolalg.bdd import BDDVariable, bddvar, BinaryDecisionDiagram

from src.ces.ActionStateTransitionFunction import ActionStateTransitionFunction
from src.pddl.Action import Action
from src.pddl.Atom import Atom
from src.smt.SMTBoolVariable import SMTBoolVariable
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

    def __init__(self, t: ActionStateTransitionFunction):
        self.transitionFunction = t
        self.action = self.transitionFunction.action
        self.m = self.transitionFunction.m
        self.atoms = list(self.transitionFunction.atoms)
        self.staticAtoms = self.transitionFunction.atoms - (
                self.transitionFunction.addedAtoms | self.transitionFunction.deletedAtoms)
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
        return tfbdd

    def getXs(self, a: int, b: int) -> Dict[int, Dict[SMTBoolVariable, BDDVariable]]:
        Xs: Dict[int, Dict[SMTBoolVariable, BDDVariable]] = dict()
        Xs[a] = dict()
        Xs[b] = dict()
        for v in self.atoms:
            Xs[a][self.currentState[v]] = bddvar(f"{v.name}_{a}")
            Xs[b][self.nextState[v]] = bddvar(f"{v.name}_{b}") if v not in self.staticAtoms else bddvar(f"{v.name}_0")
        return Xs

    def smoothingSet(self, func: BinaryDecisionDiagram, vars: List[BDDVariable],
                     var: BDDVariable or None = None):
        if not var:
            return self.smoothingSet(func, vars[1:], vars[0])

        console: LogPrint = LogPrint(LogPrintLevel.PLAN)
        ts: TimeStat = TimeStat()
        sFunc = self.smoothingSet(func, vars[1:], vars[0]) if vars else func
        ts.start(f"SMOOTHING {var}")
        left = sFunc.restrict({var: 0})
        right = sFunc.restrict({var: 1})
        join = left | right
        ts.end(f"SMOOTHING {var}", console=console)
        return join

    def computeTransition(self, reflexive=True) -> TransitionFunctionBDD:
        ith = TransitionFunctionBDD(self.transitionFunction)
        ith.Xs = self.Xs
        ith.atomsOrder = self.atomsOrder

        console: LogPrint = LogPrint(LogPrintLevel.PLAN)
        ts: TimeStat = TimeStat()

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

        ts.start("COMPOSE")
        bdd1 = self.bdd.compose(rep1)
        bdd2 = self.bdd.compose(rep2)
        print("T(X0,X1)", bdd1.to_dot())
        print("T(X1,X2)", bdd2.to_dot())
        ts.end("COMPOSE", console=console)

        ts.start("TO BE SMOOTHED")
        toBeSmoothed = bdd1 & bdd2
        print("toBeSmoothed:", toBeSmoothed.to_dot())
        ts.end("TO BE SMOOTHED", console=console)

        smoothVariables = [Xs2[1][self.currentState[v]] for v in self.atomsOrder if v not in self.staticAtoms]

        ts.start("SMOOTHING")
        smoothed = self.smoothingSet(toBeSmoothed, smoothVariables)
        ts.end("SMOOTHING", console=console)

        ts.start("JOIN PREVIOUS")
        if reflexive:
            ith.bdd = smoothed | self.bdd
        else:
            ith.bdd = smoothed
        ts.end("JOIN PREVIOUS", console=console)

        # exit()
        print("Iteration:", ith.bdd.to_dot())

        return ith

    def isEquivalent(self, nextBDD: TransitionFunctionBDD) -> bool:
        return self.bdd.equivalent(nextBDD.bdd)
