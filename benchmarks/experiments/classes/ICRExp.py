import subprocess
from subprocess import Popen

from classes.CloudLogger import CloudLogger
from classes.ICRResult import ICRResult
from classes.Result import Result


class ICRExp:
    name: str
    settings: str

    def __init__(self):
        self.settings = ""
        pass

    def run(self, expType: str, domain: str, domainFile: str, problemFile: str, traceFile: str, cProblemFile: str,
            timeout: int) -> ICRResult:
        stdout, code, cmd = self.exec(domainFile, problemFile, traceFile, cProblemFile, timeout)
        r = ICRResult(expType, domain, problemFile)
        r.code = code
        r.cmd = cmd
        r.timeout = r.code == 124
        r.solved = r.code == 0
        r.stdout = stdout
        self.parseOutput(r, stdout)

        return r

    @staticmethod
    def getCommand(domain: str, problem: str, trace: str, cProblem: str):
        cmd = ["icr", "-o", domain, "-f", problem, "-t", trace, "-c", cProblem]
        return cmd

    def exec(self, domain: str, problem: str, traceFile: str, cProblemFile: str, timeout: int) -> (str, int):
        cmd: [str] = self.getCommand(domain, problem, traceFile, cProblemFile)
        output = ""
        command = ["timeout", str(timeout)] + ["time", "-p"] + cmd
        print(" ".join(command))
        with Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT) as p:
            for line in iter(p.stdout.readline, b''):
                output += line.decode('utf-8').rstrip() + "\n"
        return output, p.returncode, " ".join(cmd)

    @staticmethod
    def parseOutput(r: ICRResult, stdout: str):
        pass
