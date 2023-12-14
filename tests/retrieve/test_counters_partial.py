import unittest
from unittest import TestCase

from src.pddl.Domain import Domain, GroundedDomain
from src.pddl.InitialCondition import InitialCondition
from src.pddl.Problem import Problem
from src.pddl.State import State
from src.pddl.Trace import Trace
from src.retrieve.InitialConditionRetriever import InitialConditionRetriever
from src.retrieve.InitialConditionSpace import InitialConditionSpace


class TestCountersPartial(TestCase):

    def setUp(self) -> None:
        folder = "../../files/numeric/ipc-2023/counters/"
        problem = "rnd_instance_4_1"
        self.domain: Domain = Domain.fromFile(f"{folder}/domain.pddl")
        self.problem: Problem = Problem.fromFile(f"{folder}/partial/{problem}/100.pddl")
        self.gDomain: GroundedDomain = self.domain.ground(self.problem, avoidSimplification=True)

        self.trace: Trace = Trace.fromENHSP(f"{folder}/plans/{problem}.pddl.txt", self.gDomain)

        self.ics: InitialConditionSpace = InitialConditionSpace(self.trace, self.problem, self.gDomain)

        pass

    def test_solve(self):
        self.assertTrue(self.ics.checkInitialCondition(self.problem.init))
        icr = InitialConditionRetriever(self.ics, self.problem.init)
        init, obj = icr.solve()

        finalState: State = self.trace.apply(init)

        self.assertTrue(finalState.satisfies(self.problem.goal, tolerance=0.1))


if __name__ == '__main__':
    unittest.main()
