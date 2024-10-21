import traceback

from z3 import z3

from src.pddl.Domain import Domain, GroundedDomain
from src.pddl.Plan import Plan
from src.pddl.Problem import Problem
from src.search.AStarSearchMax import AStarSearchMax
from src.search.ChainSearch import ChainSearch
from src.search.PlanImprover import PlanImprover
from src.search.Search import Search
from src.search.StepSearch import StepSearch
from src.search.TransitiveClosureSolver import TransitiveClosureSolver
from src.utils.Arguments import Arguments
from src.utils.LogPrint import LogPrint, LogPrintLevel
from src.utils.TimeStat import TimeStat


def main():
    args = Arguments()
    if args.isHelp:
        exit(0)

    try:
        print(f"Using z3 version {z3.get_version_string()}")
        console: LogPrint = LogPrint(args.verboseLevel)
        ts: TimeStat = TimeStat()
        ts.start("Overall")
        domain: Domain = Domain.fromFile(args.domain)
        problem: Problem = Problem.fromFile(args.problem)

        ts.start("Grounding", console=console)
        gDomain: GroundedDomain = domain.ground(problem, console=console)
        ts.end("Grounding", console=console)

        if domain.hasConditionalEffects:
            tcs = TransitiveClosureSolver(domain, problem, gDomain, args)
            exit()

        solver: Search

        if args.search == "astar":
            solver = AStarSearchMax(gDomain, problem, args)
        elif args.search == "step":
            solver = StepSearch(gDomain, problem, args)
        else:
            solver = ChainSearch(gDomain, problem, args)
        plan: Plan = solver.solve()

        if args.quality == "improve-plan":
            ts.start("Improving Plan", console=console)
            improver = PlanImprover(gDomain, problem, args, plan)
            improvedPlan = improver.solve()
            ts.end("Improving Plan", console=console)
            if improvedPlan:
                console.log(f"First Plan Length: {len(plan)}", LogPrintLevel.PLAN)
                console.log(f"Improved Plan Length: {len(improvedPlan)}", LogPrintLevel.PLAN)
                plan = improvedPlan

        console.log(plan.toValString(), LogPrintLevel.PLAN)
        isValid = plan.validate(problem, avoidRaising=True, logger=console)
        if isValid:
            console.log("Plan is valid", LogPrintLevel.PLAN)
            if args.savePlan:
                fn = args.savePlan if args.savePlan != "PROBLEM" else args.problem + ".plan"
                with open(fn, "w") as f:
                    f.write(plan.toValString())
        else:
            console.log("Plan is NOT valid", LogPrintLevel.PLAN)

        ts.end("Overall")
        console.log(str(ts), LogPrintLevel.TIMES)

    except:
        print("Something went wrong.")
        traceback.print_exc()


if __name__ == '__main__':
    main()
