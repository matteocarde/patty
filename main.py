import traceback

from src.pattern.PatternTranslator import PatternTranslator
from src.pddl.Domain import Domain, GroundedDomain
from src.pddl.NumericPlan import NumericPlan
from src.pddl.Problem import Problem
from src.search.AStarSearchMax import AStarSearchMax
from src.search.Search import Search
from src.search.StaticSearch import StaticSearch
from src.search.StepSearch import StepSearch
from src.utils.Arguments import Arguments
from src.utils.LogPrint import LogPrint, LogPrintLevel
from src.utils.TimeStat import TimeStat


def search(args: Arguments):
    console: LogPrint = LogPrint(args.verboseLevel)
    ts: TimeStat = TimeStat()
    ts.start("Overall")
    domain: Domain = Domain.fromFile(args.domain)
    problem: Problem = Problem.fromFile(args.problem)

    ts.start("Grounding", console=console)
    gDomain: GroundedDomain = domain.ground(problem, console=console)
    ts.end("Grounding", console=console)

    solver: Search
    if args.search == "astar":
        solver = AStarSearchMax(gDomain, problem, args)
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


def translate(args: Arguments):
    domain: Domain = Domain.fromFile(args.domain)
    problem: Problem = Problem.fromFile(args.problem)

    pt: PatternTranslator = PatternTranslator(domain, problem)

    tDomain: Domain = pt.getTranslatedDomain()
    tProblem: Problem = pt.getTranslatedProblem()

    tDomainString = tDomain.toPDDL()



def main():
    args = Arguments()
    if args.isHelp:
        exit(0)

    try:

        if args.translate:
            translate(args)
        else:
            search(args)


    except:
        print("Something went wrong.")
        traceback.print_exc()


if __name__ == '__main__':
    main()
