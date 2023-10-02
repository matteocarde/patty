import re

from classes.Planner import Planner

from classes.Result import Result

NAME = "ENHSP"


class ENHSP(Planner):
    name = NAME

    def __init__(self, p: str or bool, settings="", name=""):
        super().__init__()
        self.p = p
        self.name = name if name else f"{NAME}-{p}"
        self.settings = settings

    @staticmethod
    def parseOutput(r: Result, stdout: str):
        r.solved = len(re.findall(r"Problem Solved", stdout)) > 0
        r.time = Result.parseTime(stdout)
        r.plan = re.findall(r"^.*?: (\(.*?\))$", stdout, re.MULTILINE)
        r.planLength = len(r.plan)

        return r

    def getCommand(self, domain: str, problem: str):
        cmd = ["enhsp", "-o", domain, "-f", problem, self.settings]
        if self.p:
            cmd += ["-planner", self.p]
        return cmd
