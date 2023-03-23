from unittest import TestCase

import unittest
from pysmt.logics import QF_UFLIRA
from pysmt.shortcuts import Real, Symbol, Portfolio, Not, TRUE, FALSE, Implies, get_model, And
from pysmt.typing import REAL, INT, BOOL

from classes.smt.SMTBoolVariable import SMTBoolVariable
from classes.smt.SMTExpression import SMTExpression
from classes.smt.SMTNumericVariable import SMTNumericVariable, SMTRealVariable, SMTIntVariable
from classes.smt.SMTSolution import SMTSolution
from classes.smt.SMTSolver import SMTSolver


class TestSMT(TestCase):

    def setUp(self) -> None:
        self.a: SMTBoolVariable = SMTBoolVariable("a")
        self.b: SMTBoolVariable = SMTBoolVariable("b")
        self.x: SMTNumericVariable = SMTRealVariable("x")
        self.y: SMTNumericVariable = SMTRealVariable("y")
        self.p: SMTNumericVariable = SMTIntVariable("p")
        self.q: SMTNumericVariable = SMTIntVariable("q")
        pass

    def test_variableShouldBeAnExpression(self):
        self.assertIsInstance(self.a, SMTExpression)

    def test_andShouldBeAnExpression(self):
        self.assertIsInstance(self.a.AND(self.b), SMTExpression)
        self.assertEqual(str(self.a.AND(self.b)), "(a & b)")

    def test_orShouldBeAnExpression(self):
        self.assertIsInstance(self.a.OR(self.b), SMTExpression)
        self.assertEqual(str(self.a.OR(self.b)), "(a | b)")

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

    def test_integerSumWithFloatShouldBeAnExpression(self):
        expr = self.p + 10.5
        self.assertIsInstance(expr, SMTExpression)
        self.assertEqual(expr.type, REAL)

    def test_integerSumWithIntegerShouldBeAnExpression(self):
        expr = self.p + 10
        self.assertIsInstance(expr, SMTExpression)
        self.assertEqual(expr.type, INT)

    def test_lesserShouldBeAnExpression(self):
        expr = self.x < 10.5
        self.assertIsInstance(expr, SMTExpression)
        self.assertEqual(expr.type, BOOL)

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

    def test_mixedIntRealExpression(self):
        a = self.p + 10
        b = 4.5 * a
        self.assertIsInstance(a, SMTExpression)
        self.assertIsInstance(b, SMTExpression)
        self.assertEqual(a.type, INT)
        self.assertEqual(b.type, REAL)

    def test_solver_real_easy(self):
        solver: SMTSolver = SMTSolver()
        lhs: SMTExpression = self.x > 10
        rhs: SMTExpression = self.y == 5.5
        solver.addAssertion(lhs.implies(rhs))
        solver.addAssertion(self.x == 20)

        solution: SMTSolution = solver.solve()

        self.assertEqual(solution.getVariable(self.x), Real(20.0))
        self.assertEqual(solution.getVariable(self.y), Real(5.5))

    def test_solver_int_easy(self):
        solver: SMTSolver = SMTSolver()
        lhs: SMTExpression = self.x > 10.1
        rhs: SMTExpression = (self.y > 4.5).AND(self.y < 5.6)
        solver.addAssertion(lhs.implies(rhs))
        solver.addAssertion(self.x == 20)

        solution: SMTSolution = solver.solve()

        self.assertEqual(solution.getVariable(self.x), Real(20))
        self.assertEqual(solution.getVariable(self.y), Real(5))

    def test_solver_real_hard(self):
        solver: SMTSolver = SMTSolver()
        lhs: SMTExpression = self.x * 5 > 10
        rhs: SMTExpression = self.y * 2 == 6.2
        solver.addAssertion(lhs.implies(rhs))
        solver.addAssertion(self.x == 2.0)

        solution: SMTSolution = solver.solve()

        self.assertEqual(solution.getVariable(self.x), Real(2.0))
        self.assertNotEqual(solution.getVariable(self.y), Real(3.1))

    def test_z3(self):
        x, y = Symbol("x1"), Symbol("y1")
        f = Implies(x, y)

        solvers_set = ["z3"]
        with Portfolio(solvers_set,
                       logic=QF_UFLIRA,
                       incremental=True,
                       generate_models=True) as s:
            s.add_assertion(f)
            s.push()
            s.add_assertion(x)
            res = s.solve()
            v_y = s.get_value(y)
            self.assertEqual(v_y, TRUE())

            s.pop()
            s.add_assertion(Not(y))
            res = s.solve()
            v_x = s.get_value(x)
            self.assertEqual(v_x, FALSE())

    def test_yices(self):
        x, y = Symbol("x1"), Symbol("y1")
        f = Implies(x, y)

        solvers_set = ["yices"]
        with Portfolio(solvers_set,
                       logic=QF_UFLIRA,
                       incremental=True,
                       generate_models=True) as s:
            s.add_assertion(f)
            s.push()
            s.add_assertion(x)

            res = s.solve()
            v_y = s.get_value(y)
            self.assertEqual(v_y, TRUE())

            s.pop()
            s.add_assertion(Not(y))
            res = s.solve()
            v_x = s.get_value(x)
            self.assertEqual(v_x, FALSE())


if __name__ == '__main__':
    unittest.main()
