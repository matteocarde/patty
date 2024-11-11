from unittest import TestCase

import os
import unittest

from src.pddl.Domain import Domain, GroundedDomain
from src.pddl.NumericPlan import NumericPlan
from src.pddl.Problem import Problem
from src.plan.NumericEncoding import NumericEncoding
from src.plan.Pattern import Pattern
from src.smt.SMTSolver import SMTSolver
from src.utils.Arguments import Arguments


class TestSailing(TestCase):

    def setUp(self) -> None:
        self.domainFile = "../../files/numeric/ipc-2023/sailing/domain.pddl"
        self.problemFile = "../../files/numeric/ipc-2023/sailing/instances/instance_1_4_1229.pddl"
        self.domain: Domain = Domain.fromFile(self.domainFile)
        self.problem: Problem = Problem.fromFile(self.problemFile)
        self.gDomain: GroundedDomain = self.domain.ground(self.problem)
        self.horizon = 5
        self.pattern = Pattern.fromOrder(self.gDomain.arpg.getActionsOrder())
        self.args = Arguments(keepRequired=False)
        self.pddl2smt: NumericEncoding = NumericEncoding(self.gDomain, self.problem, self.pattern, self.horizon,
                                                         self.args)
        print(self.pddl2smt.pattern)
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


if __name__ == '__main__':
    unittest.main()
