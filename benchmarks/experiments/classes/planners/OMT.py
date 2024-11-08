import re

from classes.planners.Planner import Planner
from classes.Result import Result

NAME = "OMT"


class OMT(Planner):
    name = NAME

    def __init__(self):
        self.name = f"{NAME}"
        super().__init__()

    @staticmethod
    def parseOutput(r: Result, stdout: str):
        r.solved = len(re.findall(r"Plan found!", stdout)) > 0
        r.time = Result.parseTime(stdout)
        reBound = re.findall(r"^Found solution at bound: (\d*?)$", stdout, re.MULTILINE)
        r.bound = -1 if not reBound else reBound[0]
        r.plan = re.findall(r"Step .*?: (.*?)$", stdout, re.MULTILINE)
        r.planLength = len(r.plan)
        reNOfVars = re.findall(r"Number of vars at bound .*?: (.*?)$", stdout, re.MULTILINE)
        r.nOfVars = -1 if not reNOfVars else int(reNOfVars[-1])
        reNOfRules = re.findall(r"Number of rules at bound .*?: (.*?)$", stdout, re.MULTILINE)
        r.nOfRules = -1 if not reNOfRules else int(reNOfRules[-1])
        reLastSearchedBound = re.findall(r"Current Horizon: (\d*)", stdout, re.MULTILINE)
        r.lastSearchedBound = -1 if not reLastSearchedBound else int(reLastSearchedBound[-1])

        return r

    def getCommand(self, domain: str, problem: str):
        # omtplan -smt -parallel -domain
        return ["omtplan", "-smt", "-parallel", "-domain", domain, problem]
