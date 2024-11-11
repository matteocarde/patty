import time
import unittest
from unittest import TestCase

from src.pddl.Domain import Domain, GroundedDomain
from src.pddl.NumericPlan import NumericPlan
from src.pddl.Problem import Problem
from src.plan.NumericEncoding import NumericEncoding
from src.plan.Pattern import Pattern
from src.smt.SMTSolution import SMTSolution
from src.smt.SMTSolver import SMTSolver
from src.utils.Arguments import Arguments


class TestRover(TestCase):

    def setUp(self) -> None:
        a = time.perf_counter()
        self.domain: Domain = Domain.fromFile("../../files/numeric/ipc-2023/rover/domain.pddl")
        b = time.perf_counter()
        self.problem: Problem = Problem.fromFile("../../files/numeric/ipc-2023/rover/instances/pfile1.pddl")
        c = time.perf_counter()
        self.gDomain: GroundedDomain = self.domain.ground(self.problem)
        d = time.perf_counter()
        self.horizon = 4
        self.pattern = Pattern.fromOrder(self.gDomain.arpg.getActionsOrder())
        self.args = Arguments(keepRequired=False)
        self.pddl2smt: NumericEncoding = NumericEncoding(self.gDomain, self.problem, self.pattern, self.horizon,
                                                         self.args)
        e = time.perf_counter()
        print(self.pddl2smt.pattern)
        print("Domain Time:", b - a)
        print("Problem Time:", c - b)
        print("Grounding Time:", d - c)
        print("NumericEncoding Time:", e - d)
        pass

    def test_transform(self):
        self.assertGreater(len(self.pddl2smt.initial), 0)
        self.assertGreater(len(self.pddl2smt.transitions), 0)
        self.assertGreater(len(self.pddl2smt.rules), 0)

    def test_solve(self):
        solver: SMTSolver = SMTSolver(self.pddl2smt)

        solution: SMTSolution = solver.getSolution()

        plan: NumericPlan = self.pddl2smt.getPlanFromSolution(solution)
        solver.exit()

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
