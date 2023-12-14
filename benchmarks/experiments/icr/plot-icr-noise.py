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
    "Solar-Rover": {
        "text": r"\textsc{SolarRover} (L)",
        "kind": "Hybrid",
    },
    "counters": {
        "text": r"\textsc{Counters} (L)",
        "kind": "Numeric",
    },
    "fo_counters": {
        "text": r"\textsc{Counters-FO} (L)",
        "kind": "Numeric",
    },
    "delivery": {
        "text": r"\textsc{Delivery} (L)",
        "kind": "Numeric",
    },
    "drone": {
        "text": r"\textsc{Drone} (L)",
        "kind": "Numeric",
    },
    "expedition": {
        "text": r"\textsc{Expedition} (L)",
        "kind": "Numeric",
    },
    "farmland": {
        "text": r"\textsc{Farmland} (L)",
        "kind": "Numeric",
    },
    "fo-farmland": {
        "text": r"\textsc{Farmland-FO} (L)",
        "kind": "Numeric",
    },
    "hydropower": {
        "text": r"\textsc{Hydropower} (L)",
        "kind": "Numeric",
    },
    "mprime": {
        "text": r"\textsc{MPrime} (L)",
        "kind": "Numeric",
    },
    "rover": {
        "text": r"\textsc{Rover} (L)",
        "kind": "Numeric",
    },
    "sailing": {
        "text": r"\textsc{Sailing} (L)",
        "kind": "Numeric",
    },
    "fo-sailing": {
        "text": r"\textsc{Sailing-FO} (L)",
        "kind": "Numeric",
    },
    "sugar": {
        "text": r"\textsc{Sugar} (L)",
        "kind": "Numeric",
    },
    "watering": {
        "text": r"\textsc{PlantWatering} (L)",
        "kind": "Numeric",
    },
}


def main():
    DOMAINS_BY_KIND: Dict[Dict[str, List[str]]] = dict()

    for (dom, domDict) in DOMAINS.items():
        kind = domDict["kind"]
        DOMAINS_BY_KIND[kind] = DOMAINS_BY_KIND.setdefault(kind, [])
        DOMAINS_BY_KIND[kind].append(dom)

    filename = "2023-12-13-ICR-FINALNOISE-v1.csv"
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
        problem = int(r.problem[:-5].split("-")[1])
        if type != "NOISE" or domain not in DOMAINS:
            continue
        domains.add(domain)

        rDict[domain] = rDict.setdefault(domain, dict())
        rDict[domain][problem] = rDict[domain].setdefault(problem, [])
        rDict[domain][problem].append(r)

        if r.time > TIMEOUT:
            TIMEOUT = r.time
    pass

    domains = sorted(list(domains))
    byRow = 4

    nOfRows = (len(domains) // byRow) + 1

    plt.rcParams.update({
        "text.usetex": True,
        "figure.figsize": [2.5 * byRow, 2 * nOfRows],
        "figure.autolayout": True
    })

    fig, axs = plt.subplots(nOfRows, byRow)
    i = 0

    for d in DOMAINS.keys():
        print(i, len(DOMAINS.keys()))
        ax = axs[i // byRow][i % byRow]
        ax.grid()
        ax.set_xlabel("Noise Variance $\eta$ (\%)")
        ax.set_ylabel("Distance")
        ax.set_yscale("log")
        ax.set_title(DOMAINS[d]["text"])

        x = sorted([k for k in rDict[d].keys() if k < 750])
        dRW = [statistics.mean([r.dRW for r in rDict[d][p]]) for p in x]
        dRC = [statistics.mean([r.dRC for r in rDict[d][p]]) for p in x]

        ax.plot(x, dRW, label=r"$||I_R - \tilde{I}||$")
        ax.plot(x, dRC, label=r"$||I_R - I_\star||$")
        ax.legend(loc="lower right", fontsize="8")
        i += 1
        pass

    folder = f'benchmarks/figures/{exp}'
    if os.path.exists(folder):
        shutil.rmtree(folder)
    os.mkdir(folder)
    plt.savefig(f'{folder}/{exp}.pdf', dpi=100, bbox_inches='tight', pad_inches=0.01)
    plt.show()


if __name__ == '__main__':
    main()
