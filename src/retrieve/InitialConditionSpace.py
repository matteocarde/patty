from typing import Set, Dict, List

from sympy import Expr, symbols
from sympy.core import symbol

from src.pddl.Atom import Atom
from src.pddl.Domain import GroundedDomain
from src.pddl.Goal import Goal
from src.pddl.Problem import Problem
from src.pddl.Trace import Trace


class InitialConditionSpace:

    def __init__(self, trace: Trace, problem: Problem, domain: GroundedDomain):
        self.trace = trace
        self.problem = problem
        self.domain = domain
        self.Xis: Dict[int, Dict[Atom, Expr]] = dict()
        # self.conditions: List[Expr] = []

        self.m = len(trace)
        for i in range(0, self.m + 1):
            Xi: Dict[Atom, Expr] = dict()
            self.Xis[i] = Xi
            for v in self.domain.allAtoms:
                Xi[v] = symbols(f"{v.name}_{i}")

        self.conditions = self.getGoalConditions(self.problem.goal) + self.getTraceConditions(self.trace)

        pass

    def getGoalConditions(self, goal: Goal) -> List[Expr]:
        return goal.expressify(self.Xis[self.m])

    def getTraceConditions(self, trace: Trace) -> List[Expr]:
        conditions: [Expr] = []
        


        return conditions
