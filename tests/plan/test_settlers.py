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


class TestSettlers(TestCase):

    def setUp(self) -> None:
        a = time.perf_counter()
        self.domain: Domain = Domain.fromFile("../../files/ipc-2023/settlers/domain.pddl")
        b = time.perf_counter()
        self.problem: Problem = Problem.fromFile("../../files/ipc-2023/settlers/instances/pfile02.pddl")
        c = time.perf_counter()
        self.gDomain: GroundedDomain = self.domain.ground(self.problem)
        d = time.perf_counter()
        self.horizon = 4
        self.pattern = Pattern.fromOrder(self.gDomain.arpg.getActionsOrder())
        self.pddl2smt: PDDL2SMT = PDDL2SMT(self.gDomain, self.problem, self.pattern, self.horizon)
        e = time.perf_counter()
        pass

    def test_transform(self):
        self.assertGreater(len(self.pddl2smt.initial), 0)
        self.assertGreater(len(self.pddl2smt.transitions), 0)
        self.assertGreater(len(self.pddl2smt.rules), 0)

    def test_solve(self):
        solver: SMTSolver = SMTSolver(self.pddl2smt)

        solution: SMTSolution = solver.getSolution()
        solver.exit()

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
