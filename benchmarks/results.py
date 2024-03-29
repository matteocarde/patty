import csv
import statistics
from typing import Dict, List

from classes.Result import Result

SMT_SOLVERS = {'SpringRoll', 'PATTY', 'RANTANPLAN', "OMT"}

SOLVERS = {
    'SpringRoll': "SR",
    'PATTY': "P",
    # 'PATTY-R': "P_r",
    'RANTANPLAN': "\mathrm{R^2\exists}",
    'METRIC-FF': "\mathrm{FF}",
    'ENHSP': r"\mathrm{ENHSP}",
    'NFD': "\mathrm{NFD}",
    'SMTPLAN+': "\mathrm{SMTP}^+",
    'OMT': "\mathrm{OMT}",
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
    ## Parsing the results
    files = [
        "benchmarks/results/FINAL.csv"
    ]

    aResults: [Result] = []
    for file in files:
        with open(file, "r") as f:
            reader = csv.reader(f, delimiter=",")
            for i, line in enumerate(reader):
                aResults.append(Result.fromCSVLine(line[0].split(",")))

    ## Joining together portfolios
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
        }

        commonlySolved = {}
        commonlyGrounded = {}
        for solver in SMT_SOLVERS:
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
            t[domain]["time"][solver] = r(statistics.mean([r.time if r.solved else 300000 for r in pResult]) / 1000,
                                          2) if \
                t[domain]["coverage"][solver] != "-" else "-"
            t[domain]["length"][solver] = r(statistics.mean([r.planLength for r in pResult if r.solved]), 0) if \
                t[domain]["coverage"][solver] != "-" else "-"

            v = [r.nOfVars for r in pResult if r.nOfVars > 0 and r.problem in commonlyGrounded]
            t[domain]["nOfVars"][solver] = r(statistics.mean(v), 0) if len(v) else "-"
            v = [r.nOfRules for r in pResult if r.nOfRules > 0 and r.problem in commonlyGrounded]
            t[domain]["nOfRules"][solver] = r(statistics.mean(v), 0) if len(v) else "-"

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
            # "line-exchange",
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
    }

    tables = [{
        "name": "tab:experiments",
        "type": "table*",
        "width": r"\textwidth",
        "columns": {
            "coverage": ("Coverage (\%)", {"SMT", "SEARCH"}),
            "time": ("Time (s)", {"SMT", "SEARCH"}),
            "bound": ("Bound (Common)", {"SMT"}),
            "nOfVars": ("$|\mathcal{X} \cup \mathcal{A} \cup \mathcal{X}'|$", {"SMT"}),
            "nOfRules": ("$|\mathcal{T}(\mathcal{X},\mathcal{A},\mathcal{X}')|$", {"SMT"}),
        },
        "solvers": {
            'PATTY': "SMT",
            # 'PATTY-R',
            'RANTANPLAN': "SMT",
            'SpringRoll': "SMT",
            "OMT": "SMT",
            'ENHSP': "SEARCH",
            'METRIC-FF': "SEARCH",
            "NFD": "SEARCH"
        },
        "caption": r"Comparative analysis between the \textsc{Patty} (P) planner, the symbolic planners \textsc{\re{"
                   r"}} (\re), \textsc{SpringRoll} (SR), \textsc{OMTPlan} (OMT) and the search-based planners "
                   r"\textsc{ENHSP} (E), \textsc{MetricFF} (FF) and \textsc{NumericFastDownward} (NFD). The labels S "
                   r"and L specify if the domain presents simple or linear effects, respectively, see \cite{ipc2023}. "
                   r"''Best numbers'' are in bold. The numbers in the Highly and Lowly Numeric rows are the number of "
                   r"bolds in the subcolumn."
    },
        #     {
        #     "name": "tab:exp-search",
        #     "type": "table",
        #     "width": r"\columnwidth",
        #     "columns": {
        #         "coverage": "Coverage (\%)",
        #         "time": "Time (s)",
        #         # "length": "Plan Length"
        #     },
        #     "solvers": [
        #         # 'PATTY-arpg-yices-binary',
        #         'PATTY',
        #         # 'RANTANPLAN',
        #         # 'SpringRoll',
        #         'ENHSP',
        #         'METRIC-FF',
        #         "NFD"
        #     ],
        #     "caption": r"Comparative analysis between \textsc{Patty} and the search-based solvers \textsc{ENHSP} (E), "
        #                r"\textsc{MetricFF} (FF) and \textsc{NumericFastDownward} (NFD)."
        # }
    ]

    for table in tables:
        stats = table["columns"].keys()
        solvers = table["solvers"].keys()

        best = dict()
        for (domain, domainDict) in d.items():
            best[domain] = dict()
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
                best[domain][stat] = better

        print(r"""
            \begin{""" + table["type"] + r"""}[tb]
            \centering
            \resizebox{""" + table["width"] + r"""}{!}{""")

        solversHeader = []
        mString = []
        cString = ""
        for (stat, (name, statTypes)) in table["columns"].items():
            nCells = 0
            for (solver, type) in table["solvers"].items():
                if type not in statTypes:
                    continue
                solversHeader.append(f"${SOLVERS[solver]}$")
                nCells += 1
            mString.append(r"\multicolumn{" + str(nCells) + "}{c||}{" + name + "}")
            cString += f"|{nCells * 'c'}|"

        columns = f"|l|{cString}" + "|"

        print(r"\begin{tabular}{" + columns + "}")
        print(r"\hline")
        print(fr" & " + "&".join(mString) + r"\\")
        print(fr"Domain & " + "&".join(solversHeader) + r"\\")
        print(fr"\hline")

        for (cluster, clusterDomains) in domainsClusters.items():
            rows = []
            row = [cluster]
            for (stat, (name, statTypes)) in table["columns"].items():
                for (solver, type) in table["solvers"].items():
                    if type not in statTypes:
                        continue
                    nOfBest = 0
                    for domain in clusterDomains:
                        if solver in best[domain][stat]:
                            nOfBest += 1
                    row.append(r"\textbf{" + str(nOfBest) + "}")
            print("&".join(row) + r"\\\hline")
            for domain in clusterDomains:
                row = [DOMAINS[domain]]
                for (stat, (name, statTypes)) in table["columns"].items():
                    for (solver, type) in table["solvers"].items():
                        if type not in statTypes:
                            continue
                        if solver not in t[domain][stat]:
                            row.append("TBD")
                            continue
                        if solver in best[domain][stat]:
                            row.append(r"\textbf{" + t[domain][stat][solver] + "}")
                        else:
                            row.append(t[domain][stat][solver])
                rows.append("&".join(row))
            print("\\\\\n".join(rows))
            print(fr"\\\hline")

        print(r"""
        \end{tabular}}
        \caption{""" + table["caption"] + """}
        \label{""" + table["name"] + """}
        \end{""" + table["type"] + """}
        """)

    pass


if __name__ == '__main__':
    main()
