import random
import os
from natsort import natsort

from benchmarks.tables.aij.domains import AIJ_DOMAINS

# PLANNERS = ["PATTY", "PATTY-R-YICES", "PATTY-R-Z3-NL", "PATTY-NL", "PATTY-Z3", "SPRINGROLL"]
PLANNERS = [
    "PATTY-R",
    # "PATTY-A",
    # "PATTY-E",
    # "PATTY-M",
    # "PATTY-I",
    # "PATTY-L",
    # "SPRINGROLL",
    # "ENHSP-SAT-HADD",
    # "ENHSP-SAT-AIBR",
    # "ENHSP-SAT-HMRP",
    # "METRIC-FF",
    # "NFD",
    # "OMT",
    # "RANTANPLAN"
]
RANDOM = 5
NAME = "aij.csv"


def main():
    domains = AIJ_DOMAINS.keys()

    instances = list()

    for domain in domains:
        problems = natsort.natsorted(os.listdir(f"files/{domain}/instances"))
        domainFile = f"files/{domain}/domain.pddl"
        problemFiles = set()
        for problem in problems:
            if problem[-5:] != ".pddl":
                continue
            problemFile = f"files/{domain}/instances/{problem}"
            problemFiles.add(problem)

            for planner in PLANNERS:
                n = 1 if "PATTY-R" not in planner else RANDOM
                for i in range(0, n):
                    instances.append([planner, domain, domainFile, problemFile])
        assert len(problemFiles) == 20
        print(domain, problemFiles)

    random.shuffle(instances)
    print(f"Listing {len(instances)} instances")
    f = open(f"benchmarks/instances/{NAME}", "w")
    f.write("\n".join([",".join(i) for i in instances]))
    f.close()

    print(AIJ_DOMAINS)


if __name__ == '__main__':
    main()
