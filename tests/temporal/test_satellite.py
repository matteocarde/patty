import unittest
from unittest import TestCase

from src.pddl.Domain import Domain, GroundedDomain
from src.pddl.Problem import Problem
from src.plan.Pattern import Pattern
from src.plan.TemporalEncoding import TemporalEncoding


class TestTemporalSatellite(TestCase):

    def setUp(self) -> None:
        folder = "../../files/temporal/satellite"
        problem = "instance-20"
        self.domain: Domain = Domain.fromFile(f"{folder}/domain.pddl")
        self.problem: Problem = Problem.fromFile(f"{folder}/instances/{problem}.pddl")
        self.gDomain: GroundedDomain = self.domain.ground(self.problem)
        self.horizon = 1
        self.pattern = Pattern.fromOrder(self.gDomain.arpg.getActionsOrder())
        self.pattern = self.pattern.multiply(self.horizon)
        self.encoding: TemporalEncoding = TemporalEncoding(self.gDomain, self.problem, self.pattern, 1)
        # print(self.pattern)
        self.encoding.printRules()
        pass

    def test_solve(self):
        self.assertIsInstance(self.domain, Domain)
        self.assertIsInstance(self.problem, Problem)
        self.assertIsInstance(self.gDomain, GroundedDomain)
        # solver: SMTSolver = SMTSolver(self.encoding)
        # solution: TemporalPlan = solver.solve()
        #
        # self.assertIsInstance(solution, TemporalPlan)
        #
        # print(solution)
        pass


if __name__ == '__main__':
    unittest.main()
