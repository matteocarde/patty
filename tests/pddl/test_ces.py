import unittest
from unittest import TestCase

from src.pddl.Domain import Domain, GroundedDomain
from src.pddl.Problem import Problem


class TestCES(TestCase):

    def setUp(self) -> None:
        self.domain: Domain = Domain.fromFile("../../files/ces/counter/domains/2/domain-2.pddl")
        self.problem: Problem = Problem.fromFile("../../files/ces/counter/domains/2/problem-2.pddl")
        self.gDomain: GroundedDomain = self.domain.ground(self.problem)
        pass

    def test_transform(self):
        self.assertIsInstance(self.gDomain, GroundedDomain)
        self.assertEqual(len(self.gDomain.actions), 5)


if __name__ == '__main__':
    unittest.main()
