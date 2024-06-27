import csv
import os
import shutil
import statistics
from typing import Dict, List

from classes.Result import Result

SMT_SOLVERS = {'SpringRoll', "PATTY-G", "PATTY-H", "PATTY-F", "PATTY-O", 'RANTANPLAN', "OMT"}
TIME_LIMIT = 30 * 1000

COMMANDS = r"""
\newcommand{\pattyg}{\ensuremath{\textsc{Patty}_\textsc{G}}\xspace}
\newcommand{\pattyh}{\ensuremath{\textsc{Patty}_\textsc{H}}\xspace}
\newcommand{\pattyf}{\ensuremath{\textsc{Patty}_\textsc{F}}\xspace}
"""

SOLVERS = {
    'SpringRoll': r"\mathrm{SR}",
    'RANTANPLAN': r"\mathrm{R^2\exists}",
    'METRIC-FF': r"\mathrm{FF}",
    'ENHSP': r"\mathrm{ENHSP}",
    'NFD': r"\mathrm{NFD}",
    'SMTPLAN+': r"\mathrm{SMTP}^+",
    'OMT': r"\mathrm{OMT}",
    "PATTY-O": r"\mathrm{P}_\mathrm{O}",
    "PATTY-G": r"\mathrm{P}_\mathrm{G}",
    "PATTY-H": r"\mathrm{P}_\mathrm{H}",
    "PATTY-F": r"\mathrm{P}_\mathrm{F}"
}

