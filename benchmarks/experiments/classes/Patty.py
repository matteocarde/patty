import re

from classes.Planner import Planner
from classes.Result import Result

NAME = "PATTY"


class Patty(Planner):
    name = NAME

    def __init__(self, name, search="static", maximize=False, useSCCs=False, noCompression=False,
                 pattern="enhanced", quality="none", tcTime=0):
        self.search = search
        self.maximize = maximize
        self.name = name
        self.useSCCs = useSCCs
        self.noCompression = noCompression
        self.pattern = pattern
        self.quality = quality
        self.tcTime = tcTime
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

        transitiveClosureTime = re.findall(r"Ended Computing Transitive Closure: (\d*?)$", stdout, re.MULTILINE)
        print(transitiveClosureTime)
        r.transitiveClosureTime = -1 if not transitiveClosureTime else int(transitiveClosureTime[-1])

        return r

    def getCommand(self, domain: str, problem: str):
        cmd = [
            "patty",
            # "-pp",
            "-o", domain,
            "-f", problem,
            "-s", self.search,
            "--pattern", self.pattern,
            "--quality", self.quality
        ]
        if self.noCompression:
            cmd += ["--no-compression"]
        if self.maximize:
            cmd += ["--maximize"]
        if self.useSCCs:
            cmd += ["--use-sccs"]
        if self.tcTime:
            cmd += ["--max-closure-time", str(self.tcTime)]
        return cmd
