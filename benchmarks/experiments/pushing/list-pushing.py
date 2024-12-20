import random
import os
from natsort import natsort

from benchmarks.tables.pushing.domains_table2 import PUSHING_DOMAINS_TABLE2

PLANNERS = [
    "PATTY-EO",
    "PATTY-EG",
    "PATTY-EH",
    "PATTY-EF"
]
NAME = "pushing.csv"


def main():
    domains = PUSHING_DOMAINS_TABLE2.keys()

    instances = list()

    for domain in domains:
        problems = natsort.natsorted(os.listdir(f"files/{domain}/instances"))
        for problem in problems:
            if problem[-5:] != ".pddl":
                continue
            domainFile = f"files/{domain}/domain.pddl"
            problemFile = f"files/{domain}/instances/{problem}"

            for planner in PLANNERS:
                n = 1 if "JSHDKJSHDK" not in planner else 5
                for i in range(0, n):
                    instances.append([planner, domain, domainFile, problemFile])

    random.shuffle(instances)
    print(f"Listing {len(instances)} instances")
    f = open(f"benchmarks/instances/{NAME}", "w")
    f.write("\n".join([",".join(i) for i in instances]))
    f.close()


if __name__ == '__main__':
    main()
