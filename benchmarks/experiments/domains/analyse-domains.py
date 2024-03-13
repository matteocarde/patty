import json
import os
import shutil
from typing import Dict, List, Tuple

from natsort import natsort

from src.pddl.Domain import Domain, GroundedDomain
from src.pddl.DomainStats import DomainStats
from src.pddl.Problem import Problem
from utilties.utilities import r

DOMAINS = [
    "numeric/ipc-2023/drone",
    "numeric/ipc-2023/block-grouping",
    "numeric/ipc-2023/counters",
    "numeric/ipc-2023/delivery",
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
    statsName = "numeric"
    stats: Dict[str, Dict[str, Dict]] = dict()

    pList: List[Tuple[str, str]] = list()

    for domainName in DOMAINS:
        problems = natsort.natsorted(os.listdir(f"files/{domainName}/instances"))
        for problemName in problems:
            if problemName[-5:] != ".pddl":
                continue
            pList.append((domainName, problemName))

    total = len(pList)
    index = 0

    for (domainName, problemName) in pList:
        stats[domainName] = stats.setdefault(domainName, dict())
        print(f"{domainName} - {problemName}: {r(index / total * 100, 2)}%")
        domainFile = f"files/{domainName}/domain.pddl"
        problemFile = f"files/{domainName}/instances/{problemName}"

        domain: Domain = Domain.fromFile(domainFile)
        problem: Problem = Problem.fromFile(problemFile)
        gDomain: GroundedDomain = domain.ground(problem)

        stats[domainName][problemName] = DomainStats.fromGroundedDomain(gDomain).toJSON()
        index += 1

    folder = f'benchmarks/stats/{statsName}'
    if os.path.exists(folder):
        shutil.rmtree(folder)
    os.mkdir(folder)
    with open(f"{folder}/{statsName}.json", "w") as f:
        json.dump(stats, f)

    print("Finished")


if __name__ == '__main__':
    main()
