import sys
from typing import Dict, List, Set

from sympy import Expr, symbols, S, Symbol, expand

from src.pddl.Atom import Atom
from src.pddl.BinaryPredicate import BinaryPredicate
from src.pddl.Domain import GroundedDomain
from src.pddl.Goal import Goal
from src.pddl.InitialCondition import InitialCondition
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

        sys.setrecursionlimit(max(2 * len(self.trace), 1000))

        self.m = len(trace)

        for log in self.trace:
            log.squash()

        self.vg = VariablesGraph(self.domain, self.trace)

        self.addVariablesGraphConnections()
        self.updateXis()
        self.conditions = self.getGoalConditions(self.problem.goal) | self.getTraceConditions(self.trace)

        pass

    def addVariablesGraphConnections(self):
        for (i, log) in enumerate(self.trace):
            untouched = self.domain.allAtoms - log.squashed.influencedAtoms
            for atom in untouched:
                node = self.vg.getNode(i, atom)
                nodePrime = self.vg.getNode(i + 1, atom)
                node.addConnection(nodePrime)

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
                eAtom = eff.getAtom()
                self.vg.getNode(i, eAtom).setValue(S(0))

    def setEffXis(self, h: Operation, i: int) -> [Expr]:
        for eff in h.effects:
            if isinstance(eff, BinaryPredicate):
                Xi = self.vg.getXi(i)
                atom = eff.lhs.getAtom()
                rhs = eff.rhs.expressify(Xi)
                if rhs.is_Mul:
                    rhs = expand(rhs)
                rhsXi = None
                if eff.operator == "increase":
                    rhsXi = Xi[atom] + rhs
                if eff.operator == "decrease":
                    rhsXi = Xi[atom] - rhs
                if eff.operator == "assign":
                    rhsXi = rhs

                self.vg.getNode(i + 1, atom).setValue(rhsXi)

    def getGoalConditions(self, goal: Goal) -> Set[Expr]:
        conditions = set()
        if goal.containsOrs():
            raise Exception("Cannot expressify OR formula")
        Xi = self.vg.getXi(self.m)

        for c in goal.conditions:
            if isinstance(c, BinaryPredicate):
                expr = c.expressify(Xi)
                if isinstance(expr, Expr):
                    conditions.add(expr)

        return conditions

    def getTraceConditions(self, trace: Trace) -> Set[Expr]:
        conditions: Set[Expr] = set()

        log: Log
        for i, log in enumerate(trace):
            Xi = self.vg.getXi(i)
            XiPrime = self.vg.getXi(i + 1)
            conditions |= self.getPreConditions(log.squashed, Xi)
            conditions |= self.getEffConditions(log.squashed, Xi, XiPrime)

        return conditions

    @staticmethod
    def getPreConditions(h: Operation, Xi: Dict[Atom, Expr]) -> Set[Expr]:
        conditions = set()
        for pre in h.preconditions:
            if isinstance(pre, BinaryPredicate):
                f = pre.expressify(Xi)
                if isinstance(f, Expr):
                    conditions.add(f)
                elif isinstance(f, bool):
                    assert f

        return conditions

    @staticmethod
    def getEffConditions(h: Operation, Xi: Dict[Atom, Expr], XiPrime: Dict[Atom, Expr]) -> Set[Expr]:
        conditions = set()
        for eff in h.effects:
            if isinstance(eff, BinaryPredicate):
                rhs: Expr = eff.rhs.expressify(Xi)
                atom = eff.getAtom()
                if eff.operator == "assign":
                    rhs: Expr = eff.rhs.expressify(Xi)
                    if not rhs.free_symbols:
                        c = XiPrime[atom] - rhs
                        if c.free_symbols:
                            conditions.add(c)
        return conditions

    def checkInitialCondition(self, init: InitialCondition):
        sub: Dict[Symbol, float] = dict()
        for (atom, value) in init.numericAssignments.items():
            sub[self.vg.getNode(0, atom).var] = value

        for c in self.conditions:
            res = c.subs(sub)
            if c.is_Relational and not res:
                print(c, res, c.lhs.subs(sub), c.rel_op, c.rhs.subs(sub))
                return False
            elif not c.is_Relational and res != 0:
                print(c, res)
                return False

        return True
