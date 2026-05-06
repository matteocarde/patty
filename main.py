import traceback

from z3 import z3

from main_ices import main_ices
from src.pddl.Domain import Domain, GroundedDomain
from src.pddl.NumericPlan import NumericPlan
from src.pddl.Plan import Plan
from src.pddl.Problem import Problem
from src.plan.Pattern import Pattern
from src.search.AStarSearchMax import AStarSearchMax
from src.search.BDCSearch import BDCSearch
from src.search.ChainSearch import ChainSearch
from src.search.ChrpaImprover import ChrpaImprover
from src.search.GDSearch import GDSearch
from src.search.JairSearch import JairSearch
from src.search.PASSearch import PASSearch
from src.search.PlanImproverLess import PlanImproverLess
from src.search.PlanImproverPattern import PlanImproverPattern
from src.search.Search import Search
from src.search.StepSearch import StepSearch
from src.utils.Arguments import Arguments
from src.utils.LogPrint import LogPrint, LogPrintLevel, console
from src.utils.TimeStat import TimeStat


def main():
    args = Arguments()
    console.setLogLevel(args.verboseLevel)

    if args.isHelp:
        exit(0)

    if args.ices:
        main_ices(args)
        return

    try:
        console.log(f"Using z3 version {z3.get_version_string()}", LogPrintLevel.INFO)
        ts: TimeStat = TimeStat()
        ts.start("Overall")
        domain: Domain = Domain.fromFile(args.domain)
        problem: Problem = Problem.fromFile(args.problem, domain=domain)

        ts.start("Quantifier Elimination")
        qeDomain: Domain = domain.eliminateQuantifiers(problem)
        ts.end("Quantifier Elimination")

        ts.start("Grounding")
        gDomain: GroundedDomain = qeDomain.ground(problem)
        ts.end("Grounding")

        isTemporal = len(gDomain.durativeActions) > 0
        solver: Search
        pattern: Pattern
        bound: int

        if gDomain.hasConditionalEffects():
            solver = PASSearch(gDomain, problem, args, liftedDomain=domain)
        elif args.search == "astar":
            solver = AStarSearchMax(gDomain, problem, args)
        elif args.search == "jair":
            solver = JairSearch(gDomain, problem, args)
        elif args.search == "gd":
            solver = GDSearch(gDomain, problem, args)
        elif args.search == "bdc":
            solver = BDCSearch(gDomain, problem, args)
        elif args.search == "step":
            solver = StepSearch(gDomain, problem, args)
        else:
            solver = ChainSearch(gDomain, problem, args, liftedDomain=domain)
        plan: Plan = solver.solve()

        if isinstance(plan, NumericPlan) and "improve" in args.quality:
            ts.start("Improving Plan")
            improver: Search
            if args.quality == "improve-plan":
                improver = PlanImproverPattern(gDomain, problem, args, plan)
            elif args.quality == "improve-chrpa":
                improver = ChrpaImprover(gDomain, problem, args, plan)
            elif args.quality == "improve-less":
                assert solver.finalPattern and solver.finalBound
                improver = PlanImproverLess(gDomain, problem, args, plan, solver.finalPattern, solver.finalBound)
            else:
                raise Exception("Unknown quality improver " + args.quality)
            improvedPlan = improver.solve()
            ts.end("Improving Plan")
            if improvedPlan:
                console.log(f"First Plan Length: {len(plan)}", LogPrintLevel.STATS)
                console.log(f"Improved Plan Length: {len(improvedPlan)}", LogPrintLevel.STATS)
                plan = improvedPlan

        console.log(plan.toIPCString(), LogPrintLevel.PLAN)
        console.log("------", LogPrintLevel.STATS)
        console.log(f"Distinct Actions: {len(plan.getDistinctActions())}", LogPrintLevel.STATS)
        if isinstance(plan, NumericPlan):
            console.log(f"Rolled Actions: {len(plan.getRolledActions())}", LogPrintLevel.STATS)
            console.log(f"Max Rolling: {plan.getMaxRolling()}", LogPrintLevel.STATS)
        console.log("------", LogPrintLevel.STATS)
        isValid = plan.validate(problem, avoidRaising=True, logger=console)
        if isValid:
            console.log("Plan is valid", LogPrintLevel.STATS)
            if args.plan is not None:
                with open(args.plan, "w") as f:
                    f.write(plan.toIPCString())
        else:
            console.log("Plan is NOT valid", LogPrintLevel.PLAN)

        ts.end("Overall")
        console.log(str(ts), LogPrintLevel.TIMES)

    except:
        print("Something went wrong.")
        traceback.print_exc()


if __name__ == '__main__':
    main()
