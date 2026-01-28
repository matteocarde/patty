import copy
import csv
import json
import os
import shutil
import statistics
import sys
from typing import Dict, List, Set

import numpy as np
from matplotlib import pyplot as plt
from sympy.physics.continuum_mechanics.beam import numpy

from benchmarks.tables.ices.domains import ICES_DOMAINS
from benchmarks.tables.ices.planners import ICES_PLANNERS
from benchmarks.tables.ices.table_all import ICES_ALL, TABLE_ICES_PLANNERS
from classes.CloudLogger import CloudLogger
from classes.Result import Result

SOLVERS = {
    "PATTY-T-OR-ASTAR": r"\textsc{Patty}",
    # "PATTY-T-SIGMA-ASTAR": r"\textsc{Patty}_\Sigma",
    "ANMLSMT": r"\textsc{AnmlSMT}",
    "ITSAT": r"\textsc{ITSat}",
    "LPG": r"\textsc{LPG}",
    "OPTIC": r"\textsc{Optic}",
    "TFD": r"\textsc{TFD}",
}

DOMAINS = {
    "propositional": {"temporal/cushing",
                      "temporal/match-ac",
                      "temporal/match-ms",
                      "temporal/oversub",
                      "temporal/painter",
                      "temporal/bottles-pour",
                      "temporal/bottles-shake",
                      "temporal/bottles-pack",
                      "temporal/bottles-all",
                      "temporal/majsp"
                      }
}

TIMEOUT = 300 * 1000


def round(fValue, n):
    return '{:.{n}f}'.format(fValue, n=n)


def rVec(v, n):
    if not v:
        return "-"
    mean = statistics.mean(v)
    return round(mean, n)


def transformTextValue(v):
    if v in {"-", "*"}:
        return v
    val = float(v)
    if val > 1000:
        return round(val / 1000, 1) + "k"
    return v


def main():
    # Parsing the results
    exp = "2025-12-16-ICES-REALLY-FINAL-v7"
    joinWith = [
        (exp, [
            "PATTY-ICES",
        ]),
        ("2025-12-16-ICES-REALLY-FINAL-v6", [
            "TAMER",
            "ANMLSMT",
        ]),
        ("2025-12-16-ICES-REALLY-FINAL-v4", [
            "PATTY-ICES",
        ]),
        ("2024-01-14-TOTAL-v1", [
            "PATTY-T-OR-ASTAR",
            "ITSAT",
            "LPG",
            "OPTIC",
            "TFD",
        ])
    ]

    file = f"benchmarks/results/csv/{exp}.csv"

    folder = f'benchmarks/latex/{exp}'
    if os.path.exists(folder):
        shutil.rmtree(folder)
    os.mkdir(folder)

    if os.path.exists(file):
        os.remove(file)

    for (exp2, keepSolvers) in joinWith:
        CloudLogger.appendLogs(exp2, file, keepSolvers)

    tables = [
        ("all", ICES_ALL)
    ]

    PLANNERS = ICES_PLANNERS

    joinWith = [file]
    # joinWith = [file]

    oversub_instances = list(ICES_DOMAINS["temporal/oversub"]["instances"])

    aResults: [Result] = []
    for fileJoin in joinWith:
        with open(fileJoin, "r") as f:
            reader = csv.reader(f, delimiter=",")
            oversubIndex = dict()
            for i, line in enumerate(reader):
                if not line:
                    continue
                r = Result.fromCSVLine(line[0].split(","))
                r.problem = r.problem[:-5]
                if "/anml" in r.domain and "instradi" not in r.domain:
                    r.domain = r.domain.replace("/anml", "")
                if r.domain == "temporal/oversub":
                    oversubIndex.setdefault(r.solver, 0)
                    if oversubIndex[r.solver] < len(oversub_instances):
                        r.problem = oversub_instances[oversubIndex[r.solver]]
                        oversubIndex[r.solver] += 1
                    pass
                aResults.append(r)

    dOrig = dict()
    planners = TABLE_ICES_PLANNERS.keys()

    for r in aResults:
        dOrig[r.domain] = dOrig.setdefault(r.domain, dict())
        dOrig[r.domain][r.solver] = dOrig[r.domain].setdefault(r.solver, dict())
        dOrig[r.domain][r.solver][r.problem] = dOrig[r.domain][r.solver].setdefault(r.problem, list())
        dOrig[r.domain][r.solver][r.problem].append(r)

    resultsByPlanner: Dict[str, List[Result]] = dict()
    for domain, domainDict in dOrig.items():
        if domain not in ICES_DOMAINS:
            continue
        for planner, plannerDict in domainDict.items():
            if planner not in planners:
                continue
            resultsByPlanner.setdefault(planner, list())
            for problem, problemList in plannerDict.items():
                if problem not in ICES_DOMAINS[domain]["instances"]:
                    continue
                resultsByPlanner[planner].append(problemList[0])

    plots = [{
        "key": "time",
        "yLabel": "Planning Time [s]",
        "xLabel": "Solved Instances",
        "steps": 5000,
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
            "figure.figsize": [12.50, 4],
            "figure.autolayout": True,
            'font.size': 22
        })

        figs, ax = plt.subplots(1, 1)
        arrayByPlanner: Dict[str, np.ndarray] = dict()
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
        Y = np.linspace(p["min"], 300 * 1000, p["steps"])
        cactusByPlanner: Dict[str, List[float]] = dict()
        for planner, array in arrayByPlanner.items():
            cactusByPlanner[planner] = [len(array[array <= y]) for y in Y]

        ax.grid()
        ax.set_xlabel(p["xLabel"])
        ax.set_xlim([0, 190])
        ax.set_ylim([0, p["yLim"]])
        ax.set_ylabel(p["yLabel"])
        ax.set_yscale(p["yScale"])
        ax.set_xticks(np.linspace(0, 190, 20))
        ax.tick_params(axis="x", labelsize=14)
        ax.tick_params(axis="y", labelsize=14)

        for planner in planners:
            pInfo = ICES_PLANNERS[planner]
            cactusByPlanner[planner][0] = 0
            ax.plot(cactusByPlanner[planner], Y / p["scalingFactor"], label=f'${pInfo["name"]}$',
                    linestyle=pInfo["style"], linewidth=2)

        ax.legend(loc="lower right", fontsize="10")

        filename = f"{exp}-{p['key']}.pdf"
        plt.savefig(f'{folder}/{filename}', bbox_inches='tight', pad_inches=0.01)
        # plt.show()
        os.system(f"open {folder}/{filename}")


if __name__ == '__main__':
    main()
