import os
import random

from natsort import natsort

PLANNERS = [
    "TFD",
    "LPG",
    "ITSAT",
    "Optic"
]


def main():
    domains = [
        "temporal/airport",
        "temporal/cushing",
        "temporal/driverlog",
        "temporal/floortile",
        "temporal/machine_shop",
        "temporal/majsp",
        "temporal/map_analyser",
        "temporal/match-ac",
        "temporal/match-ms",
        "temporal/match_cellar",
        "temporal/oversub",
        "temporal/painter",
        "temporal/paper-example",
        "temporal/parking",
        "temporal/quantum_circuit",
        "temporal/road_traffic_accident",
        "temporal/satellite",
        "temporal/sokoban",
        "temporal/storage",
        "temporal/trucks",
        "temporal/turn_and_open",
    ]

    instances = list()

    for domain in domains:
        if os.path.exists(f"files/{domain}/instances"):
            problems = natsort.natsorted(os.listdir(f"files/{domain}/instances"))
            for problem in problems:
                if problem[-5:] != ".pddl":
                    continue
                domainFile = f"files/{domain}/domain.pddl"
                problemFile = f"files/{domain}/instances/{problem}"

                for planner in PLANNERS:
                    instances.append([planner, domain, domainFile, problemFile])
        else:
            folders = natsort.natsorted(os.listdir(f"files/{domain}/"))
            for folder in folders:
                domainFile = f"files/{domain}/{folder}/domain.pddl"
                problemFile = f"files/{domain}/{folder}/problem.pddl"

                for planner in PLANNERS:
                    instances.append([planner, domain, domainFile, problemFile])

    random.shuffle(instances)
    print(f"Listing {len(instances)} instances")
    f = open("benchmarks/instances/temporal.csv", "w")
    f.write("\n".join([",".join(i) for i in instances]))
    f.close()


if __name__ == '__main__':
    main()
