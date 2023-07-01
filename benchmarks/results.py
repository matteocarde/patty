import statistics

import csv
from pip._internal.utils.misc import tabulate
from prettytable import PrettyTable

from classes.Result import Result

SOLVERS = {
    'SpringRoll': "SR",
    'PATTY-arpg-yices-binary': "P_{arpg}^{y,b}",
    'PATTY-arpg-z3-binary': "P_{arpg}^{z3,b}",
    'PATTY-arpg-z3-non-linear': "P_{arpg}^{z3,nl}",
    'PATTY-random-yices-binary': "P_{r}^{y,b}",
    'PATTY-random-z3-binary': "P_{r}^{z3,b}",
    'PATTY-random-z3-non-linear': "P_r^{z3,nl}",
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
    file = "benchmarks/results/2023-07-01-SMT-v3.csv"
    results: [Result] = []
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
            t[domain]["coverage"][solver] = round(sum([r.solved for r in pResult]) / TOTALS[domain] * 100, 2)
            t[domain]["bound"][solver] = round(statistics.mean([r.bound for r in pResult if r.solved]), 2)
            t[domain]["time"][solver] = round(statistics.mean([r.time for r in pResult if r.solved]) / 1000, 2)
            t[domain]["length"][solver] = round(statistics.mean([r.planLength for r in pResult if r.solved]), 2)
            stats = t[domain].keys()

    STATS_TR = {
        "coverage": "Coverage (\%)",
        "bound": "Bound",
        "time": "Time (s)",
        "length": "Plan Length"
    }

    print(r"""
        \begin{table}[]
        \centering
        \resizebox{\columnwidth}{!}{""")
    columns = f"|l|{len(stats) * ('|' + 'c' * len(solvers) + '|')}" + "|"
    print(r"\begin{tabular}{" + columns + "}")
    print(r"\hline")
    print(fr" & " + "&".join(
        [r"\multicolumn{" + str(len(solvers)) + "}{c||}{" + STATS_TR[s] + "}" for s in stats]) + r"\\")
    print(fr"Domain & " + "&".join([f"${SOLVERS[p]}$" for s in stats for p in solvers]) + r"\\")
    print(fr"\hline")

    rows = []
    for domain in domains:
        row = [domain.replace(r"_", r"\_")]
        for stat in stats:
            for solver in solvers:
                row.append(str(t[domain][stat][solver]))
        rows.append("&".join(row))
    print("\\\\\n".join(rows))
    print(fr"\\\hline")

    print(r"""
    \end{tabular}}
    \caption{Comparative analysis against the two symbolic-based solvers \textsc{Patty} (P) and \textsc{SpringRoll} (SR). $P_{\prec}^{s,e}$ represents the \textsc{Patty} solver with the pattern $\prec \in \{r,arpg\}$ for random and ARPG, the solver $s \in \{y, z3\}$ for yices and z3, the encoding $e \in \{b, nl\}$ for the binary and non-linear version of the encoding.}
    \label{tab:my-table}
    \end{table}
    """)

    pass


if __name__ == '__main__':
    main()
