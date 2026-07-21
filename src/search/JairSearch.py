import copy
import datetime

from src.goalFunctions.DeltaPlusClauses import DeltaPlusClauses
from src.goalFunctions.DeltaSingle import DeltaSingle
from src.pddl.Domain import GroundedDomain
from src.pddl.NumericPlan import NumericPlan
from src.pddl.Plan import Plan
from src.pddl.Problem import Problem
from src.pddl.State import State
from src.plan.NumericEncoding import NumericEncoding
from src.plan.Pattern import Pattern
from src.search.ChrpaImprover import ChrpaImprover
from src.search.Search import Search
from src.smt.SMTSolution import SMTSolution
from src.smt.SMTSolver import SMTSolver
from src.utils.Arguments import Arguments
from src.utils.LogPrint import LogPrintLevel, console


class JairSearch(Search):
    initialState: State
    staticPattern: Pattern

    def __init__(self, domain: GroundedDomain, problem: Problem, args: Arguments):
        super().__init__(domain, problem, args)
        self.enhanced = (self.args.pattern == "enhanced")
        self.incompleteSaturationLevel = 1
        self.hasCheckedComplete = False

    def solve(self) -> Plan:

        self.ts.start(f"Initializing Solving Phase")
        callsToSolver = 0

        subgoalsAchieved = set()

        bound = 0
        I: State = State.fromInitialCondition(self.problem.init)
        P: State = I

        self.initialState = I

        patS: Pattern = Pattern.empty()
        patG: Pattern = Pattern.empty()
        patH: Pattern = self.computeP2G(I, P)
        lastPatH: Pattern = copy.copy(patH)

        self.staticPattern = patH

        normalizedGoal = self.problem.goal.normalize()
        c = DeltaSingle.compute(I, normalizedGoal, I)

        plan = NumericPlan.empty()

        console.log(f"Goal Function Value: {c}", LogPrintLevel.STATS)

        unsatN = 0

        self.ts.end(f"Initializing Solving Phase", group="PREPROCESSING")

        while bound <= self.maxBound:

            bound += 1

            pat = (patG + patH).addPostfix(bound)
            S = P if len(patG) == 0 else I

            if self.args.printPattern:
                console.log("Pattern: " + str(pat), LogPrintLevel.STATS)

            hasMinimize = self.problem.goal.hasOnlyOneNumericConditions() and self.args.jairGoalFunction == "n"

            self.ts.start(f"Constructing Encoding at Bound {bound}")
            encoding: NumericEncoding = NumericEncoding(
                domain=self.domain,
                problem=self.problem,
                state=S,
                pattern=pat,
                goalFunctionValue=c,
                bound=1,
                args=self.args,
                booleanActions=True,
                subgoalsAchieved=subgoalsAchieved,
                minimizeGoalFunction=self.problem.goal.hasOnlyOneNumericConditions() and self.args.jairGoalFunction == "n",
                goalAsSoftAsserts=(self.args.jairGoalFunction in {"n", "g"})
            )

            self.ts.end(f"Constructing Encoding at Bound {bound}", group="PREPROCESSING")
            console.log(f"Bound {bound} - Vars = {encoding.getNVars()}", LogPrintLevel.STATS)
            console.log(f"Bound {bound} - Rules = {encoding.getNRules()}", LogPrintLevel.STATS)
            console.log(f"Bound {bound} - Avg Rule Length = {encoding.getAvgRuleLength()}", LogPrintLevel.STATS)
            console.log(f"Bound {bound} - Pattern Length = {pat.getLength()}", LogPrintLevel.STATS)

            self.ts.start(f"Constructing SMT-LIB Formulas - {bound}")
            solver: SMTSolver = SMTSolver(encoding, trySoftAsHard=hasMinimize)
            self.ts.end(f"Constructing SMT-LIB Formulas - {bound}", group="PREPROCESSING")
            callsToSolver += 1

            def onImprovedModel(solution: SMTSolution):
                c = solution.getVariable(encoding.c)
                console.log(f"[SMT] Intermediate improved plan found: c = {c} [{datetime.datetime.now()}]",
                            LogPrintLevel.STATS)

            # if self.args.jairGoalFunction in {"n"}:
            #     solver.registerOnImprovedModel(onImprovedModel)

            self.ts.start(f"Solving Bound {bound}")
            partialPlan: Plan = solver.solve()
            solver.exit()
            self.ts.end(f"Solving Bound {bound}", group="SOLVING")

            if self.args.saveSMT:
                self.saveSMT(bound, encoding, callsToSolver=callsToSolver)

            if self.args.printPartialPlan:
                console.log("--Partial Plan---", LogPrintLevel.STATS)
                console.log(partialPlan.toValString(), LogPrintLevel.STATS)
                console.log("-----------------", LogPrintLevel.STATS)

            if not isinstance(partialPlan, Plan):
                unsatN += 1
                patG = self.computeS2Pn(patS, plan, unsatN, P).addPostfix(f"{bound}_g")
                patH = self.computeP2Gn(I, P, unsatN, lastPatH, patH).addPostfix(bound)
                console.log(f"Bound {bound} - No improvement", LogPrintLevel.STATS)
                continue

            unsatN = 0
            plan = partialPlan if S == I else plan + partialPlan
            patS = pat.addPostfix(bound) if S == I else (patS + pat).addPostfix(bound)
            P = S.applyPlan(partialPlan)

            if P.satisfies(self.problem.goal):
                console.log(f"Calls to Solver: {callsToSolver}", LogPrintLevel.STATS)
                console.log(f"Bound: {bound}", LogPrintLevel.STATS)
                return plan

            subgoalsAchieved = {g for g in self.problem.goal if P.satisfies(g)}
            console.log(f"Bound {bound} - Improvement - {len(subgoalsAchieved)}/{len(self.problem.goal)} subgoals",
                        LogPrintLevel.STATS)

            patG = self.computeS2P(patS, plan, P).addPostfix(f"{bound}_g")
            patH = self.computeP2G(I, P).addPostfix(bound)
            lastPatH = patH
            c = DeltaPlusClauses.compute(P, normalizedGoal, I)

        pass

    def getPattern(self, patS, plan, P):
        if self.args.jairPatternG == "e":
            return Pattern.empty()
        if self.args.jairPatternG == "o":
            chrpaPlan = ChrpaImprover.improve(plan, self.problem, P)
            return Pattern.fromPlan(chrpaPlan)
        if self.args.jairPatternG == "p":
            return Pattern.fromPlan(plan)
        if self.args.jairPatternG == "r":
            return patS

    def computeS2P(self, patS, plan, P):
        self.ts.start(f"computeS2P")
        p = Pattern.empty()
        if self.args.jairSearchStrategy in "C":
            p = self.getPattern(patS, plan, P)
        self.ts.end(f"computeS2P", group="PREPROCESSING")
        return p

    def computeP2G(self, I, P):
        self.ts.start(f"computeP2G")
        pat = Pattern.empty()
        if self.args.jairPatternH == "s":
            pat = Pattern.fromState(I, self.problem.goal, self.domain, self.enhanced)
        elif self.args.jairPatternH == "c":
            pat = Pattern.fromState(P, self.problem.goal, self.domain, self.enhanced)
        elif self.args.jairPatternH == "i":
            p = Pattern.fromStateGreedy(P, self.problem.goal, self.domain, 1)
            if not p:
                self.incompleteSaturationLevel = 0
                pat = Pattern.fromState(P, self.problem.goal, self.domain, self.enhanced)
            self.incompleteSaturationLevel = 1
            pat = p
        self.ts.end(f"computeP2G", group="PREPROCESSING")
        return pat

    def computeS2Pn(self, patS, plan, unsatN, P):
        self.ts.start(f"ComputeS2Pn")
        p: Pattern = Pattern.empty()
        if self.args.jairSearchStrategy in "C":
            p = self.getPattern(patS, plan, P)
        if self.args.jairSearchStrategy in "B":
            p = self.getPattern(patS, plan, P)
        self.ts.end(f"ComputeS2Pn", group="PREPROCESSING")
        return p

    def computeP2Gn(self, I, P, n, lastPatH, patH):
        self.ts.start(f"computeP2Gn")
        pat = Pattern.empty()
        if self.args.jairPatternH == "s":
            pat = patH + lastPatH.addPostfix(n)
        elif self.args.jairPatternH == "c":
            pat = patH + lastPatH.addPostfix(n)
        elif self.args.jairPatternH == "i":
            if self.incompleteSaturationLevel > 1:
                self.incompleteSaturationLevel += 1
                n = self.incompleteSaturationLevel
                pat = Pattern.fromState(P, self.problem.goal, self.domain, self.enhanced).multiply(n)
            else:
                p = Pattern.fromStateGreedy(P, self.problem.goal, self.domain, 2 ** n)
                p_ = Pattern.fromStateGreedy(P, self.problem.goal, self.domain, 2 ** (n - 1))
                if len(p) == len(p_):
                    self.incompleteSaturationLevel += 1
                    pat = Pattern.fromState(P, self.problem.goal, self.domain, self.enhanced).multiply(
                        self.incompleteSaturationLevel)
                else:
                    pat = p
        self.ts.end(f"computeP2Gn", group="PREPROCESSING")
        return pat
