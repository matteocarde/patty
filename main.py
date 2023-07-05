import random
import traceback
from typing import List

from src.pddl.Domain import Domain, GroundedDomain
from src.pddl.NumericPlan import NumericPlan
from src.pddl.Operation import Operation
from src.pddl.Problem import Problem
from src.plan.PDDL2SMT import PDDL2SMT
from src.plan.Pattern import Pattern
from src.smt.SMTSolver import SMTSolver
from src.utils.Arguments import Arguments
from src.utils.LogPrint import LogPrint, LogPrintLevel
from src.utils.TimeStat import TimeStat


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

        bound = args.bound if args.bound else 1
        bMax = args.bound if args.bound else len(gDomain.actions)

        order: List[Operation]
        if args.pattern == "arpg":
            order = gDomain.getARPG().getActionsOrder()
        elif args.pattern == "random":
            order = list(gDomain.actions)
            random.shuffle(order)
        else:
            raise Exception(f"Pattern generation method '{args.pattern}' unknown")
        pattern: Pattern = Pattern.fromOrder(order)

        if args.printPattern:
            console.log("Pattern: " + str(pattern), LogPrintLevel.PLAN)

        while bound <= bMax:

            ts.start(f"Conversion to SMT at bound {bound}", console=console)
            pddl2smt: PDDL2SMT = PDDL2SMT(
                domain=gDomain,
                problem=problem,
                pattern=pattern,
                bound=bound,
                encoding=args.encoding,
                binaryActions=args.binaryActions
            )
            ts.end(f"Conversion to SMT at bound {bound}", console=console)

            ts.start(f"Solving Bound {bound}", console=console)
            solver: SMTSolver = SMTSolver(pddl2smt, solver=args.solver)

            plan: NumericPlan
            if args.deep:
                plan = solver.optimizeBinary()
            else:
                plan = solver.solve()
            solver.exit()
            ts.end(f"Solving Bound {bound}", console=console)

            if args.saveSMT:
                filename = f"{args.saveSMT}-{bound}.smt"
                console.log(f"Saving to {filename}", LogPrintLevel.STATS)
                with open(f"{args.saveSMT}-{bound}.smt", "w") as f:
                    f.write(str(pddl2smt))

            if not plan:
                console.log(
                    f"NO SOLUTION: A solution could not be found with bound {bound}. Try to increase the bound",
                    LogPrintLevel.PLAN)
            else:
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
                console.log(f"Bound: {bound}", LogPrintLevel.STATS)

                break

            bound += 1

        ts.end("Overall")
        console.log(str(ts), LogPrintLevel.TIMES)

    except:
        print("Something went wrong.")
        traceback.print_exc()


if __name__ == '__main__':
    main()
