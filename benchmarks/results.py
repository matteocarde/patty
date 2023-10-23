import csv
import os
import shutil
import statistics
from typing import Dict, List

from classes.Result import Result

SMT_SOLVERS = {'SpringRoll', "PATTY", "PATTY-MAX", "PATTY-ASTAR", "PATTY-STATIC", "PATTY-STATIC-MAX",
               'RANTANPLAN', "OMT"}
TIME_LIMIT = 300 * 1000

SOLVERS = {
    'SpringRoll': "SR",
    'RANTANPLAN': "\mathrm{R^2\exists}",
    'METRIC-FF': "\mathrm{FF}",
    'ENHSP': r"\mathrm{ENHSP}",
    'NFD': "\mathrm{NFD}",
    'SMTPLAN+': "\mathrm{SMTP}^+",
    'OMT': "\mathrm{OMT}",
    "PATTY": "P",
    "PATTY-MAX": "P^{max}",
    "PATTY-STATIC": "P_{cat}",
    "PATTY-STATIC-MAX": "P_{cat}^{max}",
    "PATTY-ASTAR": "P_{A^*}",
}

DOMAINS = {
    "ipc-2023/block-grouping": r"\textsc{BlockGrouping} (S)",
    "ipc-2023/counters": r"\textsc{Counters} (S)",
    "ipc-2023/delivery": r"\textsc{Delivery} (S)",
    "ipc-2023/drone": r"\textsc{Drone} (S)",
    "ipc-2023/expedition": r"\textsc{Expedition} (S)",
    "ipc-2023/ext-plant-watering": r"\textsc{PlantWatering} (S)",
    "ipc-2023/farmland": r"\textsc{Farmland} (S)",
    "ipc-2023/fo-farmland": r"\textsc{Farmland} (L)",
    "ipc-2023/fo-sailing": r"\textsc{Sailing} (L)",
    "ipc-2023/fo_counters": r"\textsc{Counters} (L)",
    "ipc-2023/hydropower": r"\textsc{HydroPower} (S)",
    # "ipc-2023/markettrader": r"\textsc{MarketTrader}",
    "ipc-2023/mprime": r"\textsc{MPrime} (S)",
    "ipc-2023/pathwaysmetric": r"\textsc{PathwaysMetric} (S)",
    "ipc-2023/rover": r"\textsc{Rover} (S)",
    "ipc-2023/sailing": r"\textsc{Sailing} (S)",
    "ipc-2023/satellite": r"\textsc{Satellite} (S)",
    "ipc-2023/settlers": r"\textsc{Settlers} (S)",
    "ipc-2023/sugar": r"\textsc{Sugar} (S)",
    "ipc-2023/tpp": r"\textsc{TPP} (L)",
    "ipc-2023/zenotravel": r"\textsc{ZenoTravel} (S)",
    "line-exchange": r"\textsc{LineExchange} (L)",
    "line-exchange-quantity": r"\textsc{LineExchange-QTY} (L)"
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
    "ipc-2023/markettrader": 20,
    "ipc-2023/mprime": 20,
    "ipc-2023/pathwaysmetric": 20,
    "ipc-2023/rover": 20,
    "ipc-2023/sailing": 20,
    "ipc-2023/satellite": 20,
    "ipc-2023/settlers": 20,
    "ipc-2023/sugar": 20,
    "ipc-2023/tpp": 20,
    "ipc-2023/zenotravel": 20,
    "line-exchange": 108,
    "line-exchange-quantity": 20
}


