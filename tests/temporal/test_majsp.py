import unittest
from unittest import TestCase

from src.pddl.Domain import Domain, GroundedDomain
from src.pddl.Problem import Problem
from src.pddl.TemporalPlan import TemporalPlan
from src.plan.Pattern import Pattern
from src.plan.TemporalEncoding import TemporalEncoding
from src.smt.SMTSolver import SMTSolver


class TestMajsp(TestCase):

    def setUp(self) -> None:
        folder = "../../files/temporal/majsp"
        problem = "instance_2_1_2_4"
        self.domain: Domain = Domain.fromFile(f"{folder}/domain.pddl")
        self.problem: Problem = Problem.fromFile(f"{folder}/instances/{problem}.pddl")
        self.gDomain: GroundedDomain = self.domain.ground(self.problem)
        self.horizon = 5
        self.pattern = Pattern.fromOrder(self.gDomain.arpg.getActionsOrder())
        self.pattern = self.pattern.multiply(self.horizon, addFake=False)
        self.encoding: TemporalEncoding = TemporalEncoding(self.gDomain, self.problem, self.pattern, 1,
                                                           constraints="logical")
        # print(self.pattern)
        # self.encoding.printRules()
        pass

    def test_solve(self):
        solver: SMTSolver = SMTSolver(self.encoding)
        solution: TemporalPlan = solver.solve()

        self.assertIsInstance(solution, TemporalPlan)
        self.assertTrue(solution.validate(self.problem))

        print(solution)
        pass


if __name__ == '__main__':
    unittest.main()
