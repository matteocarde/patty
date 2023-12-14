import copy
import os
import random
import shutil
from math import floor

import numpy as np
from natsort import natsort

from src.pddl.InitialCondition import InitialCondition
from src.pddl.PDDLWriter import PDDLWriter
from src.pddl.Problem import Problem

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

PARTIAL = [0, 25, 50, 75, 100]
maxPartial = 20

NOISE = [floor(x) for x in np.linspace(0, 1000, 51)]
maxNoise = 1

noiseIterations = 1


def main():
    instances = list()

    for (name, path) in DOMAINS.items():
        if not os.path.exists(f"files/{path}/plans"):
            continue
        plans = natsort.natsorted(os.listdir(f"files/{path}/plans"))
        if os.path.exists(f"files/{path}/partial"):
            shutil.rmtree(f"files/{path}/partial")
        os.mkdir(f"files/{path}/partial")

        if os.path.exists(f"files/{path}/noise"):
            shutil.rmtree(f"files/{path}/noise")
        os.mkdir(f"files/{path}/noise")

        nOfPartial = 0
        nOfNoise = 0
        for plan in plans:

            if plan[-4:] != ".txt":
                continue
            problemFile = f"files/{path}/instances/{plan[:-9]}.pddl"
            print(problemFile)
            prob: Problem = Problem.fromFile(problemFile)

            if nOfPartial < maxPartial:

                partialFolder = f"files/{path}/partial/{plan[:-9]}"
                if os.path.exists(partialFolder):
                    shutil.rmtree(partialFolder)
                os.mkdir(partialFolder)
                for amount in PARTIAL:
                    pw = PDDLWriter()
                    partialProb = copy.deepcopy(prob)
                    partialProb.init = InitialCondition.partialize(partialProb.init, amount / 100)
                    pddl: str = partialProb.toPDDL(pw).toString()
                    with open(f"{partialFolder}/{plan[:-9]}-{amount}.pddl", "w") as f:
                        f.write(pddl)
                    pass
                nOfPartial += 1

            if nOfNoise < maxNoise:
                noiseFolder = f"files/{path}/noise/{plan[:-9]}"
                if os.path.exists(noiseFolder):
                    shutil.rmtree(noiseFolder)
                os.mkdir(noiseFolder)
                for j in range(1, noiseIterations + 1):
                    for amount in NOISE:
                        pw = PDDLWriter()
                        noiseProb = copy.deepcopy(prob)
                        noiseProb.init = InitialCondition.noise(noiseProb.init, amount)
                        noisePDDL: str = noiseProb.toPDDL(pw).toString()
                        with open(f"{noiseFolder}/{j}-{amount}.pddl", "w") as f:
                            f.write(noisePDDL)
                        pass
                    nOfNoise += 1


if __name__ == '__main__':
    main()
