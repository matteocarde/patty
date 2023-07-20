import csv
import statistics

from classes.Result import Result

SOLVERS = {
    'SpringRoll': "SR",
    'PATTY': "P_{arpg}",
    'PATTY-R': "P_r",
    'RANTANPLAN': "\mathrm{RTP}",
    'METRIC-FF': "\mathrm{FF}",
    'ENHSP-sat-hadd': r"E_{hadd}",
    'ENHSP-sat-hradd': r"E_{hradd}",
    'ENHSP-sat-hmrphj': r"E_{hmrphj}",
    'NFD': "\mathrm{NFD}",
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
    files = [
        "benchmarks/results/2023-07-20-IPC-v8.csv"
    ]
    results: [Result] = []
    for file in files:
        with open(file, "r") as f:
            reader = csv.reader(f, delimiter=",")
            for i, line in enumerate(reader):
                results.append(Result.fromCSVLine(line[0].split(",")))

    solvers = set()
    sorted(solvers)
    domains = set()
    sorted(domains)

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

        pResult: [Result]
        for solver in solvers:
            if solver not in domainDict:
                continue
            pResult = domainDict[solver]
            t[domain]["coverage"][solver] = r(sum([r.solved for r in pResult]) / TOTALS[domain] * 100, 1)
            t[domain]["coverage"][solver] = "-" if t[domain]["coverage"][solver] == "0.0" else t[domain]["coverage"][
                solver]
            t[domain]["bound"][solver] = r(statistics.mean([r.lastSearchedBound for r in pResult if r.solved]), 2) if \
                t[domain]["coverage"][solver] != "-" else "-"
            t[domain]["time"][solver] = r(statistics.mean([r.time if r.solved else 300000 for r in pResult]) / 1000,
                                          2) if \
                t[domain]["coverage"][solver] != "-" else "-"
            t[domain]["length"][solver] = r(statistics.mean([r.planLength for r in pResult if r.solved]), 0) if \
                t[domain]["coverage"][solver] != "-" else "-"
            v = [r.nOfVars for r in pResult if r.nOfVars > 0]
            t[domain]["nOfVars"][solver] = r(statistics.mean(v), 0) if len(v) else "G"
            v = [r.nOfRules for r in pResult if r.nOfRules > 0]
            t[domain]["nOfRules"][solver] = r(statistics.mean(v), 0) if len(v) else "G"

    domainsClusters = {
        "Purely Numeric": [
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
            "ipc-2023/satellite",
            "line-exchange",
            "line-exchange-quantity"
        ],
        "Scarcely Numeric": [
            "ipc-2023/delivery",
            "ipc-2023/expedition",
            # "ipc-2023/markettrader",
            "ipc-2023/mprime",
            "ipc-2023/pathwaysmetric",
            "ipc-2023/rover",
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
        "name": "tab:exp-smt",
        "columns": {
            "coverage": "Coverage (\%)",
            "bound": "Bound",
            "time": "Time (s)",
            "nOfVars": "Vars $n=1$",
            "nOfRules": "Rules $n=1$",
        },
        "solvers": [
            'PATTY',
            'PATTY-R',
            'RANTANPLAN',
            'SpringRoll'
        ],
        "caption": r"Comparative analysis between the SMT-based solvers \textsc{Patty} (P), "
                   r"\textsc{SpringRoll} (SR) and \textsc{RanTanPlan} (RTP). $P_{\prec}$ represents the \textsc{Patty} "
                   r"solver with a pattern built randomly (r) or with the ARPG (arpg). The labels S and L specifies if the domain presents simple "
                   r"or linear effects, respectively. $G$ signifies all the instances couldn't be grounded."
    }, {
        "name": "tab:exp-search",
        "columns": {
            "coverage": "Coverage (\%)",
            "time": "Time (s)",
            # "length": "Plan Length"
        },
        "solvers": [
            # 'PATTY-arpg-yices-binary',
            'PATTY',
            'RANTANPLAN',
            'SpringRoll',
            'ENHSP-sat-hradd',
            'ENHSP-sat-hadd',
            'ENHSP-sat-hmrphj',
            'METRIC-FF',
            "NFD"
        ],
        "caption": r"Comparative analysis between \textsc{Patty} and two search-based solvers \textsc{ENHSP} (E) and "
                   r"\textsc{MetricFF} (FF). The \textsc{ENHSP} solver has been launched with the GBFS search "
                   r"strategy and the two heuristics $hadd$ and $hradd$."
    }]

    for table in tables:
        stats = table["columns"].keys()
        solvers = table["solvers"]

        best = dict()
        for (domain, domainDict) in d.items():
            best[domain] = dict()
            for stat in table["columns"].keys():
                better = {}
                betterValue = float("-inf") if winners[stat] > 0 else float("+inf")
                for solver in solvers:
                    value = t[domain][stat][solver]
                    if value in {"-", "G"}:
                        continue
                    if float(value) * winners[stat] > betterValue * winners[stat]:
                        betterValue = float(value)
                        better = {solver}
                    elif float(value) == betterValue:
                        better |= {solver}
                best[domain][stat] = better

        print(r"""
            \begin{table}[]
            \centering
            \resizebox{\columnwidth}{!}{""")
        columns = f"|l|{len(stats) * ('|' + 'c' * len(solvers) + '|')}" + "|"
        print(r"\begin{tabular}{" + columns + "}")
        print(r"\hline")
        print(fr" & " + "&".join(
            [r"\multicolumn{" + str(len(solvers)) + "}{c||}{" + table["columns"][s] + "}" for s in stats]) + r"\\")
        print(fr"Domain & " + "&".join([f"${SOLVERS[p]}$" for s in stats for p in solvers]) + r"\\")
        print(fr"\hline")

        for (cluster, clusterDomains) in domainsClusters.items():
            rows = []
            row = [cluster] + [" "] * len(stats) * len(solvers)
            print("&".join(row) + r"\\\hline")
            for domain in clusterDomains:
                row = [DOMAINS[domain]]
                for stat in stats:
                    for solver in solvers:
                        if solver not in t[domain][stat]:
                            row.append("-")
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
        \label{tab:""" + table["name"] + """}
        \end{table}
        """)

    pass


if __name__ == '__main__':
    main()
