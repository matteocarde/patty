import csv
import statistics

from classes.Result import Result

SOLVERS = {
    'SpringRoll': "SR",
    'PATTY-arpg-yices-binary': "P_{arpg}^{y,la}",
    'PATTY-arpg-z3-binary': "P_{arpg}^{z3,la}",
    'PATTY-arpg-z3-non-linear': "P_{arpg}^{z3,nl}",
    'PATTY-random-yices-binary': "P_{r}^{y,la}",
    'PATTY-random-z3-binary': "P_{r}^{z3,la}",
    'PATTY-random-z3-non-linear': "P_r^{z3,nl}",
    'METRIC-FF': "FF",
    'ENHSP-gbfs-hadd': r"E_{hadd}^{\mathit{gbfs}}",
    'ENHSP-gbfs-hradd': r"E_{hradd}^{\mathit{gbfs}}"
}

DOMAINS = {
    'block-grouping': r"\textsc{BlockGrouping} (S)",
    'farmland': r"\textsc{Farmland} (S)",
    'farmland_ln': r"\textsc{Farmland} (L)",
    'fn-counters': r"\textsc{Counters} (S)",
    'fn-counters-inv': r"\textsc{CountersInv} (S)",
    'fn-counters-rnd': r"\textsc{CountersRnd} (S)",
    'gardening': r"\textsc{Gardening} (S)",
    'plant-watering': r"\textsc{PlantWatering} (S)",
    'sailing': r"\textsc{Sailing} (S)",
    'sailing_ln': r"\textsc{Sailing} (L)"
}

TOTALS = {
    'block-grouping': 192,
    'farmland': 50,
    'farmland_ln': 50,
    'fn-counters': 11,
    'fn-counters-inv': 11,
    'fn-counters-rnd': 33,
    'gardening': 63,
    'plant-watering': 51,
    'sailing': 40,
    'sailing_ln': 20
}


def main():
    files = ["benchmarks/results/2023-07-01-SMT-v3.csv", "benchmarks/results/2023-07-02-SEARCH-v2.csv",
             "benchmarks/results/2023-07-02-SEARCH-v3.csv"]
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
            for problem in d[domain][solver].keys():
                problems.append(Result.average(d[domain][solver][problem]))
            d[domain][solver] = problems


    def r(i, n):
        return '{:.{n}f}'.format(i, n=n)

    t = dict()
    stats = set()
    for (domain, domainDict) in d.items():
        t[domain] = {
            "coverage": dict(),
            "bound": dict(),
            "time": dict(),
            "length": dict(),
        }

        pResult: [Result]
        for solver in solvers:
            pResult = domainDict[solver]
            t[domain]["coverage"][solver] = r(sum([r.solved for r in pResult]) / TOTALS[domain] * 100, 1)
            t[domain]["bound"][solver] = r(statistics.mean([r.bound for r in pResult if r.solved]), 2) if \
                t[domain]["coverage"][solver] != "0.0" else "-"
            t[domain]["time"][solver] = r(statistics.mean([r.time for r in pResult if r.solved]) / 1000, 2) if \
                t[domain]["coverage"][solver] != "0.0" else "-"
            t[domain]["length"][solver] = r(statistics.mean([r.planLength for r in pResult if r.solved]), 0) if \
                t[domain]["coverage"][solver] != "0.0" else "-"

    tables = [{
        "name": "tab:exp-smt",
        "columns": {
            "coverage": "Coverage (\%)",
            "bound": "Bound",
            "time": "Time (s)",
            # "length": "Plan Length"
        },
        "solvers": ['PATTY-arpg-yices-binary',
                    'PATTY-arpg-z3-binary',
                    'PATTY-arpg-z3-non-linear',
                    'PATTY-random-yices-binary',
                    'PATTY-random-z3-non-linear',
                    'SpringRoll'],
        "caption": r"Comparative analysis between the two symbolic-based solvers \textsc{Patty} (P) and \textsc{"
                   r"SpringRoll} (SR). $P_{\prec}^{s,e}$ represents the \textsc{Patty} solver with the pattern $\prec "
                   r"\in \{r,arpg\}$ for random and ARPG, the solver $s \in \{y, z3\}$ for yices and z3, the encoding "
                   r"$e \in \{la, nl\}$ for the linear-arithmetic and non-linear version of the encoding. The labels "
                   r"S and L specifies if the domain presents simple or linear effects, respectively."
    }, {
        "name": "tab:exp-search",
        "columns": {
            "coverage": "Coverage (\%)",
            "time": "Time (s)",
            # "length": "Plan Length"
        },
        "solvers": ['PATTY-arpg-yices-binary',
                    'PATTY-arpg-z3-non-linear',
                    'ENHSP-gbfs-hadd',
                    'ENHSP-gbfs-hradd',
                    'METRIC-FF'],
        "caption": r"Comparative analysis between \textsc{Patty} and two search-based solvers \textsc{ENHSP} (E) and "
                   r"\textsc{MetricFF} (FF). The solver \textsc{ENHSP} has been launched with the GBFS search "
                   r"strategy and the two heuristics $hadd$ and $hradd$."
    }]

    for table in tables:
        stats = table["columns"].keys()
        solvers = table["solvers"]

        print(r"""
            \begin{table*}[]
            \centering
            \resizebox{\textwidth}{!}{""")
        columns = f"|l|{len(stats) * ('|' + 'c' * len(solvers) + '|')}" + "|"
        print(r"\begin{tabular}{" + columns + "}")
        print(r"\hline")
        print(fr" & " + "&".join(
            [r"\multicolumn{" + str(len(solvers)) + "}{c||}{" + table["columns"][s] + "}" for s in stats]) + r"\\")
        print(fr"Domain & " + "&".join([f"${SOLVERS[p]}$" for s in stats for p in solvers]) + r"\\")
        print(fr"\hline")

        rows = []
        for domain in domains:
            row = [DOMAINS[domain]]
            for stat in stats:
                for solver in solvers:
                    row.append(t[domain][stat][solver])
            rows.append("&".join(row))
        print("\\\\\n".join(rows))
        print(fr"\\\hline")

        print(r"""
        \end{tabular}}
        \caption{""" + table["caption"] + """}
        \label{tab:""" + table["name"] + """}
        \end{table*}
        """)

    pass


if __name__ == '__main__':
    main()
