import copy
import datetime
from typing import Type

from src.goalFunctions.DeltaPlusClauses import DeltaPlusClauses
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


class JairSearch(Search):
    initialState: State
    staticPattern: Pattern

    def __init__(self, domain: GroundedDomain, problem: Problem, args: Arguments):
        super().__init__(domain, problem, args)
        self.enhanced = (self.args.pattern == "enhanced")
        self.incompleteSaturationLevel = 1

    def solve(self) -> Plan:
        callsToSolver = 0

        subgoalsAchieved = set()

        bound = 0
        I: State = State.fromInitialCondition(self.problem.init)
        P: State = I

        self.initialState = I

        patS: Pattern = Pattern.empty()
        patG: Pattern = Pattern.empty()
        patH: Pattern = self.satPatH(I, P)

        self.staticPattern = patH

        normalizedGoal = self.problem.goal.normalize()
        c = DeltaPlusClauses.compute(I, normalizedGoal, I)

        plan = NumericPlan.empty()

        self.console.log(f"Goal Function Value: {c}", LogPrintLevel.PLAN)

        unsatN = 0

        while bound <= self.maxBound:

            bound += 1

            pat = (patG + patH).addPostfix(bound)
            S = P if len(patG) == 0 else I

            if self.args.printPattern:
                self.console.log("Pattern: " + str(pat), LogPrintLevel.PLAN)

            self.ts.start(f"Conversion to SMT at bound {bound}", console=self.console)
            encoding: NumericEncoding = NumericEncoding(
                domain=self.domain,
                problem=self.problem,
                state=S,
                pattern=pat,
                goalFunction=DeltaPlusClauses,
                minimizeGoalFunction=True,
                goalFunctionWithEpsilon=False,
                goalFunctionValue=c,
                goalAsSoftAssertAndMinimize=True,
                bound=1,
                args=self.args,
                relaxGoal=False,
                subgoalsAchieved=subgoalsAchieved
            )

            self.ts.end(f"Conversion to SMT at bound {bound}", console=self.console)
            self.console.log(f"Bound {bound} - Vars = {encoding.getNVars()}", LogPrintLevel.STATS)
            self.console.log(f"Bound {bound} - Rules = {encoding.getNRules()}", LogPrintLevel.STATS)
            self.console.log(f"Bound {bound} - Avg Rule Length = {encoding.getAvgRuleLength()}", LogPrintLevel.STATS)
            self.console.log(f"Bound {bound} - Pattern Length = {pat.getLength()}", LogPrintLevel.STATS)

            self.ts.start(f"Solving Bound {bound}", console=self.console)
            solver: SMTSolver = SMTSolver(encoding, trySoftAsHard=True)
            callsToSolver += 1

            def onImprovedModel(solution: SMTSolution):
                c = solution.getVariable(encoding.c)
                print(f"[SMT] Intermediate improved plan found: c = {c} [{datetime.datetime.now()}]")

            solver.registerOnImprovedModel(onImprovedModel)

            partialPlan: Plan = solver.solve()
            solver.exit()
            self.ts.end(f"Solving Bound {bound}", console=self.console)

            if self.args.saveSMT:
                self.saveSMT(bound, encoding, callsToSolver=callsToSolver)

            if self.args.printPartialPlan:
                print("--Partial Plan---")
                print(partialPlan)
                print("-----------------")

            if not isinstance(partialPlan, Plan):
                unsatN += 1
                patG = self.unsatPatG(patS, plan, unsatN).addPostfix(f"{bound}_g")
                patH = self.unsatPatH(I, P, unsatN).addPostfix(bound)
                self.console.log(f"Bound {bound} - No improvement", LogPrintLevel.STATS)
                continue

            unsatN = 0
            plan = partialPlan if S == I else plan + partialPlan
            patS = pat.addPostfix(bound) if S == I else (patS + pat).addPostfix(bound)
            P = S.applyPlan(partialPlan)

            if P.satisfies(self.problem.goal):
                self.console.log(f"Calls to Solver: {callsToSolver}", LogPrintLevel.STATS)
                self.console.log(f"Bound: {bound}", LogPrintLevel.STATS)
                return plan

            subgoalsAchieved = {g for g in self.problem.goal if P.satisfies(g)}

            patG = self.satPatG(patS, plan).addPostfix(f"{bound}_g")
            patH = self.satPatH(I, P).addPostfix(bound)
            c = DeltaPlusClauses.compute(P, normalizedGoal, I)

        pass

    def satPatG(self, patS, plan):
        if self.args.jairSearchStrategy in {"brave", "greedy"}:
            return Pattern.empty()
        if self.args.jairRefinement == "yes":
            return Pattern.fromPlan(plan)
        if self.args.jairRefinement == "no":
            return patS

    def satPatH(self, I, P):
        if self.args.jairPatternChange == "static":
            return Pattern.fromState(I, self.problem.goal, self.domain, self.enhanced)
        if self.args.jairPatternChange == "dynamic":
            if self.args.jairPatternH == "complete":
                return Pattern.fromState(P, self.problem.goal, self.domain, self.enhanced)
            else:
                self.incompleteSaturationLevel = 1
                return Pattern.fromStateGreedy(P, self.problem.goal, self.domain, 1)

    def unsatPatG(self, patS, plan, unsatN):
        if self.args.jairSearchStrategy == "greedy":
            return Pattern.empty()
        if self.args.jairRefinement == "yes":
            return Pattern.fromPlan(plan)
        if self.args.jairRefinement == "no":
            return patS

    def unsatPatH(self, I, P, n):
        if self.args.jairPatternChange == "static":
            return Pattern.fromState(I, self.problem.goal, self.domain, self.enhanced).multiply(n)
        if self.args.jairPatternChange == "dynamic":
            if self.args.jairPatternH == "complete":
                return Pattern.fromState(P, self.problem.goal, self.domain, self.enhanced).multiply(n)
            if self.args.jairPatternH == "incomplete":
                if self.incompleteSaturationLevel > 1:
                    self.incompleteSaturationLevel += 1
                    n = self.incompleteSaturationLevel
                    return Pattern.fromState(P, self.problem.goal, self.domain, self.enhanced).multiply(n)
                else:
                    p = Pattern.fromStateGreedy(P, self.problem.goal, self.domain, 2 ** n)
                    p_ = Pattern.fromStateGreedy(P, self.problem.goal, self.domain, 2 ** (n - 1))
                    if len(p) == len(p_):
                        self.incompleteSaturationLevel += 1
                        return Pattern.fromState(P, self.problem.goal, self.domain, self.enhanced).multiply(2)
                    else:
                        return p
