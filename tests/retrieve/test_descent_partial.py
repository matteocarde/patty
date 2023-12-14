import unittest
from unittest import TestCase

from src.pddl.Domain import Domain, GroundedDomain
from src.pddl.InitialCondition import InitialCondition
from src.pddl.Problem import Problem
from src.pddl.State import State
from src.pddl.Trace import Trace
from src.retrieve.Bounds import Bounds
from src.retrieve.InitialConditionRetriever import InitialConditionRetriever
from src.retrieve.InitialConditionSpace import InitialConditionSpace


class TestDescentPartial(TestCase):

    def setUp(self) -> None:
        folder = "../../files/hybrid/Descent"
        problem = "prob_earth01"
        self.domain: Domain = Domain.fromFile(f"{folder}/domain.pddl")
        self.problem: Problem = Problem.fromFile(f"{folder}/partial/{problem}/{problem}-0.pddl")
        self.gDomain: GroundedDomain = self.domain.ground(self.problem, avoidSimplification=True)
        self.bounds: Bounds = Bounds.fromFile(f"{folder}/bounds.json", self.gDomain)

        self.trace: Trace = Trace.fromENHSP(f"{folder}/plans/{problem}.pddl.txt", self.gDomain)

        self.ics: InitialConditionSpace = InitialConditionSpace(self.trace, self.problem, self.gDomain)

        pass

    def test_check(self):
        self.assertIsInstance(self.domain, Domain)
        self.assertIsInstance(self.problem, Problem)
        self.assertIsInstance(self.gDomain, GroundedDomain)

    def test_condition(self):
        self.assertTrue(self.ics.checkInitialCondition(self.problem.init))

    def test_solve(self):
        icr = InitialConditionRetriever(self.ics, self.problem.init, bounds=self.bounds)
        (init, obj) = icr.solve()

        finalState: State = self.trace.apply(init)

        self.assertTrue(finalState.satisfies(self.problem.goal))


if __name__ == '__main__':
    unittest.main()
