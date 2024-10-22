from src.pddl.Domain import GroundedDomain, Domain
from src.pddl.NumericPlan import NumericPlan
from src.pddl.Plan import Plan
from src.pddl.Problem import Problem
from src.pddl.State import State
from src.pddl.TemporalPlan import TemporalPlan
from src.plan.CESEncoding import CESEncoding
from src.plan.NumericEncoding import NumericEncoding
from src.plan.Pattern import Pattern
from src.plan.TemporalEncoding import TemporalEncoding
from src.plan.TransitionRelations import TransitionRelations
from src.search.Search import Search
from src.smt.SMTSolver import SMTSolver
from src.utils.Arguments import Arguments
from src.utils.LogPrint import LogPrintLevel


class ChainSearch(Search):

    def __init__(self, domain: GroundedDomain, problem: Problem, args: Arguments, liftedDomain: Domain = None):
        self.useSCCs = args.useSCCs
        super().__init__(domain, problem, args, liftedDomain=liftedDomain)
        self.isCES = self.domain.hasConditionalEffects()

    def getPattern(self) -> Pattern:
        if self.args.pattern == "arpg":
            return Pattern.fromARPG(self.domain)
        if self.args.pattern == "enhanced":
            return Pattern.fromARPGEnhanced(self.domain)
        if self.args.pattern == "random":
            return Pattern.fromRandom(self.domain)
        if self.args.pattern == "alpha":
            return Pattern.fromAlphabetical(self.domain)

        raise Exception(f"Pattern generation method '{self.args.pattern}' unknown")

    def solve(self) -> Plan:
        callsToSolver = 0
        pattern: Pattern = self.getPattern()

        if self.args.printARPG:
            self.console.log(str(self.domain.arpg), LogPrintLevel.PLAN)

        bound = self.startBound

        relations = None
        if self.isCES:
            relations = TransitionRelations(self.liftedDomain)

        while bound <= self.maxBound:

            fPattern = pattern.multiply(bound, addFake=not self.isTemporal)
            if self.args.printPattern:
                self.console.log("Pattern: " + str(fPattern), LogPrintLevel.PLAN)

            self.ts.start(f"Conversion to SMT at bound {bound}", console=self.console)
            if self.isTemporal:
                encoding: TemporalEncoding = TemporalEncoding(
                    domain=self.domain,
                    problem=self.problem,
                    pattern=fPattern,
                    bound=1)
            elif self.isCES:
                assert relations
                encoding: CESEncoding = CESEncoding(
                    domain=self.domain,
                    liftedDomain=self.liftedDomain,
                    problem=self.problem,
                    pattern=fPattern,
                    bound=1,
                    transitionRelations=relations
                )
            else:
                encoding: NumericEncoding = NumericEncoding(
                    domain=self.domain,
                    problem=self.problem,
                    pattern=fPattern,
                    bound=1,
                    args=self.args
                )
            self.ts.end(f"Conversion to SMT at bound {bound}", console=self.console)

            self.console.log(f"Bound {bound} - Vars = {encoding.getNVars()}", LogPrintLevel.STATS)
            self.console.log(f"Bound {bound} - Rules = {encoding.getNRules()}", LogPrintLevel.STATS)
            self.console.log(f"Calls to Solver: {callsToSolver}", LogPrintLevel.STATS)
            self.ts.start(f"Solving Bound {bound}", console=self.console)
            solver: SMTSolver = SMTSolver(encoding)

            plan: Plan
            plan = solver.solve()
            callsToSolver += 1
            solver.exit()
            self.ts.end(f"Solving Bound {bound}", console=self.console)

            if self.args.saveSMT:
                self.saveSMT(bound, encoding)

            if isinstance(plan, TemporalPlan if self.isTemporal else NumericPlan):
                self.console.log(f"Bound: {bound}", LogPrintLevel.STATS)
                return plan

            self.console.log(f"NO SOLUTION: No solution with bound {bound}. Try to increase the bound",
                             LogPrintLevel.PLAN)

            bound += 1

        pass
