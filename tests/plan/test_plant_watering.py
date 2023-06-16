import unittest
from unittest import TestCase

from Domain import Domain, GroundedDomain
from NumericPlan import NumericPlan
from Problem import Problem
from src.plan.PDDL2SMT import PDDL2SMT
from src.smt.SMTSolution import SMTSolution
from src.smt.SMTSolver import SMTSolver


class TestPlantWatering(TestCase):

    def setUp(self) -> None:
        self.domain: Domain = Domain.fromFile("../files/plant-watering/domain.pddl")
        self.problem: Problem = Problem.fromFile("../files/plant-watering/instances/instance_4_1.pddl")
        self.gDomain: GroundedDomain = self.domain.ground(self.problem)
        self.horizon = 4
        self.pddl2smt: PDDL2SMT = PDDL2SMT(self.gDomain, self.problem, self.horizon)
        print(self.pddl2smt.order)
        pass

    def test_transform(self):
        self.assertGreater(len(self.pddl2smt.initial), 0)
        self.assertGreater(len(self.pddl2smt.transitions), 0)
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

    def test_optimize(self):
        solver: SMTSolver = SMTSolver(self.pddl2smt)

        plan: NumericPlan = solver.optimize()
        solver.exit()

        self.assertIsInstance(plan, NumericPlan)

        print("Plan length: ", len(plan))
        print("No repetitions:")
        plan.print()
        print("With repetitions:")
        plan.printWithRepetitions()

        self.assertTrue(plan.validate(self.problem))
        self.assertTrue(plan.optimal)

    def test_optimize_binary(self):
        solver: SMTSolver = SMTSolver(self.pddl2smt)

        plan: NumericPlan = solver.optimizeBinary()
        solver.exit()

        self.assertIsInstance(plan, NumericPlan)

        print("Plan length: ", len(plan))
        print("No repetitions:")
        plan.print()
        print("With repetitions:")
        plan.printWithRepetitions()

        self.assertTrue(plan.validate(self.problem))
        self.assertTrue(plan.optimal)


if __name__ == '__main__':
    unittest.main()
