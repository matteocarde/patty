import unittest
from unittest import TestCase

from Domain import Domain, GroundedDomain
from NumericPlan import NumericPlan
from PDDLException import PDDLException
from Problem import Problem
from classes.plan.PDDL2SMT import PDDL2SMT
from classes.smt.SMTSolution import SMTSolution
from classes.smt.SMTSolver import SMTSolver


class TestPaper(TestCase):

    def setUp(self) -> None:
        self.domain: Domain = Domain.fromFile("../files/paper-example/domain.pddl")
        self.problem: Problem = Problem.fromFile("../files/paper-example/problem.pddl")
        self.unreachable: Problem = Problem.fromFile("../files/paper-example/unreachable.pddl")
        self.gDomain: GroundedDomain = self.domain.ground(self.problem)
        self.horizon = 2
        self.pddl2smt: PDDL2SMT = PDDL2SMT(self.gDomain, self.problem, self.horizon)
        pass

    def test_transform(self):
        self.assertGreater(len(self.pddl2smt.initial), 0)
        self.assertGreater(len(self.pddl2smt.transitions), 0)
        self.assertGreater(len(self.pddl2smt.rules), 0)

    def test_solve(self):
        solver: SMTSolver = SMTSolver()
        solver.addAssertions(self.pddl2smt.rules)

        print(self.pddl2smt.order)
        self.pddl2smt.printRules()

        solution: SMTSolution = solver.solve()
        print(solution)
        self.assertIsInstance(solution, SMTSolution)

        plan: NumericPlan = self.pddl2smt.getPlanFromSolution(solution)
        print("No repetitions:")
        plan.print()
        print("With repetitions:")
        plan.printWithRepetitions()

        self.assertTrue(plan.validate(self.problem))

    def test_unreach(self):
        raised = False
        try:
            PDDL2SMT(self.gDomain, self.unreachable, self.horizon)
        except PDDLException.GoalNotReachable:
            raised = True

        self.assertTrue(raised)


if __name__ == '__main__':
    unittest.main()
