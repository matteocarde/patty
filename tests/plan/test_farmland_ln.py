from unittest import TestCase

import unittest

from src.pddl.Domain import Domain, GroundedDomain
from src.pddl.NumericPlan import NumericPlan
from src.pddl.Problem import Problem
from src.plan.PDDL2SMT import PDDL2SMT
from src.smt.SMTSolver import SMTSolver


class TestFarmlandLinear(TestCase):

    def setUp(self) -> None:
        self.domain: Domain = Domain.fromFile("../../files/farmland_ln/domain.pddl")
        self.problem: Problem = Problem.fromFile("../../files/farmland_ln/instances/instance_2_100_1229.pddl")
        self.gDomain: GroundedDomain = self.domain.ground(self.problem)
        self.horizon = 2
        self.pddl2smt: PDDL2SMT = PDDL2SMT(self.gDomain, self.problem, self.horizon)
        print(self.pddl2smt.pattern)
        pass

    def test_transform(self):
        self.assertGreater(len(self.pddl2smt.rules), 0)

    def test_solve(self):
        solver: SMTSolver = SMTSolver(self.pddl2smt)

        plan: NumericPlan = solver.solve()
        solver.exit()

        self.assertIsInstance(plan, NumericPlan)
        print("No repetitions:")
        plan.print()
        print("With repetitions:")
        plan.printWithRepetitions()

        self.assertTrue(plan.validate(self.problem))

    def test_optimize_binary(self):
        solver: SMTSolver = SMTSolver(self.pddl2smt)

        plan: NumericPlan = solver.optimizeBinary()
        solver.exit()

        self.assertIsInstance(plan, NumericPlan)

        print("Plan length: ", len(plan))
        print("No repetitions:")
        plan.print()
        print("With repetitions:")
        plan.printWithRepetitions()

        self.assertTrue(plan.validate(self.problem))
        self.assertTrue(plan.optimal)


if __name__ == '__main__':
    unittest.main()