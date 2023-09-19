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


class AStarSearch(Search):

    def __init__(self, domain: GroundedDomain, problem: Problem, args: Arguments):
        super().__init__(domain, problem, args)

    def solve(self) -> NumericPlan:
        callsToSolve = 0
        totalSubgoals = self.problem.goal.conditions
        subgoalsAchieved = set()
        bound = self.startBound
        initialState: State = State.fromInitialCondition(self.problem.init)
        s: State = initialState
        sprime: State = copy.deepcopy(s)

        patG: Pattern = Pattern.fromOrder([])
        patH: Pattern = Pattern.fromState(s, self.problem.goal, self.domain)
        patHPrime: Pattern = copy.deepcopy(patH)
        patF: Pattern = copy.deepcopy(patG + patH)

        while bound <= self.maxBound:

            self.ts.start(f"Conversion to SMT at bound {bound}", console=self.console)
            pddl2smt: PDDL2SMT = PDDL2SMT(
                domain=self.domain,
                problem=self.problem,
                pattern=patF,
                bound=1,
                relaxGoal=True,
                subgoalsAchieved=subgoalsAchieved,
                encoding=self.args.encoding,
                binaryActions=self.args.binaryActions,
                rollBound=self.args.rollBound,
                hasEffectAxioms=self.args.hasEffectAxioms
            )
            self.ts.end(f"Conversion to SMT at bound {bound}", console=self.console)

            self.ts.start(f"Solving Bound {bound}", console=self.console)
            solver: SMTSolver = SMTSolver(pddl2smt, solver=self.args.solver)
            callsToSolve += 1
            plan: NumericPlan = solver.solve()
            solver.exit()
            self.ts.end(f"Solving Bound {bound}", console=self.console)

            self.console.log(f"Bound {bound} - Vars = {pddl2smt.getNVars()}", LogPrintLevel.STATS)
            self.console.log(f"Bound {bound} - Rules = {pddl2smt.getNRules()}", LogPrintLevel.STATS)

            if self.args.saveSMT:
                self.saveSMT(bound, pddl2smt)

            if plan:
                # IF SAT
                sprime = initialState.applyPlan(plan)
                subgoalsAchieved = {g for g in self.problem.goal.conditions if sprime.satisfies(g)}
                self.console.log(f"Subgoals achieved: {len(subgoalsAchieved)}/{len(totalSubgoals)}",
                                 LogPrintLevel.STATS)
                patG = Pattern.fromPlan(plan)
                patG.addPostfix("G")
                patH = Pattern.fromOrder([])
                self.console.log(f"Calls to solve: {callsToSolve}",
                                 LogPrintLevel.STATS)
                if len(subgoalsAchieved) == len(self.problem.goal.conditions):
                    return plan
                pass

            else:
                if s != sprime:
                    patHPrime = Pattern.fromState(sprime, self.problem.goal, self.domain)
                    sprime = s
                bound += 1
                patHPrime.addPostfix(bound)
                patH += patHPrime
                patF = patG + patH

        pass
