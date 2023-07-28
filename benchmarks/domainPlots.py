import csv
import statistics
import time
from typing import Dict, List, Set

import numpy as np
from matplotlib import pyplot as plt
from natsort import natsorted

from classes.Result import Result

SOLVERS = {
    'SpringRoll': "\mathrm{SR}",
    'PATTY': "P_{arpg}",
    'PATTY-R': "P_r",
    'RANTANPLAN': "\mathrm{RTP}",
    'METRIC-FF': "\mathrm{FF}",
    'ENHSP': r"\mathrm{ENHSP}",
    'NFD': "\mathrm{NFD}",
}

DOMAINS = {
    # "ipc-2023/block-grouping": r"\textsc{BlockGrouping} (S)",
    # "ipc-2023/counters": r"\textsc{Counters} (S)",
    # "ipc-2023/delivery": r"\textsc{Delivery} (S)",
    # "ipc-2023/drone": r"\textsc{Drone} (S)",
    # "ipc-2023/expedition": r"\textsc{Expedition} (S)",
    # "ipc-2023/ext-plant-watering": r"\textsc{PlantWatering} (S)",
    # "ipc-2023/farmland": r"\textsc{Farmland} (S)",
    # "ipc-2023/fo-farmland": r"\textsc{Farmland} (L)",
    # "ipc-2023/fo-sailing": r"\textsc{Sailing} (L)",
    # "ipc-2023/fo_counters": r"\textsc{Counters} (L)",
    # "ipc-2023/hydropower": r"\textsc{HydroPower} (S)",
    # # "ipc-2023/markettrader": r"\textsc{MarketTrader}",
    # "ipc-2023/mprime": r"\textsc{MPrime} (S)",
    # "ipc-2023/pathwaysmetric": r"\textsc{PathwaysMetric} (S)",
    # "ipc-2023/rover": r"\textsc{Rover} (S)",
    # "ipc-2023/sailing": r"\textsc{Sailing} (S)",
    # "ipc-2023/satellite": r"\textsc{Satellite} (S)",
    # # "ipc-2023/settlers": r"\textsc{Settlers} (S)",
    # "ipc-2023/sugar": r"\textsc{Sugar} (S)",
    # "ipc-2023/tpp": r"\textsc{TPP} (L)",
    # "ipc-2023/zenotravel": r"\textsc{ZenoTravel} (S)",
    # "line-exchange": r"\textsc{LineExchange} (L)",
    "line-exchange-quantity": r"\textsc{LineExchange}"
}

TOTALS = {
    "ipc-2023/block-grouping": 20,
    "ipc-2023/counters": 20,
    "ipc-2023/delivery": 20,
    "ipc-2023/drone": 20,
    "ipc-2023/expedition": 20,
    "ipc-2023/ext-plant-watering": 20,
    "ipc-2023/farmland": 20,
    "ipc-2023/fo-farmland": 20,
    "ipc-2023/fo-sailing": 20,
    "ipc-2023/fo_counters": 20,
    "ipc-2023/hydropower": 20,
    # "ipc-2023/markettrader": 20,
    "ipc-2023/mprime": 20,
    "ipc-2023/pathwaysmetric": 20,
    "ipc-2023/rover": 20,
    "ipc-2023/sailing": 20,
    "ipc-2023/satellite": 20,
    # "ipc-2023/settlers": 20,
    "ipc-2023/sugar": 20,
    "ipc-2023/tpp": 20,
    "ipc-2023/zenotravel": 20,
    "line-exchange": 108,
    "line-exchange-quantity": 20
}


def main():
    files = [
        "benchmarks/results/2023-07-20-IPC-v8.csv"
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
        plt.xlabel("Allowed Quantity for Each Robot")
        plt.ylabel("Planning Time (s)")
        for solver in SOLVERS:
            tuple = rDomain[domain][solver]
            x = np.linspace(1, len(xAxes[domain]), len(xAxes[domain]))
            y = [tuple[prob].time / 1000 if prob in tuple and tuple[prob].solved else 30 for prob in xAxes[domain]]
            ticks = [tick.replace(".pddl", "").replace("_", "\_") for tick in xAxes[domain]]

            plt.xticks(x, ticks)
            plt.plot(x, y, label=rf"${SOLVERS[solver]}$")

        plt.legend(loc="upper right")
        plt.savefig(f'benchmarks/figures/{domain}-{time.time_ns()}.pdf')
        plt.show()
        i += 1

    pass


if __name__ == '__main__':
    main()
