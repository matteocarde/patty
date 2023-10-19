import random
import os
from natsort import natsort

# PLANNERS = ["PATTY", "PATTY-R-YICES", "PATTY-R-Z3-NL", "PATTY-NL", "PATTY-Z3", "SPRINGROLL"]
PLANNERS = [
    "PATTY",
    # "PATTY-SCCS",
    "PATTY-STATIC",
    # "PATTY-ASTAR",
    "PATTY-ASTAR-MAX-NO-P",
    "PATTY-ASTAR-MAX",
    # "PATTY-ASTAR-MAX-SCCS",
    # "PATTY-GBFS-MAX-NO-P",
    # "PATTY-ASTAR-MAX-NO-P-SCCS",
    # # "PATTY-R",
    # "SPRINGROLL",
    # "RANTANPLAN",
    # "ENHSP-HADD",
    # "ENHSP-HRADD",
    # "ENHSP-HMRP",
    # "METRIC-FF",
    # "NFD",
    # "OMT"
]
NAME = "instances-search.csv"


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
        "line-exchange",
        "line-exchange-quantity"
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
    f = open(f"benchmarks/{NAME}", "w")
    f.write("\n".join([",".join(i) for i in instances]))
    f.close()


if __name__ == '__main__':
    main()
