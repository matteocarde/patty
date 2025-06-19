import csv
import os
import shutil
from typing import Dict, List, Tuple

import numpy as np
from matplotlib import pyplot as plt
from numpy import ndarray

from benchmarks.tables.aij.domains import AIJ_DOMAINS
from benchmarks.tables.aij.planners import AIJ_PLANNERS
from classes.CloudLogger import CloudLogger
from classes.Result import Result


def main():
    # Parsing the results
    exp = "2025-06-19-CHRPA-v4"
    joinWith = [
        (exp, ["PATTY-C"]),
        ("2025-05-26-AIJ-REBUTTAL-v3", ["R2E+ROLL"]),
        ("2024-11-12-DOMAINS-v7", ["PATTY-A", "PATTY-L", "PATTY-M", "PATTY-R", "PATTY-E"]),
        ("2024-11-12-DOMAINS-v1", ["ENHSP-SAT-AIBR", "RANTANPLAN", "SPRINGROLL", "ENHSP-SAT-HADD",
                                   "ENHSP-SAT-HMRP", "METRIC-FF", "NFD", "OMT", "ENHSP-SOCS"]),
        ("2024-11-11-SOCS-v1", ["ENHSP-SOCS"]),
        ("2024-10-24-AIJ-v1", ["PATTY-R"]),
        ("2024-10-07-AIJ-FINAL-v10", ["PATTY-A"]),
        ("2024-10-07-AIJ-FINAL-v9", ["PATTY-E", "PATTY-L", "PATTY-M"]),
        ("2024-10-07-AIJ-FINAL-v7", ["RANTANPLAN"]),
        ("2024-10-07-AIJ-FINAL-v6", ["SPRINGROLL"]),
        ("2024-10-07-AIJ-FINAL-v5", ["OMT"]),
        ("2024-10-07-AIJ-FINAL-v2",
         ["ENHSP-SAT-AIBR", "PATTY-A", "PATTY-E", "ENHSP-SAT-HADD", "ENHSP-SAT-HMRP", "METRIC-FF", "NFD"])
    ]
    file = f"benchmarks/results/csv/{exp}.csv"

    folder = f'benchmarks/figures/{exp}'
    if os.path.exists(folder):
        shutil.rmtree(folder)
    os.mkdir(folder)

    for (exp2, keepSolvers) in joinWith:
        CloudLogger.appendLogs(exp2, file, keepSolvers)

    aResults: [Result] = []
    with open(file, "r") as f:
        reader = csv.reader(f, delimiter=",")
        for i, line in enumerate(reader):
            if not line:
                continue
            aResults.append(Result.fromCSVLine(line[0].split(",")))

    # Joining together portfolios
    results = Result.joinPorfolios(aResults, {
        "ENHSP-SAT-HADD": "ENHSP",
        "ENHSP-SAT-AIBR": "ENHSP",
        "ENHSP-SAT-HMRP": "ENHSP",
    })
    results = Result.splitRandom(results, "PATTY-R")

    dOrig = dict()
    planners = [
        "PATTY-E",
        "PATTY-A",
        "ENHSP-SOCS",
        "PATTY-C",
        "PATTY-R-MIN",
        "PATTY-R-MED",
        "PATTY-L",
        "PATTY-R-MAX",
        "ENHSP",
        "R2E+ROLL",
        "PATTY-M",
        "METRIC-FF",
        "NFD",
        "SPRINGROLL",
        "OMT",
        "RANTANPLAN"
    ]

    for r in results:
        dOrig[r.domain] = dOrig.setdefault(r.domain, dict())
        dOrig[r.domain][r.solver] = dOrig[r.domain].setdefault(r.solver, dict())
        dOrig[r.domain][r.solver][r.problem] = dOrig[r.domain][r.solver].setdefault(r.problem, list())
        dOrig[r.domain][r.solver][r.problem].append(r)

    resultsByPlanner: Dict[str, List[Result]] = dict()
    for domain, domainDict in dOrig.items():
        if domain not in AIJ_DOMAINS:
            continue
        for planner, plannerDict in domainDict.items():
            if planner not in planners:
                continue
            resultsByPlanner.setdefault(planner, list())
            for problem, problemList in plannerDict.items():
                if problem not in AIJ_DOMAINS[domain]["instances"]:
                    continue
                resultsByPlanner[planner].append(problemList[0])

    plots = [{
        "key": "time",
        "yLabel": "Planning Time [s]",
        "xLabel": "Solved Instances",
        "steps": 1000,
        "min": 500,
        "scalingFactor": 1000,
        "yScale": "linear",
        "yLim": 300
    },
    #     {
    #     "key": "planLength",
    #     "yLabel": "Plan Length",
    #     "xLabel": "Solved Instances",
    #     "steps": 1000,
    #     "yLim": 2500,
    #     "min": 1,
    #     "scalingFactor": 1,
    #     "yScale": "linear"
    # }
    ]

    folder = f"benchmarks/figures/CACTUS-{exp}"
    if os.path.exists(folder):
        shutil.rmtree(folder)
    os.mkdir(folder)

    for i, p in enumerate(plots):
        plt.rcParams.update({
            "text.usetex": True,
            "figure.figsize": [12.50, 6],
            "figure.autolayout": True,
            'font.size': 22
        })

        figs, ax = plt.subplots(1, 1)
        arrayByPlanner: Dict[str, ndarray] = dict()
        maxY = float("-inf")
        minY = float("+inf")
        for planner, results in resultsByPlanner.items():
            arrayByPlanner[planner] = np.array([r.get(p["key"]) for r in results if r.solved])
            print(planner, len(arrayByPlanner[planner]))
            minOfPlanner = min(arrayByPlanner[planner])
            minY = minOfPlanner if minOfPlanner < minY else minY
            maxOfPlanner = max(arrayByPlanner[planner])
            maxY = maxOfPlanner if maxOfPlanner > maxY else maxY

        print(p["key"], [p["min"], maxY])
        Y = np.linspace(p["min"], maxY, p["steps"])
        cactusByPlanner: Dict[str, List[float]] = dict()
        for planner, array in arrayByPlanner.items():
            cactusByPlanner[planner] = [len(array[array <= y]) for y in Y]

        ax.grid()
        ax.set_xlabel(p["xLabel"])
        ax.set_xlim([-10, 290])
        ax.set_ylim([0, p["yLim"]])
        ax.set_ylabel(p["yLabel"])
        ax.set_yscale(p["yScale"])

        for planner in planners:
            pInfo = AIJ_PLANNERS[planner]
            ax.plot(cactusByPlanner[planner], Y / p["scalingFactor"], label=f'${pInfo["name"]}$',
                    linestyle=pInfo["style"], linewidth=2)

        ax.legend(loc="upper left", fontsize="10")

        filename = f"{exp}-{p['key']}.pdf"
        plt.savefig(f'{folder}/{filename}', bbox_inches='tight', pad_inches=0.01)
        # plt.show()
        os.system(f"open {folder}/{filename}")


if __name__ == '__main__':
    main()
