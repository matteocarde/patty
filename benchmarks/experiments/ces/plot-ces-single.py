import csv
import os
import shutil
from typing import Dict, List, Tuple

import numpy
from matplotlib import pyplot as plt

from classes.CloudLogger import CloudLogger
from classes.Result import Result

if __name__ == '__main__':
    # Parsing the results
    exp = "2025-01-20-IJCAI-CES-FINAL-v2"
    joinWith = [
        (exp, ["PATTY-CES", "PATTY-CES-NO-TC", "PATTY-CES-NO-C"]),
        # ("2025-01-16-IJCAI-CES-v3", ["PATTY-CES", "PATTY-CES-NO-TC", "PATTY-CES-NO-TC-NO-C"])
    ]
    file = f"benchmarks/results/csv/{exp}.csv"
    if os.path.exists(file):
        os.remove(file)

    folder = f'benchmarks/figures/{exp}-single'
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

    DOMAINS = {
        "ces/counter": {
            "xAxis": "Number of bits (B)",
            "xLimit": [3, 14],
            "yLimit": {
                "bound": [0, 300],
                "time": [0, 600],
                "transitiveClosureSize": [0, 500]
            }
        },
        "ces/meeting": {
            "xAxis": "Cube side (L)",
            "xLimit": [3, 15],
            "yLimit": {
                "bound": [0, 32],
                "time": [0, 600],
                "transitiveClosureSize": [0, 500]
            }
        },
        "ces/meeting-no-pacman": {
            "xAxis": "Cube side (L)",
            "xLimit": [3, 15],
            "yLimit": {
                "bound": [0, 32],
                "time": [0, 600],
                "transitiveClosureSize": [0, 200]
            }
        }
    }

    PROPERTIES = {
        "bound": {
            "yAxis": "Bound",
            "showClosureTime": False,
            "scalingFactor": 1
        },
        "time": {
            "yAxis": "Planning Time [s]",
            "showClosureTime": True,
            "scalingFactor": 1000
        },
        # "transitiveClosureSize": {
        #     "yAxis": "TC Size",
        #     "showClosureTime": False,
        #     "scalingFactor": 1
        # }
    }

    SOLVERS = {
        "PATTY-CES": {
            "color": "green",
            "label": r"$\Pi^+$",
            "hasClosure": True
        },
        # "PATTY-CES-NO-C": {
        #     "color": "blue",
        #     "label": r"$\Pi^+_\top$",
        #     "hasClosure": True
        # },
        "PATTY-CES-NO-TC": {
            "color": "red",
            "label": r"$\Pi^0$",
            "hasClosure": False
        },
    }

    # points[domain][property][solver] = List[Tuple[int,float]]
    points: Dict[str, Dict[str, Dict[str, List[Tuple[int, float]]]]] = dict()
    closurePoints: Dict[str, Dict[str, Dict[str, List[Tuple[int, float]]]]] = dict()

    for d in DOMAINS.keys():
        points[d] = dict()
        closurePoints[d] = dict()
        for p in PROPERTIES.keys():
            points[d][p] = dict()
            closurePoints[d][p] = dict()
            for s in SOLVERS.keys():
                points[d][p][s] = list()
                closurePoints[d][p][s] = list()

    for r in aResults:
        if r.domain not in DOMAINS or r.solver not in SOLVERS or not r.solved:
            continue
        for p in PROPERTIES:
            x = int(r.problem.replace(".pddl", "").split("-")[1])
            y = r.get(p)

            points[r.domain][p][r.solver].append((x, y))
            if SOLVERS[r.solver]["hasClosure"]:
                y = r.transitiveClosureTime
                closurePoints[r.domain][p][r.solver].append((x, y))

    pass

    for d, dDict in DOMAINS.items():

        plt.rcParams.update({
            "text.usetex": True,
            "figure.figsize": [7.50, 4.0],
            "figure.autolayout": True,
            'font.size': 16
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

            for solver, sDict in SOLVERS.items():
                ps = sorted(points[d][p][solver])
                x = [p[0] for p in ps]
                y = [p[1] / pDict["scalingFactor"] for p in ps]
                ax.plot(x, y, color=sDict["color"], label=sDict["label"])

                if pDict["showClosureTime"] and sDict["hasClosure"]:
                    ps = sorted(closurePoints[d][p][solver])
                    x = [p[0] for p in ps]
                    y = [p[1] / pDict["scalingFactor"] for p in ps]
                    ax.plot(x, y, linestyle="dashed", color=sDict["color"], label=f"TC {sDict['label']}")

            ax.legend(loc="upper center", fontsize="13", ncol=3)

            ax.set_xlim(dDict["xLimit"])
            ax.set_xticks(range(dDict["xLimit"][0], dDict["xLimit"][1] + 1))
            ax.set_ylim(dDict["yLimit"][p])
            ticks = numpy.linspace(dDict["yLimit"][p][0], dDict["yLimit"][p][1], 5)
            ax.set_yticks(ticks)

            ax.spines['top'].set_visible(False)
            ax.spines['right'].set_visible(False)
            ax.spines['bottom'].set_visible(False)
            ax.spines['left'].set_visible(False)

        domain = d.replace("ces/", "")
        plt.savefig(f'{folder}/{exp}-{domain}.pdf', bbox_inches='tight', pad_inches=0.01)
        # plt.show()
        os.system(f"open {folder}/{exp}-{domain}.pdf")
