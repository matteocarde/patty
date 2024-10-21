from __future__ import annotations
from typing import Dict, Set, List

from pyeda.boolalg.bdd import BDDVariable, bddvar, BinaryDecisionDiagram, _NODES
from pyeda.boolalg.expr import And

from src.ces.ActionStateTransitionFunction import ActionStateTransitionFunction
from src.pddl.Action import Action
from src.pddl.Atom import Atom
from src.smt.SMTBoolVariable import SMTBoolVariable
from src.utils.LogPrint import LogPrint, LogPrintLevel
from src.utils.TimeStat import TimeStat


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
        tfbdd.setOrderForOneStep()
        tfbdd.Xs = tfbdd.getOneStepXs()
        tfbdd.bdd = tfbdd.clauses.toBDDExpression({**tfbdd.Xs[0], **tfbdd.Xs[1]})
        return tfbdd

    def getOneStepXs(self) -> Dict[int, Dict[SMTBoolVariable, BDDVariable]]:
        Xs: Dict[int, Dict[SMTBoolVariable, BDDVariable]] = dict()
        Xs[0] = dict()
        Xs[1] = dict()
        for v in self.atoms:
            Xs[0][self.currentState[v]] = bddvar(f"{v.name}")
            Xs[1][self.nextState[v]] = bddvar(f"{v.name}'") if v not in self.staticAtoms else bddvar(f"{v.name}")
        return Xs

    def setOrderForOneStep(self):
        for v in self.atomsOrder:
            bddvar(f"{v.name}")
            if v not in self.staticAtoms:
                bddvar(f"{v.name}'")

    def setOrderForTwoStep(self):
        for v in self.atomsOrder:
            if v in self.staticAtoms:
                continue
            bddvar(f"{v.name}_1")
        for v in self.atomsOrder:
            bddvar(f"{v.name}_0")
            bddvar(f"{v.name}_2")

    def getTwoStepXs(self, a: int, b: int) -> Dict[int, Dict[SMTBoolVariable, BDDVariable]]:
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
        left = sFunc.restrict({var: 0})
        right = sFunc.restrict({var: 1})
        join = left | right
        return join

    def computeTransition(self, ) -> TransitionFunctionBDD:
        ith = TransitionFunctionBDD(self.transitionFunction)
        ith.Xs = self.Xs
        ith.atomsOrder = self.atomsOrder

        console: LogPrint = LogPrint(LogPrintLevel.PLAN)
        ts: TimeStat = TimeStat()

        ith.setOrderForTwoStep()

        Xs1 = ith.getTwoStepXs(0, 1)
        Xs2 = ith.getTwoStepXs(1, 2)

        rep1: Dict[BDDVariable, BDDVariable] = dict()
        rep2: Dict[BDDVariable, BDDVariable] = dict()
        repBack: Dict[BDDVariable, BDDVariable] = dict()
        for (smtVar, bddVar) in self.Xs[0].items():
            rep1[bddVar] = Xs1[0][smtVar]
            rep2[bddVar] = Xs2[1][smtVar] if smtVar not in self.staticVars else Xs1[0][smtVar]
            repBack[Xs1[0][smtVar]] = bddVar
        for (smtVar, bddVar) in self.Xs[1].items():
            rep1[bddVar] = Xs1[1][smtVar]
            rep2[bddVar] = Xs2[2][smtVar]
            repBack[Xs2[2][smtVar]] = bddVar

        ts.start("COMPOSE")
        bdd1 = self.bdd.compose(rep1)
        bdd2 = self.bdd.compose(rep2)
        ts.end("COMPOSE", console=console)

        ts.start("TO BE SMOOTHED")
        toBeSmoothed = bdd1 & bdd2
        ts.end("TO BE SMOOTHED", console=console)

        smoothVariables = [Xs2[1][self.currentState[v]] for v in self.atomsOrder if v not in self.staticAtoms]

        ts.start("SMOOTHING")
        smoothed = self.smoothingSet(toBeSmoothed, smoothVariables)
        ts.end("SMOOTHING", console=console)

        ts.start("COMPOSE BACK")
        ith.bdd = smoothed.compose(repBack) | self.bdd
        ts.end("COMPOSE BACK", console=console)

        # exit()

        del bdd1
        del bdd2

        print("Iteration:", ith.bdd.to_dot())

        return ith

    def isEquivalent(self, nextBDD: TransitionFunctionBDD) -> bool:
        return self.bdd.equivalent(nextBDD.bdd)
