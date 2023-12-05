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
    "rover": "numeric/ipc-2023/rover",
    "sailing": "numeric/ipc-2023/sailing",
    "sugar": "numeric/ipc-2023/sugar",
    "zenotravel": "numeric/ipc-2023/zenotravel",
    "Baxter": "hybrid/Baxter",
    "Descent": "hybrid/Descent",
    "HVAC": "hybrid/HVAC",
    "Linear-Car": "hybrid/Linear-Car",
    "Linear-Car-2": "hybrid/Linear-Car-2",
    "Solar-Rover": "hybrid/Solar-Rover",
    "UTC": "hybrid/UTC",
}

KINDS = [("partial", "PARTIAL"), ("noise", "NOISE")]

active = {
    # "TOTAL", 
    # "PARTIAL",
    "NOISE"
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
            probName = plan[:-9]
            domainFile = f"files/{path}/domain.pddl"
            problemFile = f"files/{path}/instances/{probName}.pddl"
            cProblemFile = f"files/{path}/instances/{probName}.pddl"
            traceFile = f"files/{path}/plans/{plan}"
            # CORRECT: Repair correct init condition
            # PARTIAL: Repair partial correct init condition
            # NOISE: Repair noisy initial condition
            if "TOTAL" in active:
                instances.append(["TOTAL", name, domainFile, problemFile, traceFile, cProblemFile])

            for (folder, kind) in KINDS:
                if os.path.exists(f"files/{path}/{folder}") and os.path.exists(f"files/{path}/{folder}/{probName}"):
                    kindList = natsort.natsorted(os.listdir(f"files/{path}/{folder}/{probName}"))
                    for p in kindList:
                        partialFile = f"files/{path}/{folder}/{probName}/{p}"
                        if kind in active:
                            instances.append([kind, name, domainFile, partialFile, traceFile, cProblemFile])

    random.shuffle(instances)
    print(f"Listing {len(instances)} instances")
    f = open(f"benchmarks/instances/icr.csv", "w")
    f.write("\n".join([",".join(i) for i in instances]))
    f.close()


if __name__ == '__main__':
    main()
