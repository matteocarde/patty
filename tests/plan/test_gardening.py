import unittest
from unittest import TestCase

from src.pddl.Domain import Domain, GroundedDomain
from src.pddl.NumericPlan import NumericPlan
from src.pddl.Problem import Problem
from src.plan.PDDL2SMT import PDDL2SMT
from src.plan.Pattern import Pattern
from src.smt.SMTSolver import SMTSolver


class TestGardening(TestCase):

    def setUp(self) -> None:
        self.domain: Domain = Domain.fromFile("../../files/gardening/domain.pddl")
        self.problem: Problem = Problem.fromFile("../../files/gardening/instances/instance_7_1_2.pddl")
        self.gDomain: GroundedDomain = self.domain.ground(self.problem)
        self.horizon = 3
        self.pattern = Pattern.fromOrder(self.gDomain.arpg.getActionsOrder())
        self.pddl2smt: PDDL2SMT = PDDL2SMT(self.gDomain, self.problem, self.pattern, self.horizon)
        print(self.pddl2smt.pattern)
        pass

    def test_transform(self):
        self.assertGreater(len(self.pddl2smt.rules), 0)

    def test_solve(self):
        solver: SMTSolver = SMTSolver(self.pddl2smt)

        plan: NumericPlan = solver.solve()
        solver.exit()

        self.assertIsInstance(plan, NumericPlan)
        print("No repetitions:")
        plan.print()
        print("With repetitions:")
        plan.printWithRepetitions()

        self.assertTrue(plan.validate(self.problem))



if __name__ == '__main__':
    unittest.main()
