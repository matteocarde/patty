import copy

from src.pddl.Domain import GroundedDomain
from src.pddl.NumericPlan import NumericPlan
from src.pddl.Plan import Plan
from src.pddl.Problem import Problem
from src.pddl.State import State
from src.plan.NumericEncoding import NumericEncoding
from src.plan.Pattern import Pattern
from src.plan.TemporalEncoding import TemporalEncoding
from src.search.Search import Search
from src.smt.SMTSolver import SMTSolver
from src.utils.Arguments import Arguments
from src.utils.LogPrint import LogPrintLevel


class AStarSearchMax(Search):

    def __init__(self, domain: GroundedDomain, problem: Problem, args: Arguments):
        self.useSCCs = args.useSCCs
        super().__init__(domain, problem, args)

    def solve(self) -> Plan:
        callsToSolver = 0

        totalSubgoals = self.problem.goal.conditions
        subgoalsAchieved = set()

        bound = self.startBound
        initialState: State = State.fromInitialCondition(self.problem.init)
        s: State = initialState

        patG: Pattern = Pattern.fromOrder([], addFake=not self.isTemporal)
        patH: Pattern = Pattern.fromState(s, self.problem.goal, self.domain, useSCCs=self.useSCCs,
                                          addFake=not self.isTemporal)

        while bound <= self.maxBound:

            patF: Pattern = copy.deepcopy(patG + patH)

            if self.args.printPattern:
                self.console.log("Pattern: " + str(patF), LogPrintLevel.PLAN)

            self.ts.start(f"Conversion to SMT at bound {bound}", console=self.console)
            if self.isTemporal:
                encoding: TemporalEncoding = TemporalEncoding(
                    domain=self.domain,
                    problem=self.problem,
                    pattern=patF,
                    relaxGoal=True,
                    subgoalsAchieved=subgoalsAchieved,
                    constraints=self.args.temporalConstraints,
                    bound=1)
            else:
                encoding: NumericEncoding = NumericEncoding(
                    domain=self.domain,
                    problem=self.problem,
                    pattern=patF,
                    bound=1,
                    relaxGoal=True,
                    subgoalsAchieved=subgoalsAchieved,
                    encoding=self.args.encoding,
                    rollBound=self.args.rollBound,
                    hasEffectAxioms=self.args.hasEffectAxioms
                )
            self.ts.end(f"Conversion to SMT at bound {bound}", console=self.console)
            self.console.log(f"Bound {bound} - Vars = {encoding.getNVars()}", LogPrintLevel.STATS)
            self.console.log(f"Bound {bound} - Rules = {encoding.getNRules()}", LogPrintLevel.STATS)

            self.ts.start(f"Solving Bound {bound}", console=self.console)
            solver: SMTSolver = SMTSolver(encoding, maximize=True)
            callsToSolver += 1
            plan: Plan = solver.solve()
            solver.exit()
            self.ts.end(f"Solving Bound {bound}", console=self.console)

            if self.args.printPartialPlan and plan:
                print("--Partial Plan---")
                print(plan)
                print("-----------------")

            if self.args.saveSMT:
                self.saveSMT(bound, encoding, callsToSolver=callsToSolver)

            subgoalsAchievedNow = set()
            state = None
            if isinstance(plan, Plan):
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
                patG = Pattern.fromPlan(plan, addFake=not self.isTemporal) if not self.args.noCompression else patF
                patG.addPostfix("G")
                patH = Pattern.fromState(state, self.problem.goal, self.domain, useSCCs=self.useSCCs,
                                         addFake=not self.isTemporal)
            else:
                patF.addPostfix(bound)
                patG = patF

            bound = bound + 1
        pass
