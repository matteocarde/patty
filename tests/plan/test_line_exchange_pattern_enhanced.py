import unittest
from unittest import TestCase

from src.pddl.Domain import Domain, GroundedDomain
from src.pddl.Problem import Problem
from src.plan.Pattern import Pattern


class TestLineExchangePatternEnhanced(TestCase):

    def setUp(self) -> None:
        self.domain: Domain = Domain.fromFile("../../files/numeric/line-exchange/domain.pddl")
        self.problem: Problem = Problem.fromFile("../../files/numeric/line-exchange/instances/3_5_50_50.pddl")
        self.gDomain: GroundedDomain = self.domain.ground(self.problem)
        self.patternRandom = Pattern.fromRandom(self.gDomain)
        self.patternNormal = Pattern.fromARPG(self.gDomain)
        self.patternEnhanced = Pattern.fromARPGEnhanced(self.gDomain)
        pass

    def test_pattern(self):
        self.assertIsInstance(self.patternRandom, Pattern)
        self.assertIsInstance(self.patternNormal, Pattern)
        self.assertIsInstance(self.patternEnhanced, Pattern)

        print("--Pattern random---")
        print(self.patternRandom)
        print("--Pattern normal---")
        print(self.patternNormal)
        print("--Pattern enhanced---")
        print(self.patternEnhanced)


if __name__ == '__main__':
    unittest.main()
