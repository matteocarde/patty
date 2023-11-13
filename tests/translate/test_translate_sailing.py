import unittest
from unittest import TestCase

from src.pattern.PatternTranslator import PatternTranslator
from src.pddl.Domain import Domain
from src.pddl.Problem import Problem


class TestSailing(TestCase):

    def setUp(self) -> None:
        self.folder = "../../files/ipc-2023/fo-sailing"
        self.domain: Domain = Domain.fromFile(f"{self.folder}/domain.pddl")
        self.problem: Problem = Problem.fromFile(f"{self.folder}/instances/instance_1_1_1229.pddl")
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
        tProblemString = tProblem.toPDDL().toString()
        self.assertIsInstance(tDomainString, str)
        self.assertIsInstance(tProblemString, str)

        with open(f"{self.folder}/domain_pattern.pddl", "w") as fDomain:
            fDomain.write(tDomainString)

        with open(f"{self.folder}/problem_pattern.pddl", "w") as fDomain:
            fDomain.write(tProblemString)


if __name__ == '__main__':
    unittest.main()
