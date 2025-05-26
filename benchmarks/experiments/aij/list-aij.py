import random
import os
from natsort import natsort

from benchmarks.tables.aij.domains import AIJ_DOMAINS
from benchmarks.tables.aij.domains_left import AIJ_DOMAINS_LEFT

# PLANNERS = ["PATTY", "PATTY-R-YICES", "PATTY-R-Z3-NL", "PATTY-NL", "PATTY-Z3", "SPRINGROLL"]
PLANNERS = [
    # "PATTY-R",
    # "PATTY-A",
    # "PATTY-G",
    # "PATTY-H",
    # "PATTY-F",
    # "PATTY-E",
    # "PATTY-M",
    # "PATTY-L",
    # "SPRINGROLL",
    # "ENHSP-SOCS",
    # "ENHSP-SAT-HADD",
    # "ENHSP-SAT-AIBR",
    # "ENHSP-SAT-HMRP",
    # "METRIC-FF",
    # "NFD",
    # "OMT",
    # "RANTANPLAN",
    "R2E+ROLL"
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

    random.shuffle(instances)
    print(f"Listing {len(instances)} instances")
    f = open(f"benchmarks/instances/{NAME}", "w")
    f.write("\n".join([",".join(i) for i in instances]))
    f.close()


if __name__ == '__main__':
    main()
