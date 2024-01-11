import unittest
from unittest import TestCase

from src.pddl.Domain import Domain, GroundedDomain
from src.pddl.Problem import Problem
from src.pddl.TemporalPlan import TemporalPlan
from src.plan.Pattern import Pattern
from src.plan.TemporalEncoding import TemporalEncoding
from src.smt.SMTSolution import SMTSolution
from src.smt.SMTSolver import SMTSolver


class TestPour(TestCase):

    def setUp(self) -> None:
        folder = "../../files/temporal/bottles-pour"
        problem = "problem_2_1_1"
        self.domain: Domain = Domain.fromFile(f"{folder}/domain.pddl")
        self.problem: Problem = Problem.fromFile(f"{folder}/instances/{problem}.pddl")
        self.gDomain: GroundedDomain = self.domain.ground(self.problem)
        self.horizon = 2
        self.pattern = Pattern.fromOrder(self.gDomain.arpg.getActionsOrder())
        self.pattern = self.pattern.multiply(self.horizon, addFake=False)
        self.encoding: TemporalEncoding = TemporalEncoding(self.gDomain, self.problem, self.pattern, 1)
        # print(self.pattern)
        # self.encoding.printRules()
        pass

    def test_solve(self):
        solver: SMTSolver = SMTSolver(self.encoding)
        solution: TemporalPlan = solver.solve()

        print(solution)
        self.assertIsInstance(solution, TemporalPlan)
        self.assertTrue(solution.validate(self.problem, avoidRaising=True))

        pass


if __name__ == '__main__':
    unittest.main()
