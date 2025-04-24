import unittest
from unittest import TestCase

from src.pddl.Domain import Domain, GroundedDomain
from src.pddl.NumericPlan import NumericPlan
from src.pddl.Problem import Problem
from src.search.AStarSearchMax import AStarSearchMax
from src.search.JairSearch import JairSearch
from src.utils.Arguments import Arguments


class TestJairGreedySailing(TestCase):

    def setUp(self) -> None:
        domainFile = "../../files/numeric/ipc-2023/sailing/domain.pddl"
        problemFile = "../../files/numeric/ipc-2023/sailing/instances/instance_1_10_1229.pddl"

        self.domain: Domain = Domain.fromFile(domainFile)
        self.problem: Problem = Problem.fromFile(problemFile)
        self.gDomain: GroundedDomain = self.domain.ground(self.problem)
        self.args = Arguments(keepRequired=False)
        self.args.goalFunction = "DELTA-XOR-CLAUSES"
        self.args.useIncompletePattern = True
        self.args.minimizeGoalFunction = True
        self.args.printPattern = True
        self.args.greedyLevel = 0
        pass

    def test_solve(self):
        solver = JairSearch(self.gDomain, self.problem, self.args)
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
