import copy
import datetime
from typing import Type

from src.goalFunctions.GoalFunction import GoalFunction
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


class GDSearch(Search):

    def __init__(self, domain: GroundedDomain, problem: Problem, args: Arguments):
        super().__init__(domain, problem, args)
        self.enhanced = self.args.pattern == "enhanced"

    def solve(self) -> Plan:

        bound = 0
        callsToSolver = 0

        initialState: State = State.fromInitialCondition(self.problem.init)
        s: State = initialState

        pat: Pattern = Pattern.empty()
        plan: NumericPlan = NumericPlan.empty()
        GF: Type[GoalFunction] = GoalFunction.getGoalFunctionFromString(self.args.goalFunction)
        normalizedGoal = self.problem.goal.normalize()
        GF.assertGoalIsRightForm(normalizedGoal)
        c = GF.compute(s, normalizedGoal, initialState)
        patS: Pattern = Pattern.fromState(s, self.problem.goal, self.domain).addPostfix("I")

        self.console.log(f"Goal Function Value: {c}", LogPrintLevel.PLAN)

        while bound <= self.maxBound:

            pat: Pattern = copy.deepcopy(pat + patS)

            if self.args.printPattern:
                self.console.log("Pattern: " + str(pat), LogPrintLevel.PLAN)

            self.ts.start(f"Conversion to SMT at bound {bound}", console=self.console)
            encoding: NumericEncoding = NumericEncoding(
                domain=self.domain,
                problem=self.problem,
                state=s,
                pattern=pat,
                goalFunction=GF,
                minimizeGoalFunction=self.args.minimizeGoalFunction,
                goalFunctionWithEpsilon=not self.args.noCompression,
                goalFunctionValue=c,
                goalAsSoftAssert=False,
                bound=1,
                args=self.args,
                relaxGoal=False
            )

            self.ts.end(f"Conversion to SMT at bound {bound}", console=self.console)
            self.console.log(f"Bound {bound} - Vars = {encoding.getNVars()}", LogPrintLevel.STATS)
            self.console.log(f"Bound {bound} - Rules = {encoding.getNRules()}", LogPrintLevel.STATS)
            self.console.log(f"Bound {bound} - Avg Rule Length = {encoding.getAvgRuleLength()}", LogPrintLevel.STATS)
            self.console.log(f"Bound {bound} - Pattern Length = {pat.getLength()}", LogPrintLevel.STATS)

            self.ts.start(f"Solving Bound {bound}", console=self.console)
            solver: SMTSolver = SMTSolver(encoding)
            callsToSolver += 1

            def onImprovedModel(solution: SMTSolution):
                c = solution.getVariable(encoding.c)
                print(f"[SMT] Intermediate improved plan found: c = {c} [{datetime.datetime.now()}]")

            if self.args.minimizeGoalFunction:
                solver.registerOnImprovedModel(onImprovedModel)

            partialPlan: Plan = solver.solve()
            solver.exit()
            self.ts.end(f"Solving Bound {bound}", console=self.console)

            if self.args.saveSMT:
                self.saveSMT(bound, encoding, callsToSolver=callsToSolver)

            if not isinstance(partialPlan, Plan):
                continue

            plan = plan + partialPlan
            if self.args.printPartialPlan:
                print("--Partial Plan---")
                print(plan)
                print("-----------------")

            s = initialState.applyPlan(plan)
            c = GF.compute(s, normalizedGoal, initialState)
            if c == 0:
                self.console.log(f"Calls to Solver: {callsToSolver}", LogPrintLevel.STATS)
                self.console.log(f"Bound: {bound}", LogPrintLevel.STATS)
                return plan

            self.console.log(f"Found intermediate state {s}", LogPrintLevel.PLAN)
            self.console.log(f"New Goal Function Value: {c} [{datetime.datetime.now()}]", LogPrintLevel.PLAN)
            bound = bound + 1
            pat = Pattern.empty()
            patS = Pattern.fromState(s, self.problem.goal, self.domain).addPostfix(bound)

        pass
