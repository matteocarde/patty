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
from src.utils.ToolsArguments import ToolsArguments


def main():
    args = ToolsArguments()
    if args.isHelp:
        exit(0)

    try:

        if args.tool == "delta":

            domain: Domain = Domain.fromFile(args.domain)
            problem: Problem = Problem.fromFile(args.problem)

            print("Everything ok")

        else:
            raise Exception(f"The tool '{args.tool}' has not been implemented yet.")

    except:
        print("Something went wrong.")
        traceback.print_exc()


if __name__ == '__main__':
    main()
