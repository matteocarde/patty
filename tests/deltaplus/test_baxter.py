import unittest
from unittest import TestCase

from src.deltaplus.DeltaKnowledge import DeltaKnowledge
from src.deltaplus.PDDLDeltaPlus import PDDLDeltaPlus
from src.pddl.Domain import Domain, GroundedDomain
from src.pddl.Problem import Problem


class TestBaxter(TestCase):

    def setUp(self) -> None:
        self.domain: Domain = Domain.fromFile("../../files/hybrid/Baxter/domain.pddl")
        self.problem: Problem = Problem.fromFile("../../files/hybrid/Baxter/instances/P4_i1.pddl")
        self.kdelta: DeltaKnowledge = DeltaKnowledge.fromFile("../../files/hybrid/Baxter/domain.kdelta.json",
                                                              self.domain)
        self.deltaPlus: PDDLDeltaPlus = PDDLDeltaPlus(self.domain, self.problem)
        pass

    def test_transform(self):
        deltaDomain: Domain = self.deltaPlus.transformDomain(self.kdelta)
        deltaProblem: Problem = self.deltaPlus.transformProblem(self.kdelta)


if __name__ == '__main__':
    unittest.main()
