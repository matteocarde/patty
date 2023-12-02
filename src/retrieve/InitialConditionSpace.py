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


class InitialConditionSpace:

    def __init__(self, trace: Trace, problem: Problem, domain: GroundedDomain):
        self.trace = trace
        self.problem = problem
        self.domain = domain
        self.Xis: Dict[int, Dict[Atom, Expr]] = dict()

        for log in self.trace:
            log.squash()

        self.m = len(trace)
        for i in range(0, self.m + 1):
            Xi: Dict[Atom, Expr] = dict()
            self.Xis[i] = Xi
            for atom in self.domain.allAtoms:
                name = str(atom).replace(' ', '\_')
                var = symbols(f"{name}_{{{i}}}")
                Xi[atom] = var

        self.updateXis()
        self.conditions = self.getGoalConditions(self.problem.goal) + self.getTraceConditions(self.trace)

        pass

    def updateXis(self):
        for i, log in enumerate(self.trace):
            self.getPropXis(log.squashed, self.Xis[i])
            self.getEffXis(log.squashed, self.Xis[i], self.Xis[i + 1])

        self.getGoalXis(self.problem.goal, self.Xis[self.m])

        for i, log in reversed(list(enumerate(self.trace))):
            self.getFrameXis(log.squashed, self.Xis[i], self.Xis[i + 1])

    def getGoalConditions(self, goal: Goal) -> List[Expr]:
        conditions = []
        if goal.type == "OR":
            raise Exception("Cannot expressify OR formula")
        for c in goal.conditions:
            if isinstance(c, BinaryPredicate):
                expr = c.expressify(self.Xis[self.m])
                if isinstance(expr, Expr):
                    conditions.append(expr)

        return conditions

    def getTraceConditions(self, trace: Trace) -> List[Expr]:
        conditions: [Expr] = []

        log: Log
        for i, log in enumerate(trace):
            conditions += self.getPreConditions(log.squashed, self.Xis[i])

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

    @staticmethod
    def getPropXis(h: Operation, Xi: Dict[Atom, Expr]) -> [Expr]:

        atomsInPre = set()
        for pre in h.preconditions:
            if isinstance(pre, Literal):
                atom = pre.getAtom()
                Xi[atom] = S(1) if pre.sign == "+" else S(-1)
                atomsInPre.add(pre.getAtom())

        for eff in h.effects:
            if isinstance(eff, Literal) and eff.getAtom() not in atomsInPre:
                atom = eff.getAtom()
                Xi[atom] = S(0)

    @staticmethod
    def getGoalXis(goal: Goal, Xi: Dict[Atom, Expr]):
        if goal.type == "OR":
            raise Exception("Cannot expressify OR formula")
        for c in goal.conditions:
            if isinstance(c, Literal):
                atom = c.getAtom()
                Xi[atom] = S(+1) if c.sign == "+" else S(-1)

    @staticmethod
    def getEffXis(h: Operation, Xi: Dict[Atom, Expr], XiPrime: Dict[Atom, Expr]) -> [Expr]:

        for eff in h.effects:
            if isinstance(eff, BinaryPredicate):
                atom = eff.lhs.getAtom()
                rhs = eff.rhs.expressify(Xi)
                c = None
                if eff.operator == "increase":
                    XiPrime[atom] = Xi[atom] + rhs
                if eff.operator == "decrease":
                    XiPrime[atom] = Xi[atom] - rhs
                if eff.operator == "assign":
                    XiPrime[atom] = rhs  # Eq(lhsPrime, rhs)

    def getFrameXis(self, h: Operation, Xi: Dict[Atom, Expr], XiPrime: Dict[Atom, Expr]) -> [Expr]:
        untouched = self.domain.allAtoms - h.influencedAtoms
        for atom in untouched:
            if isinstance(Xi[atom], Expr):
                Xi[atom] = XiPrime[atom]
