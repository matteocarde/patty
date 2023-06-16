import os
import pathlib
import sys
import time
import traceback

from natsort import natsort

from Domain import Domain, GroundedDomain
from NumericPlan import NumericPlan
from Problem import Problem
from classes.plan.PDDL2SMT import PDDL2SMT
from classes.smt.SMTSolution import SMTSolution
from classes.smt.SMTSolver import SMTSolver
from classes.utils.Arguments import Arguments
from classes.utils.LogPrint import LogPrint, LogPrintLevel
from classes.utils.TimeStat import TimeStat


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
        pddl2smt: PDDL2SMT = PDDL2SMT(gDomain, problem, args.horizon)
        ts.end("Conversion to SMT", console=console)

        ts.start("Solving", console=console)
        solver: SMTSolver = SMTSolver(pddl2smt)
        ts.end("Solving", console=console)

        plan: NumericPlan = solver.solve()
        solver.exit()
        if not plan:
            print("NO SOLUTION: A solution could not be found")
        else:
            print(plan.toValString())

        ts.end("Overall")

        console.log(str(ts), LogPrintLevel.TIMES)

    except:
        print("Something went wrong.")
        traceback.print_exc()


if __name__ == '__main__':
    main()
