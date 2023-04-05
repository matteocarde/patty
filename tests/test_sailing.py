import os
import unittest
from unittest import TestCase

from Domain import Domain, GroundedDomain
from NumericPlan import NumericPlan
from Problem import Problem
from classes.plan.PDDL2SMT import PDDL2SMT
from classes.smt.SMTSolution import SMTSolution
from classes.smt.SMTSolver import SMTSolver


class TestSailing(TestCase):

    def setUp(self) -> None:
        self.domainFile = "../files/sailing/domain.pddl"
        self.problemFile = "../files/sailing/instances/instance_1_2_1229.pddl"
        self.domain: Domain = Domain.fromFile(self.domainFile)
        self.problem: Problem = Problem.fromFile(self.problemFile)
        self.gDomain: GroundedDomain = self.domain.ground(self.problem)
        self.horizon = 2
        self.pddl2smt: PDDL2SMT = PDDL2SMT(self.gDomain, self.problem, self.horizon)
        print(self.pddl2smt.order)
        pass

    def test_transform(self):
        self.assertGreater(len(self.pddl2smt.initial), 0)
        self.assertGreater(len(self.pddl2smt.transitions), 0)
        self.assertGreater(len(self.pddl2smt.rules), 0)

    def test_solve(self):
        solver: SMTSolver = SMTSolver(self.pddl2smt)

        solution = solver.getSolution()
        solver.exit()
        print(solution)
        plan: NumericPlan = self.pddl2smt.getPlanFromSolution(solution)
        print(plan)

        self.assertIsInstance(plan, NumericPlan)

        print("Plan length: ", len(plan))
        print("No repetitions:")
        plan.print()
        print("With repetitions:")
        plan.printWithRepetitions()

        self.assertTrue(plan.validate(self.problem))

    def test_valValidation(self):
        solver: SMTSolver = SMTSolver(self.pddl2smt)

        solution = solver.getSolution()
        plan: NumericPlan = self.pddl2smt.getPlanFromSolution(solution)
        solver.exit()
        planFile = "/tmp/sailing_plan.txt"
        f = open(planFile, "w")
        f.write(plan.toValString())
        f.close()

        val = "/Users/carde/Bin/VAL/Validate"
        cmd = f"{val} {self.domainFile} {self.problemFile} {planFile}"
        result = os.popen(cmd).read()

        self.assertIn("Plan valid", result)

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
