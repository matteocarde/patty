import os
import pathlib
import sys
import time
import traceback

import func_timeout
from natsort import natsort

from Domain import Domain, GroundedDomain
from NumericPlan import NumericPlan
from Problem import Problem
from src.plan.PDDL2SMT import PDDL2SMT
from src.smt.SMTSolution import SMTSolution
from src.smt.SMTSolver import SMTSolver

domains = {

    # "block-grouping": {
    #     "folder": "block-grouping",
    #     "domain": "domain.pddl",
    #     "problems-folder": "instances/",
    #     "horizon": 1
    # },
    # "fn-counters": {
    #     "folder": "fn-counters",
    #     "domain": "domain.pddl",
    #     "problems-folder": "instances/",
    #     "horizon": 20
    # },
    # "fn-counters-inv": {
    #     "folder": "fn-counters-inv",
    #     "domain": "domain.pddl",
    #     "problems-folder": "instances/",
    #     "horizon": 1
    # },
    # "fn-counters-rnd": {
    #     "folder": "fn-counters-rnd",
    #     "domain": "domain.pddl",
    #     "problems-folder": "instances/",
    #     "horizon": 1
    # },
    # "farmland": {
    #     "folder": "farmland",
    #     "domain": "domain.pddl",
    #     "problems-folder": "instances/",
    #     "horizon": 5
    # },
    # "gardening": {
    #     "folder": "gardening",
    #     "domain": "domain.pddl",
    #     "problems-folder": "instances/",
    #     "horizon": 10
    # },
    # "plant-watering": {
    #     "folder": "plant-watering",
    #     "domain": "domain.pddl",
    #     "problems-folder": "instances/",
    #     "horizon": "CUSTOM"
    # },
    # "sailing": {
    #     "folder": "sailing",
    #     "domain": "domain.pddl",
    #     "problems-folder": "instances/",
    #     "horizon": "CUSTOM"
    # },
    "rover": {
        "folder": "rover",
        "domain": "domain.pddl",
        "problems-folder": "instances/",
        "horizon": 5
    }
}

TIMEOUT = 60

OPTIMIZE = True


def myRound(n: str or float):
    return n if type(n) == str else round(n, 2)


def printResults(file, domain, problem, preTime, firstTime, lastTime, firstLength, planTime, totalTime, planFound,
                 planLength, isOptimal, rules):
    row = [domain, problem, myRound(preTime), myRound(firstTime), myRound(lastTime), firstLength, myRound(planTime),
           myRound(totalTime), planLength, planFound, isOptimal, rules]

    print('| {:<15} | {:<25} | {:^7} | {:^7} | {:^7} | {:^7} | {:^7} | {:^7} | {:^7} | {:^7} | {:^5} | {:^8} |'.format(
        *row))
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
        preTime="PRE. T",
        firstTime="FIRST T",
        lastTime="LAST T",
        firstLength="FIRST L",
        planTime="PLAN T",
        totalTime="TOT T",
        planLength="PLAN L",
        planFound="IS PLAN",
        isOptimal="OPT",
        rules="RULES"
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

                horizon = domainObj["horizon"]
                if horizon == "CUSTOM":
                    if domainName == "sailing":
                        horizon = max(6, int(problemFile.split("_")[2]) + 1)
                    if domainName == "plant-watering":
                        horizon = max(6, int(problemFile.split("_")[1]) + 1)

                pddl2smt: PDDL2SMT = PDDL2SMT(gDomain, problem, horizon)

                solver: SMTSolver = SMTSolver(pddl2smt)

                tocPreprocessing = time.perf_counter()

                tocFirstSolution = 0
                firstSolutionLength = 0
                tocLastSolution = 0
                lastPlan: NumericPlan or bool = False

                def onSolutionFound(plan: NumericPlan):
                    nonlocal tocFirstSolution, firstSolutionLength, lastPlan, tocLastSolution
                    lastPlan = plan
                    tocLastSolution = time.perf_counter()
                    if tocFirstSolution == 0:
                        firstSolutionLength = len(plan)
                        tocFirstSolution = time.perf_counter()

                try:
                    if OPTIMIZE:
                        lastPlan = func_timeout.func_timeout(TIMEOUT, solver.optimizeBinary, args=(1, onSolutionFound))
                    else:
                        lastPlan = func_timeout.func_timeout(TIMEOUT, solver.solve)
                        onSolutionFound(lastPlan)
                except func_timeout.FunctionTimedOut:
                    pass

                planFound = lastPlan is not False
                if isinstance(lastPlan, NumericPlan):
                    lastPlan.validate(problem)

                tocSolving = time.perf_counter()

                printResults(
                    file=f,
                    domain=domainName,
                    problem=problemFile,
                    preTime=tocPreprocessing - tic,
                    firstTime=tocFirstSolution - tic,
                    lastTime=tocLastSolution - tic,
                    firstLength=firstSolutionLength,
                    planTime=tocSolving - tocPreprocessing,
                    totalTime=tocSolving - tic,
                    planFound=planFound,
                    planLength=len(lastPlan) if planFound else 0,
                    isOptimal=lastPlan.optimal if planFound else False,
                    rules=len(pddl2smt.rules)
                )

                planFile = open(f"{domainResultsFolder}/{problemFile}", "w")
                planFile.write(lastPlan.toValString())
                planFile.close()
                solver.exit()

            except Exception:
                printResults(
                    file=f,
                    domain=domainName,
                    problem=problemFile,
                    preTime="ERROR",
                    firstTime="ERROR",
                    lastTime="ERROR",
                    firstLength="ERROR",
                    planTime="ERROR",
                    totalTime="ERROR",
                    planFound=False,
                    planLength=0,
                    isOptimal=False,
                    rules="ERROR"
                )
                print(traceback.format_exc(), file=sys.stderr)
                planFile = open(f"{domainResultsFolder}/ERRORED_{problemFile}", "w")
                planFile.write(traceback.format_exc())
                planFile.close()


if __name__ == '__main__':
    main()
