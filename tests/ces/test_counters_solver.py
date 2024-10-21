import unittest
from typing import Dict
from unittest import TestCase

from src.ces.ActionStateTransitionFunction import ActionStateTransitionFunction
from src.ces.TransitiveClosure import TransitiveClosure
from src.pddl.Action import Action
from src.pddl.Atom import Atom
from src.pddl.Domain import Domain, GroundedDomain
from src.pddl.Problem import Problem
from src.search.TransitiveClosureSolver import TransitiveClosureSolver
from src.utils.Arguments import Arguments


class TestCES(TestCase):

    def setUp(self) -> None:
        self.b = 4
        self.domain: Domain = Domain.fromFile(f"../../files/ces/counters/domains/{self.b}/domain-{self.b}.pddl")
        self.problem: Problem = Problem.fromFile(
            f"../../files/ces/counters/domains/{self.b}/instances/problem-{self.b}-3.pddl")
        self.gDomain: GroundedDomain = self.domain.ground(self.problem)
        self.args = Arguments(keepRequired=False)

    def test_solver(self):
        tcs = TransitiveClosureSolver(self.domain, self.problem, self.gDomain, self.args)


if __name__ == '__main__':
    unittest.main()
