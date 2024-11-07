from unittest import TestCase

import time
import unittest
from src.pddl.Domain import Domain, GroundedDomain
from src.pddl.NumericPlan import NumericPlan
from src.pddl.Problem import Problem

from src.plan.NumericEncoding import NumericEncoding
from src.plan.Pattern import Pattern
from src.smt.SMTSolver import SMTSolver
from src.utils.Arguments import Arguments


class TestElevator(TestCase):

    def setUp(self) -> None:
        self.domain: Domain = Domain.fromFile("../../files/numeric/elevator-num/domain.pddl")
        self.problem: Problem = Problem.fromFile("../../files/numeric/elevator-num/instances/problem-5-3-3.pddl")
        self.gDomain: GroundedDomain = self.domain.ground(self.problem)
        self.horizon = 3
        self.pattern = Pattern.fromOrder(self.gDomain.arpg.getActionsOrder())
        self.args = Arguments(keepRequired=False)
        self.pddl2smt: NumericEncoding = NumericEncoding(self.gDomain, self.problem, self.pattern, self.horizon,
                                                         self.args)
        print(self.pddl2smt.pattern)
        pass

    def test_transform(self):
        self.assertGreater(len(self.pddl2smt.initial), 0)
        self.assertGreater(len(self.pddl2smt.transitions), 0)
        self.assertGreater(len(self.pddl2smt.rules), 0)

    def test_solve(self):
        solver: SMTSolver = SMTSolver(self.pddl2smt)

        tic = time.perf_counter()
        plan: NumericPlan = solver.solve()
        toc = time.perf_counter()
        solver.exit()
        print("Time to solve:", toc - tic)

        self.assertIsInstance(plan, NumericPlan)

        print("Plan length: ", len(plan))
        print("No repetitions:")
        plan.print()
        print("With repetitions:")
        plan.printWithRepetitions()

        self.assertTrue(plan.validate(self.problem))


if __name__ == '__main__':
    unittest.main()