def main():
    # Parsing the results
    exp = "2023-10-22-FINAL-v1"
    file = f"benchmarks/results/{exp}.csv"

    joinWith = ["benchmarks/results/SEARCH-300.csv"] + [file]
    # joinWith = [file]

    aResults: [Result] = []
    for fileJoin in joinWith:
        with open(fileJoin, "r") as f:
            reader = csv.reader(f, delimiter=",")
            for i, line in enumerate(reader):
                aResults.append(Result.fromCSVLine(line[0].split(",")))

    folder = f'benchmarks/latex/{exp}'
    if os.path.exists(folder):
        shutil.rmtree(folder)
    os.mkdir(folder)

    # Joining together portfolios
    results = Result.joinPorfolios(aResults, {
        "ENHSP-sat-hadd": "ENHSP",
        "ENHSP-sat-hradd": "ENHSP",
        "ENHSP-sat-hmrphj": "ENHSP",
    })

    solvers = set()
    domains = set()
    d = dict()
    for r in results:
        d[r.domain] = d.setdefault(r.domain, dict())
        solvers.add(r.solver)
        domains.add(r.domain)
        d[r.domain][r.solver] = d[r.domain].setdefault(r.solver, dict())
        d[r.domain][r.solver][r.problem] = d[r.domain][r.solver].setdefault(r.problem, list())
        d[r.domain][r.solver][r.problem].append(r)

    solvers = list(solvers)
    solvers.sort()
    domains = list(domains)
    domains.sort()

    for domain in domains:
        for solver in solvers:
            problems = list()
            if solver not in d[domain]:
                continue
            for problem in d[domain][solver].keys():
                problems.append(Result.average(d[domain][solver][problem]))
            d[domain][solver] = problems

    def r(fValue, n):
        return '{:.{n}f}'.format(fValue, n=n)

    t = dict()
    stats = set()
    for (domain, domainDict) in d.items():
        t[domain] = {
            "coverage": dict(),
            "bound": dict(),
            "time": dict(),
            "length": dict(),
            "nOfVars": dict(),
            "nOfRules": dict(),
            "lastCallsToSolver": dict(),
        }

        commonlySolved = {}
        commonlyGrounded = {}
        for solver in SMT_SOLVERS:
            if solver not in domainDict:
                continue
            solved = {r.problem for r in domainDict[solver] if r.solved}
            grounded = {r.problem for r in domainDict[solver] if r.nOfVars > 0}
            if solved:
                commonlySolved = solved if not commonlySolved else commonlySolved.intersection(solved)
            if grounded:
                commonlyGrounded = solved if not commonlyGrounded else commonlyGrounded.intersection(grounded)

        a = 1 + 1

        for solver in solvers:
            if solver not in domainDict:
                continue
            pResult = domainDict[solver]
            t[domain]["coverage"][solver] = r(sum([r.solved for r in pResult]) / TOTALS[domain] * 100, 1)
            t[domain]["coverage"][solver] = "-" if t[domain]["coverage"][solver] == "0.0" else t[domain]["coverage"][
                solver]
            bounds = [r.bound for r in pResult if r.solved if r.problem in commonlySolved]
            t[domain]["bound"][solver] = r(statistics.mean(bounds), 2) if t[domain]["coverage"][
                                                                              solver] != "-" and bounds else "-"
            t[domain]["time"][solver] = r(statistics.mean([r.time if r.solved else TIME_LIMIT for r in pResult]) / 1000,
                                          2) if \
                t[domain]["coverage"][solver] != "-" else "-"
            t[domain]["length"][solver] = r(statistics.mean([r.planLength for r in pResult if r.solved]), 0) if \
                t[domain]["coverage"][solver] != "-" else "-"

            v = [r.nOfVars for r in pResult if r.nOfVars > 0 and r.problem in commonlySolved]
            t[domain]["nOfVars"][solver] = r(statistics.mean(v), 0) if len(v) else "-"
            v = [r.nOfRules for r in pResult if r.nOfRules > 0 and r.problem in commonlySolved]
            t[domain]["nOfRules"][solver] = r(statistics.mean(v), 0) if len(v) else "-"
            v = [r.lastCallsToSolver for r in pResult if r.lastCallsToSolver > 0 and r.problem in commonlySolved]
            t[domain]["lastCallsToSolver"][solver] = r(statistics.mean(v), 2) if len(v) else "-"

    domainsClusters = {
        r"\textit{Highly Numeric}": [
            "ipc-2023/block-grouping",
            "ipc-2023/counters",
            "ipc-2023/fo_counters",
            "ipc-2023/drone",
            "ipc-2023/ext-plant-watering",
            "ipc-2023/farmland",
            "ipc-2023/fo-farmland",
            "ipc-2023/hydropower",
            "ipc-2023/sailing",
            "ipc-2023/fo-sailing",
            "line-exchange",
            # "line-exchange-quantity"
        ],
        r"\textit{Lowly Numeric}": [
            "ipc-2023/delivery",
            "ipc-2023/expedition",
            # "ipc-2023/markettrader",
            "ipc-2023/mprime",
            "ipc-2023/pathwaysmetric",
            "ipc-2023/rover",
            "ipc-2023/satellite",
            # "ipc-2023/settlers",
            "ipc-2023/sugar",
            "ipc-2023/tpp",
            "ipc-2023/zenotravel"
        ]
    }

    winners = {
        "coverage": +1,
        "bound": -1,
        "time": -1,
        "nOfVars": -1,
        "nOfRules": -1,
        "lastCallsToSolver": -1,
    }

    tables = [{
        "name": "tab:experiments",
        "type": "table*",
        "width": r"\textwidth",
        "columns": {
            "coverage": ("Coverage (\%)", {"SMT", "SEARCH"}),
            "time": ("Time (s)", {"SMT", "SEARCH"}),
            "bound": (r"Calls to \textsc{Solve}", {"SMT"}),
            "nOfVars": ("$|\mathcal{X} \cup \mathcal{A} \cup \mathcal{X}'|$", {"SMT"}),
            "nOfRules": ("$|\mathcal{T}(\mathcal{X},\mathcal{A},\mathcal{X}')|$", {"SMT"}),
            # "lastCallsToSolver": (r"$\textsc{Solve}(\Pi^\prec)$ calls", {"SMT"}),
        },
        "planners": [
            {
                'PATTY': "SMT",
                'PATTY-STATIC': "SMT",
                'PATTY-ASTAR': "SMT",
                'ENHSP': "SEARCH",
                'METRIC-FF': "SEARCH",
                "NFD": "SEARCH",
            },
            # {
            #     # 'PATTY': "SMT",
            #     # 'PATTY-STATIC': "SMT",
            #     'PATTY-ASTAR': "SEARCH",
            #     'ENHSP': "SEARCH",
            #     'METRIC-FF': "SEARCH",
            #     "NFD": "SEARCH",
            # }
        ],
        "caption": r"Comparative analysis between the search-based solver $\textsc{ENHSP}$ and  $\textsc{Patty}$ run "
                   r"with the standard algorithm ($P$),  $\textsc{SolveConcat}$ ($P_{cat}$), \textsc{SolveGBFS} ("
                   r"$P_\text{gbfs}$), \textsc{SolveA}$^*$ ($P_{A^*}$), \textsc{SolveGBFSMax} ($P_\text{gbfs}^{"
                   r"max}$), \textsc{SolveA*Max} ($P_{A^*}^{max}$). ''Best numbers'' are in bold.  The numbers in the "
                   r"Highly and Lowly Numeric rows are the number of bolds in the subcolumn."
    }]

    latex = []
    latex.append(r"""
           \documentclass[11pt,landscape]{article}
           \usepackage{graphicx}
           \usepackage{lscape}
           \usepackage{multirow}
           \usepackage[a4paper,margin=1in,landscape]{geometry}

           \begin{document}""")

    for table in tables:
        stats = table["columns"].keys()

        best: List[Dict] = list()
        for i in range(len(table["planners"])):
            bestCluster = dict()
            solvers = table["planners"][i].keys()
            best.append(bestCluster)
            for (domain, domainDict) in d.items():
                bestCluster[domain] = dict()
                for stat in table["columns"].keys():
                    better = {}
                    betterValue = float("-inf") if winners[stat] > 0 else float("+inf")
                    for solver in solvers:
                        if solver not in t[domain][stat]:
                            continue
                        value = t[domain][stat][solver]
                        if value in {"-", "G", "-1.00"}:
                            continue
                        if float(value) * winners[stat] > betterValue * winners[stat]:
                            betterValue = float(value)
                            better = {solver}
                        elif float(value) == betterValue:
                            better |= {solver}
                    bestCluster[domain][stat] = better

        latex.append(r"""
            \begin{""" + table["type"] + r"""}[tb]
            \centering
            \resizebox{""" + table["width"] + r"""}{!}{""")

        solversHeader = []
        mString = []
        cString = ""
        for (stat, (name, statTypes)) in table["columns"].items():
            nCells = 0
            clString = []
            for cluster in table["planners"]:
                clCells = 0
                for (solver, type) in cluster.items():
                    if type not in statTypes:
                        continue
                    solversHeader.append(f"${SOLVERS[solver]}$")
                    nCells += 1
                    clCells += 1
                if clCells > 0:
                    clString.append(clCells * 'c')
            cString += f"|{'|'.join(clString)}|"
            mString.append(r"\multicolumn{" + str(nCells) + "}{c||}{" + name + "}")

        columns = f"|l|{cString}" + "|"

        latex.append(r"\begin{tabular}{" + columns + "}")
        latex.append(r"\hline")
        latex.append(fr" & " + "&".join(mString) + r"\\")
        latex.append(fr"Domain & " + "&".join(solversHeader) + r"\\")
        latex.append(fr"\hline")

        for (cluster, clusterDomains) in domainsClusters.items():
            rows = []
            row = [cluster]
            for (stat, (name, statTypes)) in table["columns"].items():
                for i, plCluster in enumerate(table["planners"]):
                    for (solver, type) in plCluster.items():
                        if type not in statTypes:
                            continue
                        nOfBest = 0
                        for domain in clusterDomains:
                            if solver in best[i][domain][stat]:
                                nOfBest += 1
                        row.append(r"\textbf{" + str(nOfBest) + "}")
            latex.append("&".join(row) + r"\\\hline")
            for domain in clusterDomains:
                row = [DOMAINS[domain]]
                for (stat, (name, statTypes)) in table["columns"].items():
                    for i, plCluster in enumerate(table["planners"]):
                        for (solver, type) in plCluster.items():
                            if type not in statTypes:
                                continue
                            if solver not in t[domain][stat]:
                                row.append("TBD")
                                continue
                            if solver in best[i][domain][stat]:
                                row.append(r"\textbf{" + t[domain][stat][solver] + "}")
                            else:
                                row.append(t[domain][stat][solver])
                rows.append("&".join(row))
            latex.append("\\\\\n".join(rows))
            latex.append(fr"\\\hline")
        row = [r"\textit{Total}"]
        for (stat, (name, statTypes)) in table["columns"].items():
            for i, plCluster in enumerate(table["planners"]):
                for (solver, type) in plCluster.items():
                    if type not in statTypes:
                        continue
                    nOfBest = 0
                    for (cluster, clusterDomains) in domainsClusters.items():
                        for domain in clusterDomains:
                            if solver in best[i][domain][stat]:
                                nOfBest += 1
                    row.append(r"\textbf{" + str(nOfBest) + "}")
        latex.append("&".join(row) + r"\\\hline")

        latex.append(r"""
        \end{tabular}}
        \caption{""" + table["caption"] + """}
        \label{""" + table["name"] + """}
        \end{""" + table["type"] + """}
        """)

    pass

    latex.append("\end{document}")

    latexStr = "\n".join(latex)
    folder = f'benchmarks/latex/{exp}'
    if os.path.exists(folder):
        shutil.rmtree(folder)
    os.mkdir(folder)
    with open(f"{folder}/{exp}.tex", "w") as f:
        f.write(latexStr)
    os.system(f"pdflatex -interaction=nonstopmode --output-directory='{folder}' {folder}/{exp}.tex ")

    os.remove(f"{folder}/{exp}.aux")
    os.remove(f"{folder}/{exp}.log")


if __name__ == '__main__':
    main()
