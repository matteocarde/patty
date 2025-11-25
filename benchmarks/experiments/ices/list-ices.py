import os
import random
from typing import Tuple, List

from natsort import natsort

PLANNERS = [
    "PATTY-ICES",
]


def main():
    domains = [
        "temporal/cushing",
        "temporal/majsp",
        "temporal/bottles-all",
        "temporal/bottles-pack",
        "temporal/bottles-pour",
        "temporal/bottles-shake",
        "temporal/match-ac",
        "temporal/match-ms",
        "temporal/oversub",
        "temporal/painter"
    ]

    instances = list()

    for domain in domains:
        for planner in PLANNERS:

            problemList: List[Tuple[str, str]] = list()

            if not os.path.exists(f"files/{domain}/anml"):
                raise Exception(f"We require anml files for {domain}")
            if os.path.exists(f"files/{domain}/anml/instances"):
                for problem in natsort.natsorted(os.listdir(f"files/{domain}/anml/instances")):
                    if problem[-5:] != ".anml":
                        continue
                    problemList.append(
                        (f"files/{domain}/anml/domain.anml", f"files/{domain}/anml/instances/{problem}"))
            else:
                for problem in natsort.natsorted(os.listdir(f"files/{domain}/anml")):
                    if problem[-5:] != ".anml":
                        continue
                    problemList.append(("", f"files/{domain}/anml/{problem}"))
            instances += [[planner, domain, domainFile, problemFile] for (domainFile, problemFile) in problemList]

    random.shuffle(instances)
    print(f"Listing {len(instances)} instances")
    f = open("benchmarks/instances/ices.csv", "w")
    f.write("\n".join([",".join(i) for i in instances]))
    f.close()


if __name__ == '__main__':
    main()
