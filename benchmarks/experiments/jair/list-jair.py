import os
import random

from natsort import natsort

from benchmarks.tables.jair.domains import JAIR_DOMAINS

PLANNERS = [
    "PATTY-S",
    "PATTY-D",
    "PATTY-DR",
    "PATTY-DI", "PATTY-DP",
    "PATTY-DIR", "PATTY-DPR",
    "PATTY-DB",
    "PATTY-DBR",
    "PATTY-DBI", "PATTY-DBP",
    "PATTY-DBIR", "PATTY-DBPR",
    "PATTY-DG",
    "PATTY-DGI", "PATTY-DGP",
]
RANDOM = 5
NAME = "jair.csv"


def main():
    domains = JAIR_DOMAINS.keys()

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
