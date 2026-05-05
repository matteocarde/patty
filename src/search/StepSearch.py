from typing import Tuple

from src.pddl.Domain import GroundedDomain
from src.pddl.NumericPlan import NumericPlan
from src.pddl.Problem import Problem
from src.pddl.State import State
from src.plan.NumericEncoding import NumericEncoding
from src.plan.Pattern import Pattern
from src.search.Search import Search
from src.smt.SMTSolution import SMTSolution
from src.smt.SMTSolver import SMTSolver
from src.utils.Arguments import Arguments
from src.utils.LogPrint import LogPrintLevel, console


class StepSearch(Search):

    def __init__(self, domain: GroundedDomain, problem: Problem, args: Arguments):
        super().__init__(domain, problem, args)

    def getPattern(self) -> Pattern:
        if self.args.pattern == "arpg":
            return Pattern.fromARPG(self.domain)
        if self.args.pattern == "enhanced":
            return Pattern.fromARPGEnhanced(self.domain)
        if self.args.pattern == "random":
            return Pattern.fromRandom(self.domain)

        raise Exception(f"Pattern generation method '{self.args.pattern}' unknown")

    def solve(self) -> NumericPlan:
        callsToSolver = 0
        pattern: Pattern = self.getPattern()
        subgoalsAchieved = set()
        totalSubgoals = self.problem.goal.conditions

        initialState: State = State.fromInitialCondition(self.problem.init)

        if self.args.printPattern:
            console.log("Pattern: " + str(pattern), LogPrintLevel.STATS)

        if self.args.printARPG:
            console.log(str(self.domain.arpg), LogPrintLevel.STATS)

        bound = self.startBound

        while bound <= self.maxBound:

            self.ts.start(f"Conversion to SMT at bound {bound}")
            encoding: NumericEncoding = NumericEncoding(
                domain=self.domain,
                problem=self.problem,
                pattern=pattern,
                bound=bound,
                args=self.args
            )
            self.ts.end(f"Conversion to SMT at bound {bound}")

            self.ts.start(f"Solving Bound {bound}")
            solver: SMTSolver = SMTSolver(encoding)

            plan: NumericPlan
            solution = solver.getSolution()
            callsToSolver += 1
            solver.exit()
            self.ts.end(f"Solving Bound {bound}")

            console.log(f"Bound {bound} - Vars = {encoding.getNVars()}", LogPrintLevel.STATS)
            console.log(f"Bound {bound} - Rules = {encoding.getNRules()}", LogPrintLevel.STATS)
            console.log(f"Bound {bound} - Avg Rule Length = {encoding.getAvgRuleLength()}", LogPrintLevel.STATS)
            console.log(f"Bound {bound} - Pattern Length = {pattern.getLength()}", LogPrintLevel.STATS)
            console.log(f"Calls to Solver: {callsToSolver}", LogPrintLevel.STATS)

            if self.args.saveSMT:
                self.saveSMT(bound, encoding)

            if solution:
                plan = encoding.getPlanFromSolution(solution)
                state = initialState.applyPlan(plan)
                subgoalsAchieved = {g for g in self.problem.goal.conditions if state.satisfies(g)}
                if len(subgoalsAchieved) == len(totalSubgoals):
                    console.log(f"Bound: {bound}", LogPrintLevel.STATS)
                    self.finalBound = bound
                    self.finalPattern = pattern
                    return plan

            console.log(f"NO SOLUTION: No solution with bound {bound}. Try to increase the bound",
                             LogPrintLevel.PLAN)

            bound += 1

        pass
