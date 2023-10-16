import unittest
from unittest import TestCase

from src.pddl.Domain import Domain, GroundedDomain
from src.pddl.NumericPlan import NumericPlan
from src.pddl.Problem import Problem
from src.search.AStarSearch import AStarSearch
from src.search.AStarSearchMax import AStarSearchMax
from src.utils.Arguments import Arguments


class TestAStarDrone(TestCase):

    def setUp(self) -> None:
        domainFile = "../../files/ipc-2023/drone/domain.pddl"
        problemFile = "../../files/ipc-2023/drone/instances/problem_4_2_5.pddl"

        self.domain: Domain = Domain.fromFile(domainFile)
        self.problem: Problem = Problem.fromFile(problemFile)
        self.gDomain: GroundedDomain = self.domain.ground(self.problem)
        self.args = Arguments(keepRequired=False)
        pass

    def test_solve(self):
        solver = AStarSearch(self.gDomain, self.problem, self.args, maximize=True)
        plan: NumericPlan = solver.solve()

        self.assertIsInstance(plan, NumericPlan)

        print("Plan length: ", len(plan))
        print("No repetitions:")
        plan.print()
        print("With repetitions:")
        plan.printWithRepetitions()

        self.assertTrue(plan.validate(self.problem))


if __name__ == '__main__':
    unittest.main()
