import re

from classes.Planner import Planner
from classes.Result import Result

NAME = "LPG"


class LPG(Planner):
    name = NAME

    def __init__(self):
        self.name = f"{NAME}"
        super().__init__()

    @staticmethod
    def parseOutput(r: Result, stdout: str):
        r.solved = len(re.findall(r"Plan computed:", stdout)) > 0
        r.time = Result.parseTime(stdout)
        r.plan = re.findall(r"^ (\d.*?\.\d.*?): \((.*?)\) \[D:(.*?); C:(.*?)\]$", stdout, re.MULTILINE)
        r.planLength = len(r.plan)

        return r

    def getCommand(self, domain: str, problem: str):
        return ["lpg-td", "-o", domain, "-f", problem, "-n", "1"]
