import unittest
from typing import Dict
from unittest import TestCase

from src.ces.ActionStateTransitionFunction import ActionStateTransitionFunction
from src.pddl.Action import Action
from src.pddl.Domain import Domain, GroundedDomain
from src.pddl.Problem import Problem
from src.smt.SMTBoolVariable import SMTBoolVariable


class TestCES(TestCase):

    def setUp(self) -> None:
        self.domain: Domain = Domain.fromFile("../../files/ces/counter/domains/2/domain-2.pddl")
        self.problem: Problem = Problem.fromFile("../../files/ces/counter/domains/2/problem-2.pddl")
        self.gDomain: GroundedDomain = self.domain.ground(self.problem)
        self.transFunctions: Dict[Action, ActionStateTransitionFunction] = dict()
        self.current = dict([(v, SMTBoolVariable(f"{v}")) for v in self.gDomain.predicates])
        self.next = dict([(v, SMTBoolVariable(f"{v}'")) for v in self.gDomain.predicates])
        for action in self.gDomain.actions:
            self.transFunctions[action] = ActionStateTransitionFunction(action, self.current, self.next)
        pass

    def test_transform(self):
        self.assertIsInstance(self.gDomain, GroundedDomain)
        self.assertEqual(len(self.gDomain.actions), 5)
        self.assertEqual(len(self.transFunctions.items()), 5)

    def test_bdd(self):
        tFunc = self.transFunctions[list(self.gDomain.actions)[0]]
        tFunc.toBDD()
        pass


if __name__ == '__main__':
    unittest.main()
