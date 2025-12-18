import os
import random
from typing import Tuple, List

from natsort import natsort


def main():
    PLANNERS = [
        # "PATTY-ICES",
        "TAMER",
        "ANMLSMT"
    ]

    domains = [
        "temporal/cushing",
        "temporal/majsp/anml",
        "temporal/bottles-all",
        "temporal/bottles-pack",
        "temporal/bottles-pour",
        "temporal/bottles-shake",
        "temporal/match-ms",
        "temporal/oversub",
        "temporal/instradi/anml",
        "temporal/painter/anml"
    ]

    ANMLPLANNERS = {"ANMLSMT", "TAMER"}

    instances = list()

    for domainOrig in domains:
        for planner in PLANNERS:

            domain = domainOrig
            if planner in ANMLPLANNERS and "/anml" not in domain:
                domain += "/anml"

            ext = "anml" if "/anml" in domain else "pddl"

            problemList: List[Tuple[str, str]] = list()

            if os.path.exists(f"files/{domain}/domains"):
                folders = natsort.natsorted(os.listdir(f"files/{domain}/domains"))
                for folder in folders:
                    if folder in {".DS_Store"}:
                        continue
                    domainFile = f"files/{domain}/domains/{folder}/{folder}_domain.{ext}"
                    problemFile = f"files/{domain}/domains/{folder}/{folder}_problem.{ext}"
                    assert os.path.exists(domainFile), domainFile
                    assert os.path.exists(problemFile), problemFile
                    if not os.path.exists(domainFile):
                        continue
                    problemList.append((domainFile, problemFile))
            else:
                if os.path.exists(f"files/{domain}/instances"):
                    problems = natsort.natsorted(os.listdir(f"files/{domain}/instances"))
                else:
                    problems = natsort.natsorted(os.listdir(f"files/{domain}"))
                for problem in problems:
                    if problem[-4:] != ext:
                        continue
                    if ext == "pddl":
                        domainFile = f"files/{domain}/domain.pddl"
                        assert os.path.exists(domainFile), domainFile
                        problemFile = f"files/{domain}/instances/{problem}"
                    elif os.path.exists(f"files/{domain}/instances"):
                        domainFile = f"files/{domain}/domain.anml"
                        problemFile = f"files/{domain}/instances/{problem}"
                    else:
                        domainFile = ""
                        problemFile = f"files/{domain}/{problem}"
                    assert not domainFile or os.path.exists(domainFile), domainFile
                    assert os.path.exists(problemFile), problemFile
                    problemList.append((domainFile, problemFile))

            instances += [[planner, domain, domainFile, problemFile] for (domainFile, problemFile) in problemList]

    random.shuffle(instances)
    print(f"Listing {len(instances)} instances")
    f = open("benchmarks/instances/ices.csv", "w")
    f.write("\n".join([",".join(i) for i in instances]))
    f.close()


if __name__ == '__main__':
    main()
