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


class TestPatty_Jair(TestCase):

    def setUp(self) -> None:
        pass

    def test_solve(self):
        domainFile = "../../files/numeric/ipc-2023/ext-plant-watering/domain.pddl"
        problemFile = "../../files/numeric/ipc-2023/ext-plant-watering/instances/instance_10_5_2_1.pddl"

        versions = {
            # Table 2
            "Cnpc",
            "Bnpc",
            "Rnec",
            "Gnei",
            "Cgpc",
            "Bgpc",
            "Rgec",
            "Ggei",
            "Caes",
            # Table 3
            "Cnpc",
            "Cnrc",
            "Cnoc",
            "Bnpc",
            "Bnrc",
            "Bnoc",
            # Table 4
            "Cnpc",
            "Bnpc",
            "Rnec",
            "Gnei",
            "Cnps",
            "Bnps",
            "Rnes",
            "Gnes",
            "Cnpi",
            "Bnpi",
        }

        for v in versions:
            try:
                print(f"Testing {v}")
                self.domain: Domain = Domain.fromFile(domainFile)
                self.problem: Problem = Problem.fromFile(problemFile)
                self.gDomain: GroundedDomain = self.domain.ground(self.problem)
                self.args = Arguments(keepRequired=False)

                self.args.jairSearchStrategy = v[0]
                self.args.jairGoalFunction = v[1]
                self.args.jairPatternG = v[2]
                self.args.jairPatternH = v[3]
                solver = JairSearch(self.gDomain, self.problem, self.args)
                plan: NumericPlan = solver.solve()

                print(f"Testing {v}: OK")
            except Exception as e:
                print(e)
                self.assertTrue(False)

        self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()
