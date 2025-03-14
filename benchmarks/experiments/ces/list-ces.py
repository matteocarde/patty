import random
import os
from natsort import natsort

# PLANNERS = ["PATTY", "PATTY-R-YICES", "PATTY-R-Z3-NL", "PATTY-NL", "PATTY-Z3", "SPRINGROLL"]
PLANNERS = [
    "PATTY-CES",
    "PATTY-CES-NO-TC",
    "PATTY-CES-NO-C"
]
NAME = "ces.csv"


def main():
    domains = [
        "ces/counter",
        # "ces/grid",
        # "ces/tapes",
        "ces/meeting",
        "ces/meeting-no-pacman"
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

        if os.path.exists(f"{dFolder}/domains"):
            subDomains = natsort.natsorted(os.listdir(f"{dFolder}/domains"))
            for subDomain in subDomains:
                subDFolder = f"{dFolder}/domains/{subDomain}"
                files.append((f"{subDFolder}/domain-{subDomain}.pddl", f"{subDFolder}/problem-{subDomain}.pddl"))

        for planner in PLANNERS:
            for (domainFile, problemFile) in files:
                instances.append([planner, domain, domainFile, problemFile])

    random.shuffle(instances)
    print(f"Listing {len(instances)} instances")
    f = open(f"benchmarks/instances/{NAME}", "w")
    f.write("\n".join([",".join(i) for i in instances]))
    f.close()


if __name__ == '__main__':
    main()
