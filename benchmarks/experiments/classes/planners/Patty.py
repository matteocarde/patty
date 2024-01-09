import re

from classes.planners.Planner import Planner
from classes.Result import Result

NAME = "PATTY"


class Patty(Planner):
    name = NAME

    def __init__(self, name, search="static", maximize=False, useSCCs=False, noCompression=False):
        self.search = search
        self.maximize = maximize
        self.name = name
        self.useSCCs = useSCCs
        self.noCompression = noCompression
        super().__init__()

    @staticmethod
    def parseOutput(r: Result, stdout: str):
        r.solved = len(re.findall(r"Plan is valid", stdout)) > 0
        r.time = Result.parseTime(stdout)
        reBound = re.findall(r"^Bound: (\d*?)$", stdout, re.MULTILINE)
        r.bound = -1 if not reBound else int(reBound[0])
        r.plan = re.findall(r"^\d*?: (\(.*?\))$", stdout, re.MULTILINE)
        r.planLength = len(r.plan)
        reNOfVars = re.findall(r"Bound .*? - Vars = (.*?)$", stdout, re.MULTILINE)
        r.nOfVars = -1 if not reNOfVars else int(reNOfVars[-1])
        reNOfRules = re.findall(r"Bound .*? - Rules = (.*?)$", stdout, re.MULTILINE)
        r.nOfRules = -1 if not reNOfRules else int(reNOfRules[-1])
        reLastSearchedBound = re.findall(r"Started Solving Bound (\d*?)$", stdout, re.MULTILINE)
        r.lastSearchedBound = -1 if not reLastSearchedBound else int(reLastSearchedBound[-1])

        lastCallsToSolver = re.findall(r"Calls to Solver: (\d*?)$", stdout, re.MULTILINE)
        r.lastCallsToSolver = -1 if not lastCallsToSolver else int(lastCallsToSolver[-1])

        return r

    def getCommand(self, domain: str, problem: str):
        cmd = [
            "patty",
            "-o", domain,
            "-f", problem,
            "-s", self.search
        ]
        if self.noCompression:
            cmd += ["--no-compression"]
        if self.maximize:
            cmd += ["--maximize"]
        if self.useSCCs:
            cmd += ["--use-sccs"]
        return cmd
