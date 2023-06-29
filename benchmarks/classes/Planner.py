import subprocess

from subprocess import Popen

from classes.Result import Result


class Planner:
    name: str

    def __init__(self, timeout: int):
        self.timeout = timeout
        pass

    def run(self, domain: str, problem: str) -> Result:
        raise NotImplemented()

    def exec(self, command: [str]) -> str:
        output = ""
        # command = ["timeout", str(self.timeout)] + command
        print(" ".join(command))
        with Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT) as p:
            for line in iter(p.stdout.readline, b''):
                output += str(line.rstrip())
        return output

    def getCommand(self, domain: str, problem: str) -> str:
        raise NotImplemented()
