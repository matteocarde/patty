import unittest
from unittest import TestCase

from src.pddl.Domain import Domain, GroundedDomain
from src.pddl.NumericPlan import NumericPlan
from src.pddl.Problem import Problem
from src.search.JairSearchRelaxed import JairSearchRelaxed
from src.utils.Arguments import Arguments


class TestJairGreedyRelaxedMarketTrader(TestCase):

    def setUp(self) -> None:
        domainFile = "../../files/numeric/ipc-2023/markettrader/domain.pddl"
        problemFile = "../../files/numeric/ipc-2023/markettrader/instances/pfile01.pddl"

        self.domain: Domain = Domain.fromFile(domainFile)
        self.problem: Problem = Problem.fromFile(problemFile)
        self.gDomain: GroundedDomain = self.domain.ground(self.problem)
        self.args = Arguments(keepRequired=False)
        self.args.goalFunction = "DELTA-MAX-CLAUSES"
        self.args.useIncompletePattern = True
        self.args.minimizeGoalFunction = True
        self.args.printPattern = True
        self.args.greedyLevel = 0
        pass

    def test_solve(self):
        solver = JairSearchRelaxed(self.gDomain, self.problem, self.args)
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
