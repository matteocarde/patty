import subprocess

from subprocess import Popen

from classes.Result import Result

TIMEOUT = 5


class Planner:
    name: str

    def __init__(self):
        pass

    def run(self, benchmark: str, domainFile: str, problemFile: str) -> Result:
        stdout, code = self.exec(domainFile, problemFile)
        r = Result(benchmark, problemFile)
        r.solver = self.name
        r.code = code
        r.timeout = r.code == 124
        r.stdout = stdout
        if not r.timeout:
            self.parseOutput(r, stdout)
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
        return output, p.returncode

    def getCommand(self, domain: str, problem: str) -> [str]:
        raise NotImplemented()

    @staticmethod
    def parseOutput(r: Result, stdout: str):
        raise NotImplemented()
