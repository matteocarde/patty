import unittest
from unittest import TestCase

from src.pddl.Domain import Domain, GroundedDomain
from src.pddl.NumericPlan import NumericPlan
from src.pddl.Problem import Problem
from src.plan.PDDL2SMT import PDDL2SMT
from src.plan.Pattern import Pattern
from src.smt.SMTSolution import SMTSolution
from src.smt.SMTSolver import SMTSolver


class TestSideExchange(TestCase):

    def setUp(self) -> None:
        self.domain: Domain = Domain.fromFile("../../files/side-exchange/domain.pddl")
        self.problem: Problem = Problem.fromFile("../../files/side-exchange/instances/1.pddl")
        self.gDomain: GroundedDomain = self.domain.ground(self.problem)
        self.horizon = 3
        self.pattern = Pattern.fromOrder(self.gDomain.arpg.getActionsOrder())
        self.pddl2smt: PDDL2SMT = PDDL2SMT(self.gDomain, self.problem, self.pattern, self.horizon)
        # print(self.pddl2smt.pattern)
        pass

    def test_transform(self):
        self.assertGreater(len(self.pddl2smt.initial), 0)
        self.assertGreater(len(self.pddl2smt.transitions), 0)
        self.assertGreater(len(self.pddl2smt.rules), 0)

    def test_solve(self):
        solver: SMTSolver = SMTSolver(self.pddl2smt)
        solution: SMTSolution = solver.getSolution()
        print(solution)
        plan: NumericPlan = self.pddl2smt.getPlanFromSolution(solution)
        solver.exit()

        self.assertIsInstance(plan, NumericPlan)

        print("No repetitions:")
        plan.print()
        print("With repetitions:")
        plan.printWithRepetitions()

        self.assertTrue(plan.validate(self.problem))


if __name__ == '__main__':
    unittest.main()
