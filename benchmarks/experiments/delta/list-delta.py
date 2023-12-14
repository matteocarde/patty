import os
import random

from natsort import natsort

PLANNERS = {
    "DELTA": [
        "ENHSP-SAT-HMRP[-de 1 -dp 1 -dh 1]",
        "ENHSP-SAT-HADD[-de 1 -dp 1 -dh 1]",
        "ENHSP-SAT-AIBR[-de 1 -dp 1 -dh 1]",
        "ENHSP-OPT-HMRP[-de 1 -dp 1 -dh 1]",
        "ENHSP-OPT-HADD[-de 1 -dp 1 -dh 1]",
        "ENHSP-OPT-AIBR[-de 1 -dp 1 -dh 1]",
    ],
    "NODELTA": [
        "ENHSP-SAT-HMRP[-de 1 -dp 3 -dh 3]",
        "ENHSP-SAT-HADD[-de 1 -dp 3 -dh 3]",
        "ENHSP-SAT-AIBR[-de 1 -dp 3 -dh 3]",
        "ENHSP-OPT-HMRP[-de 1 -dp 3 -dh 3]",
        "ENHSP-OPT-HADD[-de 1 -dp 3 -dh 3]",
        "ENHSP-OPT-AIBR[-de 1 -dp 3 -dh 3]",

        "ENHSP-SAT-HMRP[-de 1 -dp 1 -dh 1]",
        "ENHSP-SAT-HADD[-de 1 -dp 1 -dh 1]",
        "ENHSP-SAT-AIBR[-de 1 -dp 1 -dh 1]",
        "ENHSP-OPT-HMRP[-de 1 -dp 1 -dh 1]",
        "ENHSP-OPT-HADD[-de 1 -dp 1 -dh 1]",
        "ENHSP-OPT-AIBR[-de 1 -dp 1 -dh 1]",

        # "ENHSP-SAT-HMRP[-de 0.1 -dp 1 -dh 1]",
        # "ENHSP-SAT-HADD[-de 0.1 -dp 1 -dh 1]",
        # "ENHSP-SAT-AIBR[-de 0.1 -dp 1 -dh 1]",
        # "ENHSP-SAT-BLIND[-de 0.1 -dp 1 -dh 1]",
        # "ENHSP-OPT-HMRP[-de 0.1 -dp 1 -dh 1]",
        # "ENHSP-OPT-HADD[-de 0.1 -dp 1 -dh 1]",
        # "ENHSP-OPT-AIBR[-de 0.1 -dp 1 -dh 1]",
        # "ENHSP-OPT-BLIND[-de 0.1 -dp 1 -dh 1]"
    ]
}


