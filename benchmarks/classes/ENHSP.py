import re

from classes.Planner import Planner
from classes.Result import Result

NAME = "ENHSP"


class ENHSP(Planner):
    name = NAME

    def __init__(self, s: str, h: str):
        self.s = s
        self.h = h
        self.name = f"{NAME}-{s}-{h}"
        super().__init__()

    @staticmethod
    def parseOutput(r: Result, stdout: str):
        r.solved = len(re.findall(r"Problem Solved", stdout)) > 0
        r.time = Result.parseTime(stdout)
        r.plan = re.findall(r"^.*?: (\(.*?\))$", stdout, re.MULTILINE)
        r.planLength = len(r.plan)

        return r

    def getCommand(self, domain: str, problem: str):
        return ["enhsp", "-o", domain, "-f", problem, "-s", self.s, "-h", self.h]
