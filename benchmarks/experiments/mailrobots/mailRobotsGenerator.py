import os
import time

from classes.MailRobots import MailRobots


def main():
    folder = f"./instances/{time.time_ns()}/"
    os.makedirs(folder)

    robots = range(2, 40)

    for r in robots:
        l = MailRobots(
            nOfRobots=r,
            L=20
        )
        with open(f"{folder}/prob_{r}.pddl", "w") as f:
            f.write(l.toPDDL())


if __name__ == '__main__':
    main()