# PLANNERS = {
#     "DELTA": [
#         "ENHSP-SAT-HMRP[-de 0.1 -dp 0.1 -dh 0.1]",
#         "ENHSP-SAT-HADD[-de 0.1 -dp 0.1 -dh 0.1]",
#         "ENHSP-SAT-AIBR[-de 0.1 -dp 0.1 -dh 0.1]",
#         "ENHSP-SAT-BLIND[-de 0.1 -dp 0.1 -dh 0.1]",
#         "ENHSP-OPT-HMRP[-de 0.1 -dp 0.1 -dh 0.1]",
#         "ENHSP-OPT-HADD[-de 0.1 -dp 0.1 -dh 0.1]",
#         "ENHSP-OPT-AIBR[-de 0.1 -dp 0.1 -dh 0.1]",
#         "ENHSP-OPT-BLIND[-de 0.1 -dp 0.1 -dh 0.1]"
#     ],
#     "NODELTA": [
#         "ENHSP-SAT-HMRP[-de 0.1 -dp 0.1 -dh 0.1]",
#         "ENHSP-SAT-HADD[-de 0.1 -dp 0.1 -dh 0.1]",
#         "ENHSP-SAT-AIBR[-de 0.1 -dp 0.1 -dh 0.1]",
#         "ENHSP-SAT-BLIND[-de 0.1 -dp 0.1 -dh 0.1]",
#         "ENHSP-OPT-HMRP[-de 0.1 -dp 0.1 -dh 0.1]",
#         "ENHSP-OPT-HADD[-de 0.1 -dp 0.1 -dh 0.1]",
#         "ENHSP-OPT-AIBR[-de 0.1 -dp 0.1 -dh 0.1]",
#         "ENHSP-OPT-BLIND[-de 0.1 -dp 0.1 -dh 0.1]",
#
#         "ENHSP-SAT-HMRP[-de 0.1 -dp 1 -dh 1]",
#         "ENHSP-SAT-HADD[-de 0.1 -dp 1 -dh 1]",
#         "ENHSP-SAT-AIBR[-de 0.1 -dp 1 -dh 1]",
#         "ENHSP-SAT-BLIND[-de 0.1 -dp 1 -dh 1]",
#         "ENHSP-OPT-HMRP[-de 0.1 -dp 1 -dh 1]",
#         "ENHSP-OPT-HADD[-de 0.1 -dp 1 -dh 1]",
#         "ENHSP-OPT-AIBR[-de 0.1 -dp 1 -dh 1]",
#         "ENHSP-OPT-BLIND[-de 0.1 -dp 1 -dh 1]"
#     ]
# }


def main():
    NAME = "delta"
    domains = {
        "CoOpRobots": {
            "DELTA": "hybrid/CoOpRobots/delta",
            "NODELTA": "hybrid/CoOpRobots"
        },
        # "BaxterMulti": {
        #     "DELTA": "hybrid/BaxterMulti/delta",
        #     "NODELTA": "hybrid/BaxterMulti"
        # },
        # "Baxter": {
        #     "DELTA": "hybrid/Baxter/delta",
        #     "NODELTA": "hybrid/Baxter"
        # },
        # "Descent": {
        #     "DELTA": "hybrid/Descent/delta",
        #     "NODELTA": "hybrid/Descent"
        # },
        # "HVAC": {
        #     "DELTA": "hybrid/HVAC/delta",
        #     "NODELTA": "hybrid/HVAC"
        # },
        # "Linear-Car": {
        #     "DELTA": "hybrid/Linear-Car/delta",
        #     "NODELTA": "hybrid/Linear-Car"
        # },
        # "Linear-Car-2": {
        #     "DELTA": "hybrid/Linear-Car-2/delta",
        #     "NODELTA": "hybrid/Linear-Car-2"
        # },
        # "Linear-Generator": {
        #     "DELTA": "hybrid/Linear-Generator/delta",
        #     "NODELTA": "hybrid/Linear-Generator"
        # },
        # "OT-Car": {
        #     "DELTA": "hybrid/OT-Car/delta",
        #     "NODELTA": "hybrid/OT-Car"
        # },
        # "Solar-Rover": {
        #     "DELTA": "hybrid/Solar-Rover/delta",
        #     "NODELTA": "hybrid/Solar-Rover"
        # }

    }

    instances = list()

    for (domainName, domainObj) in domains.items():
        for (t, path) in domainObj.items():
            problems = natsort.natsorted(os.listdir(f"files/{path}/instances"))
            for problem in problems:
                if problem[-5:] != ".pddl":
                    continue
                domainFile = f"files/{path}/domain.pddl"
                problemFile = f"files/{path}/instances/{problem}"

                for planner in PLANNERS[t]:
                    n = 1 if "PATTY-R" not in planner else 5
                    for i in range(0, n):
                        instances.append([planner, f"{domainName}-{t}", domainFile, problemFile])

    random.shuffle(instances)
    print(f"Listing {len(instances)} instances")
    f = open(f"benchmarks/instances/{NAME}.csv", "w")
    f.write("\n".join([",".join(i) for i in instances]))
    f.close()


if __name__ == '__main__':
    main()
