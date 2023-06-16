import argparse

from src.utils.LogPrint import LogPrintLevel


class Arguments:

    def __init__(self):
        parser = argparse.ArgumentParser(
            description='Patty - The Symbolic Numeric Planner using Patterns')
        parser.add_argument('-o', '--domain', dest='domain', help='The .pddl domain file', required=True)
        parser.add_argument('-f', '--problem', dest='problem', help='The .pddl problem file', required=True)
        parser.add_argument('-n', '--horizon', help='The number of steps of the SMT encoding', default=1, type=int)
        parser.add_argument('-v', '--verboseLevel', help=f'The level of verbosity: {LogPrintLevel.getLevels()} ',
                            default=LogPrintLevel.getDefault(), type=int)

        args = parser.parse_args()
        self.domain = args.domain
        self.problem = args.problem
        self.horizon = args.horizon
        self.verboseLevel = LogPrintLevel(args.verboseLevel)
