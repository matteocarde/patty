import re

from classes.Planner import Planner
from classes.Result import Result

NAME = "Optic"


class Optic(Planner):
    name = NAME

    def __init__(self):
        self.name = f"{NAME}"
        super().__init__()

    @staticmethod
    def parseOutput(r: Result, stdout: str):
        r.solved = len(re.findall(r"Solution Found", stdout)) > 0
        r.time = Result.parseTime(stdout)
        r.plan = re.findall(r"^(\d.*?.\d.*?): \((.*?)\)  \[(.*?)\]", stdout, re.MULTILINE)
        r.planLength = len(r.plan)

        return r

    def getCommand(self, domain: str, problem: str):
        return ["optic -N", domain, problem]
