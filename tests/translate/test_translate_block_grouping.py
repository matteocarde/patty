import unittest
from unittest import TestCase

from src.pattern.PatternTranslator import PatternTranslator
from src.pddl.Domain import Domain
from src.pddl.Problem import Problem


class TestBlockGrouping(TestCase):

    def setUp(self) -> None:
        self.domain: Domain = Domain.fromFile("../../files/block-grouping/domain.pddl")
        self.problem: Problem = Problem.fromFile("../../files/block-grouping/instances/instance_7_15_3_1.pddl")
        self.pt: PatternTranslator = PatternTranslator(self.domain, self.problem)
        pass

    def test_instance(self):
        self.assertIsInstance(self.pt, PatternTranslator)

    def test_domainTranslation(self):
        domain = self.pt.getTranslatedDomain()
        self.assertIsInstance(domain, Domain)


if __name__ == '__main__':
    unittest.main()
