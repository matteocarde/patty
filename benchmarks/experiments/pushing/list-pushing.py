import random
import os
from natsort import natsort

# PLANNERS = ["PATTY", "PATTY-R-YICES", "PATTY-R-Z3-NL", "PATTY-NL", "PATTY-Z3", "SPRINGROLL"]
PLANNERS = [
    # "PATTY",
    "PATTY-G",
    "PATTY-H",
    "PATTY-F",
    # "PATTY-ASTAR",
    # "SPRINGROLL",
    # "ENHSP-HADD",
    # "ENHSP-HRADD",
    # "ENHSP-HMRP",
    # "METRIC-FF",
    # "NFD",
    # "OMT"
]
NAME = "pushing.csv"


def main():
    domains = [
        "numeric/ipc-2023/block-grouping",
        "numeric/ipc-2023/counters",
        "numeric/ipc-2023/delivery",
        "numeric/ipc-2023/drone",
        "numeric/ipc-2023/expedition",
        "numeric/ipc-2023/ext-plant-watering",
        "numeric/ipc-2023/farmland",
        "numeric/ipc-2023/fo-farmland",
        "numeric/ipc-2023/fo-sailing",
        "numeric/ipc-2023/fo_counters",
        "numeric/ipc-2023/hydropower",
        "numeric/ipc-2023/mprime",
        "numeric/ipc-2023/pathwaysmetric",
        "numeric/ipc-2023/rover",
        "numeric/ipc-2023/sailing",
        "numeric/ipc-2023/satellite",
        "numeric/ipc-2023/sugar",
        "numeric/ipc-2023/tpp",
        "numeric/ipc-2023/zenotravel",
    ]

    instances = list()

    for domain in domains:
        problems = natsort.natsorted(os.listdir(f"files/{domain}/instances"))
        for problem in problems:
            if problem[-5:] != ".pddl":
                continue
            domainFile = f"files/{domain}/domain.pddl"
            problemFile = f"files/{domain}/instances/{problem}"

            for planner in PLANNERS:
                n = 1 if "PATTY-R" not in planner else 5
                for i in range(0, n):
                    instances.append([planner, domain, domainFile, problemFile])

    random.shuffle(instances)
    print(f"Listing {len(instances)} instances")
    f = open(f"benchmarks/instances/{NAME}", "w")
    f.write("\n".join([",".join(i) for i in instances]))
    f.close()


if __name__ == '__main__':
    main()
