import re

from classes.Result import Result
from classes.planners.Planner import Planner


class Tamer(Planner):

    def __init__(self):
        self.name = "TAMER"
        super().__init__()

    @staticmethod
    def parseOutput(r: Result, stdout: str):
        r.solved = len(re.findall(r";; A plan has been found:", stdout)) > 0
        r.time = Result.parseTime(stdout)
        r.plan = re.findall(r"^[.\d]*?: (.*?) \[(.*?)]", stdout, re.MULTILINE)
        r.planLength = len(r.plan)

        return r

    def getCommand(self, domain: str, problem: str):
        cmd = ["tamer", "solve", "-e", "0.001", "-s", "-k", "-w", "0.8"]
        if ".pddl" in domain:
            cmd += ["-P"]
        if domain.strip():
            cmd += [domain]
        if problem.strip():
            cmd += [problem]
        print(cmd)
        return cmd
