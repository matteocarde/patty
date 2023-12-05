import csv
import os
import shutil
import statistics
from math import ceil
from typing import Dict, List

from matplotlib import pyplot as plt

from classes.ICRResult import ICRResult
from classes.Result import Result


def myMean(elements):
    return statistics.mean(elements) if elements else float("-inf")


def rString(fValue, n):
    return '{:.{n}f}'.format(fValue, n=n)


DOMAINS = {
    "Baxter": {
        "text": r"\textsc{Baxter} (L)",
        "kind": "Hybrid",
    },
    "Descent": {
        "text": r"\textsc{Descent} (NL)",
        "kind": "Hybrid",
    },
    "HVAC": {
        "text": r"\textsc{HVAC} (NL)",
        "kind": "Hybrid",
    },
    "Linear-Car": {
        "text": r"\textsc{LinearCar} (L)",
        "kind": "Hybrid",
    },
    "Linear-Car-2": {
        "text": r"\textsc{LinearCar2} (L)",
        "kind": "Hybrid",
    },
    "Solar-Rover": {
        "text": r"\textsc{SolarRover} (L)",
        "kind": "Hybrid",
    },
    "UTC": {
        "text": r"\textsc{UTC} (L)",
        "kind": "Hybrid",
    },
    "counters": {
        "text": r"\textsc{Counters} (S)",
        "kind": "Numeric",
    },
    "fo_counters": {
        "text": r"\textsc{Counters} (L)",
        "kind": "Numeric",
    },
    "delivery": {
        "text": r"\textsc{Delivery} (S)",
        "kind": "Numeric",
    },
    "drone": {
        "text": r"\textsc{Drone} (S)",
        "kind": "Numeric",
    },
    "expedition": {
        "text": r"\textsc{Expedition} (S)",
        "kind": "Numeric",
    },
    "watering": {
        "text": r"\textsc{PlantWatering} (S)",
        "kind": "Numeric",
    },
    "farmland": {
        "text": r"\textsc{Farmland} (S)",
        "kind": "Numeric",
    },
    "fo-farmland": {
        "text": r"\textsc{Farmland} (L)",
        "kind": "Numeric",
    },
    "hydropower": {
        "text": r"\textsc{Hydropower} (S)",
        "kind": "Numeric",
    },
    "mprime": {
        "text": r"\textsc{MPrime} (S)",
        "kind": "Numeric",
    },
    "rover": {
        "text": r"\textsc{Rover} (S)",
        "kind": "Numeric",
    },
    "sailing": {
        "text": r"\textsc{Sailing} (S)",
        "kind": "Numeric",
    },
    "fo-sailing": {
        "text": r"\textsc{Sailing} (L)",
        "kind": "Numeric",
    },
    "sugar": {
        "text": r"\textsc{Sugar} (S)",
        "kind": "Numeric",
    },
    "zenotravel": {
        "text": r"\textsc{ZenoTravel} (S)",
        "kind": "Numeric",
    },

}


def main():
    DOMAINS_BY_KIND: Dict[Dict[str, List[str]]] = dict()

    for (dom, domDict) in DOMAINS.items():
        kind = domDict["kind"]
        DOMAINS_BY_KIND[kind] = DOMAINS_BY_KIND.setdefault(kind, [])
        DOMAINS_BY_KIND[kind].append(dom)

    filename = "2023-12-05-ICR-NOISE-v2.csv"
    file = f"benchmarks/results/{filename}"

    exp = filename.replace(".csv", "")
    folder = f'benchmarks/latex/{exp}'
    if os.path.exists(folder):
        shutil.rmtree(folder)
    os.mkdir(folder)

    results: [ICRResult] = []
    with open(file, "r") as f:
        reader = csv.reader(f, delimiter=",")
        for i, line in enumerate(reader):
            results.append(ICRResult.fromCSVLine(line[0].split(",")))

    # Domain/Solver/Delta
    rDict: Dict[str, Dict[int, [ICRResult]]] = dict()

    domains = set()
    TIMEOUT = 0
    for r in results:
        type = r.expType
        domain = r.domain
        domains.add(domain)
        problem = int(r.problem[:-5].split("-")[1])
        if type != "NOISE":
            continue

        rDict[domain] = rDict.setdefault(domain, dict())
        rDict[domain][problem] = rDict[domain].setdefault(problem, [])
        rDict[domain][problem].append(r)

        if r.time > TIMEOUT:
            TIMEOUT = r.time
    pass

    domains = sorted(list(domains))
    byRow = 6

    nOfRows = (len(domains) // byRow) + 1

    plt.rcParams.update({
        "text.usetex": True,
        "figure.figsize": [2.5 * byRow, 2 * nOfRows],
        "figure.autolayout": True
    })

    fig, axs = plt.subplots(nOfRows, byRow)
    i = 0

    for d in domains:
        ax = axs[i // byRow][i % byRow]
        ax.grid()
        ax.set_xlabel("Noise")
        ax.set_ylabel("Value")
        # ax.set_yscale("log")
        ax.set_title(DOMAINS[d]["text"])

        x = sorted([k for k in rDict[d].keys()])
        dRW = [statistics.mean([r.dRW for r in rDict[d][p]]) for p in x]
        dRC = [statistics.mean([r.dRC for r in rDict[d][p]]) for p in x]

        ax.plot(x, dRW, label=r"$||I - \tilde{I}||^2$")
        ax.plot(x, dRC, label=r"$||I - I_\star||^2$")
        ax.legend(loc="upper left", fontsize="8")
        i += 1
        pass

    folder = f'benchmarks/figures/{exp}'
    if os.path.exists(folder):
        shutil.rmtree(folder)
    os.mkdir(folder)
    plt.savefig(f'{folder}/plot.pdf', dpi=100)
    plt.show()


if __name__ == '__main__':
    main()
