import traceback

from src.pddl.Domain import Domain, GroundedDomain
from src.pddl.InitialCondition import InitialCondition
from src.pddl.Problem import Problem
from src.pddl.Trace import Trace
from src.retrieve.InitialConditionRetriever import InitialConditionRetriever
from src.retrieve.InitialConditionSpace import InitialConditionSpace
from src.utils.ICRArguments import ICRArguments


def main():
    args = ICRArguments()
    if args.isHelp:
        exit(0)

    try:

        domain: Domain = Domain.fromFile(args.domain)
        problem: Problem = Problem.fromFile(args.problem)
        gDomain: GroundedDomain = domain.ground(problem, avoidSimplification=True)
        trace: Trace = Trace.fromPatty(args.trace, gDomain)

        print("Creating ICS...")
        ics: InitialConditionSpace = InitialConditionSpace(trace, problem, gDomain)

        print("Solving ICR...")
        icr = InitialConditionRetriever(ics, problem.init)
        initSolution: InitialCondition = icr.solve()

        print("Retrieved Initial Condition:")
        print(initSolution)

        isValid = trace.validate(initSolution, problem.goal, tolerance=0.1)
        if not isValid:
            print("Thi initial condition is NOT valid")
            return

        print("The initial condition is valid")


    except:
        print("Something went wrong.")
        traceback.print_exc()


if __name__ == '__main__':
    main()
