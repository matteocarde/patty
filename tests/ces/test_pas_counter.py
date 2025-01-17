import unittest
from unittest import TestCase

from src.pddl.Domain import Domain, GroundedDomain
from src.pddl.Problem import Problem
from src.search.PASSearch import PASSearch
from src.utils.Arguments import Arguments


class TestCESCounter(TestCase):

    def setUp(self) -> None:
        self.b = 8
        self.domain: Domain = Domain.fromFile(f"../../files/ces/counter/domains/{self.b}/domain-{self.b}.pddl")
        self.problem: Problem = Problem.fromFile(
            f"../../files/ces/counter/domains/{self.b}/problem-{self.b}.pddl")
        self.gDomain: GroundedDomain = self.domain.ground(self.problem)
        self.args = Arguments(keepRequired=False)
        self.args.pattern = "alpha"
        self.args.maxClosureTime = 2

    def test_solver(self):
        search = PASSearch(self.gDomain, self.problem, self.args, liftedDomain=self.domain)
        plan = search.solve()
        print(plan)
        isValid = plan.validate(self.problem)
        self.assertTrue(isValid)


if __name__ == '__main__':
    unittest.main()
