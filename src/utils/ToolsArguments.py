import argparse


class ToolsArguments:

    def __init__(self):
        parser = argparse.ArgumentParser(
            description='Patty Tools - Various tools for papers')

        parser.add_argument('-o', '--domain', dest='domain', help='The .pddl domain file')
        parser.add_argument('-f', '--problem', dest='problem', help='The .pddl problem file')
        parser.add_argument('tool', help="The tool to call")

        args = parser.parse_args()
        self.isHelp = "help" in args
        self.domain = args.domain
        self.problem = args.problem
        self.tool = args.tool
