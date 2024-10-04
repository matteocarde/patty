from __future__ import annotations

import statistics

import json

import re

from typing import List, Dict, Callable


class Result(dict):
    solver: str = ""
    domain: str
    problem: str
    time: int = -1  # ms
    bound: int = -1
    plan: List[str]
    planLength: int = -1
    solved: bool = False
    timeout: bool = False
    stdout: str = ""
    cmd: str = ""
    nOfVars: int = -1
    nOfRules: int = -1
    lastSearchedBound: int = -1
    lastCallsToSolver: int = -1

    def __init__(self, domain: str, problem: str):
        super().__init__()
        self.plan = list()
        self.domain = domain
        self.problem = problem.split("/")[-1]

    @classmethod
    def fromCSVLine(cls, csvLine: str):
        r = cls("x", "x")
        r.solver = csvLine[0]
        r.domain = csvLine[1]
        r.problem = csvLine[2]
        r.solved = csvLine[3] == "True"
        r.timeout = csvLine[4] == "True"
        r.time = float(csvLine[5])
        r.bound = int(csvLine[6])
        r.planLength = float(csvLine[7])
        r.nOfVars = int(csvLine[8])
        r.nOfRules = int(csvLine[9])
        r.lastSearchedBound = int(csvLine[10])
        if len(csvLine) > 11:
            r.lastCallsToSolver = int(csvLine[11])
        r.__setDict()
        return r

    def __setDict(self):
        self["solved"] = self.solved
        self["timeout"] = self.timeout
        self["time"] = self.time
        self["bound"] = self.bound
        self["planLength"] = self.planLength
        self["nOfVars"] = self.nOfVars
        self["nOfRules"] = self.nOfRules
        self["lastSearchedBound"] = self.lastSearchedBound
        self["lastCallsToSolver"] = self.lastCallsToSolver

    @classmethod
    def parseTime(cls, stdout):
        reTime = re.findall(r"^real (.*?)$", stdout, re.MULTILINE)
        time = reTime[0] if len(reTime) > 0 else 0
        return float(time) * 1000

    def __str__(self):
        row = [
            (str(self.solver), 30),
            (str(self.domain), 20),
            (str(self.problem), 30),
            (str(self.solved), 6),
            (str(self.timeout), 6),
            (str(self.time), 8),
            (str(self.bound), 5),
            (str(self.planLength), 5),
            (str(self.nOfVars), 5),
            (str(self.nOfRules), 5),
            (str(self.lastSearchedBound), 5),
            (str(self.lastCallsToSolver), 5)
        ]

        string = "|" + "|".join(["{:^" + str(n[1]) + "}" for n in row]) + "|"
        values = [n[0] for n in row]
        return string.format(*values)

    def toCSV(self):
        return ",".join([
            str(self.solver),
            str(self.domain),
            str(self.problem),
            str(self.solved),
            str(self.timeout),
            str(self.time),
            str(self.bound),
            str(self.planLength),
            str(self.nOfVars),
            str(self.nOfRules),
            str(self.lastSearchedBound),
            str(self.lastCallsToSolver),
        ])

    @classmethod
    def aggregator(cls, results: [Result], agg: Callable[List[float], float], solver=None) -> Result:
        r = cls("x", "x")
        r.solver = results[0].solver if not solver else solver
        r.domain = results[0].domain
        r.problem = results[0].problem
        r.solved = statistics.mean([1 if e.solved else 0 for e in results])
        r.timeout = statistics.mean([1 if e.timeout else 0 for e in results])
        r.nOfVars = agg([e.nOfVars for e in results])
        r.nOfRules = agg([e.nOfRules for e in results])
        r.lastSearchedBound = agg([e.lastSearchedBound for e in results])
        r.lastCallsToSolver = agg([e.lastCallsToSolver for e in results])
        if r.solved > 0:
            r.time = agg([e.time for e in results if e.solved])
            r.bound = agg([e.bound for e in results if e.solved])
            r.planLength = agg([e.planLength for e in results if e.solved])
        r.solved = bool(r.solved)
        r.timeout = bool(r.timeout)
        r.__setDict()
        return r

    @classmethod
    def max(cls, results: [Result], solver=None):
        return Result.aggregator(results, max, solver)

    @classmethod
    def min(cls, results: [Result], solver=None):
        return Result.aggregator(results, min, solver)

    @classmethod
    def avg(cls, results: [Result], solver=None):
        return Result.aggregator(results, statistics.mean, solver)

    @classmethod
    def stdev(cls, results: [Result], solver=None):
        return Result.aggregator(results, mystdev, solver)

    @classmethod
    def portfolio(cls, portfolio: [Result], solver: str) -> Result:
        solved = [r for r in portfolio if r.solved]
        if not solved:
            result = portfolio[0]
            result.solver = solver
            return result

        minResult: Result = solved[0]
        for r in solved:
            if r.time < minResult.time:
                minResult = r

        minResult.solver = solver
        return minResult

    @classmethod
    def joinPorfolios(cls, aResults: List[Result], PORTFOLIOS: Dict[str, str]) -> List[Result]:
        results = list()
        pResults: Dict[str, Dict[str, Dict[str, List[Result]]]] = dict()

        for r in aResults:
            if r.solver not in PORTFOLIOS:
                results.append(r)
                continue
            solver = PORTFOLIOS[r.solver]
            pResults.setdefault(solver, dict())
            pResults[solver].setdefault(r.domain, dict())
            pResults[solver][r.domain].setdefault(r.problem, list())
            pResults[solver][r.domain][r.problem].append(r)

        for (solver, solverDict) in pResults.items():
            for (domain, domainDict) in solverDict.items():
                for (problem, portfolio) in domainDict.items():
                    results.append(Result.portfolio(portfolio, solver))
        return results

    @classmethod
    def splitRandom(cls, aResults: List[Result], randomSolver: str) -> List[Result]:

        results: List[Result] = list()
        rResults: Dict[str, Dict[str, List[Result]]] = dict()

        for r in aResults:
            if r.solver != randomSolver:
                results.append(r)
                continue
            rResults.setdefault(r.domain, dict())
            rResults[r.domain].setdefault(r.problem, list())
            rResults[r.domain][r.problem].append(r)

        for (domain, domainDict) in rResults.items():
            for (problem, problems) in domainDict.items():
                results.append(Result.avg(problems, f"{randomSolver}-AVG"))
                results.append(Result.stdev(problems, f"{randomSolver}-STDEV"))

        return results

    def toJSON(self):
        return json.dumps(self.__dict__)


def mystdev(el):
    if len(el) < 2:
        return 0
    return statistics.stdev(el)
