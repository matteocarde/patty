import random
import subprocess

from subprocess import Popen

from classes.Result import Result
from classes.CloudLogger import CloudLogger


class Planner:
    name: str
    settings: str

    def __init__(self):
        self.settings = ""
        pass

    def run(self, benchmark: str, domainFile: str, problemFile: str, logger: CloudLogger, timeout: int) -> Result:
        output, code, cmd = self.exec(domainFile, problemFile, timeout)
        r = Result(benchmark, problemFile)
        r.solver = self.name
        r.code = code
        r.cmd = cmd
        r.timeout = r.code == 124
        r.solved = r.code == 0
        r.stdout = output
        self.parseOutput(r, output)
        if not r.timeout and r.solved:
            return r
        if not r.timeout and not r.solved:
            print(r.stdout)
            logger.error(r.toJSON())
        else:
            r.solved = False
            r.time = timeout * 1000
        return r

    def exec(self, domain: str, problem: str, timeout: int) -> (str, int):
        cmd: [str] = self.getCommand(domain, problem)
        command = ["timeout", str(timeout)] + ["time", "-p"] + cmd
        # command = cmd
        output = " ".join(command) + "\n"
        print(output)
        with Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE) as p:
            (stdout, stderr) = p.communicate()

        output += "-------STDOUT-------\n" + stdout.decode("utf-8")
        output += "-------STDERR-------\n" + stderr.decode("utf-8")
        output += "--------CODE--------\n" + str(p.returncode)
        return output, p.returncode, " ".join(cmd)

    def getCommand(self, domain: str, problem: str) -> [str]:
        raise NotImplemented()

    def addSettings(self, settings: str):
        self.settings += " " + settings

    @staticmethod
    def parseOutput(r: Result, stdout: str):
        raise NotImplemented()
