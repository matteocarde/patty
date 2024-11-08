from unittest import TestCase

import unittest
from src.pddl.Domain import Domain, GroundedDomain
from src.pddl.NumericPlan import NumericPlan
from src.pddl.Problem import Problem

from src.plan.NumericEncoding import NumericEncoding
from src.plan.Pattern import Pattern
from src.smt.SMTSolution import SMTSolution
from src.smt.SMTSolver import SMTSolver
from src.utils.Arguments import Arguments


class TestLineExchangeGeneral(TestCase):

    def setUp(self) -> None:
        self.domain: Domain = Domain.fromFile("../../files/numeric/line-exchange/domain.pddl")
        self.problem: Problem = Problem.fromFile("../../files/numeric/line-exchange/instances/4_5_25_50.pddl")
        self.gDomain: GroundedDomain = self.domain.ground(self.problem)
        self.horizon = 3
        self.pattern = Pattern.fromOrder(self.gDomain.arpg.getActionsOrder())
        self.args = Arguments(keepRequired=False)
        self.pddl2smt: NumericEncoding = NumericEncoding(self.gDomain, self.problem, self.pattern, self.horizon,
                                                         self.args)
        print(self.pddl2smt.pattern)
        self.pddl2smt.printRules()
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

    # def test_optimize(self):
    #     solver: SMTSolver = SMTSolver(self.pddl2smt)
    #
    #     plan: NumericPlan = solver.optimize()
    #     solver.exit()
    #
    #     self.assertIsInstance(plan, NumericPlan)
    #
    #     print("Plan length: ", len(plan))
    #     print("No repetitions:")
    #     plan.print()
    #     print("With repetitions:")
    #     plan.printWithRepetitions()
    #
    #     self.assertTrue(plan.validate(self.problem))
    #     self.assertTrue(plan.optimal)
    #
    # def test_optimize_binary(self):
    #     solver: SMTSolver = SMTSolver(self.pddl2smt)
    #
    #     plan: NumericPlan = solver.optimizeBinary()
    #     solver.exit()
    #
    #     self.assertIsInstance(plan, NumericPlan)
    #
    #     print("Plan length: ", len(plan))
    #     print("No repetitions:")
    #     plan.print()
    #     print("With repetitions:")
    #     plan.printWithRepetitions()
    #
    #     self.assertTrue(plan.validate(self.problem))
    #     self.assertTrue(plan.optimal)


if __name__ == '__main__':
    unittest.main()
