import csv
import os
import re
import shutil
from typing import Dict, List, Tuple

from matplotlib import pyplot as plt
from matplotlib.axes import Subplot

from classes.Result import Result

TIMEOUT = 300000

PRINTONLY = ["PORTFOLIO"]
PLANNERS = {
    "ENHSP-SAT-HMRP",
    "ENHSP-SAT-HADD",
    "ENHSP-SAT-HMAX",
    "ENHSP-SAT-AIBR",
    "ENHSP-SAT-HRADD",
    # "ENHSP-SAT-BLIND",
    "ENHSP-OPT-HMRP",
    "ENHSP-OPT-HADD",
    "ENHSP-OPT-HMAX",
    "ENHSP-OPT-AIBR",
    "ENHSP-OPT-HRADD",
    "UPMURPHI"
}

LINES = {
    ("NODELTA", "-de 1 -dp 1 -dh 1"): {
        "id": "1DELTA",
        "name": r"$1\delta$",
        "type": "NODELTA",
        "config": "-de 1 -dp 1 -dh 1"
    },
    ("NODELTA", "-de 1 -dp 3 -dh 3"): {
        "id": "2DELTA",
        "name": r"$2\delta$",
        "type": "NODELTA",
        "config": "-de 1 -dp 5 -dh 5"
    },
    ("DELTA", "-de 1 -dp 1 -dh 1"): {
        "id": "KDELTA",
        "name": r"$K\delta$",
        "type": "DELTA",
        "config": "-de 1 -dp 1 -dh 1"
    }
}


def problemToInt(problem):
    return int(re.findall('problem-(.*?).pddl', problem)[0])
    pass


def main():
    filename = "2023-11-30-FINAL-v3.csv"
    file = f"benchmarks/results/{filename}"

    results: [Result] = []
    with open(file, "r") as f:
        reader = csv.reader(f, delimiter=",")
        for i, line in enumerate(reader):
            results.append(Result.fromCSVLine(line[0].split(",")))

    # Domain/Solver/Delta
    rDict: Dict[str, Dict[str, Dict[str, List[Result]]]] = dict()
    portfolio: Dict[str, Dict[str, Dict[str, List[Result]]]] = dict()

    for r in results:
        domain = r.domain.split("-")[0]
        type = r.domain.split("-")[1]
        heuristic = r.solver.split("[")[0]
        if heuristic not in PLANNERS:
            continue

        solver = heuristic.split("-")[0]

        config = r.solver.split("[")[1][:-1]
        if (type, config) not in LINES:
            continue
        line = LINES[(type, config)]
        id = line["id"]
        rDict[solver] = rDict.setdefault(solver, {})
        rDict[solver][id] = rDict[solver].setdefault(id, {})
        rDict[solver][id][r.problem] = rDict[solver][id].setdefault(r.problem, [])
        rDict[solver][id][r.problem].append(r)

        r.time = r.time if r.solved else TIMEOUT

    lines: Dict[str, List[Tuple[int, int]]] = dict()

    for (solver, solverDict) in rDict.items():
        for (line, lineDict) in solverDict.items():
            key = f"{solver}-{line}"
            lines[key] = []
            for (problem, problemList) in lineDict.items():
                alpha = int(problem.split("-")[1].split(".")[0])
                value = min([r.time for r in problemList]) / 1000
                lines[key].append((alpha, value))
            lines[key].sort(key=lambda l: l[0])

    plt.rcParams.update({
        "text.usetex": True,
        "figure.figsize": [7.50, 2 * len(PRINTONLY)],
        "figure.autolayout": True
    })

    fig, ax = plt.subplots()
    ax.grid()
    ax.set_xlabel("Distance between Base Camp and Location ExpB")
    ax.set_ylabel("Run Time (s)")
    ax.set_xscale("log")

    LABELS = {
        "ENHSP-KDELTA": {
            "label": "$E-K\delta$",
            "style": "g-"
        },
        "ENHSP-1DELTA": {
            "label": "$E-1\delta$",
            "style": "r-"
        },
        "ENHSP-2DELTA": {
            "label": "$E-2\delta$",
            "style": "b-"
        },
        "UPMURPHI-KDELTA": {
            "label": "$U-K\delta$",
            "style": "g--"
        },
        "UPMURPHI-1DELTA": {
            "label": "$U-1\delta$",
            "style": "r--"
        }
    }

    for (key, points) in lines.items():
        x = [p[0] for p in points]
        y = [p[1] for p in points]
        ax.plot(x, y, LABELS[key]["style"], label=LABELS[key]["label"])

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    # ax.spines['bottom'].set_visible(False)
    # ax.spines['left'].set_visible(False)
    ax.legend(loc="upper left", fontsize="8")

    exp = filename.replace(".csv", "")
    folder = f'benchmarks/figures/{exp}'
    if os.path.exists(folder):
        shutil.rmtree(folder)
    os.mkdir(folder)
    plt.savefig(f'{folder}/{exp}.pdf', bbox_inches='tight', pad_inches=0.01)
    plt.show()


if __name__ == '__main__':
    main()
