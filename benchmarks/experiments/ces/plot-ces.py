import csv
import json
import os
import shutil
import statistics
import sys
from typing import Dict, List, Set, Tuple

from matplotlib import pyplot as plt

from classes.CloudLogger import CloudLogger
from classes.Result import Result


def main():
    # Parsing the results
    exp = "2024-10-23-CES-v6"
    file = f"benchmarks/results/csv/{exp}.csv"

    CloudLogger.saveLogs(exp, file)

    joinWith = [file]

    aResults: [Result] = []
    for fileJoin in joinWith:
        with open(fileJoin, "r") as f:
            reader = csv.reader(f, delimiter=",")
            for i, line in enumerate(reader):
                aResults.append(Result.fromCSVLine(line[0].split(",")))

    # Joining together portfolios
    results = Result.joinPorfolios(aResults, {
        "ENHSP-SAT-HADD": "ENHSP",
        "ENHSP-SAT-HMAX": "ENHSP",
        "ENHSP-SAT-HMRP": "ENHSP",
    })

    points: Dict[str, Dict[str, Dict[int, List[Tuple[int, float]]]]] = dict()

    bits = set()
    counters = set()

    properties = ["time", "bound"]
    closurePoints: Dict[int, List[Tuple[int, float]]] = dict()

    for p in properties:
        points[p] = dict()
        for r in results:
            b = int(r.problem.replace(".pddl", "").split("-")[1])
            bits.add(b)
            c = int(r.problem.replace(".pddl", "").split("-")[2])
            counters.add(c)

            if not r.solved:
                continue

            if p == "bound" and r.bound < 0:
                continue

            if p == "time" and r.transitiveClosureTime > 0:
                closurePoints.setdefault(c, list())
                closurePoints[c].append((b, r.transitiveClosureTime / 1000))

            property = r.time / 1000 if p == "time" else r.bound
            points[p].setdefault(r.solver, dict())
            points[p][r.solver].setdefault(c, list())
            points[p][r.solver][c].append((b, property))

    plt.rcParams.update({
        "text.usetex": True,
        "figure.figsize": [7.50, 4.0],
        "figure.autolayout": True
    })

    lines = [{
        "solver": "ENHSP",
        "color": "blue",
        "label": r"$\textsc{enhsp}$"
    }, {
        "solver": "PATTY-CES",
        "color": "green",
        "label": r"$\textsc{p}$"
    }, {
        "solver": "MADAGASCAR",
        "color": "red",
        "label": r"$\textsc{mpc}$"
    }]

    fCounters = 5
    figs, axs = plt.subplots(2, 1)
    for i, p in enumerate(properties):
        ax = axs[i]
        ax.grid()
        ax.set_xlabel(r"Number of bits")
        ax.set_ylabel("Planning Time [s]" if p == "time" else "Bound")
        # ax.set_xscale("log")
        if p == "time":
            ps = sorted(closurePoints[fCounters])
            x = [p[0] for p in ps]
            y = [p[1] for p in ps]
            ax.plot(x, y, linestyle="dashed", color="black", label=r"${\textsc{tc}}$")

        for line in lines:
            solver = line["solver"]
            if not solver in points[p]:
                continue
            ps = sorted(points[p][solver][fCounters])
            x = [p[0] for p in ps]
            y = [p[1] for p in ps]
            ax.plot(x, y, color=line["color"], label=line["label"])

        ax.legend(loc="upper left", fontsize="8")

        # ax.spines['top'].set_visible(False)
        # ax.spines['right'].set_visible(False)

        ax.set_xticks(range(1, 13))
        if p == "bound":
            ax.set_yticks([0, 2, 4, 6, 8, 10])
        # ax.spines['bottom'].set_visible(False)
        # ax.spines['left'].set_visible(False)
        # ax.legend(loc="upper left", fontsize="8")

    folder = f'benchmarks/figures/{exp}'
    if os.path.exists(folder):
        shutil.rmtree(folder)
    os.mkdir(folder)
    plt.savefig(f'{folder}/{exp}.pdf', bbox_inches='tight', pad_inches=0.01)
    plt.show()


if __name__ == '__main__':
    main()
