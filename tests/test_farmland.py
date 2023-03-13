import unittest
from unittest import TestCase

from Domain import Domain, GroundedDomain
from Problem import Problem
from classes.plan.PDDL2SMT import PDDL2SMT


class TestFarmland(TestCase):

    def setUp(self) -> None:
        self.domain: Domain = Domain.fromFile("../files/farmland/domain.pddl")
        self.problem: Problem = Problem.fromFile("../files/farmland/instances/instance_2_100_1229.pddl")
        self.gDomain: GroundedDomain = self.domain.ground(self.problem)
        self.horizon = 5
        self.pddl2smt: PDDL2SMT = PDDL2SMT(self.gDomain, self.problem, self.horizon)
        pass

    def test_transform(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()
