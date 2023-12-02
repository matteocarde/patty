from typing import Set, Dict, List

from sympy import Expr, symbols, Eq, solve, solveset, solve_rational_inequalities, latex, S, linsolve, nonlinsolve
from sympy.core import symbol

from src.pddl.Atom import Atom
from src.pddl.BinaryPredicate import BinaryPredicate
from src.pddl.Domain import GroundedDomain
from src.pddl.Goal import Goal
from src.pddl.Literal import Literal
from src.pddl.Operation import Operation
from src.pddl.Problem import Problem
from src.pddl.Trace import Trace, Log
from src.pddl.Utilities import Utilities


class InitialConditionSpace:

    def __init__(self, trace: Trace, problem: Problem, domain: GroundedDomain):
        self.trace = trace
        self.problem = problem
        self.domain = domain
        self.Xis: Dict[int, Dict[Atom, Expr]] = dict()
        self.vars = list()
        # self.conditions: List[Expr] = []

        self.m = len(trace)
        for i in range(0, self.m + 1):
            Xi: Dict[Atom, Expr] = dict()
            self.Xis[i] = Xi
            for v in self.domain.allAtoms:
                name = v.name.replace('_', '\_')
                Xi[v] = symbols(f"{name}_{{{i}}}")
                self.vars.append(Xi[v])

        deltaVar = symbols("delta")
        self.vars.append(deltaVar)
        self.conditions = []
        # self.conditions = [Eq(deltaVar, 1)]
        self.conditions += self.getGoalConditions(self.problem.goal) + self.getTraceConditions(self.trace)

        for c in self.conditions:
            print(latex(c) + r"\\")

        x = nonlinsolve(self.conditions, self.vars)
        pass

    def getGoalConditions(self, goal: Goal) -> List[Expr]:
        conditions = []
        if goal.type == "OR":
            raise Exception("Cannot expressify OR formula")
        for c in goal.conditions:
            if isinstance(c, BinaryPredicate):
                conditions.append(c.expressify(self.Xis[self.m]))
            elif isinstance(c, Literal):
                conditions.append(c.expressifyWithEquation(self.Xis[self.m]))

        return conditions

    def getTraceConditions(self, trace: Trace) -> List[Expr]:
        conditions: [Expr] = []

        log: Log
        for i, log in enumerate(trace):
            h: Operation = log.squash()
            conditions += self.getPropConditions(h, self.Xis[i])
            conditions += self.getPreConditions(h, self.Xis[i])
            conditions += self.getEffConditions(h, self.Xis[i], self.Xis[i + 1])
            conditions += self.getFrameConditions(h, self.Xis[i], self.Xis[i + 1])

        return conditions

    def getPreConditions(self, h: Operation, Xi: Dict[Atom, Expr]) -> [Expr]:
        conditions = []
        for pre in h.preconditions:
            if isinstance(pre, BinaryPredicate):
                conditions.append(pre.expressify(Xi))
        return conditions

    def getPropConditions(self, h: Operation, Xi: Dict[Atom, Expr]) -> [Expr]:
        conditions = []

        atomsInPre = set()
        for pre in h.preconditions:
            if isinstance(pre, Literal):
                conditions.append(pre.expressifyWithEquation(Xi))
                atomsInPre.add(pre.getAtom())

        for eff in h.effects:
            if isinstance(eff, Literal) and eff.getAtom() not in atomsInPre:
                # conditions.append(Eq(eff.expressify(Xi), 0))
                conditions.append(eff.expressify(Xi))

        return conditions

    def getEffConditions(self, h: Operation, Xi: Dict[Atom, Expr], XiPrime: Dict[Atom, Expr]) -> [Expr]:
        conditions = []
        for eff in h.effects:
            if isinstance(eff, BinaryPredicate):
                lhs = eff.lhs.expressify(Xi)
                lhsPrime = eff.lhs.expressify(XiPrime)
                rhs = eff.rhs.expressify(Xi)
                c = None
                if eff.operator == "increase":
                    c = lhsPrime - (lhs + rhs)  # Eq(lhsPrime, lhs + rhs)
                if eff.operator == "decrease":
                    c = lhsPrime - (lhs - rhs)  # Eq(lhsPrime, lhs - rhs)
                if eff.operator == "assign":
                    c = lhsPrime - rhs  # Eq(lhsPrime, rhs)
                assert c is not None
                conditions.append(c)

        return conditions

    def getFrameConditions(self, h: Operation, Xi: Dict[Atom, Expr], XiPrime: Dict[Atom, Expr]) -> [Expr]:
        conditions = []
        untouched = self.domain.allAtoms - h.influencedAtoms
        for atom in untouched:
            # conditions.append(Eq(Xi[atom], XiPrime[atom]))
            conditions.append(Xi[atom] - XiPrime[atom])

        return conditions
