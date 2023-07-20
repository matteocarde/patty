import time
import unittest
from unittest import TestCase

from src.pddl.Domain import Domain, GroundedDomain
from src.pddl.NumericPlan import NumericPlan
from src.pddl.Problem import Problem
from src.plan.PDDL2SMT import PDDL2SMT
from src.plan.Pattern import Pattern
from src.smt.SMTSolution import SMTSolution
from src.smt.SMTSolver import SMTSolver


class TestZeno(TestCase):

    def setUp(self) -> None:
        self.domain: Domain = Domain.fromFile("../../files/zeno-travel/domain.pddl")
        self.problem: Problem = Problem.fromFile("../../files/zeno-travel/instances/pfile1.pddl")
        self.gDomain: GroundedDomain = self.domain.ground(self.problem)
        self.horizon = 5
        self.pattern = Pattern.fromOrder(self.gDomain.arpg.getActionsOrder())
        self.pddl2smt: PDDL2SMT = PDDL2SMT(self.gDomain, self.problem, self.pattern, self.horizon)
        print(self.pddl2smt.pattern)
        print("Number of rules:", len(self.pddl2smt.rules))
        pass

    def test_transform(self):
        self.assertGreater(len(self.pddl2smt.initial), 0)
        self.assertGreater(len(self.pddl2smt.transitions), 0)
        self.assertGreater(len(self.pddl2smt.rules), 0)

    def test_solve(self):
        tic = time.perf_counter()
        solver: SMTSolver = SMTSolver(self.pddl2smt)

        solution: SMTSolution = solver.getSolution()
        solver.exit()
        toc = time.perf_counter()

        print("Solution found in ", toc - tic)

        self.assertIsInstance(solution, SMTSolution)

        plan: NumericPlan = self.pddl2smt.getPlanFromSolution(solution)

        self.assertIsInstance(plan, NumericPlan)

        print("Plan length: ", len(plan))
        print("No repetitions:")
        plan.print()
        print("With repetitions:")
        plan.printWithRepetitions()

        valid = plan.validate(self.problem)
        self.assertTrue(valid)


if __name__ == '__main__':
    unittest.main()
