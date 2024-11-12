import unittest
from unittest import TestCase

from src.pddl.Domain import Domain, GroundedDomain
from src.pddl.NumericPlan import NumericPlan
from src.pddl.Problem import Problem
from src.plan.NumericEncoding import NumericEncoding
from src.plan.Pattern import Pattern
from src.smt.SMTSolver import SMTSolver
from src.utils.Arguments import Arguments


class TestFarmland(TestCase):

    def setUp(self) -> None:
        self.domain: Domain = Domain.fromFile("../../files/numeric/ipc-2023/farmland/domain.pddl")
        self.problem: Problem = Problem.fromFile(
            "../../files/numeric/ipc-2023/farmland/instances/instance_2_300_1229.pddl")
        self.gDomain: GroundedDomain = self.domain.ground(self.problem)
        self.horizon = 1
        self.pattern = Pattern.fromOrder(self.gDomain.arpg.getActionsOrder())
        self.args = Arguments(keepRequired=False)
        self.pddl2smt: NumericEncoding = NumericEncoding(self.gDomain, self.problem, self.pattern, self.horizon,
                                                         self.args)
        self.pddl2smt.printRules()
        pass

    def test_solve(self):
        solver: SMTSolver = SMTSolver(self.pddl2smt)
        sol = solver.getSolution()
        print(sol)
        plan: NumericPlan = solver.solve()
        solver.exit()

        self.assertIsInstance(plan, NumericPlan)
        print("No repetitions:")
        plan.print()
        print("With repetitions:")
        plan.printWithRepetitions()

        self.assertTrue(plan.validate(self.problem))


if __name__ == '__main__':
    unittest.main()
