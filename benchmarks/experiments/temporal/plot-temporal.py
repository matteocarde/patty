import csv
import os
import shutil
import statistics
from typing import List, Dict

import numpy
import numpy as np
from matplotlib import pyplot as plt

from classes.Result import Result

SOLVERS = {
    "PATTY-T-OR-ASTAR": r"\textsc{Patty}_\vee",
    "PATTY-T-SIGMA-ASTAR": r"\textsc{Patty}_\Sigma",
    "ANMLSMT": r"\textsc{AnmlSMT}",
    "ITSAT": r"\textsc{ITSat}",
    "LPG": r"\textsc{LPG}",
    "OPTIC": r"\textsc{Optic}",
    "TFD": r"\textsc{TFD}",
}

DOMAINS = {
    "temporal/cushing": r"\textsc{Cushing} (B)",
    "temporal/bottles-pour": r"\textsc{BottlesPour} (N)",
    "temporal/bottles-shake": r"\textsc{BottlesShake} (N)",
    "temporal/bottles-pack": r"\textsc{BottlesPack} (N)",
    "temporal/bottles-all": r"\textsc{BottlesAll} (N)",
    "temporal/majsp": r"\textsc{Majsp} (N)",
    "temporal/match-ac": r"\textsc{MatchAC} (B)",
    "temporal/match-ms": r"\textsc{MatchMS} (B)",
    "temporal/oversub": r"\textsc{Oversub} (B)",
    "temporal/painter": r"\textsc{Painter} (B)",
}

TIMEOUT = 300 * 1000


def main():
    filename = "2024-01-14-TOTAL-v1.csv"
    files = [f"benchmarks/results/{filename}"]

    results: [Result] = []
    for file in files:
        with open(file, "r") as f:
            reader = csv.reader(f, delimiter=",")
            for i, line in enumerate(reader):
                results.append(Result.fromCSVLine(line[0].split(",")))

    bins: Dict[str, List[int]] = dict()
    ys = np.linspace(0, TIMEOUT, TIMEOUT // 500)
    for solver in SOLVERS:
        bins[solver] = [0 for _ in ys]

    for r in results:
        solver = r.solver
        if not r.solved:
            continue
        time = r.time
        i = numpy.searchsorted(ys, time, side='left', sorter=None)
        bins[solver][i] += 1

    xsSolver: Dict[str, List[int]] = dict()
    for solver in SOLVERS:
        xsSolver[solver] = numpy.cumsum(bins[solver])

    plt.rcParams.update({
        "text.usetex": True,
        "figure.figsize": [7, 3],
        "figure.autolayout": True
    })
    plt.figure()
    plt.grid()
    for solver in SOLVERS.keys():
        xs = xsSolver[solver]
        plt.plot(xs, ys / 1000, label=f"${SOLVERS[solver]}$")
        pass
    plt.xlabel("Instances solved")
    plt.ylabel("Time to solve [s]")
    plt.legend(loc='upper left')

    exp = filename.replace(".csv", "")
    folder = f'benchmarks/figures/{exp}'
    if os.path.exists(folder):
        shutil.rmtree(folder)
    os.mkdir(folder)
    plt.savefig(f'{folder}/plot-{exp}.pdf', dpi=100, bbox_inches='tight', pad_inches=0.01)
    plt.show()


if __name__ == '__main__':
    main()
