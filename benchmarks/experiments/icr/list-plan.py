import os
import random

from natsort import natsort

DOMAINS = {
    "counters": ("numeric/ipc-2023/counters", "PATTY"),
    "delivery": ("numeric/ipc-2023/delivery", "ENHSP-SAT-HMRP"),
    "drone": ("numeric/ipc-2023/drone", "ENHSP-SAT-HMRP"),
    "expedition": ("numeric/ipc-2023/expedition", "ENHSP-SAT-HADD"),
    "watering": ("numeric/ipc-2023/ext-plant-watering", "ENHSP-SAT-HMRP"),
    "farmland": ("numeric/ipc-2023/farmland", "PATTY"),
    "fo-farmland": ("numeric/ipc-2023/fo-farmland", "PATTY"),
    "fo-sailing": ("numeric/ipc-2023/fo-sailing", "PATTY"),
    "fo_counters": ("numeric/ipc-2023/fo_counters", "PATTY"),
    "hydropower": ("numeric/ipc-2023/hydropower", "PATTY"),
    "mprime": ("numeric/ipc-2023/mprime", "PATTY"),
    "pathwaysmetric": ("numeric/ipc-2023/pathwaysmetric", "ENHSP-SAT-HMRP"),
    "rover": ("numeric/ipc-2023/rover", "PATTY"),
    "sailing": ("numeric/ipc-2023/sailing", "PATTY"),
    "satellite": ("numeric/ipc-2023/satellite", "ENHSP-SAT-HMRP"),
    "sugar": ("numeric/ipc-2023/sugar", "PATTY"),
    "tpp": ("numeric/ipc-2023/tpp", "ENHSP-SAT-HMRP"),
    "zenotravel": ("numeric/ipc-2023/zenotravel", "ENHSP-SAT-HMRP"),
    "Baxter": ("hybrid/Baxter", "ENHSP-OPT-HADD"),
    "Descent": ("hybrid/Descent", "ENHSP-OPT-AIBR"),
    "HVAC": ("hybrid/HVAC", "ENHSP-OPT-HADD"),
    "Linear-Car": ("hybrid/Linear-Car", "ENHSP-OPT-AIBR"),
    "Solar-Rover": ("hybrid/Solar-Rover", "ENHSP-OPT-AIBR"),
    "Linear-Car-2": ("hybrid/Linear-Car-2", "ENHSP-OPT-AIBR"),
    "UTC": ("hybrid/UTC", "ENHSP-OPT-AIBR"),
    "UTC2": ("hybrid/UTC2", "ENHSP-OPT-AIBR"),
}


def main():
    instances = list()

    for (name, (path, planner)) in DOMAINS.items():
        problems = natsort.natsorted(os.listdir(f"files/{path}/instances"))
        for problem in problems:
            if problem[-5:] != ".pddl":
                continue
            domainFile = f"files/{path}/domain.pddl"
            problemFile = f"files/{path}/instances/{problem}"
            planFile = f"files/{path}/plans/{problem}.txt"
            if not os.path.exists(f"files/{path}/plans") or not os.path.exists(planFile):
                instances.append([planner, name, domainFile, problemFile])

    random.shuffle(instances)
    print(f"Listing {len(instances)} instances")
    f = open(f"benchmarks/instances/icr-plan.csv", "w")
    f.write("\n".join([",".join(i) for i in instances]))
    f.close()


if __name__ == '__main__':
    main()