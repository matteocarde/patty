import unittest
from unittest import TestCase

from src.pddl.Domain import Domain, GroundedDomain
from src.pddl.InitialCondition import InitialCondition
from src.pddl.Problem import Problem
from src.pddl.State import State
from src.pddl.Trace import Trace
from src.retrieve.InitialConditionRetriever import InitialConditionRetriever
from src.retrieve.InitialConditionSpace import InitialConditionSpace


class TestBlockGrouping(TestCase):

    def setUp(self) -> None:
        folder = "../../files/numeric/ipc-2023/block-grouping"
        problem = "instance_11_35_8_3"
        self.domain: Domain = Domain.fromFile(f"{folder}/domain.pddl")
        self.problem: Problem = Problem.fromFile(f"{folder}/instances/{problem}.pddl")
        self.gDomain: GroundedDomain = self.domain.ground(self.problem, avoidSimplification=True)

        self.trace: Trace = Trace.fromPatty(f"{folder}/plans/{problem}.txt", self.gDomain)

        self.ics: InitialConditionSpace = InitialConditionSpace(self.trace, self.problem, self.gDomain)

        pass

    def test_check(self):
        self.assertIsInstance(self.domain, Domain)
        self.assertIsInstance(self.problem, Problem)
        self.assertIsInstance(self.gDomain, GroundedDomain)

    def test_solve(self):
        icr = InitialConditionRetriever(self.ics)
        init: InitialCondition = icr.solve()

        finalState: State = self.trace.apply(init)

        self.assertTrue(finalState.satisfies(self.problem.goal))


if __name__ == '__main__':
    unittest.main()
