from src.pddl.Domain import GroundedDomain
from src.pddl.Problem import Problem
from src.plan.NumericEncoding import NumericEncoding
from src.plan.Pattern import Pattern
from src.smt.SMTSolution import SMTSolution
from src.utils.Arguments import Arguments
from src.utils.LogPrint import LogPrint, LogPrintLevel
from src.utils.TimeStat import TimeStat


class Search:
    finalPattern: Pattern or None
    finalSolution: SMTSolution or None
    finalBound: int or None

    def __init__(self, domain: GroundedDomain, problem: Problem, args: Arguments):
        self.domain = domain
        self.problem = problem

        self.args = args
        self.isTemporal = len(domain.durativeActions) > 0

        self.startBound = 1
        self.maxBound = args.bound if args.bound else 1000

        self.console: LogPrint = LogPrint(self.args.verboseLevel)
        self.ts: TimeStat = TimeStat()

        self.finalPattern = None
        self.finalSolution = None
        self.finalBound = None

        pass

    def solve(self):
        raise NotImplementedError

    def saveSMT(self, bound: int, pddl2smt: NumericEncoding, callsToSolver=0):
        filename = f"{self.args.saveSMT}-{bound}-{callsToSolver}.smt"
        self.console.log(f"Saving to {filename}", LogPrintLevel.STATS)
        pddl2smt.writeSMTLIB(filename)
        # with open(f"{self.args.saveSMT}-{bound}.smt", "w") as f:
        #     f.write(str(pddl2smt))
