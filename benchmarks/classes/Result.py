from __future__ import annotations

import statistics

import json

import re

from typing import List


class Result:
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

    def __init__(self, domain: str, problem: str):
        self.plan = list()
        self.domain = domain
        self.problem = problem.split("/")[-1]
        pass

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

        return r

    @classmethod
    def parseTime(cls, stdout):
        time = re.findall(r"^real (.*?)$", stdout, re.MULTILINE)[0]
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
            (str(self.planLength), 5)
        ]

        string = "|" + "|".join(["{:^" + str(n[1]) + "}" for n in row]) + "|"
        values = [n[0] for n in row]
        return string.format(*values)

    def toJSON(self):
        return json.dumps(self.__dict__)

    def toCSV(self):
        return ",".join([
            str(self.solver),
            str(self.domain),
            str(self.problem),
            str(self.solved),
            str(self.timeout),
            str(self.time),
            str(self.bound),
            str(self.planLength)
        ])

    @classmethod
    def average(cls, list: [Result]):
        r = cls("x", "x")
        r.solver = list[0].solver
        r.domain = list[0].domain
        r.problem = list[0].problem
        r.solved = statistics.mean([1 if e.solved else 0 for e in list])
        r.timeout = statistics.mean([1 if e.timeout else 0 for e in list])
        if r.solved > 0:
            r.time = statistics.mean([e.time for e in list if e.solved])
            r.bound = statistics.mean([e.bound for e in list if e.solved])
            r.planLength = statistics.mean([e.planLength for e in list if e.solved])
        return r
