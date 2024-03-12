import json
import os
from typing import Dict

from natsort import natsort

from src.pddl.Domain import Domain, GroundedDomain
from src.pddl.DomainStats import DomainStats
from src.pddl.Problem import Problem

DOMAINS = [
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
    # numeric/ "ipc-2023/markettrader",
    "numeric/ipc-2023/mprime",
    "numeric/ipc-2023/pathwaysmetric",
    "numeric/ipc-2023/rover",
    "numeric/ipc-2023/sailing",
    "numeric/ipc-2023/satellite",
    # numeric/ "ipc-2023/settlers",
    "numeric/ipc-2023/sugar",
    "numeric/ipc-2023/tpp",
    "numeric/ipc-2023/zenotravel",
    "numeric/line-exchange-quantity"
]


def main():
    stats: Dict[str, Dict[str, Dict]] = dict()

    for domainName in DOMAINS:
        print(f"\t {domainName}")
        problems = natsort.natsorted(os.listdir(f"files/{domainName}/instances"))
        stats[domainName] = dict()
        for problemName in problems:
            print(f"\t\t {problemName}")
            if problemName[-5:] != ".pddl":
                continue
            domainFile = f"files/{domainName}/domain.pddl"
            problemFile = f"files/{domainName}/instances/{problemName}"

            domain: Domain = Domain.fromFile(domainFile)
            problem: Problem = Problem.fromFile(problemFile)
            gDomain: GroundedDomain = domain.ground(problem)

            stats[domainName][problemName] = DomainStats.fromGroundedDomain(gDomain).toJSON()

    with open("benchmarks/stats/numeric.json", "w") as f:
        json.dump(stats, f)


if __name__ == '__main__':
    main()
