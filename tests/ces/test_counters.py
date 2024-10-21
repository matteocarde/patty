import unittest
from typing import Dict
from unittest import TestCase

from src.ces.ActionStateTransitionFunction import ActionStateTransitionFunction
from src.ces.TransitiveClosure import TransitiveClosure
from src.pddl.Action import Action
from src.pddl.Atom import Atom
from src.pddl.Domain import Domain, GroundedDomain
from src.pddl.Problem import Problem


class TestCES(TestCase):

    def setUp(self) -> None:
        self.b = 9
        self.domain: Domain = Domain.fromFile(f"../../files/ces/counter/domains/{self.b}/domain-{self.b}.pddl")
        self.problem: Problem = Problem.fromFile(f"../../files/ces/counter/domains/{self.b}/problem-{self.b}.pddl")
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
        v: Dict[str, Atom] = dict()
        for atom in tFunc.atoms:
            v[atom.name] = atom
        atomsOrder = [v["ok"]]
        for i in reversed(range(1, self.b + 1)):
            atomsOrder += [v[f"x{i}"]]
        # atomsOrder = [v[f"x{i}"] for i in reversed(range(1, self.b + 1))] + \
        #              [v[f"l{i}"] for i in reversed(range(1, self.b + 1))]
        tc = TransitiveClosure.fromActionStateTransitionFunction(tFunc, atomsOrder)
        self.assertIsInstance(tc, TransitiveClosure)


if __name__ == '__main__':
    unittest.main()
