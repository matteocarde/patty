import os
import random
import time

from classes.Level import Level
from classes.LevelType import LevelTypes


def main():
    type = LevelTypes.T_2D_TOWER_POLY
    random.seed(20121996)
    l = Level(
        levelType=type,
        gridSize=50,
        nOfObstacles=55
    )

    domainFolder = f"instances/{type.domainName}"
    problemFolder = f"{domainFolder}/instances/"
    if not os.path.exists(domainFolder):
        os.makedirs(domainFolder)
    if not os.path.exists(problemFolder):
        os.makedirs(problemFolder)
    with open(f"{domainFolder}/domain.pddl", "w") as d:
        d.write(type.getDomain())
    with open(f"{problemFolder}/problem.pddl", "w") as d:
        d.write(l.getProblem())

    l.draw(f"{problemFolder}/problem.pdf")
    pass


if __name__ == '__main__':
    main()
