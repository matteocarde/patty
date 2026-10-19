import csv
import csv
import os
import shutil
import statistics
from typing import Dict

import numpy as np
from matplotlib import pyplot as plt

from benchmarks.tables.ices.planners import ICES_PLANNERS
from benchmarks.tables.ices.table_all import TABLE_ICES_PLANNERS
from classes.CloudLogger import CloudLogger
from classes.Result import Result

PLANNERS = {
    "PATTY-ICES": r"\textsc{Patty}",
    # "PATTY-ICES-NO-ROLLING": r"\textsc{Patty}_\textsc{nr}",
    # "PATTY-T-SIGMA-ASTAR": r"\textsc{Patty}_\Sigma",
    # "ANMLSMT": r"\textsc{AnmlSMT}",
    "TAMER": r"\textsc{Tamer}",
}

DOMAINS = {"temporal/instradi-deadline/anml"}
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
    exp = "2026-10-18-ABLATIONS-AIJ-v3"
    joinWith = [
        (exp, [
            "PATTY-ICES",
            "TAMER"
        ])
    ]

    file = f"benchmarks/results/csv/{exp}.csv"

    folder = f'benchmarks/latex/{exp}-deadline'
    if os.path.exists(folder):
        shutil.rmtree(folder)
    os.mkdir(folder)

    if os.path.exists(file):
        os.remove(file)

    for (exp2, keepSolvers) in joinWith:
        CloudLogger.appendLogs(exp2, file, keepSolvers)

    joinWith = [file]

    aResults: [Result] = []
    for fileJoin in joinWith:
        with open(fileJoin, "r") as f:
            reader = csv.reader(f, delimiter=",")
            for i, line in enumerate(reader):
                if not line:
                    continue
                r = Result.fromCSVLine(line[0].split(","))
                r.problem = r.problem[:-5]
                aResults.append(r)

    resultsByPlanner = dict()
    planners = PLANNERS.keys()

    minX = 10000
    maxX = 0
    for r in aResults:
        resultsByPlanner[r.solver] = resultsByPlanner.setdefault(r.solver, dict())
        i = int(r.problem[1:].replace("_problem", ""))
        minX = min(minX, i)
        maxX = max(maxX, i)
        resultsByPlanner[r.solver][i] = r

    plots = [{
        "key": "time",
        "yLabel": "Planning Time",
        "xLabel": "Deadline",
        "steps": 5000,
        "min": 500,
        "scalingFactor": 1000,
        "yScale": "linear",
        "yLim": 300
    }]

    folder = f"benchmarks/figures/{exp}"
    if os.path.exists(folder):
        shutil.rmtree(folder)
    os.mkdir(folder)

    for i, p in enumerate(plots):
        arrayByPlanner: Dict[str, np.ndarray] = dict()
        for planner, results in resultsByPlanner.items():
            arrayByPlanner[planner] = np.array([results[i].time for i in range(minX, maxX + 1, 5)])

        X = np.linspace(minX, maxX, 21)
        plt.rcParams.update({
            "text.usetex": True,
            "figure.figsize": [12.50, 4],
            "figure.autolayout": True,
            'font.size': 22
        })

        figs, ax = plt.subplots(1, 1)

        ax.grid()
        ax.set_xlabel(p["xLabel"])
        ax.set_xlim([minX, maxX])
        ax.set_ylim([0, p["yLim"]])
        ax.set_ylabel(p["yLabel"])
        ax.set_yscale(p["yScale"])
        ax.set_xticks(np.linspace(minX, maxX, 21))
        ax.tick_params(axis="x", labelsize=14)
        ax.tick_params(axis="y", labelsize=14)

        for planner in planners:
            if planner not in arrayByPlanner:
                continue
            # arrayByPlanner[planner][0] = 0
            ax.plot(X, arrayByPlanner[planner] / p["scalingFactor"], label=f'${PLANNERS[planner]}$',
                    linestyle="-", linewidth=2)

        ax.legend(loc="upper right", fontsize="10")

        filename = f"{exp}-{p['key']}-deadline.pdf"
        plt.savefig(f'{folder}/{filename}', bbox_inches='tight', pad_inches=0.01)
        # plt.show()
        os.system(f"open {folder}/{filename}")


if __name__ == '__main__':
    main()
