import unittest
from unittest import TestCase

from pysmt.oracles import get_logic
from pysmt.shortcuts import Symbol, is_sat, And, Not, Equals, Implies, Int, Portfolio
from pysmt.solvers.solver import Solver
from pysmt.typing import INT

from Domain import Domain, GroundedDomain
from Problem import Problem
from classes.SMTExpression import SMTExpression
from classes.SMTBoolVariable import SMTBoolVariable
from classes.SMTNumericVariable import SMTNumericVariable
from classes.SMTSolution import SMTSolution
from classes.SMTSolver import SMTSolver


class TestFarmland(TestCase):

    def setUp(self) -> None:
        self.domain: Domain = Domain.fromFile("../files/farmland/domain.pddl")
        self.problem: Problem = Problem.fromFile("../files/farmland/instances/instance_2_100_1229.pddl")
        self.gDomain: GroundedDomain = self.domain.ground(self.problem)
        pass

    def test_transform(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()
