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
    # "LPG": r"\textsc{LPG}",
    "OPTIC": r"\textsc{Optic}",
    # "TFD": r"\textsc{TFD}",
}

DOMAINS = {
    "propositional": {"temporal/cushing",
                      "temporal/match-ac",
                      "temporal/match-ms",
                      "temporal/oversub",
                      "temporal/painter"},
    "numeric": {"temporal/bottles-pour",
                "temporal/bottles-shake",
                "temporal/bottles-pack",
                "temporal/bottles-all",
                "temporal/majsp"},
}

TIMEOUT = 300 * 1000


def main():
    filename = "2024-01-14-TOTAL-v1.csv"
    files = [f"benchmarks/results/{filename}"]

    plt.rcParams.update({
        "text.usetex": True,
        "figure.figsize": [7, 3],
        "figure.autolayout": True
    })
    plt.figure()
    plt.grid()

    results: [Result] = []
    for file in files:
        with open(file, "r") as f:
            reader = csv.reader(f, delimiter=",")
            for i, line in enumerate(reader):
                results.append(Result.fromCSVLine(line[0].split(",")))

    for key, domains in DOMAINS.items():
        line = "dashed" if key == "propositional" else "solid"
        suffix = "B" if key == "propositional" else "N"
        bins: Dict[str, List[int]] = dict()
        ys = np.linspace(0, TIMEOUT, TIMEOUT // 600)
        for solver in SOLVERS:
            bins[solver] = [0 for _ in ys]

        for r in results:
            solver = r.solver
            if not r.solved:
                continue
            if r.solver not in SOLVERS or r.domain not in domains:
                continue
            time = r.time
            i = numpy.searchsorted(ys, time, side='left', sorter=None)
            bins[solver][i] += 1

        xsSolver: Dict[str, List[int]] = dict()
        for solver in SOLVERS:
            xsSolver[solver] = numpy.cumsum(bins[solver])

        for solver in SOLVERS.keys():
            xs = xsSolver[solver]
            plt.plot(xs, ys / 1000, label=f"${SOLVERS[solver]} ({suffix})$", linestyle=line)
            pass

    plt.xlabel("Instances solved")
    plt.ylabel("Time to solve [s]")
    plt.legend(loc='upper left', prop={"size": 7})

    exp = filename.replace(".csv", "")
    folder = f'benchmarks/figures/{exp}'
    if os.path.exists(folder):
        shutil.rmtree(folder)
    os.mkdir(folder)
    plt.savefig(f'{folder}/plot-{exp}.pdf', dpi=100, bbox_inches='tight', pad_inches=0.01)
    plt.show()


if __name__ == '__main__':
    main()
