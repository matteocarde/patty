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
    # "SPRINGROLL",
    # "RANTANPLAN",
    "ENHSP-HADD",
    "ENHSP-HRADD",
    "ENHSP-HMRP",
    "ENHSP-AIBR",
    # "METRIC-FF",
    # "NFD",
    # "OMT"
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

    for t in {"ORIGINAL", "TRANSLATED"}:
        for domain in domains:
            problems = natsort.natsorted(os.listdir(f"files/{domain}/instances"))

            for problem in problems:
                if problem[-5:] != ".pddl":
                    continue

                if t == "ORIGINAL":
                    domainFile = f"files/{domain}/domain.pddl"
                    problemFile = f"files/{domain}/instances/{problem}"
                else:
                    domainFile = f"files/{domain}/pattern-instances/{problem.replace('.pddl', '-domain.pddl')}"
                    problemFile = f"files/{domain}/pattern-instances/{problem}"

                assert os.path.exists(domainFile)
                assert os.path.exists(problemFile)

                for planner in PLANNERS:
                    instances.append([f"{planner}", domain, domainFile, problemFile, t])

    random.shuffle(instances)
    print(f"Listing {len(instances)} instances")
    f = open(f"benchmarks/{NAME}", "w")
    f.write("\n".join([",".join(i) for i in instances]))
    f.close()


if __name__ == '__main__':
    main()
