import unittest
from typing import Dict
from unittest import TestCase

from src.ces.ActionStateTransitionFunction import ActionStateTransitionFunction
from src.ces.TransitionFunctionBDD import TransitionFunctionBDD
from src.ces.TransitiveClosure import TransitiveClosure
from src.pddl.Action import Action
from src.pddl.Domain import Domain, GroundedDomain
from src.pddl.Problem import Problem
from src.smt.SMTBoolVariable import SMTBoolVariable


class TestCES(TestCase):

    def setUp(self) -> None:
        self.domain: Domain = Domain.fromFile("../../files/ces/counter/domains/4/domain-4.pddl")
        self.problem: Problem = Problem.fromFile("../../files/ces/counter/domains/4/problem-4.pddl")
        self.gDomain: GroundedDomain = self.domain.ground(self.problem)
        self.transFunctions: Dict[Action, ActionStateTransitionFunction] = dict()
        self.name2Action: Dict[str, Action] = dict()
        for action in self.gDomain.actions:
            self.name2Action[action.name] = action
            self.transFunctions[action] = ActionStateTransitionFunction(action)
        pass

    def test_transform(self):
        self.assertIsInstance(self.gDomain, GroundedDomain)
        self.assertEqual(len(self.gDomain.actions), 5)
        self.assertEqual(len(self.transFunctions.items()), 5)

    def test_bdd(self):
        action = self.name2Action["inx"]
        tFunc = self.transFunctions[action]
        print("Starting computing Transitive Closure")
        tc = TransitiveClosure.fromActionStateTransitionFunction(tFunc)
        self.assertIsInstance(tc, TransitiveClosure)


if __name__ == '__main__':
    unittest.main()
