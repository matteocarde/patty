import re

from classes.Result import Result
from classes.planners.Planner import Planner


class AnmlSMT(Planner):

    def __init__(self):
        self.name = "ANMLSMT"
        super().__init__()

    @staticmethod
    def parseOutput(r: Result, stdout: str):
        r.solved = len(re.findall(r";; A plan has been found:", stdout)) > 0
        r.time = Result.parseTime(stdout)
        reBound = re.findall(r"INFO: \[SMTPlanner\] h: (.*?)$", stdout, re.MULTILINE)
        r.bound = -1 if not reBound else int(reBound[-1])
        r.plan = re.findall(r"^[.\d]*?: (.*?) \[(.*?)]", stdout, re.MULTILINE)
        r.planLength = len(r.plan)

        return r

    def getCommand(self, domain: str, problem: str):
        cmd = ["anmlsmt", "solve", "-l", "3", "-a", "smt-incr", "-q", "mathsat"]
        if domain:
            cmd += [domain]
        if problem:
            cmd += [problem]
        return cmd
