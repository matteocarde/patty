import csv
import os
import re
import shutil
import time
from typing import Dict, List

from matplotlib import pyplot as plt
from matplotlib.axes import Subplot

from classes.Result import Result

DOMAINS = ["Baxter",
           "Descent",
           "HVAC",
           "Linear-Car",
           "Linear-Car-2",
           "Linear-Generator",
           "Solar-Rover"
           ]

HEURISTICS = [
    "ENHSP-SAT-HMRP",
    "ENHSP-SAT-HADD",
    # "ENHSP-SAT-HMAX",
    "ENHSP-SAT-AIBR",
    # "ENHSP-SAT-HRADD",
    "ENHSP-SAT-BLIND",
    "ENHSP-OPT-HMRP",
    "ENHSP-OPT-HADD",
    # "ENHSP-OPT-HMAX",
    "ENHSP-OPT-AIBR",
    # "ENHSP-OPT-HRADD",
    "ENHSP-OPT-BLIND",
    "PORTFOLIO"
]

LINES = {
    ("NODELTA", "-de 0.1 -dp 0.1 -dh 0.1"): {
        "id": "1DELTA",
        "name": r"$1\delta$",
        "type": "NODELTA",
        "config": "-de 0.1 -dp 0.1 -dh 0.1"
    },
    ("NODELTA", "-de 0.1 -dp 1 -dh 1"): {
        "id": "2DELTA",
        "name": r"$2\delta$",
        "type": "NODELTA",
        "config": "-de 0.1 -dp 1 -dh 1"
    },
    ("DELTA", "-de 0.1 -dp 0.1 -dh 0.1"): {
        "id": "KDELTA",
        "name": r"$K\delta$",
        "type": "DELTA",
        "config": "-de 0.1 -dp 0.1 -dh 0.1"
    }
}


def main():
    filename = "2023-09-30-WELLKNOWN-v3.csv"
    file = f"benchmarks/results/{filename}"

    exp = filename.replace(".csv", "")
    folder = f'benchmarks/figures/{exp}'
    if os.path.exists(folder):
        shutil.rmtree(folder)
    os.mkdir(folder)

    results: [Result] = []
    with open(file, "r") as f:
        reader = csv.reader(f, delimiter=",")
        for i, line in enumerate(reader):
            results.append(Result.fromCSVLine(line[0].split(",")))

    # Domain/Solver/Delta
    rDict: Dict[str, Dict[str, Dict[str, List[Result]]]] = dict()
    portfolio: Dict[str, Dict[str, Dict[str, List[Result]]]] = dict()

    for r in results:
        domain = "-".join(r.domain.split("-")[:-1])
        type = r.domain.split("-")[-1]
        solver = r.solver.split("[")[0]
        config = r.solver.split("[")[1][:-1]
        line = LINES[(type, config)]
        id = line["id"]
        rDict[domain] = rDict.setdefault(domain, {})
        rDict[domain][solver] = rDict[domain].setdefault(solver, {})
        rDict[domain][solver][id] = rDict[domain][solver].setdefault(id, [])
        rDict[domain][solver][id].append(r)

        portfolio[domain] = portfolio.setdefault(domain, {})
        portfolio[domain][id] = portfolio[domain].setdefault(id, {})
        portfolio[domain][id][r.problem] = portfolio[domain][id].setdefault(r.problem, [])
        portfolio[domain][id][r.problem].append(r)

        r.time = r.time if r.solved else 60000

    for domain in DOMAINS:
        for line in LINES.values():
            id = line["id"]
            for rs in portfolio[domain][id].values():
                r = Result.portfolio(rs, "PORTFOLIO")
                rDict[domain]["PORTFOLIO"] = rDict[domain].setdefault("PORTFOLIO", {})
                rDict[domain]["PORTFOLIO"][id] = rDict[domain]["PORTFOLIO"].setdefault(id, [])
                rDict[domain]["PORTFOLIO"][id].append(r)

    plt.rcParams.update({
        "text.usetex": True,
        "figure.figsize": [7.50, 2.5 * len(HEURISTICS)],
        "figure.autolayout": True
    })

    for i, domain in enumerate(DOMAINS):
        plt.figure(num=i, figsize=(20, 5))
        plt.title(rf"${domain}$")
        fig, axs = plt.subplots(len(HEURISTICS), 1)
        for j, heuristic in enumerate(HEURISTICS):
            ax: Subplot = axs[j]
            ax.set_title(rf"{heuristic}")
            ax.grid()
            ax.set_xlabel("Scaling factor")
            ax.set_ylabel("Pl. Time (s)")
            # ax.set_xscale("log")

            for line in LINES.values():
                points = dict({(i, r.time / 1000) for i, r in enumerate(rDict[domain][heuristic][line["id"]])})
                x = list(points.keys())
                x.sort()
                y = [points[e] for e in x]
                ax.plot(x, y, label=line["name"])
                pass

            ax.legend(loc="upper right")
        plt.savefig(f'{folder}/{domain}-{exp}.pdf')
        plt.show()


if __name__ == '__main__':
    main()
