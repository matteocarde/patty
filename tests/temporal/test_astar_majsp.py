import unittest
from unittest import TestCase

from src.pddl.Domain import Domain, GroundedDomain
from src.pddl.Plan import Plan
from src.pddl.Problem import Problem
from src.pddl.TemporalPlan import TemporalPlan
from src.search.AStarSearchMax import AStarSearchMax
from src.utils.Arguments import Arguments


class TestAStarMajsp(TestCase):

    def setUp(self) -> None:
        folder = "../../files/temporal/majsp"
        problem = "instance_1_2_3_4"
        self.domain: Domain = Domain.fromFile(f"{folder}/domain.pddl")
        self.problem: Problem = Problem.fromFile(f"{folder}/instances/{problem}.pddl")
        self.gDomain: GroundedDomain = self.domain.ground(self.problem)
        self.args = Arguments(keepRequired=False)
        # print(self.pattern)
        # self.encoding.printRules()
        pass

    def test_solve(self):
        solver = AStarSearchMax(self.gDomain, self.problem, self.args)
        solution: Plan = solver.solve()

        print(solution)
        self.assertIsInstance(solution, TemporalPlan)
        self.assertTrue(solution.validate(self.problem, avoidRaising=True))

        pass


if __name__ == '__main__':
    unittest.main()
