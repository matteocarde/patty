import unittest
from unittest import TestCase

from src.pddl.Domain import Domain, GroundedDomain
from src.pddl.NumericPlan import NumericPlan
from src.pddl.Plan import Plan
from src.pddl.Problem import Problem
from src.pddl.TemporalPlan import TemporalPlan
from src.search.ChainSearch import ChainSearch
from src.utils.Arguments import Arguments


class TestStaticSearch(TestCase):

    def setUp(self) -> None:
        domainFile = "../../files/temporal/paper-example/domain.pddl"
        problemFile = "../../files/temporal/paper-example/instances/p2.pddl"

        self.domain: Domain = Domain.fromFile(domainFile)
        self.problem: Problem = Problem.fromFile(problemFile)
        self.gDomain: GroundedDomain = self.domain.ground(self.problem)
        self.args = Arguments(keepRequired=False)
        pass

    def test_solve(self):
        solver = ChainSearch(self.gDomain, self.problem, self.args)
        plan: Plan = solver.solve()

        self.assertIsInstance(plan, TemporalPlan)

        print("Plan length: ", len(plan))
        print("No repetitions:")
        plan.print()

        self.assertTrue(plan.validate(self.problem))


if __name__ == '__main__':
    unittest.main()
