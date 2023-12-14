import math
import random
from random import randrange
from typing import Tuple, List, Dict, Set

import numpy
import numpy as np
from scipy.optimize import NonlinearConstraint, minimize, LinearConstraint, OptimizeResult
from scipy.optimize import Bounds as OptBounds
from sympy import Expr, Symbol, lambdify, S, simplify
from sympy.solvers.solveset import linear_coeffs, linear_eq_to_matrix

from src.pddl.Atom import Atom
from src.pddl.InitialCondition import InitialCondition
from src.pddl.Literal import Literal
from src.retrieve.Bounds import Bounds
from src.retrieve.InitialConditionSpace import InitialConditionSpace

EPSILON = 0.01


class InitialConditionRetriever:

    def __init__(self, ics: InitialConditionSpace, wIc: InitialCondition, bounds: Bounds or None = None):
        self.conditions = ics.conditions
        self.domain = ics.domain
        self.ics = ics

        self.obj: Expr = S(0)
        for (atom, value) in wIc.numericAssignments.items():
            var = self.ics.vg.getNode(0, atom).value
            self.obj += (var - value) ** 2
        # self.obj = simplify(self.obj)

        uniqueVars: Set[Symbol] = set()
        for c in self.conditions:
            uniqueVars |= c.free_symbols
        uniqueVars |= self.obj.free_symbols

        self.variables: [Symbol] = list(uniqueVars)
        self.x: List[Tuple[Symbol]] = [tuple(self.variables)]

        lb: List[float] = []
        ub: List[float] = []
        self.x0: List[float] = []
        for var in self.variables:
            lbc, ubc = -np.inf, +np.inf
            atom = self.ics.vg.varsToAtom[var]
            if bounds and atom in bounds.interval:
                lbc = bounds.interval[atom][0]
                ubc = bounds.interval[atom][1]

            if atom in wIc.numericAssignments:
                self.x0.append(wIc.numericAssignments[atom])
            else:
                rValue = 0 if lbc == -np.inf or ubc == np.inf else random.uniform(lbc, ubc)
                self.x0.append(rValue)

            lb.append(lbc)
            ub.append(ubc)

        self.bounds = OptBounds(lb, ub)
        self.constraints = self.getConstraints()
        pass

    def solve(self, tol=0.5) -> (InitialCondition, float):

        # self.x0 = np.array([0 for x in self.variables])
        f = lambdify(self.x, self.obj, "numpy")

        options = {
            "maxiter": 10000,
            "factorization_method": "SVDFactorization",
            "gtol": tol,
            "xtol": tol,
            "barrier_tol": 1.1,
            "initial_constr_penalty": 100,
            "verbose": 3
        }

        # noinspection PyTypeChecker
        solution: OptimizeResult = minimize(f, self.x0,
                                            method='trust-constr',
                                            constraints=self.constraints,
                                            bounds=self.bounds,
                                            options=options)

        if not solution.success:
            raise Exception(f"Minimize couldn't return a solution: {solution.message}")

        res: Dict[Symbol, float] = dict()
        for i, var in enumerate(self.variables):
            res[self.variables[i]] = solution.x[i]

        init = InitialCondition()
        for atom in self.domain.predicates:
            node = self.ics.vg.getNode(0, atom)
            value = node.value
            if value.is_constant() and value > 0.5:
                init.addPredicate(Literal.fromAtom(atom, "+"))

        for atom in self.domain.functions:
            node = self.ics.vg.getNode(0, atom)
            value = node.value.subs(res)
            value = value if value.is_constant() else 0
            init.addNumericAssignment(atom, value)

        return init, solution.fun

    def getConstraints(self):
        constraints = []
        linear = []

        c: Expr
        for c in self.conditions:
            eq = self.getEquation(c)
            if self.isLinear(eq):
                if not c.is_Relational:
                    linear.append(eq)
                    linear.append(-eq)
                else:
                    if c.rel_op in {">", "<"}:
                        eq = eq - EPSILON
                    linear.append(eq)
            else:
                constraints.append(InitialConditionRetriever.toNonLinearConstraint(c, self.x))

        if linear:
            A, b = linear_eq_to_matrix(linear, self.variables)
            A = np.array(A).astype(np.float64)
            b = [float(c) for c in b]
            constraints.append(LinearConstraint(A, lb=b, ub=np.inf))

        return constraints

    @staticmethod
    def getEquation(c: Expr):

        if not c.is_Relational:
            return c

        return c.rhs - c.lhs if c.rel_op in {"<=", "<"} else c.lhs - c.rhs

    @staticmethod
    def toNonLinearConstraint(condition: Expr, vars: List[Tuple[Symbol]]):
        lb = 0
        ub = 0

        eq = condition.lhs - condition.rhs
        if condition.is_Relational:
            if condition.rel_op in {"<=", "<"}:
                lb = -np.inf
            else:
                ub = np.inf
            if condition.rel_op in {">", "<"}:
                eq = eq - EPSILON

        f = lambdify(vars, eq, "numpy")

        return NonlinearConstraint(f, lb, ub)

    def isLinear(self, c):
        try:
            linear_coeffs(self.getEquation(c), *self.variables)
            return True
        except:
            return False
