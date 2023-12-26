from unittest import TestCase

import unittest

from src.pddl.Domain import Domain, GroundedDomain
from src.pddl.NumericPlan import NumericPlan
from src.pddl.Problem import Problem
from src.plan.NumericEncoding import NumericEncoding
from src.plan.Pattern import Pattern
from src.smt.SMTSolver import SMTSolver


class TestFarmlandLinearZ3NonLinearEncoding(TestCase):

    def setUp(self) -> None:
        self.domain: Domain = Domain.fromFile("../../files/farmland_ln/domain.pddl")
        self.problem: Problem = Problem.fromFile("../../files/farmland_ln/instances/instance_2_100_1229.pddl")
        self.gDomain: GroundedDomain = self.domain.ground(self.problem)
        self.horizon = 2
        self.pattern = Pattern.fromOrder(self.gDomain.arpg.getActionsOrder())
        self.pddl2smt: NumericEncoding = NumericEncoding(self.gDomain, self.problem, self.pattern, self.horizon,
                                                         encoding="non-linear")
        print(self.pddl2smt.pattern)
        pass

    def test_transform(self):
        self.assertGreater(len(self.pddl2smt.rules), 0)

    def test_solve(self):
        solver: SMTSolver = SMTSolver(self.pddl2smt, solver="z3")

        plan: NumericPlan = solver.solve()
        solver.exit()

        self.assertIsInstance(plan, NumericPlan)
        print("No repetitions:")
        plan.print()
        print("With repetitions:")
        plan.printWithRepetitions()

        if not plan.validate(self.problem, avoidRaising=True):
            print("Not valid")

        self.assertTrue(plan.validate(self.problem))


if __name__ == '__main__':
    unittest.main()
