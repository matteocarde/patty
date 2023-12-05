import re
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

    def run(self, expType: str, domain: str, domainFile: str,
            problemFile: str, traceFile: str, cProblemFile: str,
            timeout: int, logger: CloudLogger) -> ICRResult:
        stdout, code, cmd = self.exec(domainFile, problemFile, traceFile, cProblemFile, timeout)
        r = ICRResult(expType, domain, problemFile)
        r.code = code
        r.cmd = cmd
        r.timeout = r.code == 124
        r.solved = r.code == 0
        r.stdout = stdout
        self.parseOutput(r, stdout)
        if not r.timeout and r.solved:
            return r
        if not r.timeout and not r.solved:
            print(r.stdout)
            logger.error(r.toJSON())
        else:
            r.solved = False
            r.time = timeout * 1000

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
        r.solved = len(re.findall(r"The initial condition is valid", stdout)) > 0
        r.time = ICRResult.parseTime(stdout)
        reOptimum = re.findall(r"Optimum: (.*?)$", stdout, re.MULTILINE)
        r.optimum = -1 if not reOptimum else float(reOptimum[0])
        reDRW = re.findall(r"Distance Retrieved-Wrong: (.*?)$", stdout, re.MULTILINE)
        r.dRW = -1 if not reDRW else float(reDRW[0])
        reDRC = re.findall(r"Distance Retrieved-Correct: (.*?)$", stdout, re.MULTILINE)
        r.dRC = -1 if not reDRC else float(reDRC[0])
        reNOfAtoms = re.findall(r"Atoms: (.*?)$", stdout, re.MULTILINE)
        r.nOfAtoms = -1 if not reNOfAtoms else float(reNOfAtoms[0])
        reTraceLength = re.findall(r"Trace Length: (.*?)$", stdout, re.MULTILINE)
        r.traceLength = -1 if not reTraceLength else float(reTraceLength[0])
        reConditions = re.findall(r"ICS Conditions: (.*?)$", stdout, re.MULTILINE)
        r.nOfConditions = -1 if not reConditions else float(reConditions[0])

        return r
