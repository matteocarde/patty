import datetime

from src.pddl.Domain import GroundedDomain
from src.pddl.Plan import Plan
from src.pddl.Problem import Problem
from src.pddl.State import State
from src.plan.Encoding import Encoding
from src.plan.NumericEncoding import NumericEncoding
from src.plan.Pattern import Pattern
from src.relaxed.classical.RelaxedClassicalEncodingDL import RelaxedClassicalEncodingDL
from src.search.Search import Search
from src.smt.SMTSolution import SMTSolution
from src.smt.SMTSolver import SMTSolver
from src.utils.Arguments import Arguments
from src.utils.LogPrint import console, LogPrintLevel


class HeuristicSearch(Search):
    initialState: State
    staticPattern: Pattern

    def __init__(self, domain: GroundedDomain, problem: Problem, args: Arguments):
        super().__init__(domain, problem, args)
        self.enhanced = (self.args.pattern == "enhanced")
        self.incompleteSaturationLevel = 1
        self.hasCheckedComplete = False

    def solve(self) -> Plan:

        I: State = State.fromInitialCondition(self.problem.init)

        patG: Pattern = Pattern.empty()
        patH: Pattern = Pattern.empty()

        n = 1
        c = float("inf")
        minimize = False

        while n <= self.maxBound:

            console.log(f"----------- {n} -----------", LogPrintLevel.STATS)
            console.log(f"Bound {n}: |<_g|= {len(patG)}", LogPrintLevel.STATS)
            # console.log(str(patG), LogPrintLevel.STATS)
            console.log(f"Bound {n}: |<_h|= {len(patH)}", LogPrintLevel.STATS)
            console.log(f"Cost {n}: c= {c}", LogPrintLevel.STATS)
            # console.log(str(patH), LogPrintLevel.STATS)

            pat = patG + patH
            self.ts.start(f"Conversion to SMT at bound {n}")
            hard: NumericEncoding = NumericEncoding(
                domain=self.domain,
                problem=self.problem,
                state=I,
                pattern=pat,
                goalFunctionValue=0,
                bound=1,
                args=self.args,
                skipGoal=True
            )

            relaxed: RelaxedClassicalEncodingDL = RelaxedClassicalEncodingDL(
                domain=self.domain,
                problem=self.problem,
                heuristic=self.args.heuristic,
                stateVars=hard.transitionVariables[-1].valueVariables,
                minimize=minimize,
                c=c
            )
            # minimize = False

            joined = Encoding.join([hard, relaxed])
            console.log(f"VARS: {joined.getNVars()}", LogPrintLevel.STATS)
            console.log(f"RULES: {joined.getNRules()}", LogPrintLevel.STATS)
            joined.writeSMTLIB(f"{self.args.domain.replace('domain.pddl', '')}{n}.smt")

            solver: SMTSolver = SMTSolver(joined)

            def onImprovedModel(solution: SMTSolution):
                c = relaxed.getGoalValueFunction(solution)
                # print(solution.prettyString())
                console.log(f"[SMT] Intermediate relaxed plan found: c = {c} [{datetime.datetime.now()}]",
                            LogPrintLevel.STATS)

            solver.registerOnImprovedModel(onImprovedModel)
            th = self.ts.startHolder("Solving")
            solution: SMTSolution = solver.getSolution()
            th.endHolder()
            n += 1

            if not solution:
                print("No solution was found")
                patG = pat.addPostfix(n)
                continue

            partialPlan = hard.getPlanFromSolution(solution)
            # console.log(f"Bound {n}: PARTIAL PLAN FOUND", LogPrintLevel.STATS)
            # partialPlan.print()
            # console.log(f"---------------------", LogPrintLevel.STATS)
            S = I.applyPlan(partialPlan)
            if S.satisfies(self.problem.goal):
                th.endHolder()
                return partialPlan

            patG = Pattern.fromPlan(partialPlan)
            patH = relaxed.getPattern(solution, incomplete=True)
            c = relaxed.getGoalValueFunction(solution)

        pass
