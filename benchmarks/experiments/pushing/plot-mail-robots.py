import csv
import os
import shutil
import statistics
import time
from typing import Dict, List, Set

import numpy as np
from matplotlib import pyplot as plt
from natsort import natsorted

from classes.Result import Result

SOLVERS = {
    'ENHSP': r"\mathrm{ENHSP}",
    'SPRINGROLL': r"\mathrm{SR}",
    'PATTY-G': r"\textsc{Patty}_\textsc{G}",
    'PATTY-H': r"\textsc{Patty}_\textsc{H}",
    'PATTY-F': r"\textsc{Patty}_\textsc{F}",
}

DOMAINS = {
    "numeric/mail-robots-qty-types": r"\textsc{MailRobots}"
}

TIMEOUT = 30


def main():
    filename = "2024-04-23-MAIL-TYPES-V1"
    files = [
        f"benchmarks/results/{filename}.csv"
    ]
    aResults: [Result] = []
    for file in files:
        with open(file, "r") as f:
            reader = csv.reader(f, delimiter=",")
            for i, line in enumerate(reader):
                aResults.append(Result.fromCSVLine(line[0].split(",")))

    rDomain: Dict[str, Dict[str, Dict[str, Result]]] = dict()

    ## Joining together portfolios
    results = Result.joinPorfolios(aResults, {
        "ENHSP-SAT-AIBR": "ENHSP",
        "ENHSP-SAT-HADD": "ENHSP",
        "ENHSP-SAT-HMRP": "ENHSP",
    })

    xAxes: Dict[str, Set[str]] = dict()
    for result in results:
        rDomain.setdefault(result.domain, dict())
        rDomain[result.domain].setdefault(result.solver, dict())
        rDomain[result.domain][result.solver][result.problem] = result

        xAxes.setdefault(result.domain, set())
        xAxes[result.domain].add(result.problem)

    for domain in DOMAINS.keys():
        xAxes[domain] = list(xAxes[domain])
        xAxes[domain] = natsorted(xAxes[domain])

    plt.rcParams.update({
        "text.usetex": True,
        "figure.figsize": [7.50, 1.50],
        "figure.autolayout": True
    })

    i = 1
    for domain in DOMAINS.keys():
        plt.figure(figsize=(7.50, 3))
        plt.figure(num=i, figsize=(8, 5))
        plt.title(rf"${DOMAINS[domain]}$")
        plt.grid()
        plt.xlabel("Value of $N$")
        plt.ylabel("Planning Time (s)")
        for solver in SOLVERS:
            tuple = rDomain[domain][solver]
            x = np.linspace(1, len(xAxes[domain]), len(xAxes[domain]))
            y = [tuple[prob].time / 1000 if prob in tuple and tuple[prob].solved else TIMEOUT for prob in xAxes[domain]]
            ticks = [tick.replace(".pddl", "").replace("prob_", "") for tick in xAxes[domain]]
            ticks = [t if int(t) % 2 == 0 else "" for t in ticks]
            plt.xticks(x, ticks)
            plt.plot(x, y, label=rf"${SOLVERS[solver]}$")

        # plt.ylim([0, 100])
        plt.legend(loc="upper right")
        exp = filename.replace(".csv", "")
        folder = f'benchmarks/figures/{exp}'
        if os.path.exists(folder):
            shutil.rmtree(folder)
        os.mkdir(folder)
        plt.savefig(f'{folder}/plot-{exp}.pdf', dpi=100, bbox_inches='tight', pad_inches=0.01)
        plt.show()
        i += 1

    pass


if __name__ == '__main__':
    main()
