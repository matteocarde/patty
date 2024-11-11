import re

from classes.planners.Planner import Planner

from classes.Result import Result

NAME = "ENHSP_SOCS"


class ENHSP_SOCS(Planner):
    name = NAME

    def __init__(self):
        super().__init__()

    @staticmethod
    def parseOutput(r: Result, stdout: str):
        r.solved = len(re.findall(r"Problem Solved", stdout)) > 0
        r.time = Result.parseTime(stdout)
        r.plan = re.findall(r"^.*?: (\(.*?\))$", stdout, re.MULTILINE)
        r.planLength = len(r.plan)

        return r

    def getCommand(self, domain: str, problem: str):
        cmd = ["enhsp-socs", "-o", domain, "-f", problem, "-planner", "sat-mq3h3n"]
        return cmd
