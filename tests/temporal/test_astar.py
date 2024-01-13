import unittest
from unittest import TestCase

from src.pddl.Domain import Domain, GroundedDomain
from src.pddl.Plan import Plan
from src.pddl.Problem import Problem
from src.pddl.TemporalPlan import TemporalPlan
from src.plan.Pattern import Pattern
from src.plan.TemporalEncoding import TemporalEncoding
from src.search.AStarSearchMax import AStarSearchMax
from src.utils.Arguments import Arguments


class TestAStar(TestCase):

    def setUp(self) -> None:
        folder = "../../files/temporal/bottles-pour"
        problem = "problem_2_1_1"
        self.domain: Domain = Domain.fromFile(f"{folder}/domain.pddl")
        self.problem: Problem = Problem.fromFile(f"{folder}/instances/{problem}.pddl")
        self.gDomain: GroundedDomain = self.domain.ground(self.problem)
        self.args = Arguments(keepRequired=False)
        self.args.printPattern = True
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
