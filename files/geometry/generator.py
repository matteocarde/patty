import random

from classes.Level import Level
from classes.LevelType import LevelTypes


def main():
    random.seed(20121996)
    l = Level(
        levelType=LevelTypes.T_2D_TOWER_POLY,
        gridSize=50,
        nOfObstacles=50
    )
    l.draw()
    pass


if __name__ == '__main__':
    main()
