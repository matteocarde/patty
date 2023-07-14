import subprocess

from subprocess import Popen

from classes.CloudLogger import CloudLogger
from classes.Result import Result

TIMEOUT = 30


class Planner:
    name: str

    def __init__(self):
        pass

    def run(self, benchmark: str, domainFile: str, problemFile: str, logger: CloudLogger) -> Result:
        stdout, code, cmd = self.exec(domainFile, problemFile)
        r = Result(benchmark, problemFile)
        r.solver = self.name
        r.code = code
        r.cmd = cmd
        r.timeout = r.code == 124
        r.solved = r.code == 0
        r.stdout = stdout
        if not r.timeout and r.solved:
            self.parseOutput(r, stdout)
            return r
        if not r.timeout and not r.solved:
            print(r.stdout)
            logger.error(r.toJSON())
        else:
            r.solved = False
            r.time = TIMEOUT * 1000
        return r

    def exec(self, domain: str, problem: str) -> (str, int):
        cmd: [str] = self.getCommand(domain, problem)
        output = ""
        command = ["timeout", str(TIMEOUT)] + ["time", "-p"] + cmd
        print(" ".join(command))
        with Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT) as p:
            for line in iter(p.stdout.readline, b''):
                output += line.decode('utf-8').rstrip() + "\n"
        return output, p.returncode, " ".join(cmd)

    def getCommand(self, domain: str, problem: str) -> [str]:
        raise NotImplemented()

    @staticmethod
    def parseOutput(r: Result, stdout: str):
        raise NotImplemented()
