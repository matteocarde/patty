import unittest
from unittest import TestCase

from src.pddl.Domain import Domain, GroundedDomain
from src.pddl.NumericPlan import NumericPlan
from src.pddl.Problem import Problem
from src.search.AStarSearchMax import AStarSearchMax
from src.search.BDCSearch import BDCSearch
from src.search.GDSearch import GDSearch
from src.search.JairSearch import JairSearch
from src.utils.Arguments import Arguments


class TestBDCPlantWatering(TestCase):

    def setUp(self) -> None:
        domainFile = "../../files/numeric/ipc-2023/ext-plant-watering/domain.pddl"
        problemFile = "../../files/numeric/ipc-2023/ext-plant-watering/instances/instance_15_19_2_1.pddl"

        self.domain: Domain = Domain.fromFile(domainFile)
        self.problem: Problem = Problem.fromFile(problemFile)
        self.gDomain: GroundedDomain = self.domain.ground(self.problem)
        self.args = Arguments(keepRequired=False)
        self.args.goalFunction = "DELTA-PLUS-CLAUSES"
        self.args.minimizeGoalFunction = True
        self.args.printPattern = True
        pass

    def test_solve(self):
        solver = BDCSearch(self.gDomain, self.problem, self.args)
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
