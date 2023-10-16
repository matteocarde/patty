import copy

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


class AStarSearchMax(Search):

    def __init__(self, domain: GroundedDomain, problem: Problem, args: Arguments, maximize=False, avoidP=False,
                 useSCCs=False):
        self.maximize = maximize
        self.avoidP = avoidP
        self.useSCCs = useSCCs
        super().__init__(domain, problem, args)

    def solve(self) -> NumericPlan:
        callsToSolver = 0

        totalSubgoals = self.problem.goal.conditions
        subgoalsAchieved = set()

        bound = self.startBound
        initialState: State = State.fromInitialCondition(self.problem.init)
        s: State = initialState

        patG: Pattern = Pattern.fromOrder([])
        patH: Pattern = Pattern.fromState(s, self.problem.goal, self.domain, useSCCs=self.useSCCs)

        while bound <= self.maxBound:

            patF: Pattern = copy.deepcopy(patG + patH)

            if self.args.printPattern:
                self.console.log("Pattern: " + str(patF), LogPrintLevel.PLAN)

            self.ts.start(f"Conversion to SMT at bound {bound}", console=self.console)
            pddl2smt: PDDL2SMT = PDDL2SMT(
                domain=self.domain,
                problem=self.problem,
                pattern=patF,
                bound=1,
                relaxGoal=True,
                subgoalsAchieved=set(),
                encoding=self.args.encoding,
                binaryActions=self.args.binaryActions,
                rollBound=self.args.rollBound,
                hasEffectAxioms=self.args.hasEffectAxioms
            )
            self.ts.end(f"Conversion to SMT at bound {bound}", console=self.console)

            self.ts.start(f"Solving Bound {bound}", console=self.console)
            solver: SMTSolver = SMTSolver(pddl2smt, maximize=True)
            callsToSolver += 1
            plan: NumericPlan = solver.solve()
            solver.exit()
            self.ts.end(f"Solving Bound {bound}", console=self.console)
            self.console.log(f"Bound {bound} - Vars = {pddl2smt.getNVars()}", LogPrintLevel.STATS)
            self.console.log(f"Bound {bound} - Rules = {pddl2smt.getNRules()}", LogPrintLevel.STATS)

            if self.args.saveSMT:
                self.saveSMT(bound, pddl2smt, callsToSolver=callsToSolver)

            subgoalsAchievedNow = set()
            state = None
            if isinstance(plan, NumericPlan):
                state = initialState.applyPlan(plan)
                subgoalsAchievedNow = {g for g in self.problem.goal.conditions if state.satisfies(g)}

            if len(subgoalsAchievedNow) == len(totalSubgoals):
                self.console.log(f"Calls to Solver: {callsToSolver}", LogPrintLevel.STATS)
                self.console.log(f"Bound: {bound}", LogPrintLevel.STATS)
                return plan

            if len(subgoalsAchievedNow) > len(subgoalsAchieved):
                subgoalsAchieved = subgoalsAchievedNow
                self.console.log(f"Subgoals achieved: {len(subgoalsAchieved)}/{len(totalSubgoals)}: {subgoalsAchieved}",
                                 LogPrintLevel.STATS)
                patG = Pattern.fromPlan(plan)
                patG.addPostfix("G")
                patH = Pattern.fromState(state, self.problem.goal, self.domain, useSCCs=self.useSCCs)
            else:
                patF.addPostfix(bound)
                patG = patF

            bound = bound + 1
        pass
