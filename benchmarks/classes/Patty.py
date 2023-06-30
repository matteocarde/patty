import re

from classes.Planner import Planner
from classes.Result import Result

NAME = "PATTY"


class Patty(Planner):
    name = NAME

    def __init__(self, pattern, solver, encoding):
        self.pattern = pattern
        self.solver = solver
        self.encoding = encoding
        self.name = NAME + "-" + pattern
        super().__init__()

    @staticmethod
    def parseOutput(r: Result, stdout: str):
        r.solved = len(re.findall(r"Plan is valid", stdout)) > 0
        r.time = Result.parseTime(stdout)
        reBound = re.findall(r"^Bound: (\d*?)$", stdout, re.MULTILINE)
        r.bound = -1 if not reBound else int(reBound[0])
        r.plan = re.findall(r"^\d*?: (\(.*?\))$", stdout, re.MULTILINE)
        r.planLength = len(r.plan)

        return r

    def getCommand(self, domain: str, problem: str):
        return ["patty", "-o", domain, "-f", problem, "-pp", "--pattern", self.pattern, "--solver", self.solver,
                "--encoding", self.encoding]
