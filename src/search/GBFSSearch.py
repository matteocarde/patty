import copy

from src.pddl.Domain import GroundedDomain
from src.pddl.NumericPlan import NumericPlan
from src.pddl.Problem import Problem
from src.pddl.State import State
from src.plan.NumericEncoding import NumericEncoding
from src.plan.Pattern import Pattern
from src.search.Search import Search
from src.smt.SMTSolver import SMTSolver
from src.utils.Arguments import Arguments
from src.utils.LogPrint import LogPrintLevel


class GBFSSearch(Search):

    def __init__(self, domain: GroundedDomain, problem: Problem, args: Arguments, maximize=False, avoidP=False):
        self.maximize = maximize
        self.avoidP = avoidP
        super().__init__(domain, problem, args)

    def solve(self) -> NumericPlan:

        callsToSolver = 0
        totalSubgoals = self.problem.goal.conditions
        subgoalsAchieved = set()
        bound = self.startBound
        initialState: State = State.fromInitialCondition(self.problem.init)
        s: State = initialState
        sprime: State = copy.deepcopy(s)
        patH: Pattern = Pattern.fromState(s, self.problem.goal, self.domain)
        patH.addPostfix(0)
        patHPrime: Pattern = copy.deepcopy(patH)

        while bound <= self.maxBound:

            if self.args.printPattern:
                self.console.log("Pattern: " + str(patH), LogPrintLevel.PLAN)

            self.ts.start(f"Conversion to SMT at bound {bound}", console=self.console)
            pddl2smt: NumericEncoding = NumericEncoding(
                domain=self.domain,
                problem=self.problem,
                pattern=patH,
                bound=1,
                relaxGoal=True,
                subgoalsAchieved=subgoalsAchieved if not self.avoidP else set(),
                encoding=self.args.encoding,
                binaryActions=self.args.binaryActions,
                rollBound=self.args.rollBound,
                hasEffectAxioms=self.args.hasEffectAxioms
            )
            self.ts.end(f"Conversion to SMT at bound {bound}", console=self.console)

            self.ts.start(f"Solving Bound {bound}", console=self.console)
            solver: SMTSolver = SMTSolver(pddl2smt, maximize=self.maximize)
            callsToSolver += 1
            plan: NumericPlan = solver.solve()
            solver.exit()
            self.ts.end(f"Solving Bound {bound}", console=self.console)

            self.console.log(f"Bound {bound} - Vars = {pddl2smt.getNVars()}", LogPrintLevel.STATS)
            self.console.log(f"Bound {bound} - Rules = {pddl2smt.getNRules()}", LogPrintLevel.STATS)

            if self.args.saveSMT:
                self.saveSMT(bound, pddl2smt)

            if isinstance(plan, NumericPlan):
                # IF SAT
                sprime = initialState.applyPlan(plan)
                subgoalsAchieved = {g for g in self.problem.goal.conditions if sprime.satisfies(g)}
                self.console.log(f"Subgoals achieved: {len(subgoalsAchieved)}/{len(totalSubgoals)}",
                                 LogPrintLevel.STATS)
                if len(subgoalsAchieved) == len(self.problem.goal.conditions):
                    self.console.log(f"Calls to Solver: {callsToSolver}", LogPrintLevel.STATS)
                    self.console.log(f"Bound: {bound}", LogPrintLevel.STATS)
                    return plan
                pass

            if not isinstance(plan, NumericPlan) or self.maximize:
                if s != sprime:
                    newPat = Pattern.fromState(sprime, self.problem.goal, self.domain)
                    if newPat:
                        patHPrime = newPat
                        sprime = s
                bound += 1
                patHPrime.addPostfix(bound)
                patH += patHPrime

        pass
