import argparse


class ICRArguments:

    def __init__(self):
        parser = argparse.ArgumentParser(
            description='Patty Tools - Various tools for papers')

        parser.add_argument('-o', '--domain', dest='domain', help='The .pddl domain file', required=True)
        parser.add_argument('-f', '--problem', dest='problem', help='The .pddl problem file', required=True)
        parser.add_argument('-t', '--trace', dest='trace', help='The .txt trace file', required=True)
        parser.add_argument('-c', '--correct', dest='correct', help='The .pddl correct problem file')

        args = parser.parse_args()
        self.isHelp = "help" in args
        self.domain = args.domain
        self.problem = args.problem
        self.trace = args.trace
        self.correctProblem = args.correct
