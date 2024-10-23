import csv
import json
import os
import shutil
import statistics
import sys
from typing import Dict, List, Set, Tuple

from matplotlib import pyplot as plt

from classes.CloudLogger import CloudLogger
from classes.Result import Result

SMT_SOLVERS = {'SpringRoll',
               "PATTY-R-MIN", "PATTY-R-MAX", "PATTY-R-AVG", "PATTY-A", "PATTY-E", "PATTY-M", "PATTY-I",
               'RANTANPLAN',
               "OMT"}
TIME_LIMIT = 30 * 1000

SOLVERS = {
    'SpringRoll': "SR",
    'RANTANPLAN': "\mathrm{R^2\exists}",
    'METRIC-FF': "\mathrm{FF}",
    'ENHSP': r"\mathrm{ENHSP}",
    'NFD': "\mathrm{NFD}",
    'SMTPLAN+': "\mathrm{SMTP}^+",
    'OMT': "\mathrm{OMT}",
    "PATTY-R-MIN": "P_R^{\mathrm{min}}",
    "PATTY-R-MAX": "P_R^{\mathrm{max}}",
    "PATTY-R-AVG": "P_R^{\mathrm{avg}}",
    "PATTY-A": "P_A",
    "PATTY-E": "P_E",
    "PATTY-FA": "P_{FA}",
    "PATTY-FE": "P_{FE}",
    "PATTY-M": "P_M",
    "PATTY-I": "P_I",
}


def main():
    # Parsing the results
    exp = "2024-10-23-CES-v2"
    file = f"benchmarks/results/csv/{exp}.csv"

    CloudLogger.saveLogs(exp, file)

    joinWith = [file]

    aResults: [Result] = []
    for fileJoin in joinWith:
        with open(fileJoin, "r") as f:
            reader = csv.reader(f, delimiter=",")
            for i, line in enumerate(reader):
                aResults.append(Result.fromCSVLine(line[0].split(",")))

    # Joining together portfolios
    results = Result.joinPorfolios(aResults, {
        "ENHSP-SAT-HADD": "ENHSP",
        "ENHSP-SAT-HMAX": "ENHSP",
        "ENHSP-SAT-HMRP": "ENHSP",
    })

    points: Dict[str, Dict[str, Dict[int, List[Tuple[int, float]]]]] = dict()

    bits = set()
    counters = set()

    properties = ["time", "bound"]

    for p in properties:
        points[p] = dict()
        for r in results:
            b = int(r.problem.replace(".pddl", "").split("-")[1])
            bits.add(b)
            c = int(r.problem.replace(".pddl", "").split("-")[2])
            counters.add(c)

            property = r.time if p == "time" else r.bound
            points[p].setdefault(r.solver, dict())
            points[p][r.solver].setdefault(c, list())
            points[p][r.solver][c].append((b, property))

    plt.rcParams.update({
        "text.usetex": True,
        "figure.figsize": [7.50, 4.0],
        "figure.autolayout": True
    })

    lines = [{
        "solver": "ENHSP"
    }, {
        "solver": "PATTY-CES"
    }]

    fCounters = 5
    figs, axs = plt.subplots(2, 1)
    for i, p in enumerate(properties):
        ax = axs[i]
        ax.grid()
        ax.set_xlabel(r"Number of bits")
        ax.set_ylabel(p)
        # ax.set_xscale("log")

        for line in lines:
            ps = sorted(points[p][line["solver"]][fCounters])
            x = [p[0] for p in ps]
            y = [p[1] for p in ps]
            ax.plot(x, y)

        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        # ax.spines['bottom'].set_visible(False)
        # ax.spines['left'].set_visible(False)
        # ax.legend(loc="upper left", fontsize="8")

    folder = f'benchmarks/figures/{exp}'
    if os.path.exists(folder):
        shutil.rmtree(folder)
    os.mkdir(folder)
    plt.savefig(f'{folder}/{exp}.pdf', bbox_inches='tight', pad_inches=0.01)
    plt.show()


if __name__ == '__main__':
    main()
