from typing import Dict, List

from sympy import Expr, symbols, S

from src.pddl.Atom import Atom
from src.pddl.BinaryPredicate import BinaryPredicate
from src.pddl.Domain import GroundedDomain
from src.pddl.Goal import Goal
from src.pddl.Literal import Literal
from src.pddl.Operation import Operation
from src.pddl.Problem import Problem
from src.pddl.Trace import Trace, Log
from src.retrieve.VariablesGraph import VariablesGraph


class InitialConditionSpace:

    def __init__(self, trace: Trace, problem: Problem, domain: GroundedDomain):
        self.trace = trace
        self.problem = problem
        self.domain = domain

        self.m = len(trace)

        for log in self.trace:
            log.squash()

        self.vg = VariablesGraph(self.domain, self.trace)

        self.addVariablesGraphConnections()
        self.updateXis()
        self.conditions = self.getGoalConditions(self.problem.goal) + self.getTraceConditions(self.trace)

        pass

    def addVariablesGraphConnections(self):
        subs: Dict[Expr, Expr] = dict()
        for (i, log) in enumerate(self.trace):
            untouched = self.domain.allAtoms - log.squashed.influencedAtoms
            for atom in untouched:
                node = self.vg.getNode(i, atom)
                nodePrime = self.vg.getNode(i + 1, atom)
                node.addConnection(nodePrime)

        return subs

    def updateXis(self):
        self.getGoalXis(self.problem.goal, self.m)
        for i, log in enumerate(self.trace):
            self.setPropXis(log.squashed, i)
            self.setEffXis(log.squashed, i)
        self.vg.fixXi()

    def getGoalXis(self, goal: Goal, m: int):
        if goal.type == "OR":
            raise Exception("Cannot expressify OR formula")
        for c in goal.conditions:
            if isinstance(c, Literal):
                atom = c.getAtom()
                value = S(+1) if c.sign == "+" else S(-1)
                self.vg.getNode(m, atom).setValue(value)

    def setPropXis(self, h: Operation, i: int):

        atomsInPre = set()
        for pre in h.preconditions:
            if isinstance(pre, Literal):
                atom = pre.getAtom()
                value = S(1) if pre.sign == "+" else S(-1)
                self.vg.getNode(i, atom).setValue(value)
                atomsInPre.add(pre.getAtom())

        for eff in h.effects:
            if isinstance(eff, Literal) and eff.getAtom() not in atomsInPre:
                atom = eff.getAtom()
                self.vg.getNode(i, atom).setValue(S(0))

    def setEffXis(self, h: Operation, i: int) -> [Expr]:
        for eff in h.effects:
            if isinstance(eff, BinaryPredicate):
                Xi = self.vg.getXi(i)
                atom = eff.lhs.getAtom()
                rhs = eff.rhs.expressify(Xi)
                rhsXi = None
                if eff.operator == "increase":
                    rhsXi = Xi[atom] + rhs
                if eff.operator == "decrease":
                    rhsXi = Xi[atom] - rhs
                if eff.operator == "assign":
                    rhsXi = rhs  # Eq(lhsPrime, rhs)
                self.vg.getNode(i + 1, atom).setValue(rhsXi)

    def getGoalConditions(self, goal: Goal) -> List[Expr]:
        conditions = []
        if goal.type == "OR":
            raise Exception("Cannot expressify OR formula")
        Xi = self.vg.getXi(self.m)
        for c in goal.conditions:
            if isinstance(c, BinaryPredicate):
                expr = c.expressify(Xi)
                if isinstance(expr, Expr):
                    conditions.append(expr)

        return conditions

    def getTraceConditions(self, trace: Trace) -> List[Expr]:
        conditions: [Expr] = []

        log: Log
        for i, log in enumerate(trace):
            Xi = self.vg.getXi(i)
            conditions += self.getPreConditions(log.squashed, Xi)

        return conditions

    @staticmethod
    def getPreConditions(h: Operation, Xi: Dict[Atom, Expr]) -> [Expr]:
        conditions = []
        for pre in h.preconditions:
            if isinstance(pre, BinaryPredicate):
                f = pre.expressify(Xi)
                if isinstance(f, Expr):
                    conditions.append(f)
                elif isinstance(f, bool):
                    assert f

        return conditions
