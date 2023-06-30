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
    def parseTime(cls, stdout):
        time = re.findall(r"^real (.*?)$", stdout, re.MULTILINE)[0]
        return float(time) * 1000

    def __str__(self):
        row = [
            (str(self.solver), 20),
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
