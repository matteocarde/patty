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


def main():
    experiment = "experiments/performances/1679784995.57566"

    valid = 0
    total = 0

    for domain in os.listdir(experiment):
        if domain in {"results.csv"}:
            continue

        for problem in os.listdir(f"{experiment}/{domain}"):
            if "ERRORED" in problem:
                continue

            val = "/Users/carde/Bin/VAL/Validate"
            cmd = f"{val} files/{domain}/domain.pddl files/{domain}/instances/{problem} {experiment}/{domain}/{problem}"
            result = os.popen(cmd).read()
            if "Plan valid" in result:
                print(domain, problem, "Valid")
                valid += 1
            else:
                print(domain, problem, "Invalid", file=sys.stderr)
            total += 1

    print(f"{round(valid / total * 100, 2)}% valid")


if __name__ == '__main__':
    main()
