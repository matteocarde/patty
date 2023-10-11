import traceback

from src.pddl.Domain import Domain, GroundedDomain
from src.pddl.NumericPlan import NumericPlan
from src.pddl.Problem import Problem
from src.search.AStarSearch import AStarSearch
from src.search.GBFSSearch import GBFSSearch
from src.search.Search import Search
from src.search.StaticSearch import StaticSearch
from src.search.StepSearch import StepSearch
from src.utils.Arguments import Arguments
from src.utils.LogPrint import LogPrint, LogPrintLevel
from src.utils.TimeStat import TimeStat


def main():
    args = Arguments()
    if args.isHelp:
        exit(0)

    try:

        console: LogPrint = LogPrint(args.verboseLevel)
        ts: TimeStat = TimeStat()
        ts.start("Overall")
        domain: Domain = Domain.fromFile(args.domain)
        problem: Problem = Problem.fromFile(args.problem)

        ts.start("Grounding", console=console)
        gDomain: GroundedDomain = domain.ground(problem)
        ts.end("Grounding", console=console)

        solver: Search
        if args.search == "gbfs-nomax":
            solver = GBFSSearch(gDomain, problem, args, maximize=False, avoidP=args.avoidP)
        elif args.search == "astar-nomax":
            solver = AStarSearch(gDomain, problem, args, maximize=False, avoidP=args.avoidP)
        elif args.search == "gbfs":
            solver = GBFSSearch(gDomain, problem, args, maximize=True)
        elif args.search == "astar":
            solver = AStarSearch(gDomain, problem, args, maximize=True)
        elif args.search == "step":
            solver = StepSearch(gDomain, problem, args)
        else:
            solver = StaticSearch(gDomain, problem, args)
        plan: NumericPlan = solver.solve()

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
