import unittest
from unittest import TestCase

from src.pddl.Domain import Domain, GroundedDomain
from src.pddl.NumericPlan import NumericPlan
from src.pddl.PDDLException import PDDLException
from src.pddl.Problem import Problem
from src.plan.PDDL2SMT import PDDL2SMT
from src.plan.Pattern import Pattern
from src.smt.SMTSolver import SMTSolver


class TestPaper(TestCase):

    def setUp(self) -> None:
        self.domain: Domain = Domain.fromFile("../../files/paper-example/domain.pddl")
        self.problem: Problem = Problem.fromFile("../../files/paper-example/problem.pddl")
        self.unreachable: Problem = Problem.fromFile("../../files/paper-example/unreachable.pddl")
        self.gDomain: GroundedDomain = self.domain.ground(self.problem)
        self.horizon = 2
        self.pattern = Pattern.fromOrder(self.gDomain.arpg.getActionsOrder())
        self.pddl2smt: PDDL2SMT = PDDL2SMT(self.gDomain, self.problem, self.pattern, self.horizon)
        pass

    def test_transform(self):
        self.assertGreater(len(self.pddl2smt.initial), 0)
        self.assertGreater(len(self.pddl2smt.transitions), 0)
        self.assertGreater(len(self.pddl2smt.rules), 0)

    def test_solve(self):
        solver: SMTSolver = SMTSolver(self.pddl2smt)

        print(self.pddl2smt.pattern)
        self.pddl2smt.printRules()

        plan: NumericPlan = solver.solve()
        solver.exit()
        print(plan)
        self.assertIsInstance(plan, NumericPlan)

        print("No repetitions:")
        plan.print()
        print("With repetitions:")
        plan.printWithRepetitions()

        self.assertTrue(plan.validate(self.problem))

    def test_unreach(self):
        raised = False
        try:
            gUnreachDomain = self.domain.ground(self.unreachable)
            PDDL2SMT(gUnreachDomain, self.unreachable, self.horizon)
        except PDDLException.GoalNotReachable:
            raised = True

        self.assertTrue(raised)


if __name__ == '__main__':
    unittest.main()
