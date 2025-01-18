import random
import os
from natsort import natsort

# PLANNERS = ["PATTY", "PATTY-R-YICES", "PATTY-R-Z3-NL", "PATTY-NL", "PATTY-Z3", "SPRINGROLL"]
PLANNERS = [
    # ("PATTY-CES", True),
    # ("PATTY-CES-NO-TC", True),
    # ("PATTY-CES-NO-C", True),
    ("ENHSP-SAT-HADD", False),
    ("ENHSP-SAT-HMAX", False),
    ("ENHSP-SAT-HRADD", False)
]
NAME = "ces.csv"

if __name__ == '__main__':
    domains = [
        # "ces/counter",
        # "ces/meeting"
        "ces/tapes",
    ]

    instances = list()

    for domain in domains:
        files = []
        dFolder = f"files/{domain}"
        if os.path.exists(f"{dFolder}/instances"):
            problems = natsort.natsorted(os.listdir(f"{dFolder}/instances"))
            for problem in problems:
                if problem[-5:] != ".pddl":
                    continue
                files.append((f"{dFolder}/domain.pddl", f"{dFolder}/instances/{problem}"))

        for planner, allowsConstraints in PLANNERS:
            subD = "domains" if allowsConstraints else "domains-no-constraints"
            if os.path.exists(f"{dFolder}/{subD}"):
                subDomains = natsort.natsorted(os.listdir(f"{dFolder}/{subD}"))
                for subDomain in subDomains:
                    subDFolder = f"{dFolder}/{subD}/{subDomain}"
                    domainFile = f"{subDFolder}/domain-{subDomain}.pddl"
                    problemFile = f"{subDFolder}/problem-{subDomain}.pddl"
                    instances.append([planner, domain, domainFile, problemFile])

    random.shuffle(instances)
    print(f"Listing {len(instances)} instances")
    f = open(f"benchmarks/instances/{NAME}", "w")
    f.write("\n".join([",".join(i) for i in instances]))
    f.close()
