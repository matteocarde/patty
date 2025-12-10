import unittest
from unittest import TestCase

from src.ices.ICEEncoding import ICEEncoding
from src.ices.ICEPattern import ICEPattern
from src.ices.ICEPlan import ICEPlan
from src.ices.ICETask import ICETask
from src.pddl.Domain import Domain, GroundedDomain
from src.pddl.Plan import Plan
from src.pddl.Problem import Problem
from src.pddl.TemporalPlan import TemporalPlan
from src.plan.Pattern import Pattern
from src.plan.TemporalEncoding import TemporalEncoding
from src.search.AStarSearchMax import AStarSearchMax
from src.smt.SMTSolution import SMTSolution
from src.smt.SMTSolver import SMTSolver
from src.utils.Arguments import Arguments


class TestPack(TestCase):

    def setUp(self) -> None:
        folder = "../../files/temporal/bottles-pack/"
        problem = "instances/problem_2"
        self.domain: Domain = Domain.fromFile(f"{folder}/domain.pddl")
        self.problem: Problem = Problem.fromFile(f"{folder}/{problem}.pddl")
        self.gDomain: GroundedDomain = self.domain.ground(self.problem)
        self.args = Arguments(keepRequired=False)
        self.args.printPattern = True
        # print(self.pattern)
        # self.encoding.printRules()

        task: ICETask = ICETask.fromTemporalNoICEs(self.gDomain, self.problem)

        pattern = ICEPattern.fromSnap(task)
        pattern.print()
        bound = 4

        if bound > 1:
            pattern = pattern.multiply(bound)

        self.encoding: ICEEncoding = ICEEncoding(task, pattern)

        solver: SMTSolver = SMTSolver(self.encoding)

        self.solution = solver.getSolution()

        pass

    def test_is_solution(self):
        self.assertTrue(self.solution)

        pass

    def test_is_valid_solution(self):
        if not self.solution:
            self.assertTrue(False)
            return

        plan: ICEPlan = ICEPlan.fromSMTSolution(self.encoding, self.solution)

        plan.print()

        print(f"Plan is {'valid' if plan.isValid() else 'invalid'}")

        self.assertTrue(plan.isValid())


if __name__ == '__main__':
    unittest.main()
