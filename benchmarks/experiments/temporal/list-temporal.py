import os
import random
from typing import Tuple, List

from natsort import natsort

PLANNERS = [
    # "TFD",
    # "LPG",
    # "ITSAT",
    # "OPTIC",
    "ANMLSMT",
    "PATTY-T-OR-ASTAR",
    # "PATTY-T-SIGMA-ASTAR"
]


def main():
    domains = [
        "temporal/cushing",
        "temporal/majsp",
        "temporal/bottles-all",
        "temporal/bottles-pack",
        "temporal/bottles-pour",
        "temporal/bottles-shake",
        "temporal/match-ac",
        "temporal/match-ms",
        "temporal/oversub",
        "temporal/painter"
    ]

    instances = list()

    for domain in domains:
        for planner in PLANNERS:

            problemList: List[Tuple[str, str]] = list()

            if planner == "ANMLSMT":
                if not os.path.exists(f"files/{domain}/anml"):
                    raise Exception("ANMLSMT requires anml files")
                if os.path.exists(f"files/{domain}/anml/instances"):
                    for problem in natsort.natsorted(os.listdir(f"files/{domain}/anml/instances")):
                        if problem[-5:] != ".anml":
                            continue
                        problemList.append(
                            (f"files/{domain}/anml/domain.anml", f"files/{domain}/anml/instances/{problem}"))
                else:
                    for problem in natsort.natsorted(os.listdir(f"files/{domain}/anml")):
                        if problem[-5:] != ".anml":
                            continue
                        problemList.append(("", f"files/{domain}/anml/{problem}"))
            else:
                if os.path.exists(f"files/{domain}/instances"):
                    problems = natsort.natsorted(os.listdir(f"files/{domain}/instances"))
                    for problem in problems:
                        if problem[-5:] != ".pddl":
                            continue
                        problemList.append((f"files/{domain}/domain.pddl", f"files/{domain}/instances/{problem}"))
                else:
                    folders = natsort.natsorted(os.listdir(f"files/{domain}/domains"))
                    for folder in folders:
                        domainFile = f"files/{domain}/domains/{folder}/domain.pddl"
                        problemFile = f"files/{domain}/domains/{folder}/problem.pddl"
                        if not os.path.exists(domainFile):
                            continue
                        problemList.append((domainFile, problemFile))
            print(f"{domain} with {planner} has {len(problemList)} problems")
            instances += [[planner, domain, domainFile, problemFile] for (domainFile, problemFile) in problemList]

    random.shuffle(instances)
    print(f"Listing {len(instances)} instances")
    f = open("benchmarks/instances/temporal.csv", "w")
    f.write("\n".join([",".join(i) for i in instances]))
    f.close()


if __name__ == '__main__':
    main()
