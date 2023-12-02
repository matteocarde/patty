import unittest
from math import cos, atan
from unittest import TestCase

import numpy as np
from scipy.optimize import minimize, NonlinearConstraint
from sympy import symbols, linsolve, solve, solveset, nonlinsolve, solve_rational_inequalities, Eq, reduce_inequalities, \
    lambdify

from src.pddl.Domain import Domain, GroundedDomain
from src.pddl.Problem import Problem
from src.pddl.Trace import Trace
from src.retrieve.InitialConditionSpace import InitialConditionSpace


class TestSolve(TestCase):

    def setUp(self) -> None:
        pass

    def test_solve(self):
        x, y, z = symbols("x y z")
        sys = [x + 5 * y, x + 3 * y - 5]

        sol = solve(sys, {x, y, z})
        self.assertEqual(sol[y], -5 / 2)
        self.assertEqual(sol[x], 25 / 2)

    def test_linsolve(self):
        x, y, z = symbols("x y z")
        sys = [x + 5 * y, x + 3 * y - 5]

        sol = linsolve(sys, [z, y, x])
        self.assertEqual(sol.args[0][0], z)
        self.assertEqual(sol.args[0][1], -5 / 2)
        self.assertEqual(sol.args[0][2], 25 / 2)

    def test_nonlinsolve_eqs(self):
        x, y, z = symbols("x y z")
        sys = [x * y * z + 25]

        sol = nonlinsolve(sys, [z, y, x])
        self.assertEqual(sol.args[0][0], z)
        self.assertEqual(sol.args[0][1], y)
        self.assertEqual(sol.args[0][2], - 25 / (y * z))

    def test_lambdify(self):
        x, y = symbols("x y")

        fN = lambda x: x[0] + x[1]
        a = x + y
        f = lambdify([(x, y)], a, "numpy")

        input = [1, 1]

        self.assertEqual(fN(input), 2)
        self.assertEqual(f(input), 2)

    def test_lin_ineqs(self):
        x, y = symbols("x y")
        vars = [(x, y)]

        f = lambdify(vars, x + y, "numpy")
        a = lambdify(vars, x * y, "numpy")
        b = lambdify(vars, x + y, "numpy")

        const = [NonlinearConstraint(a, 0, 25), NonlinearConstraint(b, 10, 10)]
        x0 = [1, 1]
        res = minimize(f, x0, method='trust-constr', constraints=const)

        self.assertAlmostEqual(res.x[0], 5)
        self.assertAlmostEqual(res.x[1], 5)


if __name__ == '__main__':
    unittest.main()
