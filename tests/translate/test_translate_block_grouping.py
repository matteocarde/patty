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
        tDomain: Domain = self.pt.getTranslatedDomain()
        self.assertIsInstance(tDomain, Domain)
        tProblem = self.pt.getTranslatedProblem()
        self.assertIsInstance(tProblem, Problem)

        tDomainString = tDomain.toPDDL().toString()
        print(tDomainString)
        self.assertIsInstance(tDomainString, str)

        with open("../../files/block-grouping/domain_pattern.pddl", "w") as fDomain:
            fDomain.write(tDomainString)


if __name__ == '__main__':
    unittest.main()
