import unittest
from unittest import TestCase

from src.pddl.Domain import Domain, GroundedDomain
from src.pddl.Problem import Problem


class TestTemporalParking(TestCase):

    def setUp(self) -> None:
        folder = "../../files/temporal/parking"
        problem = "p15-9-3"
        self.domain: Domain = Domain.fromFile(f"{folder}/domain.pddl")
        self.problem: Problem = Problem.fromFile(f"{folder}/instances/{problem}.pddl")
        self.gDomain: GroundedDomain = self.domain.ground(self.problem)

        pass

    def test_check(self):
        self.assertIsInstance(self.domain, Domain)
        self.assertIsInstance(self.problem, Problem)
        self.assertIsInstance(self.gDomain, GroundedDomain)


if __name__ == '__main__':
    unittest.main()
