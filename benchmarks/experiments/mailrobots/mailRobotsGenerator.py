import os
import time

from classes.RelayRace import RelayRace


def main():
    folder = f"./instances/{time.time_ns()}/"
    os.makedirs(folder)

    runners = range(1, 81)
    nOfBatonsPerType = 3

    for r in runners:
        l = RelayRace(
            halfRunners=r,
            nOfBatonsPerType=nOfBatonsPerType,
            L=20
        )
        with open(f"{folder}/prob_{2 * r + 1}.pddl", "w") as f:
            f.write(l.toPDDL())


if __name__ == '__main__':
    main()
