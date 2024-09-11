import unittest
from unittest import TestCase

from src.pddl.Domain import Domain, GroundedDomain
from src.pddl.NumericPlan import NumericPlan
from src.pddl.Problem import Problem
from src.search.PlanImprover import PlanImprover
from src.search.StepSearch import StepSearch
from src.utils.Arguments import Arguments


class TestStepSearchSailing(TestCase):

    def setUp(self) -> None:
        domainFile = "../../files/numeric/ipc-2023/sailing/domain.pddl"
        problemFile = "../../files/numeric/ipc-2023/sailing/instances/instance_1_4_1229.pddl"

        self.domain: Domain = Domain.fromFile(domainFile)
        self.problem: Problem = Problem.fromFile(problemFile)
        self.gDomain: GroundedDomain = self.domain.ground(self.problem)
        self.args = Arguments(keepRequired=False)
        pass

    def test_solve(self):
        solver = StepSearch(self.gDomain, self.problem, self.args)
        plan: NumericPlan = solver.solve()

        self.assertIsInstance(plan, NumericPlan)

        print("Plan length: ", len(plan))
        print("No repetitions:")
        plan.print()
        print("With repetitions:")
        plan.printWithRepetitions()

        self.assertTrue(plan.validate(self.problem))

    def test_improve(self):
        solver = StepSearch(self.gDomain, self.problem, self.args)
        plan: NumericPlan = solver.solve()

        self.assertIsInstance(plan, NumericPlan)

        improver = PlanImprover(self.gDomain, self.problem, self.args, plan)
        improvedPlan = improver.solve()

        self.assertIsInstance(improvedPlan, NumericPlan)
        print("Plan length: ", len(improvedPlan))
        print("With repetitions:")
        improvedPlan.printWithRepetitions()

        print(f"First Plan Length: {len(plan)}")
        print(f"Improved Plan Length: {len(improvedPlan)}")

        self.assertLessEqual(len(improvedPlan), len(plan))


if __name__ == '__main__':
    unittest.main()
