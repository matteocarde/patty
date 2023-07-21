import os
import statistics

from natsort import natsort

from src.pddl.Domain import Domain
from src.pddl.Problem import Problem


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
        # "ipc-2023/markettrader",
        "ipc-2023/mprime",
        "ipc-2023/pathwaysmetric",
        "ipc-2023/rover",
        "ipc-2023/sailing",
        "ipc-2023/satellite",
        # "ipc-2023/settlers",
        "ipc-2023/sugar",
        "ipc-2023/tpp",
        "ipc-2023/zenotravel",
        "line-exchange",
        "line-exchange-quantity"
    ]

    for domain in domains:
        statDomain = list()
        problems = natsort.natsorted(os.listdir(f"files/{domain}/instances"))
        for problem in problems:
            if problem[-5:] != ".pddl":
                continue
            try:
                d = Domain.fromFile(f"files/{domain}/domain.pddl")
                p = Problem.fromFile(f"files/{domain}/instances/{problem}")
                gd = d.ground(p)
                sat = sum([len(e.getPredicates()) for a in gd.actions for e in a.effects])
                num = sum([len(e.getFunctions()) for a in gd.actions for e in a.effects])
                statDomain.append(sat / num)
                break
            except Exception:
                print("Something went wrong")
                pass
        value = statistics.mean(statDomain)
        print(domain, value, "PURELY" if value < 1 else "SCARCELY")


if __name__ == '__main__':
    main()
