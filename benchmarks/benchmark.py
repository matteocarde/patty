from typing import Dict

import os
import random

from classes.ENHSP import ENHSP
from classes.MetricFF import MetricFF
from classes.Patty import Patty
from classes.Planner import Planner
from classes.Result import Result
from classes.SpringRoll import SpringRoll

PLANNERS: Dict[str, Planner] = {
    "PATTY": Patty("arpg"),
    "PATTY-R": Patty("random"),
    "SPRINGROLL": SpringRoll(),
    "ENHSP": ENHSP("WAStar", "aibr"),
    "METRIC-FF": MetricFF(),
}


def main():
    f = open("benchmarks/instances.csv", "r")
    csv = f.read()
    f.close()
    instances = [[v for v in line.split(",")] for line in csv.split("\n")]

    for el in instances:

        if el[0] not in {"ENHSP"}:
            continue

        planner = PLANNERS[el[0]]
        benchmark = el[1]
        domainFile = el[2]
        problemFile = el[3]

        r: Result = planner.run(benchmark, domainFile, problemFile)

        print(r)


def createRandomList():
    domains = ["block-grouping", "farmland", "farmland_ln", "fn-counters", "fn-counters-inv", "fn-counters-rnd",
               "gardening", "plant-watering", "sailing", "sailing_ln"]

    problems = list()
    instances = list()

    for domain in domains:
        for problem in os.listdir(f"files/{domain}/instances"):
            if problem[-5:] != ".pddl":
                continue
            domainFile = f"files/{domain}/domain.pddl"
            problemFile = f"files/{domain}/instances/{problem}"
            problems.append([domain, domainFile, problemFile])

    for planner in PLANNERS.keys():
        instances += [[planner] + i for i in problems]

    random.shuffle(instances)
    print(f"Listing {len(instances)} instances")
    f = open("benchmarks/instances.csv", "w")
    f.write("\n".join([",".join(i) for i in instances]))
    f.close()


if __name__ == '__main__':
    main()
