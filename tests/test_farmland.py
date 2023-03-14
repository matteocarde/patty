import unittest
from unittest import TestCase

from Domain import Domain, GroundedDomain
from Problem import Problem
from classes.plan.PDDL2SMT import PDDL2SMT
from classes.smt.SMTSolution import SMTSolution
from classes.smt.SMTSolver import SMTSolver


class TestFarmland(TestCase):

    def setUp(self) -> None:
        self.domain: Domain = Domain.fromFile("../files/farmland/domain.pddl")
        self.problem: Problem = Problem.fromFile("../files/farmland/instances/instance_2_100_1229.pddl")
        self.gDomain: GroundedDomain = self.domain.ground(self.problem)
        self.horizon = 5
        self.pddl2smt: PDDL2SMT = PDDL2SMT(self.gDomain, self.problem, self.horizon)
        pass

    def test_transform(self):
        self.assertGreater(len(self.pddl2smt.initial), 0)
        self.assertGreater(len(self.pddl2smt.goal), 0)
        self.assertGreater(len(self.pddl2smt.transitions), 0)
        self.assertGreater(len(self.pddl2smt.rules), 0)

    def test_solve(self):
        solver: SMTSolver = SMTSolver()
        solver.addAssertions(self.pddl2smt.rules)

        solution: SMTSolution = solver.solve()

        self.assertIsInstance(solution, SMTSolution)


if __name__ == '__main__':
    unittest.main()
