import random
import os
from natsort import natsort

# PLANNERS = ["PATTY", "PATTY-R-YICES", "PATTY-R-Z3-NL", "PATTY-NL", "PATTY-Z3", "SPRINGROLL"]
PLANNERS = [
    "PATTY-CES",
    "SPRINGROLL",
    "ENHSP-SAT-HADD",
    "ENHSP-SAT-HMAX",
    "ENHSP-SAT-HMRP"
]
NAME = "ces.csv"


def main():
    domains = [
        "ces/counters"
    ]

    instances = list()

    for domain in domains:
        folders = natsort.natsorted(os.listdir(f"files/{domain}/domains/"))
        for folder in folders:
            problems = natsort.natsorted(os.listdir(f"files/{domain}/domains/{folder}/instances"))
            for problem in problems:
                if problem[-5:] != ".pddl":
                    continue
                domainFile = f"files/{domain}/domains/{folder}/domain-{folder}.pddl"
                problemFile = f"files/{domain}/domains/{folder}/instances/{problem}"

                for planner in PLANNERS:
                    instances.append([planner, domain, domainFile, problemFile])

    random.shuffle(instances)
    print(f"Listing {len(instances)} instances")
    f = open(f"benchmarks/instances/{NAME}", "w")
    f.write("\n".join([",".join(i) for i in instances]))
    f.close()


if __name__ == '__main__':
    main()
