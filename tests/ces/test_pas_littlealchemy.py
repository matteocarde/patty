import unittest
from unittest import TestCase

from src.pddl.Domain import Domain, GroundedDomain
from src.pddl.Problem import Problem
from src.plan.CESEncoding import CESEncoding
from src.search.ChainSearch import ChainSearch
from src.search.PASSearch import PASSearch
from src.utils.Arguments import Arguments


class TestCES(TestCase):

    def setUp(self) -> None:
        self.domain: Domain = Domain.fromFile(f"../../files/ces/littlealchemy/domain.pddl")
        self.problem: Problem = Problem.fromFile(f"../../files/ces/littlealchemy/example/problem.pddl")
        self.gDomain: GroundedDomain = self.domain.ground(self.problem)
        self.args = Arguments(keepRequired=False)

    def test_solver(self):
        search = PASSearch(self.gDomain, self.problem, self.args, liftedDomain=self.domain)
        plan = search.solve()
        print(plan)
        isValid = plan.validate(self.problem)
        self.assertTrue(isValid)


if __name__ == '__main__':
    unittest.main()
