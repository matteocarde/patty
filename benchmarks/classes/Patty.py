import re

from classes.Planner import Planner
from classes.Result import Result

NAME = "PATTY"


class Patty(Planner):
    name = NAME

    def __init__(self, name, pattern, solver, encoding, rollBound=0, hasEffectAxioms=False, concatPatterns=False,
                 search="static", avoidP=False, useSCCs=False):
        self.pattern = pattern
        self.solver = solver
        self.encoding = encoding
        self.rollBound = rollBound
        self.hasEffectAxioms = hasEffectAxioms
        self.concatPatterns = concatPatterns
        self.search = search
        self.avoidP = avoidP
        self.useSCCs = useSCCs
        self.name = name
        super().__init__()

    @staticmethod
    def parseOutput(r: Result, stdout: str):
        r.solved = len(re.findall(r"Plan is valid", stdout)) > 0
        r.time = Result.parseTime(stdout)
        reBound = re.findall(r"^Bound: (\d*?)$", stdout, re.MULTILINE)
        r.bound = -1 if not reBound else int(reBound[0])
        r.plan = re.findall(r"^\d*?: (\(.*?\))$", stdout, re.MULTILINE)
        r.planLength = len(r.plan)
        reNOfVars = re.findall(r"Bound 1 - Vars = (.*?)$", stdout, re.MULTILINE)
        r.nOfVars = -1 if not reNOfVars else int(reNOfVars[0])
        reNOfRules = re.findall(r"Bound 1 - Rules = (.*?)$", stdout, re.MULTILINE)
        r.nOfRules = -1 if not reNOfRules else int(reNOfRules[0])
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
            "-s", self.search,
            # "-pp",
            "--pattern", self.pattern,
            "--solver", self.solver,
            "--encoding", self.encoding,
            "--roll-bound", str(self.rollBound)
        ]
        if self.hasEffectAxioms:
            cmd += ["--effect-axioms"]
        if self.avoidP:
            cmd += ["--avoid-p"]
        if self.useSCCs:
            cmd += ["--use-sccs"]
        if self.concatPatterns:
            cmd += ["--concat"]
        return cmd
