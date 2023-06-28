from typing import Dict

import os
import random

from benchmarks.classes.ENHSP import ENHSP
from benchmarks.classes.MetricFF import MetricFF
from benchmarks.classes.Patty import Patty
from benchmarks.classes.PattyRandom import PattyRandom
from benchmarks.classes.Planner import Planner
from benchmarks.classes.SpringRoll import SpringRoll

PLANNERS: Dict[str, Planner] = {
    "PATTY": Patty(),
    "PATTY-R": PattyRandom(),
    "SPRINGROLL": SpringRoll(),
    "ENHSP": ENHSP(),
    "METRIC-FF": MetricFF(),
}


def createRandomList():
    domains = ["block-grouping", "farmland", "farmland_ln", "fn-counters", "fn-counters-inv", "fn-counters-rnd",
               "gardening", "plant-watering", "sailing", "sailing_ln", "zeno-travel"]

    problems = list()
    instances = list()

    for domain in domains:
        for problem in os.listdir(f"../files/{domain}/instances"):
            if problem[-5:] != ".pddl":
                continue
            domainFile = f"files/{domain}/domain.pddl"
            problemFile = f"files/{domain}/instances/{problem}.pddl"
            problems.append([domain, domainFile, problemFile])

    for planner in PLANNERS.keys():
        instances += [[planner] + i for i in problems]

    random.shuffle(instances)
    print(f"Listing {len(instances)} instances")
    f = open("instances.csv", "w")
    f.write("\n".join([",".join(i) for i in instances]))
    f.close()


def main():
    f = open("./instances.csv", "r")
    csv = f.read()
    f.close()
    instances = [[v for v in line.split(",")] for line in csv.split("\n")]

    for el in instances[0:9]:
        planner = PLANNERS[el[0]]
        domain = el[1]
        domainFile = el[2]
        problemFile = el[3]

    print(instances)


if __name__ == '__main__':
    main()
