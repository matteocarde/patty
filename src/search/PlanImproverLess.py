import copy
from typing import Tuple

from src.pddl.Domain import GroundedDomain
from src.pddl.NumericPlan import NumericPlan
from src.pddl.Plan import Plan
from src.pddl.Problem import Problem
from src.pddl.State import State
from src.plan.NumericEncoding import NumericEncoding
from src.plan.Pattern import Pattern
from src.search.Search import Search
from src.smt.SMTSolution import SMTSolution
from src.smt.SMTSolver import SMTSolver
from src.utils.Arguments import Arguments
from src.utils.LogPrint import LogPrintLevel


class PlanImproverLess(Search):
    satPlan: NumericPlan

    def __init__(self, domain: GroundedDomain, problem: Problem, args: Arguments,
                 satPlan: NumericPlan, pattern: Pattern, bound: int):
        super().__init__(domain, problem, args)
        self.satPlan = satPlan
        self.pattern = pattern
        self.bound = bound

    def solve(self) -> NumericPlan or None:

        encoding: NumericEncoding = NumericEncoding(
            domain=self.domain,
            problem=self.problem,
            pattern=self.pattern,
            bound=self.bound,
            args=self.args,
            minimizeQuality=True,
            maxActionsRolling=self.satPlan.actionRolling
        )

        solver: SMTSolver = SMTSolver(encoding)
        plan: NumericPlan = solver.solve()
        solver.exit()

        if isinstance(plan, NumericPlan):
            print(f"The plan has been improved.")
            return plan
        else:
            print("The plan couldn't been improved")
            return None

        pass
