from unittest import TestCase

import unittest

from Domain import Domain, GroundedDomain
from NumericPlan import NumericPlan
from Problem import Problem
from classes.plan.PDDL2SMT import PDDL2SMT
from classes.plan.Pattern import Pattern
from classes.smt.SMTSolver import SMTSolver


class TestPattern(TestCase):

    def setUp(self) -> None:
        self.domain: Domain = Domain.fromFile("../files/blockworld/domain.pddl")
        self.problem: Problem = Problem.fromFile("../files/blockworld/instances/pb3.pddl")
        self.gDomain: GroundedDomain = self.domain.ground(self.problem)
        self.pattern: Pattern = Pattern.fromPlanningTask(self.gDomain, self.problem)
        pass

    def test_partial_order(self):
        self.assertGreater(len(self.pattern.getPartialOrder()), 0)
        for poset in self.pattern.getPartialOrder():
            print(poset)

    def test_plan(self):
        horizon = 2
        pddl2smt: PDDL2SMT = PDDL2SMT(self.gDomain, self.problem, horizon)
        solver: SMTSolver = SMTSolver(pddl2smt)

        print("ORDER", pddl2smt.order)

        solution = solver.getSolution()
        solver.exit()
        plan: NumericPlan = pddl2smt.getPlanFromSolution(solution)
        print(plan)


if __name__ == '__main__':
    unittest.main()
