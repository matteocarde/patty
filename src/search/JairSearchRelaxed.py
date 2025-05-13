import copy
import datetime
from typing import Type

from src.goalFunctions.GoalFunction import GoalFunction
from src.pddl.Domain import GroundedDomain
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


class JairSearchRelaxed(Search):

    def __init__(self, domain: GroundedDomain, problem: Problem, args: Arguments):
        super().__init__(domain, problem, args)
        self.enhanced = self.args.pattern == "enhanced"

    def solve(self) -> Plan:
        callsToRelaxedSolver = 0
        callsToHardSolver = 0

        bound = self.startBound
        initialState: State = State.fromInitialCondition(self.problem.init)
        s: State = initialState

        GF: Type[GoalFunction] = GoalFunction.getGoalFunctionFromString(self.args.goalFunction)
        normalizedGoal = self.problem.goal.normalize()
        GF.assertGoalIsRightForm(normalizedGoal)
        c = GF.compute(s, normalizedGoal, initialState)

        pat: Pattern = Pattern.empty()

        self.console.log(f"Goal Function Value: {c}", LogPrintLevel.PLAN)

        while bound <= self.maxBound:

            patH: Pattern = Pattern.fromState(s, self.problem.goal, self.domain).addPostfix(bound)
            pat: Pattern = copy.deepcopy(pat + patH)

            if self.args.printPattern:
                self.console.log(f"Complete Pattern:", LogPrintLevel.PLAN)
                self.console.log(f"--------------------", LogPrintLevel.PLAN)
                self.console.log(pat, LogPrintLevel.PLAN)
                self.console.log(f"--------------------", LogPrintLevel.PLAN)

            self.ts.start(f"Conversion to Relaxed SMT at bound {bound}", console=self.console)
            relaxedEncoding: NumericEncoding = NumericEncoding(
                domain=self.domain,
                problem=self.problem,
                pattern=pat,
                goalFunction=GF,
                realActionVariables=True,
                minimizeGoalFunction=self.args.minimizeGoalFunction,
                goalFunctionWithEpsilon=not self.args.noCompression,
                goalFunctionValue=c,
                bound=1,
                args=self.args,
            )

            self.ts.end(f"Conversion to Relaxed SMT at bound {bound}", console=self.console)
            # self.console.log(f"Bound {bound} - Vars = {relaxedEncoding.getNVars()}", LogPrintLevel.STATS)
            # self.console.log(f"Bound {bound} - Rules = {relaxedEncoding.getNRules()}", LogPrintLevel.STATS)
            # self.console.log(f"Bound {bound} - Avg Rule Length = {relaxedEncoding.getAvgRuleLength()}", LogPrintLevel.STATS)
            # self.console.log(f"Bound {bound} - Pattern Length = {pat.getLength()}", LogPrintLevel.STATS)

            self.ts.start(f"Solving Relaxed Bound {bound}", console=self.console)
            relaxedSolver: SMTSolver = SMTSolver(relaxedEncoding)
            callsToRelaxedSolver += 1

            def onImprovedModelRelaxed(solution: SMTSolution):
                c = solution.getVariable(relaxedEncoding.c)
                print(f"[SMT] Intermediate relaxed improved plan found: c = {c} [{datetime.datetime.now()}]")

            relaxedSolver.registerOnImprovedModel(onImprovedModelRelaxed)
            relaxedPlan: Plan = relaxedSolver.solve(relaxed=True)
            relaxedSolver.exit()
            self.ts.end(f"Solving Relaxed Bound {bound}", console=self.console)
            cRelaxed = relaxedPlan.solution.getVariable(relaxedEncoding.c)
            self.console.log(f"Relaxed Goal Function Value: {cRelaxed} [{datetime.datetime.now()}]", LogPrintLevel.PLAN)

            if self.args.saveSMT:
                self.saveSMT(bound, relaxedEncoding, callsToSolver=callsToRelaxedSolver)

            if not isinstance(relaxedPlan, Plan):
                continue

            patR = Pattern.fromPlan(relaxedPlan, addFake=not self.isTemporal)

            if self.args.printPattern:
                self.console.log(f"Relaxed Pattern:", LogPrintLevel.PLAN)
                self.console.log(f"--------------------", LogPrintLevel.PLAN)
                self.console.log(patR, LogPrintLevel.PLAN)
                self.console.log(f"--------------------", LogPrintLevel.PLAN)

            hardEncoding: NumericEncoding = NumericEncoding(
                domain=self.domain,
                problem=self.problem,
                pattern=patR,
                goalFunction=GF,
                realActionVariables=False,
                minimizeGoalFunction=self.args.minimizeGoalFunction,
                goalFunctionWithEpsilon=not self.args.noCompression,
                goalFunctionValue=c,
                bound=1,
                args=self.args,
            )

            self.ts.start(f"Solving Hard Bound {bound}", console=self.console)
            hardSolver: SMTSolver = SMTSolver(hardEncoding)
            callsToHardSolver += 1

            def onImprovedModelHard(solution: SMTSolution):
                c = solution.getVariable(hardEncoding.c)
                print(
                    f"[SMT] Intermediate hard improved plan found: c = {c} [{datetime.datetime.now()}]")

            hardSolver.registerOnImprovedModel(onImprovedModelHard)
            hardPlan: Plan = hardSolver.solve()
            hardSolver.exit()
            self.ts.end(f"Solving Hard Bound {bound}", console=self.console)

            if isinstance(hardPlan, Plan):
                s = initialState.applyPlan(hardPlan)
                if s.satisfies(self.problem.goal):
                    self.console.log(f"Calls to Solver: {callsToHardSolver} Hard + {callsToRelaxedSolver} Relaxed",
                                     LogPrintLevel.STATS)
                    self.console.log(f"Bound: {bound}", LogPrintLevel.STATS)
                    return hardPlan
                c = GF.compute(s, normalizedGoal, initialState)
                self.console.log(f"Found intermediate state {s}", LogPrintLevel.PLAN)
                self.console.log(f"New Goal Function Value: {c} [{datetime.datetime.now()}]", LogPrintLevel.PLAN)

                pat = Pattern.fromPlan(hardPlan, addFake=not self.isTemporal)

            bound = bound + 1

        pass
