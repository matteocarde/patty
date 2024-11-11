import unittest
from unittest import TestCase

from src.pddl.Domain import Domain, GroundedDomain
from src.pddl.Problem import Problem


class TestBigGroundingRover(TestCase):

    def setUp(self) -> None:
        domainFile = "../../files/numeric/ipc-2023/rover/domain.pddl"
        problemFile = "../../files/numeric/ipc-2023/rover/instances/pfile15.pddl"

        self.domain: Domain = Domain.fromFile(domainFile)
        self.problem: Problem = Problem.fromFile(problemFile)
        pass

    def test_ground(self):
        self.gDomain: GroundedDomain = self.domain.ground(self.problem)

        self.assertIsInstance(self.gDomain, GroundedDomain)


if __name__ == '__main__':
    unittest.main()
