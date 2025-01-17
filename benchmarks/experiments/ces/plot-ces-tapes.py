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
    exp = "2025-01-16-IJCAI-CES-v10"
    joinWith = [
        (exp, ["PATTY-CES", "PATTY-CES-NO-TC", "PATTY-CES-NO-C"]),
        # ("2025-01-16-IJCAI-CES-v3", ["PATTY-CES", "PATTY-CES-NO-TC", "PATTY-CES-NO-TC-NO-C"])
    ]
    file = f"benchmarks/results/csv/{exp}.csv"
    if os.path.exists(file):
        os.remove(file)

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

    DOMAIN = "ces/tapes"
    DIMENSIONS = {
        "bits": {
            "xAxis": "Number of bits",
            "filenameIndex": 0
        },
        "tapes": {
            "xAxis": "Number of tapes",
            "filenameIndex": 1
        },
        "length": {
            "xAxis": "Length of tape",
            "filenameIndex": 2
        },
    }

    PROPERTIES = {
        "bound": {
            "yAxis": "Bound",
            "showClosureTime": False
        },
        "time": {
            "yAxis": "Planning Time [s]",
            "showClosureTime": True
        }
    }

    SOLVERS = {
        "PATTY-CES": {
            "color": "blue",
            "label": r"$\Pi^+_C$",
            "hasClosure": True
        },
        "PATTY-CES-NO-C": {
            "color": "red",
            "label": r"$\Pi^+_\top$",
            "hasClosure": True
        },
        "PATTY-CES-NO-TC": {
            "color": "green",
            "label": r"$\Pi^0$",
            "hasClosure": False
        },
    }

    # points[domain][property][solver] = List[Tuple[int,float]]
    points: Dict[str, Dict[str, Dict[str, Dict[int, List[Tuple[str, float]]]]]] = dict()
    closurePoints: Dict[str, Dict[str, Dict[str, Dict[int, List[Tuple[str, float]]]]]] = dict()

    for d in DIMENSIONS.keys():
        points[d] = dict()
        closurePoints[d] = dict()
        for p in PROPERTIES.keys():
            points[d][p] = dict()
            closurePoints[d][p] = dict()
            for s in SOLVERS.keys():
                points[d][p][s] = dict()
                closurePoints[d][p][s] = dict()

    for r in aResults:
        if r.domain != DOMAIN or r.solver not in SOLVERS or not r.solved:
            continue
        for d, dDict in DIMENSIONS.items():
            for p in PROPERTIES:
                prob = r.problem.replace(".pddl", "").split("-")[1:]
                x = int(prob[dDict["filenameIndex"]])
                y = r.get(p)
                prob = "-".join(prob)

                points[d][p][r.solver].setdefault(x, list())
                points[d][p][r.solver][x].append((prob, y))

                if SOLVERS[r.solver]["hasClosure"]:
                    y = r.transitiveClosureTime
                    closurePoints[d][p][r.solver].setdefault(x, list())
                    closurePoints[d][p][r.solver][x].append((prob, y))

    for d, dDict in DIMENSIONS.items():

        plt.rcParams.update({
            "text.usetex": True,
            "figure.figsize": [7.50, 4.0],
            "figure.autolayout": True
        })

        figs, axs = plt.subplots(len(PROPERTIES), 1)
        i = 0
        for p, pDict in PROPERTIES.items():
            ax = axs[i]
            i += 1

            ax.grid()
            ax.set_xlabel(dDict["xAxis"])
            ax.set_ylabel(pDict["yAxis"])
            # ax.set_xscale("log")
            # if p == "time":
            #     ps = sorted(closurePoints[fCounters])
            #     x = [p[0] for p in ps]
            #     y = [p[1] for p in ps]
            #     ax.plot(x, y, linestyle="dashed", color="black", label=r"${\textsc{tc}}$")

            for solver, sDict in SOLVERS.items():
                xs = sorted(points[d][p][solver].keys())
                ys = [min(points[d][p][solver][x])[1] for x in xs]
                ax.plot(xs, ys, color=sDict["color"], label=sDict["label"])

                if pDict["showClosureTime"] and sDict["hasClosure"]:
                    ys = [min(closurePoints[d][p][solver][x])[1] for x in xs]
                    ax.plot(xs, ys, linestyle="dashed", color=sDict["color"], label=f"TC {sDict['label']}")

            ax.legend(loc="upper left", fontsize="8")

            # ax.spines['top'].set_visible(False)
            # ax.spines['right'].set_visible(False)

            # ax.set_xticks(range(1, 13))
            # if p == "bound":
            #     ax.set_yticks([0, 2, 4, 6, 8, 10])
            # ax.spines['bottom'].set_visible(False)
            # ax.spines['left'].set_visible(False)
            # ax.legend(loc="upper left", fontsize="8")

        plt.savefig(f'{folder}/{exp}-tapes-{d}.pdf', bbox_inches='tight', pad_inches=0.01)
        # plt.show()
        os.system(f"open {folder}/{exp}-tapes-{d}.pdf")


if __name__ == '__main__':
    main()
