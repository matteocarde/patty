import unittest
from unittest import TestCase

from src.pddl.Domain import Domain, GroundedDomain
from src.pddl.NumericPlan import NumericPlan
from src.pddl.Problem import Problem
from src.search.ChainSearch import ChainSearch
from src.search.StepSearch import StepSearch
from src.utils.Arguments import Arguments


class TestR3ELineExchange(TestCase):

    def setUp(self) -> None:
        domainFile = "../../files/numeric/line-exchange/domain.pddl"
        problemFile = "../../files/numeric/line-exchange/instances/5_5_90_10.pddl"

        self.domain: Domain = Domain.fromFile(domainFile)
        self.problem: Problem = Problem.fromFile(problemFile)
        self.gDomain: GroundedDomain = self.domain.ground(self.problem)
        self.args = Arguments(keepRequired=False)

        self.args.rollBound = 1000
        self.args.hasEffectAxioms = True
        pass

    def test_solve(self):
        self.args.printPattern = True
        self.args.maximize = True
        solver = StepSearch(self.gDomain, self.problem, self.args)
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
