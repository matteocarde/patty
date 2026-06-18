from src.pddl.Domain import GroundedDomain
from src.pddl.NumericPlan import NumericPlan
from src.pddl.Plan import Plan
from src.pddl.Problem import Problem
from src.pddl.State import State
from src.plan.Encoding import Encoding
from src.plan.NumericEncoding import NumericEncoding
from src.plan.Pattern import Pattern
from src.relaxed.classical.RelaxedClassicalEncodingDL import RelaxedClassicalEncodingDL
from src.relaxed.snp.RelaxedSimpleNumericEncoding import RelaxedSimpleNumericEncoding
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
        subgoalsAchieved = set()

        I: State = State.fromInitialCondition(self.problem.init)

        patG: Pattern = Pattern.empty()
        patH: Pattern = Pattern.empty()

        # plan = NumericPlan.empty()
        n = 0

        while n <= self.maxBound:

            pat = patG + patH
            self.ts.start(f"Conversion to SMT at bound {n}")
            hard: NumericEncoding = NumericEncoding(
                domain=self.domain,
                problem=self.problem,
                state=I,
                pattern=pat,
                goalFunctionValue=0,
                bound=n,
                args=self.args,
                skipGoal=True
            )

            relaxed: RelaxedClassicalEncodingDL = RelaxedClassicalEncodingDL(
                domain=self.domain,
                problem=self.problem,
                heuristic=self.args.heuristic,
                stateVars=hard.transitionVariables[-1].valueVariables
            )

            joined = Encoding.join([hard, relaxed])
            console.log(f"VARS: {joined.getNVars()}", LogPrintLevel.STATS)
            console.log(f"RULES: {joined.getNRules()}", LogPrintLevel.STATS)
            joined.writeSMTLIB(f"{self.args.domain.replace('domain.pddl', '')}{n}.smt")

            solver: SMTSolver = SMTSolver(joined)
            th = self.ts.startHolder("Searching for relaxed solution")
            solution: SMTSolution = solver.getSolution()
            n += 1
            if not solution:
                th.endHolder()
                patG = pat.addPostfix(n)
                continue

            partialPlan = hard.getPlanFromSolution(solution)
            S = I.applyPlan(partialPlan)
            if S.satisfies(self.problem.goal):
                th.endHolder()
                return partialPlan
            patH_ = relaxed.getPattern(solution, removeBeyondInfinite=True)
            if len(patH) == len(patH_):
                patG = pat.addPostfix(n)
                patH = patH_
                console.log("Pattern stayed the same", LogPrintLevel.STATS)
                continue

            patG = Pattern.fromPlan(partialPlan)
            patH = patH_

            print(patG)
            print(patH)
            th.endHolder()
            console.log(f"|<_g|: {len(patG)}", LogPrintLevel.STATS)
            console.log(f"|<_h|: {len(patH)}", LogPrintLevel.STATS)

        pass
