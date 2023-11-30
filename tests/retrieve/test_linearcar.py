import unittest
from unittest import TestCase

from src.pddl.Domain import Domain, GroundedDomain
from src.pddl.Problem import Problem
from src.pddl.Trace import Trace
from src.retrieve.InitialConditionSpace import InitialConditionSpace


class TestLinearCar(TestCase):

    def setUp(self) -> None:
        folder = "../../files/hybrid/Linear-Car"
        self.domain: Domain = Domain.fromFile(f"{folder}/domain.pddl")
        self.problem: Problem = Problem.fromFile(f"{folder}/instances/instance_1_30.0_0.1_10.0.pddl")
        self.gDomain: GroundedDomain = self.domain.ground(self.problem, avoidSimplification=True)

        self.trace: Trace = Trace.fromFile(f"{folder}/plans/instance_1_30.0_0.1_10.0.txt", self.gDomain)

        self.ics: InitialConditionSpace = InitialConditionSpace(self.trace, self.problem, self.gDomain)

        pass

    def test_check(self):
        self.assertIsInstance(self.domain, Domain)
        self.assertIsInstance(self.problem, Problem)
        self.assertIsInstance(self.gDomain, GroundedDomain)


if __name__ == '__main__':
    unittest.main()
