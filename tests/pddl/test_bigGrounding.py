import unittest
from unittest import TestCase

from src.pddl.Domain import Domain, GroundedDomain
from src.pddl.NumericPlan import NumericPlan
from src.pddl.Problem import Problem
from src.search.AStarSearch import AStarSearch
from src.search.GBFSSearch import GBFSSearch
from src.utils.Arguments import Arguments


class TestBigGrounding(TestCase):

    def setUp(self) -> None:
        domainFile = "../../files/ipc-2023/delivery/domain.pddl"
        problemFile = "../../files/ipc-2023/delivery/instances/prob12.pddl"

        self.domain: Domain = Domain.fromFile(domainFile)
        self.problem: Problem = Problem.fromFile(problemFile)
        pass

    def test_ground(self):
        self.gDomain: GroundedDomain = self.domain.ground(self.problem)

        self.assertIsInstance(self.gDomain, GroundedDomain)


if __name__ == '__main__':
    unittest.main()
