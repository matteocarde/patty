import os

from Domain import Domain, GroundedDomain
from NumericPlan import NumericPlan
from Problem import Problem
from classes.plan.PDDL2SMT import PDDL2SMT
from classes.smt.SMTSolution import SMTSolution
from classes.smt.SMTSolver import SMTSolver

domains = {
    # "block-grouping": {
    #     "folder": "block-grouping",
    #     "domain": "domain.pddl",
    #     "problems-folder": "instances/"
    # },
    # "fn-counters": {
    #     "folder": "counters/fn-counters",
    #     "domain": "domain.pddl",
    #     "problems-folder": "problems/"
    # },
    # "fn-counters-inv": {
    #     "folder": "counters/fn-counters-inv",
    #     "domain": "domain.pddl",
    #     "problems-folder": "problems/"
    # },
    # "fn-counters-rnd": {
    #     "folder": "counters/fn-counters-rnd",
    #     "domain": "domain.pddl",
    #     "problems-folder": "problems/"
    # },
    "farmland": {
        "folder": "farmland",
        "domain": "domain.pddl",
        "problems-folder": "instances/"
    },
    "plant-watering": {
        "folder": "plant-watering",
        "domain": "domain.pddl",
        "problems-folder": "instances/"
    },
    "sailing": {
        "folder": "sailing",
        "domain": "domain.pddl",
        "problems-folder": "instances/"
    }
}


def main():
    for (domainName, domainObj) in domains.items():
        folder = f"files/{domainObj['folder']}"
        domainFile = f"{folder}/{domainObj['domain']}"
        problemFolder = f"{folder}/{domainObj['problems-folder']}"
        domain: Domain
        try:
            domain: Domain = Domain.fromFile(f"files/{domainObj['folder']}/{domainObj['domain']}")
        except Exception as e:
            print("Error in parsing domain: ", e)
            continue

        for problemFile in os.listdir(problemFolder):

            print(folder, problemFile)
            problem: Problem
            gDomain: GroundedDomain
            pddl2smt: PDDL2SMT
            solution: SMTSolution
            try:
                problem: Problem = Problem.fromFile(f"{problemFolder}/{problemFile}")
            except Exception as e:
                print("Error in parsing problem:", e)
                continue

            try:
                gDomain: GroundedDomain = domain.ground(problem)
            except Exception as e:
                print("Error in grounding the domain:", e)
                continue

            try:
                pddl2smt: PDDL2SMT = PDDL2SMT(gDomain, problem, 4)
            except Exception as e:
                print("Error in computing the pddl2smt translation:", e)
                continue

            try:
                solver: SMTSolver = SMTSolver()
                solver.addAssertions(pddl2smt.rules)
                solution: SMTSolution = solver.solve()
            except Exception as e:
                print("Error in finding the solution:", e)
                continue

            try:
                plan: NumericPlan = pddl2smt.getPlanFromSolution(solution)
                plan.validate(problem)
                print(plan)
            except Exception as e:
                print("Error in validating the solution:", e)
                continue


if __name__ == '__main__':
    main()
