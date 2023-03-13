import unittest
from unittest import TestCase

from pysmt.oracles import get_logic
from pysmt.shortcuts import Symbol, is_sat, And, Not, Equals, Implies, Int, Portfolio
from pysmt.solvers.solver import Solver
from pysmt.typing import INT

from classes.SMTExpression import SMTExpression
from classes.SMTBoolVariable import SMTBoolVariable
from classes.SMTNumericVariable import SMTNumericVariable
from classes.SMTSolution import SMTSolution
from classes.SMTSolver import SMTSolver


class TestSMT(TestCase):

    def setUp(self) -> None:
        self.a: SMTBoolVariable = SMTBoolVariable("a")
        self.b: SMTBoolVariable = SMTBoolVariable("b")
        self.x: SMTNumericVariable = SMTNumericVariable("x")
        self.y: SMTNumericVariable = SMTNumericVariable("y")
        pass

    def test_variableShouldBeAnExpression(self):
        self.assertIsInstance(self.a, SMTExpression)

    def test_andShouldBeAnExpression(self):
        self.assertIsInstance(self.a and self.b, SMTExpression)

    def test_orShouldBeAnExpression(self):
        self.assertIsInstance(self.a or self.b, SMTExpression)

    def test_impliesShouldBeAnExpression(self):
        self.assertIsInstance(self.a.implies(self.b), SMTExpression)

    def test_impliedByShouldBeAnExpression(self):
        self.assertIsInstance(self.a.impliedBy(self.b), SMTExpression)

    # def test_equalsBooleanShouldBeAnExpression(self):
    #     self.assertIsInstance(self.a == self.b, SMTExpression)

    def test_equalsNumericShouldBeAnExpression(self):
        self.assertIsInstance(self.x == self.y, SMTExpression)

    def test_equalsConstantShouldBeAnExpression(self):
        self.assertIsInstance(self.x == 23, SMTExpression)

    def test_greaterShouldBeAnExpression(self):
        self.assertIsInstance(self.x > 10, SMTExpression)

    def test_greaterWithFloatShouldBeAnExpression(self):
        self.assertIsInstance(self.x > 10.5, SMTExpression)

    def test_lesserShouldBeAnExpression(self):
        self.assertIsInstance(self.x < 10.5, SMTExpression)

    def test_lesserEqualShouldBeAnExpression(self):
        self.assertIsInstance(self.x <= 10.5, SMTExpression)

    def test_greaterEqualShouldBeAnExpression(self):
        self.assertIsInstance(self.x >= 10.5, SMTExpression)

    def test_sumOfConstantShouldBeAnExpression(self):
        self.assertIsInstance(self.x + 2.5, SMTExpression)

    def test_subtractionOfConstantShouldBeAnExpression(self):
        self.assertIsInstance(self.x - 2.5, SMTExpression)

    def test_multiplicationByConstantShouldBeAnExpression(self):
        self.assertIsInstance(self.x * 2.5, SMTExpression)

    def test_divisionByConstantShouldBeAnExpression(self):
        self.assertIsInstance(self.x / 2.5, SMTExpression)

    def test_sumOfConstantLeftShouldBeAnExpression(self):
        self.assertIsInstance(2.5 + self.x, SMTExpression)

    def test_subtractionOfConstantLeftShouldBeAnExpression(self):
        self.assertIsInstance(2.5 - self.x, SMTExpression)

    def test_multiplicationByConstantLeftShouldBeAnExpression(self):
        self.assertIsInstance(2.5 * self.x, SMTExpression)

    def test_divisionByConstantLeftShouldBeAnExpression(self):
        self.assertIsInstance(2.5 / self.x, SMTExpression)

    def test_sumOfVariableShouldBeAnExpression(self):
        self.assertIsInstance(self.x + self.y, SMTExpression)

    def test_subtractionOfVariableShouldBeAnExpression(self):
        self.assertIsInstance(self.x - self.y, SMTExpression)

    def test_multiplicationByVariableShouldBeAnExpression(self):
        self.assertIsInstance(self.x * self.y, SMTExpression)

    def test_divisionByVariableShouldBeAnExpression(self):
        self.assertIsInstance(self.x / self.y, SMTExpression)

    def test_solver_easy(self):
        solver: SMTSolver = SMTSolver()
        lhs: SMTExpression = self.x > 10
        rhs: SMTExpression = self.y == 5
        solver.addAssertion(lhs.implies(rhs))
        solver.addAssertion(self.x == 20)

        solution: SMTSolution = solver.solve()

        self.assertEqual(solution.getVariable(self.x), 20.0)
        self.assertEqual(solution.getVariable(self.y), 5.0)

    def test_solver_hard(self):
        solver: SMTSolver = SMTSolver()
        lhs: SMTExpression = self.x * 5 > 10
        rhs: SMTExpression = self.y * 2 == 6
        solver.addAssertion(lhs.implies(rhs))
        solver.addAssertion(self.x == 2.0)

        solution: SMTSolution = solver.solve()

        self.assertEqual(solution.getVariable(self.x), 2.0)
        self.assertNotEqual(solution.getVariable(self.y), 3.0)


if __name__ == '__main__':
    unittest.main()
