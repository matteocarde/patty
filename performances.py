import os
import pathlib
import time
import traceback

from natsort import natsort

from Domain import Domain, GroundedDomain
from NumericPlan import NumericPlan
from Problem import Problem
from classes.plan.PDDL2SMT import PDDL2SMT
from classes.smt.SMTSolution import SMTSolution
from classes.smt.SMTSolver import SMTSolver

domains = {
    "block-grouping": {
        "folder": "block-grouping",
        "domain": "domain.pddl",
        "problems-folder": "instances/"
    },
    "fn-counters": {
        "folder": "counters/fn-counters",
        "domain": "domain.pddl",
        "problems-folder": "instances/"
    },
    "fn-counters-inv": {
        "folder": "counters/fn-counters-inv",
        "domain": "domain.pddl",
        "problems-folder": "instances/"
    },
    "fn-counters-rnd": {
        "folder": "counters/fn-counters-rnd",
        "domain": "domain.pddl",
        "problems-folder": "instances/"
    },
    "farmland": {
        "folder": "farmland",
        "domain": "domain.pddl",
        "problems-folder": "instances/"
    },
    "plant-watering": {
        "folder": "plant-watering",
        "domain": "domain.pddl",
        "problems-folder": "instances/"
    },
    "gardening": {
        "folder": "gardening",
        "domain": "domain.pddl",
        "problems-folder": "instances/"
    },
    # "sailing": {
    #     "folder": "sailing",
    #     "domain": "domain.pddl",
    #     "problems-folder": "instances/"
    # }
}

HORIZON = 4


def myRound(n: str or float):
    return n if type(n) == str else round(n, 2)


def printResults(file, domain, problem, preTime, planTime, totalTime, planLength):
    row = [domain, problem, myRound(preTime), myRound(planTime), myRound(totalTime), planLength]

    print('| {:<15} | {:<25} | {:^10} | {:^10} | {:^10} | {:^10} |'.format(*row))
    file.write(",".join([str(c) for c in row]) + "\n")


def main():
    testName = time.time()
    testFolder = f"experiments/performances/{testName}"

    pathlib.Path(testFolder).mkdir(parents=True, exist_ok=True)

    f = open(f"{testFolder}/results.csv", "w")

    printResults(
        file=f,
        domain="DOMAIN",
        problem="PROBLEM",
        preTime="PRE. TIME",
        planTime="PLAN TIME",
        totalTime="TOT TIME",
        planLength="PLAN LEN."
    )

    for (domainName, domainObj) in domains.items():
        folder = f"files/{domainObj['folder']}"
        domainFile = f"{folder}/{domainObj['domain']}"
        problemFolder = f"{folder}/{domainObj['problems-folder']}"

        problemFiles = natsort.natsorted(os.listdir(problemFolder))

        domainResultsFolder = f"{testFolder}/{domainName}"
        os.mkdir(domainResultsFolder)

        for problemFile in problemFiles:
            problem: Problem
            gDomain: GroundedDomain
            pddl2smt: PDDL2SMT
            solution: SMTSolution

            time.sleep(1)

            try:
                tic = time.perf_counter()
                domain: Domain = Domain.fromFile(domainFile)
                problem: Problem = Problem.fromFile(f"{problemFolder}/{problemFile}")

                gDomain: GroundedDomain = domain.ground(problem)
                pddl2smt: PDDL2SMT = PDDL2SMT(gDomain, problem, HORIZON)

                solver: SMTSolver = SMTSolver()
                solver.addAssertions(pddl2smt.rules)

                tocPreprocessing = time.perf_counter()
                solution: SMTSolution = solver.solve()

                plan: NumericPlan = pddl2smt.getPlanFromSolution(solution)
                plan.validate(problem)
                tocSolving = time.perf_counter()

                printResults(
                    file=f,
                    domain=domainName,
                    problem=problemFile,
                    preTime=tocPreprocessing - tic,
                    planTime=tocSolving - tocPreprocessing,
                    totalTime=tocSolving - tic,
                    planLength=len(plan),
                )

                planFile = open(f"{domainResultsFolder}/{problemFile}", "w")
                planFile.write(plan.toValString())
                planFile.close()

            except Exception:
                printResults(
                    file=f,
                    domain=domainName,
                    problem=problemFile,
                    preTime="ERROR",
                    planTime="ERROR",
                    totalTime="ERROR",
                    planLength=0,
                )

                planFile = open(f"{domainResultsFolder}/ERRORED_{problemFile}", "w")
                planFile.write(traceback.format_exc())
                planFile.close()


if __name__ == '__main__':
    main()
