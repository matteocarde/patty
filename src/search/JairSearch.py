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


class JairSearch(Search):

    def __init__(self, domain: GroundedDomain, problem: Problem, args: Arguments):
        super().__init__(domain, problem, args)
        self.enhanced = self.args.pattern == "enhanced"

    def solve(self) -> Plan:
        callsToSolver = 0

        subgoalsAchieved = set()

        bound = self.startBound
        initialState: State = State.fromInitialCondition(self.problem.init)
        s: State = initialState

        patG: Pattern = Pattern.empty()
        pat: Pattern = Pattern.empty()
        patH: Pattern = Pattern.empty()
        patHprev: Pattern = Pattern.empty()
        GF: Type[GoalFunction] = GoalFunction.getGoalFunctionFromString(self.args.goalFunction)
        normalizedGoal = self.problem.goal.normalize()
        GF.assertGoalIsRightForm(normalizedGoal)
        c = GF.compute(s, normalizedGoal, initialState)

        lvl = 100

        self.console.log(f"Goal Function Value: {c}", LogPrintLevel.PLAN)

        while bound <= self.maxBound:

            patH: Pattern = Pattern.fromStateGreedy(s, self.problem.goal, self.domain, lvl).addPostfix(bound)
            if len(patH) == len(patHprev):
                patH = Pattern.fromState(s, self.problem.goal, self.domain).addPostfix(bound)
                patG = copy.deepcopy(patG + patH)
                lvl = 1
            pat: Pattern = copy.deepcopy(pat + patH)

            if self.args.printPattern:
                self.console.log(f"Greedy Level {lvl}", LogPrintLevel.PLAN)
                self.console.log("Pattern: " + str(pat), LogPrintLevel.PLAN)

            self.ts.start(f"Conversion to SMT at bound {bound}", console=self.console)
            encoding: NumericEncoding = NumericEncoding(
                domain=self.domain,
                problem=self.problem,
                pattern=pat,
                goalFunction=GF,
                minimizeGoalFunction=self.args.minimizeGoalFunction,
                goalFunctionWithEpsilon=not self.args.noCompression,
                goalFunctionValue=c,
                bound=1,
                args=self.args,
                relaxGoal=False,
                subgoalsAchieved=subgoalsAchieved if not self.args.dontKeepSubgoals else set()
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

            solver.registerOnImprovedModel(onImprovedModel)
            plan: Plan = solver.solve()
            solver.exit()
            self.ts.end(f"Solving Bound {bound}", console=self.console)

            if self.args.printPartialPlan and plan:
                print("--Partial Plan---")
                print(plan)
                print("-----------------")

            if self.args.saveSMT:
                self.saveSMT(bound, encoding, callsToSolver=callsToSolver)

            if isinstance(plan, Plan):
                s = initialState.applyPlan(plan)
                if s.satisfies(self.problem.goal):
                    self.console.log(f"Calls to Solver: {callsToSolver}", LogPrintLevel.STATS)
                    self.console.log(f"Bound: {bound}", LogPrintLevel.STATS)
                    return plan
                subgoalsAchieved = {g for g in self.problem.goal if s.satisfies(g)}
                c = GF.compute(s, normalizedGoal, initialState)
                self.console.log(f"Found intermediate state {s}", LogPrintLevel.PLAN)
                self.console.log(f"New Goal Function Value: {c} [{datetime.datetime.now()}]", LogPrintLevel.PLAN)
                patG = Pattern.fromPlan(plan, addFake=not self.isTemporal) if not self.args.noCompression else pat
                patG.addPostfix("g")
                lvl = 1
            else:
                lvl += lvl
            pat = patG
            patHprev = patH
            bound = bound + 1

        pass
