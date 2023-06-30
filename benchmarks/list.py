import random
import os
from natsort import natsort

PLANNERS = ["PATTY", "PATTY-R", "SPRINGROLL", "ENHSP", "METRIC-FF"]


def main():
    domains = ["block-grouping", "farmland", "farmland_ln", "fn-counters", "fn-counters-inv", "fn-counters-rnd",
               "gardening", "plant-watering", "sailing", "sailing_ln"]

    instances = list()

    for domain in domains:
        problems = natsort.natsorted(os.listdir(f"files/{domain}/instances"))
        for problem in problems:
            if problem[-5:] != ".pddl":
                continue
            domainFile = f"files/{domain}/domain.pddl"
            problemFile = f"files/{domain}/instances/{problem}"

            for planner in PLANNERS:
                instances.append([planner, domain, domainFile, problemFile])

    random.shuffle(instances)
    print(f"Listing {len(instances)} instances")
    f = open("benchmarks/instances.csv", "w")
    f.write("\n".join([",".join(i) for i in instances]))
    f.close()


if __name__ == '__main__':
    main()
