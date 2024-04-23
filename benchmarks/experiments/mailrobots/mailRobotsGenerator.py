import os
import time

from classes.MailRobots import MailRobots


def main():
    folder = f"./instances/{time.time_ns()}/"
    os.makedirs(folder)

    robots = range(1, 21)
    nOfLetters = 2

    for r in robots:
        l = MailRobots(
            halfRobots=r,
            nOfLetters=nOfLetters,
            L=20
        )
        with open(f"{folder}/prob_{2 * r + 1}.pddl", "w") as f:
            f.write(l.toPDDL())


if __name__ == '__main__':
    main()
