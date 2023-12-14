import traceback

from src.pddl.Domain import Domain
from src.pddl.Problem import Problem
from src.utils.ToolsArguments import ToolsArguments


def main():
    args = ToolsArguments()
    if args.isHelp:
        exit(0)

    try:

        if args.tool == "delta":

            domain: Domain = Domain.fromFile(args.domain)
            problem: Problem = Problem.fromFile(args.problem)

            print("Everything ok")

        else:
            raise Exception(f"The tool '{args.tool}' has not been implemented yet.")

    except:
        print("Something went wrong.")
        traceback.print_exc()


if __name__ == '__main__':
    main()
