import csv
import statistics
import time
from typing import Dict, List, Set

import numpy as np
from matplotlib import pyplot as plt
from natsort import natsorted

from classes.Result import Result

SOLVERS = {
    'RANTANPLAN': "\mathrm{R^2\exists}",
    'OMT': "\mathrm{OMT}",
    'ENHSP': r"\mathrm{ENHSP}",
    'NFD': "\mathrm{NFD}",
    'METRIC-FF': "\mathrm{FF}",
    'SpringRoll': "\mathrm{SR}",
    'PATTY': "P",
    'PATTY-STATIC': "P_{cat}",
    'PATTY-ASTAR': "P_{A*}",
}

DOMAINS = {
    "side-exchange": r"\textsc{SideExchange}"
}


def main():
    files = [
        "benchmarks/results/2023-11-29-SIDE-v1.csv"
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
        "ENHSP-sat-hadd": "ENHSP",
        "ENHSP-sat-hradd": "ENHSP",
        "ENHSP-sat-hmrphj": "ENHSP",
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
        "figure.figsize": [7.50, 3.50],
        "figure.autolayout": True
    })

    i = 1
    for domain in DOMAINS.keys():
        plt.figure(num=i, figsize=(8, 5))
        plt.title(rf"${DOMAINS[domain]}$")
        plt.grid()
        plt.xlabel("Number of objects")
        plt.ylabel("Planning Time (s)")
        for solver in SOLVERS:
            tuple = rDomain[domain][solver]
            x = np.linspace(1, len(xAxes[domain]), len(xAxes[domain]))
            y = [tuple[prob].time / 1000 if prob in tuple and tuple[prob].solved else 300 for prob in xAxes[domain]]
            ticks = [tick.replace(".pddl", "").replace("_", "\_") for tick in xAxes[domain]]
            ticks = [t if int(t) % 2 == 0 else "" for t in ticks]
            plt.xticks(x, ticks)
            plt.plot(x, y, label=rf"${SOLVERS[solver]}$")

        # plt.ylim([0, 100])
        plt.legend(loc="upper right")
        plt.savefig(f'benchmarks/figures/{domain}-{time.time_ns()}.pdf')
        plt.show()
        i += 1

    pass


if __name__ == '__main__':
    main()
