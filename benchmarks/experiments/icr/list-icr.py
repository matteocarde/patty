import os
import random

from natsort import natsort

DOMAINS = {
    "counters": "numeric/ipc-2023/counters",
    "delivery": "numeric/ipc-2023/delivery",
    "drone": "numeric/ipc-2023/drone",
    "expedition": "numeric/ipc-2023/expedition",
    "watering": "numeric/ipc-2023/ext-plant-watering",
    "farmland": "numeric/ipc-2023/farmland",
    "fo-farmland": "numeric/ipc-2023/fo-farmland",
    "fo-sailing": "numeric/ipc-2023/fo-sailing",
    "fo_counters": "numeric/ipc-2023/fo_counters",
    "hydropower": "numeric/ipc-2023/hydropower",
    "mprime": "numeric/ipc-2023/mprime",
    "pathwaysmetric": "numeric/ipc-2023/pathwaysmetric",
    "rover": "numeric/ipc-2023/rover",
    "sailing": "numeric/ipc-2023/sailing",
    "satellite": "numeric/ipc-2023/satellite",
    "sugar": "numeric/ipc-2023/sugar",
    "tpp": "numeric/ipc-2023/tpp",
    "Baxter": "hybrid/Baxter",
    "Descent": "hybrid/Descent",
    "HVAC": "hybrid/HVAC",
    "Linear-Car": "hybrid/Linear-Car",
    "Linear-Car-2": "hybrid/Linear-Car-2",
    "UTC": "hybrid/UTC",
    "UTC2": "hybrid/UTC2",
}


def main():
    instances = list()

    for (name, path) in DOMAINS.items():
        if not os.path.exists(f"files/{path}/plans"):
            continue
        plans = natsort.natsorted(os.listdir(f"files/{path}/plans"))
        for plan in plans:

            if plan[-4:] != ".txt":
                continue
            domainFile = f"files/{path}/domain.pddl"
            problemFile = f"files/{path}/instances/{plan[:-9]}.pddl"
            cProblemFile = f"files/{path}/instances/{plan[:-9]}.pddl"
            traceFile = f"files/{path}/plans/{plan}"
            # CORRECT: Repair correct init condition
            # PARTIAL: Repair partial correct init condition
            # NOISE: Repair noisy initial condition
            instances.append(["TOTAL", name, domainFile, problemFile, traceFile, cProblemFile])

    random.shuffle(instances)
    print(f"Listing {len(instances)} instances")
    f = open(f"benchmarks/instances/icr.csv", "w")
    f.write("\n".join([",".join(i) for i in instances]))
    f.close()


if __name__ == '__main__':
    main()
