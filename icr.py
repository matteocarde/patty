import traceback

from src.pddl.Domain import Domain, GroundedDomain
from src.pddl.Problem import Problem
from src.pddl.Trace import Trace
from src.retrieve.InitialConditionRetriever import InitialConditionRetriever
from src.retrieve.InitialConditionSpace import InitialConditionSpace
from src.utils.ICRArguments import ICRArguments
from src.utils.TimeStat import TimeStat


def main():
    args = ICRArguments()
    if args.isHelp:
        exit(0)

    try:

        ts: TimeStat = TimeStat()
        ts.start("Overall")
        ts.start("Grounding")
        domain: Domain = Domain.fromFile(args.domain)
        problem: Problem = Problem.fromFile(args.problem)
        gDomain: GroundedDomain = domain.ground(problem, avoidSimplification=True)
        trace: Trace = Trace.fromPatty(args.trace, gDomain)
        correctProblem: Problem = Problem.fromFile(args.correctProblem) if args.correctProblem else None
        ts.end("Grounding")

        ts.start("Initial Condition Retrieve")
        ics: InitialConditionSpace = InitialConditionSpace(trace, problem, gDomain)

        icr = InitialConditionRetriever(ics, problem.init)
        initSolution, optimum = icr.solve()

        ts.end("Initial Condition Retrieve")

        print(f"Optimum: {optimum}")

        isValid = trace.validate(initSolution, problem.goal, tolerance=0.1)
        if not isValid:
            print("Thi initial condition is NOT valid")
            return

        print("The initial condition is valid")

        dRW: float = Problem.computeDistance(problem.init, initSolution, verbose=True, nameA="Wrong", nameB="Retrieved")
        print(f"Distance Retrieved-Wrong: {dRW}")

        if correctProblem:
            dCW: float = Problem.computeDistance(initSolution, correctProblem.init, verbose=True, nameA="Retrieved",
                                                 nameB="Correct")
            print(f"Distance Retrieved-Correct: {dCW}")

        ts.end("Overall")

        print(str(ts))


    except:
        print("Something went wrong.")
        traceback.print_exc()


if __name__ == '__main__':
    main()
