import re

from classes.Planner import Planner
from classes.Result import Result

NAME = "ENHSP"


class ENHSP(Planner):
    name = NAME

    def __init__(self, p: str):
        self.p = p
        self.name = f"{NAME}-{p}"
        super().__init__()

    @staticmethod
    def parseOutput(r: Result, stdout: str):
        r.solved = len(re.findall(r"Problem Solved", stdout)) > 0
        r.time = Result.parseTime(stdout)
        r.plan = re.findall(r"^.*?: (\(.*?\))$", stdout, re.MULTILINE)
        rePlanLength = re.findall(r"Metric (Search):(.*?)$", stdout, re.MULTILINE)
        r.planLength = len(r.plan) if not rePlanLength else int(rePlanLength[-1])

        return r

    def getCommand(self, domain: str, problem: str):
        return ["enhsp", "-o", domain, "-f", problem, "-planner", self.p]