DOMAINS = {
    "numeric/ipc-2023/block-grouping": r"\textsc{BlockGrouping} (S)",
    "numeric/ipc-2023/counters": r"\textsc{Counters} (S)",
    "numeric/ipc-2023/delivery": r"\textsc{Delivery} (S)",
    "numeric/ipc-2023/drone": r"\textsc{Drone} (S)",
    "numeric/ipc-2023/expedition": r"\textsc{Expedition} (S)",
    "numeric/ipc-2023/ext-plant-watering": r"\textsc{PlantWatering} (S)",
    "numeric/ipc-2023/farmland": r"\textsc{Farmland} (S)",
    "numeric/ipc-2023/fo-farmland": r"\textsc{Farmland} (L)",
    "numeric/ipc-2023/fo-sailing": r"\textsc{Sailing} (L)",
    "numeric/ipc-2023/fo_counters": r"\textsc{Counters} (L)",
    "numeric/ipc-2023/hydropower": r"\textsc{HydroPower} (S)",
    # "numeric/ipc-2023/markettrader": r"\textsc{MarketTrader}",
    "numeric/ipc-2023/mprime": r"\textsc{MPrime} (S)",
    "numeric/ipc-2023/pathwaysmetric": r"\textsc{PathwaysMetric} (S)",
    "numeric/ipc-2023/rover": r"\textsc{Rover} (S)",
    "numeric/ipc-2023/sailing": r"\textsc{Sailing} (S)",
    "numeric/ipc-2023/satellite": r"\textsc{Satellite} (S)",
    "numeric/ipc-2023/settlers": r"\textsc{Settlers} (S)",
    "numeric/ipc-2023/sugar": r"\textsc{Sugar} (S)",
    "numeric/ipc-2023/tpp": r"\textsc{TPP} (L)",
    "numeric/ipc-2023/zenotravel": r"\textsc{ZenoTravel} (S)",
    "numeric/line-exchange": r"\textsc{LineExchange} (L)",
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
    exp = "2024-06-26-REBUTTAL-PUSHING-V4"
    file = f"benchmarks/results/{exp}.csv"

    joinWith = [] + [file]
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
            "avgVarsInRules": dict(),
            "lastCallsToSolver": dict(),
            "actions": dict(),
            "patternLength": dict(),
            "maxRolling": dict(),
            "distinctActionsInPlan": dict()
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
            t[domain]["coverage"][solver] = r(sum([r.solved for r in pResult]) / TOTALS[domain] * 100, 0)
            t[domain]["coverage"][solver] = "-" if t[domain]["coverage"][solver] == "0" else t[domain]["coverage"][
                solver]
            bounds = [r.bound for r in pResult if r.solved if r.problem in commonlySolved]
            t[domain]["bound"][solver] = r(statistics.mean(bounds), 1) if t[domain]["coverage"][
                                                                              solver] != "-" and bounds else "-"
            t[domain]["time"][solver] = r(statistics.mean([r.time if r.solved else TIME_LIMIT for r in pResult]) / 1000,
                                          1) if \
                t[domain]["coverage"][solver] != "-" else "-"
            t[domain]["length"][solver] = r(statistics.mean([r.planLength for r in pResult if r.solved]), 0) if \
                t[domain]["coverage"][solver] != "-" else "-"

            v = [r.nOfVars for r in pResult if r.nOfVars > 0 and r.problem in commonlySolved]
            t[domain]["nOfVars"][solver] = r(statistics.mean(v), 0) if len(v) else "-"
            v = [r.nOfRules for r in pResult if r.nOfRules > 0 and r.problem in commonlySolved]
            t[domain]["nOfRules"][solver] = r(statistics.mean(v), 0) if len(v) else "-"
            v = [r.avgVarsInRules for r in pResult if r.avgVarsInRules > 0 and r.problem in commonlySolved]
            t[domain]["avgVarsInRules"][solver] = r(statistics.mean(v), 2) if len(v) else "-"
            v = [r.lastCallsToSolver for r in pResult if r.lastCallsToSolver > 0 and r.problem in commonlySolved]
            t[domain]["lastCallsToSolver"][solver] = r(statistics.mean(v), 2) if len(v) else "-"
            v = [r.actions for r in pResult if r.problem in commonlySolved]
            t[domain]["actions"][solver] = r(statistics.mean(v), 2) if len(v) else "-"
            v = [r.patternLength for r in pResult if r.patternLength > 0 and r.problem in commonlySolved]
            t[domain]["patternLength"][solver] = r(statistics.mean(v), 2) if len(v) else "-"
            v = [r.maxRolling for r in pResult if r.maxRolling > 0 and r.problem in commonlySolved]
            t[domain]["maxRolling"][solver] = r(statistics.mean(v), 2) if len(v) else "-"
            v = [r.distinctActionsInPlan for r in pResult if
                 r.distinctActionsInPlan > 0 and r.problem in commonlySolved]
            t[domain]["distinctActionsInPlan"][solver] = r(statistics.mean(v), 2) if len(v) else "-"

    domainsClusters = {
        r"\textit{Highly Numeric}": [
            "numeric/ipc-2023/block-grouping",
            "numeric/ipc-2023/counters",
            "numeric/ipc-2023/fo_counters",
            "numeric/ipc-2023/drone",
            "numeric/ipc-2023/ext-plant-watering",
            "numeric/ipc-2023/farmland",
            "numeric/ipc-2023/fo-farmland",
            "numeric/ipc-2023/hydropower",
            "numeric/ipc-2023/sailing",
            "numeric/ipc-2023/fo-sailing",
            "numeric/line-exchange",
            # "line-exchange-quantity"
        ],
        r"\textit{Lowly Numeric}": [
            "numeric/ipc-2023/delivery",
            "numeric/ipc-2023/expedition",
            # "numeric/ipc-2023/markettrader",
            "numeric/ipc-2023/mprime",
            "numeric/ipc-2023/pathwaysmetric",
            "numeric/ipc-2023/rover",
            "numeric/ipc-2023/satellite",
            # "numeric/ipc-2023/settlers",
            "numeric/ipc-2023/sugar",
            "numeric/ipc-2023/tpp",
            "numeric/ipc-2023/zenotravel"
        ]
    }

    winners = {
        "coverage": +1,
        "bound": -1,
        "time": -1,
        "nOfVars": -1,
        "nOfRules": -1,
        "avgVarsInRules": -1,
        "lastCallsToSolver": -1,
        "actions": -1,
        "patternLength": -1,
        "maxRolling": -1,
        "distinctActionsInPlan": -1,
    }

    tables = [{
        "name": "tab:exp-patty",
        "type": "table",
        "avoidTotals": True,
        "generalStats": True,
        "width": r"\textwidth",
        "columns": {
            # "coverage": ("Coverage (\%)", {"SMT", "SEARCH"}, {}),
            # "time": ("Time (s)", {"SMT", "SEARCH"}, {}),
            # "bound": (r"Calls to \textsc{Solve}", {"SMT"}, {}),
            # "nOfVars": ("$|\mathcal{X} \cup \mathcal{A} \cup \mathcal{X}'|$", {"SMT"}, {}),
            # "nOfRules": ("$|\mathcal{T}(\mathcal{X},\mathcal{A},\mathcal{X}')|$", {"SMT"}, {}),
            "actions": ("$|A|$", {"SMT"}, {}),
            # "patternLength": ("$|\prec|$", {"SMT"}, {}),
            "distinctActionsInPlan": ("$|A(\pi)|$", {"SMT"}, {}),
            "nOfRules": ("$|R(\pi)|$", {"SMT"}, {}),
            "maxRolling": ("$\max \mathsf{a}_i$", {"SMT"}, {}),

            # "lastCallsToSolver": (r"$\textsc{Solve}(\Pi^\prec)$ calls", {"SMT"}),
        },
        "planners": [{
            'PATTY-G': "SMT",
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
        "caption": r"Statistics averaged on the problems of each domain. $A$ is the number of actions, "
                   r"$A(\pi) \subseteq A$ is the set of actions in the plan $\pi$, $R(\pi) \subseteq A(\pi)$ is the "
                   r"set of actions in the plan $\pi$ consecutively executed more than once, $\max \mathsf{a} _i$ is "
                   r"the maximum amount of consecutive e achieved in the plan."
    }, {
        "name": "tab:exp-search",
        "type": "table",
        "width": r"\columnwidth",
        "avoidTotals": False,
        "generalStats": False,
        "columns": {
            "coverage": ("Coverage (\%)", {"SMT", "SEARCH"}, {}),
            "time": ("Time (s)", {"SMT", "SEARCH"}, {}),
            "bound": (r"Bound ($n$)", {"SMT"}, {}),
            "nOfVars": ("Vars", {"SMT"}, {}),
            "nOfRules": ("Rules", {"SMT"}, {}),
            "avgVarsInRules": ("Vars x Rule", {"SMT"}, {}),
        },
        "planners": [
            {
                'PATTY-O': "SMT",
                'PATTY-G': "SMT",
            }
        ],
        "caption": r"Comparison between $\textsc{patty}_\mathrm{O}$ with the standard increase of the bound and "
                   r"$\textsc{patty}_\mathrm{G}$ with the concatenation of the pattern. The table shows the number, "
                   r"in the final encoding which found the solution, of variables, rules, and avg. number of variables "
                   r"per rule. "
    }, {
        "name": "tab:exp-search",
        "type": "table",
        "width": r"\columnwidth",
        "avoidTotals": False,
        "generalStats": False,
        "columns": {
            "actions": ("$|A|$", {"SMT"}, {"PATTY-G"}),
            "bound": (r"Concats", {"SMT"}, {}),
            "patternLength": ("$|\prec|$", {"SMT"}, {}),
        },
        "planners": [
            {
                'PATTY-G': "SMT",
                'PATTY-H': "SMT",
                'PATTY-F': "SMT",
            }
        ],
        "caption": r"Average number of concatenations and average length of the pattern when the solution was found "
                   r"in all three presented approaches."
    }]

    latex = []
    latex.append(r"""
           \documentclass[11pt]{article}
           \usepackage{graphicx}
           \usepackage{lscape}
           \usepackage{multirow}
           \usepackage[a4paper,margin=1in]{geometry}""")
    latex.append(COMMANDS)
    latex.append(r"""
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
        for (stat, (name, statTypes, onlyForSolvers)) in table["columns"].items():
            nCells = 0
            clString = []
            for cluster in table["planners"]:
                clCells = 0
                for (solver, type) in cluster.items():
                    if type not in statTypes or (onlyForSolvers and solver not in onlyForSolvers):
                        continue
                    solversHeader.append(f"${SOLVERS[solver]}$" if not onlyForSolvers else "")
                    nCells += 1
                    clCells += 1
                if clCells > 0:
                    clString.append(clCells * 'c')
            cString += f"|{'|'.join(clString)}|"
            mString.append(r"\multicolumn{" + str(nCells) + "}{c||}{" + name + "}")

        columns = f"|l|{cString}" + "|"

        latex.append(r"\begin{tabular}{" + columns + "}")
        latex.append(r"\hline")
        latex.append(fr"{'Domain' if table['generalStats'] else ''} & " + "&".join(mString) + r"\\")
        if not table["generalStats"]:
            latex.append(fr"Domain & " + "&".join(solversHeader) + r"\\")
        latex.append(fr"\hline")

        for (cluster, clusterDomains) in domainsClusters.items():
            rows = []
            row = [cluster]
            for (stat, (name, statTypes, onlyForSolvers)) in table["columns"].items():
                for i, plCluster in enumerate(table["planners"]):
                    for (solver, type) in plCluster.items():
                        if type not in statTypes or (onlyForSolvers and solver not in onlyForSolvers):
                            continue
                        nOfBest = 0
                        for domain in clusterDomains:
                            if solver in best[i][domain][stat]:
                                nOfBest += 1
                        row.append(r"\textbf{" + str(nOfBest) + "}" if not onlyForSolvers else "")
            if not table["avoidTotals"]:
                latex.append("&".join(row) + r"\\\hline")
            for domain in clusterDomains:
                row = [DOMAINS[domain]]
                for (stat, (name, statTypes, onlyForSolvers)) in table["columns"].items():
                    for i, plCluster in enumerate(table["planners"]):
                        for (solver, type) in plCluster.items():
                            if type not in statTypes or (onlyForSolvers and solver not in onlyForSolvers):
                                continue
                            if solver not in t[domain][stat]:
                                row.append("TBD")
                                continue
                            if solver in best[i][domain][stat] and not table["avoidTotals"]:
                                row.append(r"\textbf{" + t[domain][stat][solver] + "}" if not onlyForSolvers else
                                           t[domain][stat][solver])
                            else:
                                row.append(t[domain][stat][solver])
                rows.append("&".join(row))
            latex.append("\\\\\n".join(rows))
            latex.append(fr"\\\hline")

        row = [r"\textit{Total}"]
        for (stat, (name, statTypes, onlyForSolvers)) in table["columns"].items():
            for i, plCluster in enumerate(table["planners"]):
                for (solver, type) in plCluster.items():
                    if type not in statTypes or (onlyForSolvers and solver not in onlyForSolvers):
                        continue
                    nOfBest = 0
                    for (cluster, clusterDomains) in domainsClusters.items():
                        for domain in clusterDomains:
                            if solver in best[i][domain][stat]:
                                nOfBest += 1
                    row.append(r"\textbf{" + str(nOfBest) + "}" if not onlyForSolvers else "")

        if not table["avoidTotals"]:
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
