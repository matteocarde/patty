import csv
import json
import os
import shutil
import statistics
from typing import Dict, List

from classes.CloudLogger import CloudLogger
from classes.Result import Result

SMT_SOLVERS = {'SpringRoll', "PATTY-R", "PATTY-A", "PATTY-E", "PATTY-M", 'RANTANPLAN', "OMT"}
TIME_LIMIT = 30 * 1000

SOLVERS = {
    'SpringRoll': "SR",
    'RANTANPLAN': "\mathrm{R^2\exists}",
    'METRIC-FF': "\mathrm{FF}",
    'ENHSP': r"\mathrm{ENHSP}",
    'NFD': "\mathrm{NFD}",
    'SMTPLAN+': "\mathrm{SMTP}^+",
    'OMT': "\mathrm{OMT}",
    "PATTY-R": "P_R",
    "PATTY-A": "P_A",
    "PATTY-E": "P_E",
    "PATTY-M": "P_M",
}

# DOMAINS = {
#     "numeric/ipc-2023/block-grouping": r"\textsc{BlockGrouping} (S)",
#     "numeric/ipc-2023/counters": r"\textsc{Counters} (S)",
#     "numeric/ipc-2023/delivery": r"\textsc{Delivery} (S)",
#     "numeric/ipc-2023/drone": r"\textsc{Drone} (S)",
#     "numeric/ipc-2023/expedition": r"\textsc{Expedition} (S)",
#     "numeric/ipc-2023/ext-plant-watering": r"\textsc{PlantWatering} (S)",
#     "numeric/ipc-2023/farmland": r"\textsc{Farmland} (S)",
#     "numeric/ipc-2023/fo-farmland": r"\textsc{Farmland} (L)",
#     "numeric/ipc-2023/fo-sailing": r"\textsc{Sailing} (L)",
#     "numeric/ipc-2023/fo_counters": r"\textsc{Counters} (L)",
#     "numeric/ipc-2023/hydropower": r"\textsc{HydroPower} (S)",
#     # "numeric/ipc-2023/markettrader": r"\textsc{MarketTrader}",
#     "numeric/ipc-2023/mprime": r"\textsc{MPrime} (S)",
#     "numeric/ipc-2023/pathwaysmetric": r"\textsc{PathwaysMetric} (S)",
#     "numeric/ipc-2023/rover": r"\textsc{Rover} (S)",
#     "numeric/ipc-2023/sailing": r"\textsc{Sailing} (S)",
#     "numeric/ipc-2023/satellite": r"\textsc{Satellite} (S)",
#     "numeric/ipc-2023/settlers": r"\textsc{Settlers} (S)",
#     "numeric/ipc-2023/sugar": r"\textsc{Sugar} (S)",
#     "numeric/ipc-2023/tpp": r"\textsc{TPP} (L)",
#     "numeric/ipc-2023/zenotravel": r"\textsc{ZenoTravel} (S)",
#     "numeric/line-exchange": r"\textsc{LineExchange} (L)",
#     "line-exchange-quantity": r"\textsc{LineExchange-QTY} (L)"
# }

DOMAINS = {
    "numeric/ipc-2023/block-grouping": r"\textsc{BlGrp} (S)",
    "numeric/ipc-2023/counters": r"\textsc{Cnt} (S)",
    "numeric/ipc-2023/delivery": r"\textsc{Del} (S)",
    "numeric/ipc-2023/drone": r"\textsc{Drn} (S)",
    "numeric/ipc-2023/expedition": r"\textsc{Exp} (S)",
    "numeric/ipc-2023/ext-plant-watering": r"\textsc{PlWat} (S)",
    "numeric/ipc-2023/farmland": r"\textsc{Farm} (S)",
    "numeric/ipc-2023/fo-farmland": r"\textsc{Farm} (L)",
    "numeric/ipc-2023/fo-sailing": r"\textsc{Sail} (L)",
    "numeric/ipc-2023/fo_counters": r"\textsc{Cnt} (L)",
    "numeric/ipc-2023/hydropower": r"\textsc{HPwr} (S)",
    # "numeric/ipc-2023/markettrader": r"\textsc{MarketTrader}",
    "numeric/ipc-2023/mprime": r"\textsc{MPrime} (S)",
    "numeric/ipc-2023/pathwaysmetric": r"\textsc{PathM} (S)",
    "numeric/ipc-2023/rover": r"\textsc{Rvr} (S)",
    "numeric/ipc-2023/sailing": r"\textsc{Sail} (S)",
    "numeric/ipc-2023/satellite": r"\textsc{Sat} (S)",
    "numeric/ipc-2023/settlers": r"\textsc{Stlr} (S)",
    "numeric/ipc-2023/sugar": r"\textsc{Sgr} (S)",
    "numeric/ipc-2023/tpp": r"\textsc{Tpp} (L)",
    "numeric/ipc-2023/zenotravel": r"\textsc{Zeno} (S)",
    "numeric/line-exchange": r"\textsc{Line} (L)",
    "line-exchange-quantity": r"\textsc{LineExchange-QTY} (L)"
}

