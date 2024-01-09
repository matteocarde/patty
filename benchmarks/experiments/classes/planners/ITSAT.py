import re

from classes.planners.Planner import Planner
from classes.Result import Result

NAME = "ITSAT"


class ITSAT(Planner):
    name = NAME

    def __init__(self):
        self.name = f"{NAME}"
        super().__init__()

    @staticmethod
    def parseOutput(r: Result, stdout: str):
        r.solved = len(re.findall(r"Valid Timed Plan found!", stdout)) > 0
        r.time = Result.parseTime(stdout)
        r.plan = re.findall(r"^(\d.*?.\d.*?): \((.*?)\) \[(.*?)\]", stdout, re.MULTILINE)
        r.planLength = len(r.plan)

        return r

    def getCommand(self, domain: str, problem: str):
        return ["itsat", "-alg", "layer", domain, problem, "*"]
