import os
import random
import shutil

from natsort import natsort

from src.pattern.PatternTranslator import PatternTranslator
from src.pddl.Domain import Domain
from src.pddl.PDDLWriter import PDDLWriter
from src.pddl.Problem import Problem

# PLANNERS = ["PATTY", "PATTY-R-YICES", "PATTY-R-Z3-NL", "PATTY-NL", "PATTY-Z3", "SPRINGROLL"]
PLANNERS = [
    # "PATTY",
    # "PATTY-MAX",
    # "PATTY-STATIC",
    # "PATTY-STATIC-MAX",
    # "PATTY-ASTAR",
    "SPRINGROLL",
    # "RANTANPLAN",
    "ENHSP-HADD",
    "ENHSP-HRADD",
    "ENHSP-HMRP",
    "ENHSP-AIBR",
    "METRIC-FF",
    "NFD",
    "OMT"
]
NAME = "instances-translate.csv"


def main():
    domains = [
        "ipc-2023/block-grouping",
        "ipc-2023/counters",
        "ipc-2023/delivery",
        "ipc-2023/drone",
        "ipc-2023/expedition",
        "ipc-2023/ext-plant-watering",
        "ipc-2023/farmland",
        "ipc-2023/fo-farmland",
        "ipc-2023/fo-sailing",
        "ipc-2023/fo_counters",
        "ipc-2023/hydropower",
        "ipc-2023/mprime",
        "ipc-2023/pathwaysmetric",
        "ipc-2023/rover",
        "ipc-2023/sailing",
        "ipc-2023/satellite",
        "ipc-2023/sugar",
        "ipc-2023/tpp",
        "ipc-2023/zenotravel",
        # "line-exchange",
        # "line-exchange-quantity"
    ]

    instances = list()

    for domain in domains:
        problems = natsort.natsorted(os.listdir(f"files/{domain}/instances"))
        folder = f"files/{domain}/pattern-instances/"
        if os.path.exists(folder):
            shutil.rmtree(folder)
        os.mkdir(folder)

        for problem in problems:
            if problem[-5:] != ".pddl":
                continue
            domainFile = f"files/{domain}/domain.pddl"
            problemFile = f"files/{domain}/instances/{problem}"

            print(f"Translating {domain} {problem}")
            domainObj = Domain.fromFile(domainFile)
            problemObj = Problem.fromFile(problemFile)

            tProblemFile = problemFile.replace("/instances/", "/pattern-instances/")
            tDomainFile = tProblemFile.replace(".pddl", "-domain.pddl")

            pt = PatternTranslator(domainObj, problemObj)
            tDomain = pt.getTranslatedDomain()
            tProblem = pt.getTranslatedProblem()

            with open(tDomainFile, "w") as f:
                f.write(tDomain.toPDDL(PDDLWriter()).toString())
            with open(tProblemFile, "w") as f:
                f.write(tProblem.toPDDL(PDDLWriter()).toString())

            for planner in PLANNERS:
                instances.append([f"{planner}-ORIGINAL", domain, domainFile, problemFile])
                instances.append([f"{planner}-TRANSLATED", domain, tDomainFile, tProblemFile])

    random.shuffle(instances)
    print(f"Listing {len(instances)} instances")
    f = open(f"benchmarks/{NAME}", "w")
    f.write("\n".join([",".join(i) for i in instances]))
    f.close()


if __name__ == '__main__':
    main()
