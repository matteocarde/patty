import unittest
from unittest import TestCase

from src.pddl.Domain import Domain, GroundedDomain
from src.pddl.Problem import Problem
from src.pddl.TemporalPlan import TemporalPlan
from src.plan.Pattern import Pattern
from src.plan.TemporalEncoding import TemporalEncoding
from src.smt.SMTSolver import SMTSolver


class TestFloortile(TestCase):

    def setUp(self) -> None:
        folder = "../../files/temporal/floortile"
        problem = "p442-1"
        self.domain: Domain = Domain.fromFile(f"{folder}/domain.pddl")
        self.problem: Problem = Problem.fromFile(f"{folder}/instances/{problem}.pddl")
        self.gDomain: GroundedDomain = self.domain.ground(self.problem)
        self.horizon = 3
        self.pattern = Pattern.fromOrder(self.gDomain.arpg.getActionsOrder())
        self.pattern = self.pattern.multiply(self.horizon, addFake=False)
        self.encoding: TemporalEncoding = TemporalEncoding(self.gDomain, self.problem, self.pattern, 1)
        # self.encoding.printRules()
        print(f"N of vars: {self.encoding.getNVars()}")
        print(f"N of rules: {self.encoding.getNRules()}")
        pass

    def test_check(self):
        self.assertIsInstance(self.domain, Domain)
        self.assertIsInstance(self.problem, Problem)
        self.assertIsInstance(self.gDomain, GroundedDomain)
        solver: SMTSolver = SMTSolver(self.encoding)
        solution: TemporalPlan = solver.solve()

        self.assertIsInstance(solution, TemporalPlan)

        print(solution)
        pass


if __name__ == '__main__':
    unittest.main()
