import os
import time

from classes.MailRobots import MailRobots


def main():
    folder = f"./instances/{time.time_ns()}/"
    os.makedirs(folder)

    robots = range(1, 21)

    for r in robots:
        nOfRobots = r * 2 + 1
        l = MailRobots(
            halfRobots=r,
            L=20
        )
        with open(f"{folder}/prob_{nOfRobots}.pddl", "w") as f:
            f.write(l.toPDDL())


if __name__ == '__main__':
    main()
