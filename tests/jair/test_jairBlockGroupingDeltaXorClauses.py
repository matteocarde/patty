import unittest
from unittest import TestCase

from src.pddl.Domain import Domain, GroundedDomain
from src.pddl.NumericPlan import NumericPlan
from src.pddl.Problem import Problem
from src.search.AStarSearchMax import AStarSearchMax
from src.search.JairSearch import JairSearch
from src.utils.Arguments import Arguments


class TestBlockGroupingDeltaXorClauses(TestCase):

    def setUp(self) -> None:
        domainFile = "../../files/numeric/ipc-2023/block-grouping/domain.pddl"
        problemFile = "../../files/numeric/ipc-2023/block-grouping/instances/instance_5_25_6_1.pddl"

        self.domain: Domain = Domain.fromFile(domainFile)
        self.problem: Problem = Problem.fromFile(problemFile)
        self.gDomain: GroundedDomain = self.domain.ground(self.problem)
        self.goalFunctions = [
            # "DELTA-MAX-CLAUSES",
            "DELTA-PLUS-CLAUSES",
            # "DELTA-XOR-CLAUSES",
            # "GAMMA-GC-CLAUSES",
            # "GAMMA-MAX-CLAUSES",
            # "GAMMA-PLUS-CLAUSES",
        ]
        pass

    def test_solve(self):
        for gf in self.goalFunctions:
            args = Arguments(keepRequired=False)
            args.goalFunction = gf
            print(gf)

            solver = JairSearch(self.gDomain, self.problem, args)
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
