import csv
import os
import shutil
from typing import Dict, List, Tuple

from matplotlib import pyplot as plt, gridspec
from matplotlib.pyplot import gcf
from sympy.physics.continuum_mechanics.beam import numpy

from classes.CloudLogger import CloudLogger
from classes.Result import Result

if __name__ == '__main__':
    # Parsing the results
    exp = "2025-01-17-IJCAI-CES-v5"
    joinWith = [
        (exp, ["PATTY-CES", "PATTY-CES-NO-TC", "PATTY-CES-NO-C"]),
        # ("2025-01-16-IJCAI-CES-v3", ["PATTY-CES", "PATTY-CES-NO-TC", "PATTY-CES-NO-TC-NO-C"])
    ]
    file = f"benchmarks/results/csv/{exp}.csv"
    if os.path.exists(file):
        os.remove(file)

    folder = f'benchmarks/figures/{exp}-tapes'
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

    aResults = Result.joinPorfolios(aResults, {
        "ENHSP-SAT-HADD": "ENHSP",
        "ENHSP-SAT-HRADD": "ENHSP",
        "ENHSP-SAT-HMAX": "ENHSP",
    })

    DOMAIN = "ces/tapes"
    DIMENSIONS = {
        "tapes": {
            "xAxis": "Number of loops/counters (K)",
            "filenameIndex": 1
        },
        "length": {
            "xAxis": "Length of loops (L)",
            "filenameIndex": 2
        },
        "bits": {
            "xAxis": "Number of bits (B)",
            "filenameIndex": 0
        },
    }

    PROPERTIES = {
        "bound": {
            "yAxis": "Bound",
            "showClosureTime": False,
            "scalingFactor": 1,
            "yLimit": [0, 72]
        },
        "time": {
            "yAxis": "Planning Time [s]",
            "showClosureTime": True,
            "scalingFactor": 1000,
            "yLimit": [0, 600]
        }
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
                prob = [int(i) for i in prob]

                points[d][p][r.solver].setdefault(x, list())
                points[d][p][r.solver][x].append((prob, y))

                if SOLVERS[r.solver]["hasClosure"]:
                    y = r.transitiveClosureTime
                    closurePoints[d][p][r.solver].setdefault(x, list())
                    closurePoints[d][p][r.solver][x].append((prob, y))

    nOfGraphs = len(DIMENSIONS) * len(PROPERTIES)
    plt.rcParams.update({
        "text.usetex": True,
        "figure.figsize": [7.50, 2.0 * nOfGraphs],
        "figure.autolayout": True,
        'font.size': 12
    })

    figs, axs = plt.subplots(nOfGraphs, 1)

    i = 0
    for d, dDict in DIMENSIONS.items():
        for p, pDict in PROPERTIES.items():
            ax = axs[i]
            i += 1

            ax.grid()
            ax.set_xlabel(dDict["xAxis"])
            ax.set_ylabel(pDict["yAxis"])

            for solver, sDict in SOLVERS.items():
                xs = sorted(points[d][p][solver].keys())
                print(d, p, solver, [(x, min(points[d][p][solver][x])[0]) for x in xs])
                ys = [min(points[d][p][solver][x])[1] / pDict["scalingFactor"] for x in xs]
                ax.plot(xs, ys, color=sDict["color"], label=sDict["label"])

                if pDict["showClosureTime"] and sDict["hasClosure"]:
                    ys = [min(closurePoints[d][p][solver][x])[1] / pDict["scalingFactor"] for x in xs]
                    ax.plot(xs, ys, linestyle="dashed", color=sDict["color"], label=f"TC {sDict['label']}")

            maxY = 17
            ax.set_xticks(range(3, maxY + 1))
            ax.set_xlim([3, maxY])

            # ax.set_yscale("log")
            ax.set_ylim(pDict["yLimit"])
            ticks = numpy.linspace(pDict["yLimit"][0], pDict["yLimit"][1], 5)
            ax.set_yticks(ticks)

            ax.legend(loc="upper left", fontsize="8")

            ax.spines['top'].set_visible(False)
            ax.spines['right'].set_visible(False)
            ax.spines['bottom'].set_visible(False)
            ax.spines['left'].set_visible(False)
    plt.plot([0.05, 0.97], [1 / 3, 1 / 3], color='gray', linestyle="dashed", lw=1, transform=gcf().transFigure,
             clip_on=False)
    plt.plot([0.05, 0.97], [2 / 3, 2 / 3], color='gray', linestyle="dashed", lw=1, transform=gcf().transFigure,
             clip_on=False)

    plt.savefig(f'{folder}/{exp}-tapes-{d}.pdf', bbox_inches='tight', pad_inches=0.01)
    # plt.show()
    os.system(f"open {folder}/{exp}-tapes-{d}.pdf")
