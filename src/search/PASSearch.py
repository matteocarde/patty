from typing import Tuple

from src.pddl.Domain import GroundedDomain
from src.pddl.NumericPlan import NumericPlan
from src.pddl.Plan import Plan
from src.pddl.Problem import Problem
from src.pddl.State import State
from src.plan.CESPASEncoding import CESPASEncoding
from src.plan.NumericEncoding import NumericEncoding
from src.plan.Pattern import Pattern
from src.plan.TransitionRelations import TransitionRelations
from src.search.Search import Search
from src.smt.SMTSolution import SMTSolution
from src.smt.SMTSolver import SMTSolver
from src.utils.Arguments import Arguments
from src.utils.LogPrint import LogPrintLevel


class PASSearch(Search):

    def __init__(self, domain: GroundedDomain, problem: Problem, args: Arguments):
        super().__init__(domain, problem, args)
        self.isCES = self.domain.hasConditionalEffects()

    def solve(self) -> NumericPlan:
        callsToSolver = 0

        bound = self.startBound

        relations = None
        if self.isCES:
            self.ts.start(f"Computing Transitive Closure", console=self.console)
            relations = TransitionRelations(self.liftedDomain, self.args.maxClosureTime)
            self.ts.end(f"Computing Transitive Closure", console=self.console)

        while bound <= self.maxBound:

            self.ts.start(f"Conversion to SMT at bound {bound}", console=self.console)
            if self.isCES:
                encoding: CESPASEncoding = CESPASEncoding(
                    domain=self.domain,
                    problem=self.problem,
                    liftedDomain=self.liftedDomain,
                    transitionRelations=relations,
                    bound=bound
                )
            else:
                raise Exception("In a PAS encoding I can only deal with CEs")
            self.ts.end(f"Conversion to SMT at bound {bound}", console=self.console)

            self.ts.start(f"Solving Bound {bound}", console=self.console)
            solver: SMTSolver = SMTSolver(encoding)

            solver: SMTSolver = SMTSolver(encoding)
            self.ts.end(f"Conversion to SMT at bound {bound}", console=self.console)

            self.console.log(f"Bound {bound} - Vars = {encoding.getNVars()}", LogPrintLevel.STATS)
            self.console.log(f"Bound {bound} - Rules = {encoding.getNRules()}", LogPrintLevel.STATS)
            self.console.log(f"Bound {bound} - Avg Rule Length = {encoding.getAvgRuleLength()}", LogPrintLevel.STATS)
            self.console.log(f"Calls to Solver: {callsToSolver}", LogPrintLevel.STATS)
            self.ts.start(f"Solving Bound {bound}", console=self.console)

            plan: Plan
            plan = solver.solve()
            callsToSolver += 1
            solver.exit()
            self.ts.end(f"Solving Bound {bound}", console=self.console)

            if self.args.saveSMT:
                self.saveSMT(bound, encoding)

            if isinstance(plan, NumericPlan):
                self.console.log(f"Bound: {bound}", LogPrintLevel.STATS)
                return plan

            self.console.log(f"NO SOLUTION: No solution with bound {bound}. Try to increase the bound",
                             LogPrintLevel.PLAN)

            bound += 1

        pass
