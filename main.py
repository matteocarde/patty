import traceback

from src.plan.PDDL2SMT import PDDL2SMT
from src.smt.SMTSolver import SMTSolver
from src.utils.Arguments import Arguments
from src.utils.LogPrint import LogPrint, LogPrintLevel
from src.utils.TimeStat import TimeStat
from src.pddl.Domain import Domain, GroundedDomain
from src.pddl.NumericPlan import NumericPlan
from src.pddl.Problem import Problem


def main():
    try:
        args = Arguments()

        console: LogPrint = LogPrint(args.verboseLevel)
        ts: TimeStat = TimeStat()
        ts.start("Overall")
        domain: Domain = Domain.fromFile(args.domain)
        problem: Problem = Problem.fromFile(args.problem)

        ts.start("Grounding", console=console)
        gDomain: GroundedDomain = domain.ground(problem)
        ts.end("Grounding", console=console)

        ts.start("Conversion to SMT", console=console)
        pddl2smt: PDDL2SMT = PDDL2SMT(gDomain, problem, args.bound)
        ts.end("Conversion to SMT", console=console)

        ts.start("Solving", console=console)
        solver: SMTSolver = SMTSolver(pddl2smt)

        plan: NumericPlan
        if args.deep:
            plan = solver.optimizeBinary()
        else:
            plan = solver.solve()
        solver.exit()
        ts.end("Solving", console=console)

        if not plan:
            console.log(
                f"NO SOLUTION: A solution could not be found with bound {args.bound}. Try to increase the bound",
                LogPrintLevel.PLAN)
        else:
            isValid = plan.validate(problem, avoidRaising=True)
            print(plan.toValString())
            if isValid:
                console.log("Plan is valid", LogPrintLevel.PLAN)
            else:
                console.log("Plan is NOT valid", LogPrintLevel.PLAN)

        ts.end("Overall")

        console.log(str(ts), LogPrintLevel.TIMES)

    except:
        print("Something went wrong.")
        traceback.print_exc()


if __name__ == '__main__':
    main()
