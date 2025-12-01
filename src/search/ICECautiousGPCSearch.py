import copy
from typing import Set

from src.ices.ICEEncoding import ICEEncoding
from src.ices.ICEPattern import ICEPattern
from src.ices.ICEPlan import ICEPlan
from src.ices.ICETask import ICETask
from src.pddl.Domain import GroundedDomain
from src.pddl.Formula import Formula
from src.pddl.NumericPlan import NumericPlan
from src.pddl.Plan import Plan
from src.pddl.Predicate import Predicate
from src.pddl.Problem import Problem
from src.pddl.State import State
from src.plan.NumericEncoding import NumericEncoding
from src.plan.Pattern import Pattern
from src.plan.TemporalEncoding import TemporalEncoding
from src.search.Search import Search
from src.smt.SMTSolver import SMTSolver
from src.utils.Arguments import Arguments
from src.utils.LogPrint import LogPrintLevel, LogPrint
from src.utils.TimeStat import TimeStat


class ICECautiousGPCSearch:

    def __init__(self, task: ICETask, args: Arguments):
        self.task: ICETask = task
        self.args: Arguments = args

        self.startBound = 1
        self.maxBound = args.bound if args.bound else 1000

        self.console: LogPrint = LogPrint(self.args.verboseLevel)
        self.ts: TimeStat = TimeStat()

    def solve(self) -> ICEPlan:
        callsToSolver = 0

        totalSubgoals = self.task.goal.conditions
        subgoalsAchieved: Set[Formula or Predicate] = set()

        bound = self.startBound
        s: State = State.fromInitialCondition(self.task.init)

        patG: ICEPattern = ICEPattern.empty()
        patH: ICEPattern = ICEPattern.fromState(s, self.task)

        while bound <= self.maxBound:

            patF: ICEPattern = patG + patH

            self.ts.start(f"Conversion to SMT at bound {bound}", console=self.console)
            if self.args.printPattern:
                patF.print()

            encoding: ICEEncoding = ICEEncoding(
                task=self.task,
                pattern=patF,
                subgoalsAchieved=subgoalsAchieved
            )

            self.ts.end(f"Conversion to SMT at bound {bound}", console=self.console)
            self.console.log(f"Bound {bound} - Vars = {encoding.getNVars()}", LogPrintLevel.STATS)
            self.console.log(f"Bound {bound} - Rules = {encoding.getNRules()}", LogPrintLevel.STATS)
            self.console.log(f"Bound {bound} - Avg Rule Length = {encoding.getAvgRuleLength()}", LogPrintLevel.STATS)
            self.console.log(f"Bound {bound} - Pattern Length = {patF.getLength()}", LogPrintLevel.STATS)

            self.ts.start(f"Solving Bound {bound}", console=self.console)
            solver: SMTSolver = SMTSolver(encoding)
            callsToSolver += 1
            solution = solver.getSolution()
            solver.exit()
            self.ts.end(f"Solving Bound {bound}", console=self.console)

            subgoalsAchievedNow = set()
            plan: ICEPlan = None
            if solution:
                plan: ICEPlan = ICEPlan.fromSMTSolution(encoding, solution)
                s = plan.getFinalState()
                subgoalsAchievedNow = {g for g in self.task.goal.conditions if s.satisfies(g)}

            if plan and len(subgoalsAchievedNow) == len(totalSubgoals):
                self.console.log(f"Calls to Solver: {callsToSolver}", LogPrintLevel.STATS)
                self.console.log(f"Bound: {bound}", LogPrintLevel.STATS)
                return plan

            if plan and len(subgoalsAchievedNow) > len(subgoalsAchieved):
                subgoalsAchieved = subgoalsAchievedNow
                self.console.log(f"Subgoals achieved: {len(subgoalsAchieved)}/{len(totalSubgoals)}: {subgoalsAchieved}",
                                 LogPrintLevel.STATS)
                # patF.addPostfix(bound)
                # patG = patF
                patG = ICEPattern.fromPlan(plan)
                patG.addPostfix("G")
                patH = ICEPattern.fromState(s, self.task)
                pass
            else:
                patF.addPostfix(bound)
                patG = patF

            bound = bound + 1
        pass
