from src.pddl.Domain import GroundedDomain
from src.pddl.NumericPlan import NumericPlan
from src.pddl.Problem import Problem
from src.pddl.State import State
from src.plan.PDDL2SMT import PDDL2SMT
from src.plan.Pattern import Pattern
from src.search.Search import Search
from src.smt.SMTSolver import SMTSolver
from src.utils.Arguments import Arguments
from src.utils.LogPrint import LogPrintLevel


class StepSearch(Search):

    def __init__(self, domain: GroundedDomain, problem: Problem, args: Arguments):
        self.useSCCs = args.useSCCs
        super().__init__(domain, problem, args)

    def getPattern(self) -> Pattern:
        if self.args.pattern == "arpg":
            return Pattern.fromARPG(self.domain, useSCCs=self.useSCCs)
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
            self.console.log("Pattern: " + str(pattern), LogPrintLevel.PLAN)

        if self.args.printARPG:
            self.console.log(str(self.domain.arpg), LogPrintLevel.PLAN)

        bound = self.startBound

        while bound <= self.maxBound:

            self.ts.start(f"Conversion to SMT at bound {bound}", console=self.console)
            pddl2smt: PDDL2SMT = PDDL2SMT(
                domain=self.domain,
                problem=self.problem,
                pattern=pattern,
                bound=bound,
                relaxGoal=self.args.maximize,
                subgoalsAchieved=set() if self.args.maximize else None,
                encoding=self.args.encoding,
                binaryActions=self.args.binaryActions,
                rollBound=self.args.rollBound,
                hasEffectAxioms=self.args.hasEffectAxioms
            )
            self.ts.end(f"Conversion to SMT at bound {bound}", console=self.console)

            self.ts.start(f"Solving Bound {bound}", console=self.console)
            solver: SMTSolver = SMTSolver(pddl2smt, maximize=self.args.maximize)

            plan: NumericPlan
            plan = solver.solve()
            callsToSolver += 1
            solver.exit()
            self.ts.end(f"Solving Bound {bound}", console=self.console)

            self.console.log(f"Bound {bound} - Vars = {pddl2smt.getNVars()}", LogPrintLevel.STATS)
            self.console.log(f"Bound {bound} - Rules = {pddl2smt.getNRules()}", LogPrintLevel.STATS)
            self.console.log(f"Calls to Solver: {callsToSolver}", LogPrintLevel.STATS)

            if self.args.saveSMT:
                self.saveSMT(bound, pddl2smt)

            if isinstance(plan, NumericPlan):
                state = initialState.applyPlan(plan)
                subgoalsAchieved = {g for g in self.problem.goal.conditions if state.satisfies(g)}
                if len(subgoalsAchieved) == len(totalSubgoals):
                    self.console.log(f"Bound: {bound}", LogPrintLevel.STATS)
                    return plan

            self.console.log(f"NO SOLUTION: No solution with bound {bound}. Try to increase the bound",
                             LogPrintLevel.PLAN)

            bound += 1

        pass
