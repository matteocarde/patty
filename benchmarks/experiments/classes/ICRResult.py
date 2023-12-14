from __future__ import annotations

import json
import re


class ICRResult:
    expType: str
    domain: str
    problem: str
    time: int = -1  # ms
    solved: bool = False
    timeout: bool = False
    stdout: str = ""
    cmd: str = ""
    optimum: float = 0
    dRW: float = 0
    dRC: float = 0
    nOfAtoms: int = 0
    traceLength: int = 0
    nOfConditions: int = 0
    timeICS: int = -1
    timeICR: int = -1

    def __init__(self, expType: str, domain: str, problem: str):
        self.plan = list()
        self.expType = expType
        self.domain = domain
        self.problem = problem.split("/")[-1]
        pass

    @classmethod
    def fromCSVLine(cls, csvLine: str):
        r = cls("x", "x", "x")
        r.expType = csvLine[0]
        r.domain = csvLine[1]
        r.problem = csvLine[2]
        r.solved = csvLine[3] == "True"
        r.timeout = csvLine[4] == "True"
        r.time = float(csvLine[5])
        r.optimum = float(csvLine[6])
        r.dRW = float(csvLine[7])
        r.dRC = float(csvLine[8])
        r.nOfAtoms = float(csvLine[9])
        r.traceLength = float(csvLine[10])
        r.nOfConditions = float(csvLine[11])
        if len(csvLine) > 12:
            r.timeICS = float(csvLine[12])
            r.timeICR = float(csvLine[13])

        return r

    @classmethod
    def parseTime(cls, stdout):
        reTime = re.findall(r"Overall: (.*?)ms$", stdout, re.MULTILINE)
        time = reTime[0] if len(reTime) > 0 else 0
        return float(time)

    def __str__(self):
        row = [
            (str(self.expType), 10),
            (str(self.domain), 20),
            (str(self.problem), 30),
            (str(self.solved), 6),
            (str(self.timeout), 6),
            (str(self.time), 8),
            (str(self.optimum), 8),
            (str(self.dRW), 8),
            (str(self.dRC), 8),
            (str(self.nOfAtoms), 8),
            (str(self.traceLength), 8),
            (str(self.nOfConditions), 8),
            (str(self.timeICS), 8),
            (str(self.timeICR), 8),
        ]

        string = "|" + "|".join(["{:^" + str(n[1]) + "}" for n in row]) + "|"
        values = [n[0] for n in row]
        return string.format(*values)

    def toJSON(self):
        return json.dumps(self.__dict__)

    def toCSV(self):
        return ",".join([
            str(self.expType),
            str(self.domain),
            str(self.problem),
            str(self.solved),
            str(self.timeout),
            str(self.time),
            str(self.optimum),
            str(self.dRW),
            str(self.dRC),
            str(self.nOfAtoms),
            str(self.traceLength),
            str(self.nOfConditions),
            str(self.timeICS),
            str(self.timeICR),
        ])
