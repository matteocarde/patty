import unittest
from unittest import TestCase

from Domain import Domain, GroundedDomain
from NumericPlan import NumericPlan
from Problem import Problem
from classes.plan.PDDL2SMT import PDDL2SMT
from classes.smt.SMTSolution import SMTSolution
from classes.smt.SMTSolver import SMTSolver


class TestPlantWatering(TestCase):

    def setUp(self) -> None:
        self.domain: Domain = Domain.fromFile("../files/plant-watering/domain.pddl")
        self.problem: Problem = Problem.fromFile("../files/plant-watering/instances/instance_20_3.pddl")
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
        solver: SMTSolver = SMTSolver()
        solver.addAssertions(self.pddl2smt.rules)

        solution: SMTSolution = solver.solve()

        self.assertIsInstance(solution, SMTSolution)

        plan: NumericPlan = self.pddl2smt.getPlanFromSolution(solution)
        print("No repetitions:")
        plan.print()
        print("With repetitions:")
        plan.printWithRepetitions()

        self.assertTrue(plan.validate(self.problem))


if __name__ == '__main__':
    unittest.main()