TOTALS = {
    "numeric/ipc-2023/block-grouping": 20,
    "numeric/ipc-2023/counters": 20,
    "numeric/ipc-2023/delivery": 20,
    "numeric/ipc-2023/drone": 20,
    "numeric/ipc-2023/expedition": 20,
    "numeric/ipc-2023/ext-plant-watering": 20,
    "numeric/ipc-2023/farmland": 20,
    "numeric/ipc-2023/fo-farmland": 20,
    "numeric/ipc-2023/fo-sailing": 20,
    "numeric/ipc-2023/fo_counters": 20,
    "numeric/ipc-2023/hydropower": 20,
    "numeric/ipc-2023/markettrader": 20,
    "numeric/ipc-2023/mprime": 20,
    "numeric/ipc-2023/pathwaysmetric": 20,
    "numeric/ipc-2023/rover": 20,
    "numeric/ipc-2023/sailing": 20,
    "numeric/ipc-2023/satellite": 20,
    "numeric/ipc-2023/settlers": 20,
    "numeric/ipc-2023/sugar": 20,
    "numeric/ipc-2023/tpp": 20,
    "numeric/ipc-2023/zenotravel": 20,
    "numeric/line-exchange": 108,
    "line-exchange-quantity": 20
}


def main():
    # Parsing the results
    exp = "2024-09-06-AIJ-v3"
    file = f"benchmarks/results/{exp}.csv"

    CloudLogger.saveLogs(exp, file)

    joinWith = [file]
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
    dView = dict()
    for r in results:
        solvers.add(r.solver)
        domains.add(r.domain)

        d[r.domain] = d.setdefault(r.domain, dict())
        d[r.domain][r.solver] = d[r.domain].setdefault(r.solver, dict())
        d[r.domain][r.solver][r.problem] = d[r.domain][r.solver].setdefault(r.problem, list())
        d[r.domain][r.solver][r.problem].append(r)

        dView[r.domain] = dView.setdefault(r.domain, dict())
        dView[r.domain][r.problem] = dView[r.domain].setdefault(r.problem, dict())
        dView[r.domain][r.problem][r.solver] = dView[r.domain][r.problem].setdefault(r.solver, list())
        dView[r.domain][r.problem][r.solver].append(r)

    with open(file.replace(".csv", ".json"), "w") as f:
        f.write(json.dumps(dView, indent=2))

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

    def rVec(v, n):
        return r(statistics.mean(v), n) if v else "-"

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

            hasCoverage = sum([r.solved for r in pResult]) > 0
            t[domain]["coverage"][solver] = r(sum([r.solved for r in pResult]) / TOTALS[domain] * 100, 0)
            t[domain]["coverage"][solver] = "-" if not hasCoverage else t[domain]["coverage"][solver]

            v = [r.bound for r in pResult if r.solved and r.problem in commonlySolved]
            t[domain]["bound"][solver] = rVec(v, 1) if hasCoverage else "-"

            v = [r.time / 1000 if r.solved else TIME_LIMIT / 1000 for r in pResult]
            t[domain]["time"][solver] = rVec(v, 1) if hasCoverage else "-"

            v = [r.planLength for r in pResult if r.solved and r.problem in commonlySolved]
            t[domain]["length"][solver] = rVec(v, 0) if hasCoverage else "-"

            v = [r.nOfVars for r in pResult if r.nOfVars > 0 and r.problem in commonlySolved]
            t[domain]["nOfVars"][solver] = rVec(v, 0) if len(v) else "-"
            v = [r.nOfRules for r in pResult if r.nOfRules > 0 and r.problem in commonlySolved]
            t[domain]["nOfRules"][solver] = rVec(v, 0) if len(v) else "-"
            v = [r.lastCallsToSolver for r in pResult if r.lastCallsToSolver > 0 and r.problem in commonlySolved]
            t[domain]["lastCallsToSolver"][solver] = rVec(v, 2) if len(v) else "-"

    domainsClusters = {
        r"\textit{High}": [
            "numeric/ipc-2023/block-grouping",
            "numeric/ipc-2023/counters",
            "numeric/ipc-2023/fo_counters",
            "numeric/ipc-2023/delivery",
            "numeric/ipc-2023/drone",
            "numeric/ipc-2023/expedition",
            "numeric/ipc-2023/farmland",
            "numeric/ipc-2023/fo-farmland",
            "numeric/ipc-2023/hydropower",
            "numeric/ipc-2023/mprime",
            "numeric/ipc-2023/pathwaysmetric",
            "numeric/ipc-2023/ext-plant-watering",
            "numeric/ipc-2023/rover",
            "numeric/ipc-2023/sailing",
            "numeric/ipc-2023/fo-sailing",
            "numeric/ipc-2023/satellite",
            "numeric/ipc-2023/sugar",
            "numeric/ipc-2023/tpp",
            "numeric/ipc-2023/zenotravel"
        ],
    }

    winners = {
        "coverage": +1,
        "bound": -1,
        "length": -1,
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
            "coverage": ("Coverage (\%)", {"SMT", "SEARCH"}, "count"),
            "time": ("Time (s)", {"SMT", "SEARCH"}, "count"),
            "bound": (r"$n$ - Calls to \smt solver", {"SMT"}, "count"),
            "length": (r"$|\pi|$", {"SMT"}, "count"),
            "nOfVars": ("$|\mathcal{X} \cup \mathcal{A}^\prec \cup \mathcal{X}'|$", {"SMT"}, "count"),
            "nOfRules": ("$|\mathcal{T}^\prec(\mathcal{X},\mathcal{A}^\prec,\mathcal{X}')|$", {"SMT"}, "count"),
            # "bound": (r"Vars x Rule", {"SMT"}, "count"),
            # "lastCallsToSolver": (r"$\textsc{Solve}(\Pi^\prec)$ calls", {"SMT"}),
        },
        "planners": [{
            'PATTY-R': "SMT",
            'PATTY-A': "SMT",
            'PATTY-E': "SMT",
            'PATTY-M': "SMT",
            # 'PATTY-H': "SMT",
            # 'PATTY-F': "SMT"
        },
            # {
            #     'PATTY-F': "SEARCH",
            #     'ENHSP': "SEARCH",
            #     'METRIC-FF': "SEARCH",
            #     "NFD": "SEARCH",
            # }
        ],
        "caption": r""
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
        for (stat, (name, statTypes, aggregate)) in table["columns"].items():
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
            for (stat, (name, statTypes, aggregate)) in table["columns"].items():
                for i, plCluster in enumerate(table["planners"]):
                    for (solver, type) in plCluster.items():
                        if type not in statTypes:
                            continue
                        nOfBest = 0
                        for domain in clusterDomains:
                            if solver in best[i][domain][stat]:
                                nOfBest += 1
                        row.append(r"\textbf{" + str(nOfBest) + "}")
            # latex.append("&".join(row) + r"\\\hline")
            for domain in clusterDomains:
                row = [DOMAINS[domain]]
                for (stat, (name, statTypes, aggregate)) in table["columns"].items():
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
        for (stat, (name, statTypes, aggregate)) in table["columns"].items():
            for i, plCluster in enumerate(table["planners"]):
                for (solver, type) in plCluster.items():
                    if type not in statTypes:
                        continue
                    nOfBest = 0
                    for (cluster, clusterDomains) in domainsClusters.items():
                        for domain in clusterDomains:
                            if solver in best[i][domain][stat]:
                                if aggregate == "count":
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

    os.system(f"open {folder}/{exp}.pdf")


if __name__ == '__main__':
    main()
