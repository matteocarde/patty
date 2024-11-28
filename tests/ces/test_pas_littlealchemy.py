import unittest
from unittest import TestCase

from src.pddl.Domain import Domain, GroundedDomain
from src.pddl.Problem import Problem
from src.search.PASSearch import PASSearch
from src.utils.Arguments import Arguments


class TestCES(TestCase):

    def setUp(self) -> None:
        self.domain: Domain = Domain.fromFile(f"../../files/ces/littlealchemy/domain.pddl")
        self.problem: Problem = Problem.fromFile(f"../../files/ces/littlealchemy/instances/problem-1.pddl")
        # self.problem: Problem = Problem.fromFile(f"../../files/ces/littlealchemy/example/problem.pddl")
        self.qeDomain: Domain = self.domain.eliminateQuantifiers(self.problem)
        self.gDomain: GroundedDomain = self.qeDomain.ground(self.problem)
        self.args = Arguments(keepRequired=False)

    def test_solver(self):
        search = PASSearch(self.gDomain, self.problem, self.args, liftedDomain=self.domain)
        plan = search.solve()
        print(plan)
        isValid = plan.validate(self.problem)
        self.assertTrue(isValid)


if __name__ == '__main__':
    unittest.main()
