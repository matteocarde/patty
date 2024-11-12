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


class TestSettlers(TestCase):

    def setUp(self) -> None:
        self.domain: Domain = Domain.fromFile("../../files/numeric/ipc-2023/settlers-compiled/domain.pddl")
        self.problem: Problem = Problem.fromFile(
            "../../files/numeric/ipc-2023/settlers-compiled/instances/pfile12.pddl")
        self.gDomain: GroundedDomain = self.domain.ground(self.problem)
        self.horizon = 1
        self.pattern = Pattern.fromOrder(self.gDomain.arpg.getActionsOrder())
        self.args = Arguments(keepRequired=False)
        self.pddl2smt: NumericEncoding = NumericEncoding(self.gDomain, self.problem, self.pattern, self.horizon,
                                                         self.args)
        print("Size:", len(self.pddl2smt.rules))
        print("Depth:", max([r.depth for r in self.pddl2smt.rules]) + 1)
        deepest = None
        depth = 0
        for r in self.pddl2smt.rules:
            if r.depth > depth:
                deepest = r
                depth = r.depth
        print(depth)
        print(deepest)

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
