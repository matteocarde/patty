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
        self.b = 5
        self.domain: Domain = Domain.fromFile(f"../../files/ces/counters/domains/{self.b}/domain-{self.b}.pddl")
        self.problem: Problem = Problem.fromFile(
            f"../../files/ces/counters/domains/{self.b}/instances/problem-{self.b}-5.pddl")
        self.gDomain: GroundedDomain = self.domain.ground(self.problem)
        self.transFunctions: Dict[Action, ActionStateTransitionFunction] = dict()
        self.name2Action: Dict[str, Action] = dict()
        for action in self.domain.actions:
            self.name2Action[action.name] = action
            self.transFunctions[action] = ActionStateTransitionFunction(action)
        pass

    def test_bdd(self):
        action = self.name2Action["incr"]
        tFunc = self.transFunctions[action]
        print("Starting computing Transitive Closure")
        v: Dict[str, Atom] = dict()
        for atom in tFunc.atoms:
            v[atom.name] = atom
        atomsOrder = [v["z"]]
        for i in reversed(range(1, self.b + 1)):
            atomsOrder += [v[f"x0{i}"]]
        bdds = TransitiveClosure.fromActionStateTransitionFunction(tFunc, atomsOrder)
        self.assertEqual(len(bdds), self.b + 1)


if __name__ == '__main__':
    unittest.main()
