import re

from classes.Result import Result
from classes.planners.Planner import Planner

NAME = "MADAGASCAR"


class Madagascar(Planner):
    name = NAME

    def __init__(self):
        self.name = f"{NAME}"
        super().__init__()

    @staticmethod
    def parseOutput(r: Result, stdout: str):
        r.solved = len(re.findall(r"PLAN FOUND:.*?", stdout)) > 0
        r.time = Result.parseTime(stdout)
        reBound = re.findall(r"PLAN FOUND: (\d*?) steps", stdout, re.MULTILINE)
        r.bound = -1 if not reBound else reBound[0]
        r.plan = re.findall(r"\d*? : \((.*?)\)$", stdout, re.MULTILINE)
        r.planLength = len(r.plan)
        reNOfVars = re.findall(r"Horizon 1: (.*?) variables$", stdout, re.MULTILINE)
        r.nOfVars = -1 if not reNOfVars else int(reNOfVars[0])

        return r

    def getCommand(self, domain: str, problem: str):
        return ["madagascar", domain, problem, "-A", "1", "-S", "1", "-Q"]
