from random import randrange
from typing import Tuple, List, Dict

import numpy
import numpy as np
from scipy.optimize import NonlinearConstraint, minimize, LinearConstraint
from sympy import Expr, Symbol, lambdify
from sympy.solvers.solveset import linear_coeffs, linear_eq_to_matrix

from src.pddl.InitialCondition import InitialCondition
from src.pddl.Literal import Literal
from src.retrieve.InitialConditionSpace import InitialConditionSpace

EPSILON = 0.01


class InitialConditionRetriever:

    def __init__(self, ics: InitialConditionSpace):
        self.conditions = ics.conditions
        self.domain = ics.domain
        uniqueVars = set()
        for c in self.conditions:
            uniqueVars |= c.free_symbols
        self.variables = list(uniqueVars)
        self.x = [tuple(self.variables)]
        self.ics = ics

        self.constraints = self.getConstraints()
        pass

    def solve(self) -> InitialCondition:
        x0 = [0 for x in self.variables]
        # bounds = Bounds([0.1 for x in self.variables], [np.inf for x in self.variables])
        f = lambda x: 0

        options = {
            "maxiter": 10000,
            "factorization_method": "SVDFactorization",
            "xtol": 0.01,
            "initial_constr_penalty": 100,
            "verbose": 2
        }
        solution = minimize(f, x0, method='trust-constr', constraints=self.constraints,
                            options=options, tol=1e-3)  # , bounds=bounds)
        if not solution.success:
            raise Exception(f"Minimize couldn't return a solution: {solution.message}")

        res: Dict[Symbol, float] = dict()
        for i, var in enumerate(self.variables):
            res[self.variables[i]] = solution.x[i]

        valid = True
        for c in self.ics.conditions:
            if c.is_Relational:
                cValid = c.subs(res)
            else:
                cValid = c.subs(res).is_constant() and c.subs(res) == 0
            valid = valid and cValid

        # if not valid:
        #     raise Exception("Error: The solution found by SciPy doesn't respect the imposed constraints")

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

        return init

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

        condition = condition.lhs - condition.rhs
        eq = None
        if not condition.is_Relational:
            eq = condition
        else:
            if condition.rel_op in {"<=", "<"}:
                eq = condition.rhs - condition.lhs
                lb = -np.inf
            else:
                eq = condition.lhs - condition.rhs
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
