import statistics

import csv
from pip._internal.utils.misc import tabulate
from prettytable import PrettyTable

from classes.Result import Result

SOLVERS = {
    'PATTY-random-z3-non-linear': "PATTY_r^{z3,nl}",
    'SpringRoll': "SR",
    'PATTY-arpg-yices-binary': "PATTY_{arpg}^{y,b}",
    'PATTY-random-yices-binary': "PATTY_{r}^{y,b}",
    'PATTY-random-z3-binary': "PATTY_{r}^{z3,b}",
}


def main():
    file = "benchmarks/results/2023-07-01-SMT-v1.csv"
    results: [Result] = []
    with open(file, "r") as f:
        reader = csv.reader(f, delimiter=",")
        for i, line in enumerate(reader):
            results.append(Result.fromCSVLine(line[0].split(",")))

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

    for domain in domains:
        for solver in solvers:
            problems = list()
            for problem in d[domain][solver].keys():
                problems.append(Result.average(d[domain][solver][problem]))
            d[domain][solver] = problems


    t = dict()

    for (domain, domainDict) in d.items():
        t[domain] = {
            "coverage": dict(),
            "bound": dict(),
            "time": dict(),
            "length": dict(),
        }

        pResult: [Result]
        row = []
        for solver in solvers:
            pResult = domainDict[solver]
            t[domain]["coverage"][solver] = sum([r.solved for r in pResult])
            t[domain]["bound"][solver] = statistics.mean([r.bound for r in pResult if r.solved])
            t[domain]["time"][solver] = statistics.mean([r.time for r in pResult if r.solved])
            t[domain]["length"][solver] = statistics.mean([r.planLength for r in pResult if r.solved])


    pass


if __name__ == '__main__':
    main()
