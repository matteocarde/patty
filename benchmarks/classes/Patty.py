from classes.Planner import Planner
from classes.Result import Result


class Patty(Planner):

    def __init__(self, timeout: int):
        super().__init__(timeout)

    def run(self, domain: str, problem: str) -> Result:
        cmd = self.getCommand(domain, problem)
        stdout: str = super().exec(cmd)
        print(stdout)

    def getCommand(self, domain: str, problem: str):
        return ["patty", "-o", domain, "-f", problem]
