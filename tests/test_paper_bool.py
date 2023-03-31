import unittest
from unittest import TestCase

from Domain import Domain, GroundedDomain
from NumericPlan import NumericPlan
from PDDLException import PDDLException
from Problem import Problem
from classes.plan.PDDL2SMT import PDDL2SMT
from classes.smt.SMTSolution import SMTSolution
from classes.smt.SMTSolver import SMTSolver


class TestPaperBool(TestCase):

    def setUp(self) -> None:
        self.domain: Domain = Domain.fromFile("../files/paper-example/domain-bool.pddl")
        self.problem: Problem = Problem.fromFile("../files/paper-example/problem-bool.pddl")
        self.gDomain: GroundedDomain = self.domain.ground(self.problem)
        self.horizon = 1
        self.pddl2smt: PDDL2SMT = PDDL2SMT(self.gDomain, self.problem, self.horizon)
        pass

    def test_transform(self):
        self.assertGreater(len(self.pddl2smt.initial), 0)
        self.assertGreater(len(self.pddl2smt.transitions), 0)
        self.assertGreater(len(self.pddl2smt.rules), 0)

    def test_solve(self):
        solver: SMTSolver = SMTSolver(self.pddl2smt)

        print(self.pddl2smt.order)
        self.pddl2smt.printRules()

        solution = solver.getSolution()
        print(solution)
        plan: NumericPlan = self.pddl2smt.getPlanFromSolution(solution)
        solver.exit()
        print(plan)
        self.assertIsInstance(plan, NumericPlan)

        print("No repetitions:")
        plan.print()
        print("With repetitions:")
        plan.printWithRepetitions()

        self.assertTrue(plan.validate(self.problem))


if __name__ == '__main__':
    unittest.main()
