import unittest
from unittest import TestCase

from src.pddl.Domain import Domain, GroundedDomain
from src.pddl.Problem import Problem
from src.plan.CESEncoding import CESEncoding
from src.search.ChainSearch import ChainSearch
from src.search.PASSearch import PASSearch
from src.utils.Arguments import Arguments


class TestCESMeetingNOC(TestCase):

    def setUp(self) -> None:
        domain = f"../../files/ces/meeting/domain.pddl"
        problem = f"../../files/ces/meeting/instances/problem-9.pddl"
        self.domain: Domain = Domain.fromFile(domain)
        self.problem: Problem = Problem.fromFile(problem)
        self.qeDomain: Domain = self.domain.eliminateQuantifiers(self.problem)
        self.gDomain: GroundedDomain = self.qeDomain.ground(self.problem)
        self.args = Arguments(keepRequired=False)
        self.args.pattern = "alpha"
        self.args.avoidClosureRelaxation = True
        self.args.printTransitiveClosures = True

    def test_solver(self):
        self.assertTrue(self.gDomain.hasConditionalEffects())
        search = PASSearch(self.gDomain, self.problem, self.args, liftedDomain=self.domain)
        plan = search.solve()
        print(plan)
        isValid = plan.validate(self.problem)
        self.assertTrue(isValid)


if __name__ == '__main__':
    unittest.main()
