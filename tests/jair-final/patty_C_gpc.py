import unittest
from unittest import TestCase

from z3 import z3

from src.pddl.Domain import Domain, GroundedDomain
from src.pddl.NumericPlan import NumericPlan
from src.pddl.Problem import Problem
from src.search.AStarSearchMax import AStarSearchMax
from src.search.BDCSearch import BDCSearch
from src.search.GDSearch import GDSearch
from src.search.JairSearch import JairSearch
from src.utils.Arguments import Arguments


class TestPatty_C_gpc(TestCase):

    def setUp(self) -> None:
        domainFile = "../../files/numeric/ipc-2023/fo_counters/domain.pddl"
        problemFile = "../../files/numeric/ipc-2023/fo_counters/instances/instance_20.pddl"

        print(z3.get_full_version())
        self.domain: Domain = Domain.fromFile(domainFile)
        self.problem: Problem = Problem.fromFile(problemFile)
        self.gDomain: GroundedDomain = self.domain.ground(self.problem)
        self.args = Arguments(keepRequired=False)
        self.args.jairSearchStrategy = "C"
        self.args.jairGoalFunction = "g"
        self.args.jairPatternG = "p"
        self.args.jairPatternH = "c"
        self.args.pattern = "enhanced"
        self.args.printPattern = True
        pass

    def test_solve(self):
        solver = JairSearch(self.gDomain, self.problem, self.args)
        plan: NumericPlan = solver.solve()

        self.assertIsInstance(plan, NumericPlan)

        print("Plan length: ", len(plan))
        print("No repetitions:")
        plan.print()
        print("With repetitions:")
        plan.printWithRepetitions()

        self.assertTrue(plan.validate(self.problem))


if __name__ == '__main__':
    unittest.main()
