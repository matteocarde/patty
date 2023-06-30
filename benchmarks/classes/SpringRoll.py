import re

from classes.Planner import Planner
from classes.Result import Result

NAME = "SpringRoll"


class SpringRoll(Planner):
    name = NAME

    def __init__(self):
        self.name = f"{NAME}"
        super().__init__()

    @staticmethod
    def parseOutput(r: Result, stdout: str):
        r.solved = len(re.findall(r"Solved: True", stdout)) > 0
        r.time = Result.parseTime(stdout)
        reBound = re.findall(r"^Plan Steps: (\d*?)$", stdout, re.MULTILINE)
        r.bound = -1 if not reBound else reBound[0]
        r.plan = re.findall(r"Action Name:(.*?)$", stdout, re.MULTILINE)
        r.planLength = len(r.plan)

        return r

    def getCommand(self, domain: str, problem: str):
        return ["springroll", "-o", domain, "-f", problem, "-s", "3"]
