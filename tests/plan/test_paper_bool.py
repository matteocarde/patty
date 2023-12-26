from unittest import TestCase

import unittest
from src.pddl.Domain import Domain, GroundedDomain
from src.pddl.NumericPlan import NumericPlan
from src.pddl.Problem import Problem

from src.plan.NumericEncoding import NumericEncoding
from src.plan.Pattern import Pattern
from src.smt.SMTSolver import SMTSolver


class TestPaperBool(TestCase):

    def setUp(self) -> None:
        self.domain: Domain = Domain.fromFile("../../files/paper-example/domain-bool.pddl")
        self.problem: Problem = Problem.fromFile("../../files/paper-example/problem-bool.pddl")
        self.gDomain: GroundedDomain = self.domain.ground(self.problem)
        self.horizon = 1
        self.pattern = Pattern.fromOrder(self.gDomain.arpg.getActionsOrder())
        self.pddl2smt: NumericEncoding = NumericEncoding(self.gDomain, self.problem, self.pattern, self.horizon)
        pass

    def test_transform(self):
        self.assertGreater(len(self.pddl2smt.initial), 0)
        self.assertGreater(len(self.pddl2smt.transitions), 0)
        self.assertGreater(len(self.pddl2smt.rules), 0)

    def test_solve(self):
        solver: SMTSolver = SMTSolver(self.pddl2smt)

        print(self.pddl2smt.pattern)
        self.pddl2smt.printRules()

        solution = solver.getSolution()
        solver.exit()
        print(solution)
        plan: NumericPlan = self.pddl2smt.getPlanFromSolution(solution)
        print(plan)
        self.assertIsInstance(plan, NumericPlan)

        print("No repetitions:")
        plan.print()
        print("With repetitions:")
        plan.printWithRepetitions()

        self.assertTrue(plan.validate(self.problem))


if __name__ == '__main__':
    unittest.main()
