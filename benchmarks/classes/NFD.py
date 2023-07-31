import re

from classes.Planner import Planner
from classes.Result import Result

NAME = "NFD"


class NFD(Planner):
    name = NAME

    def __init__(self):
        self.name = f"{NAME}"
        super().__init__()

    @staticmethod
    def parseOutput(r: Result, stdout: str):
        r.solved = len(re.findall(r"Solution found!", stdout)) > 0
        r.time = Result.parseTime(stdout)
        r.plan = re.findall(r"(.*?) \(\d*?\)", stdout, re.MULTILINE)
        r.planLength = len(r.plan)

        return r

    def getCommand(self, domain: str, problem: str):
        return ["nfd", domain, problem, "--search",
                "lazy_greedy([lmcutnumeric(use_second_order_simple=true,bound_iterations=10,ceiling_less_than_one=true)])"]
