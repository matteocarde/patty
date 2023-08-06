import random

from classes.Level import Level
from classes.LevelType import LevelTypes


def main():
    l = Level(
        levelType=LevelTypes.T_2D_TOWER_RECT,
        gridSize=50,
        nOfObstacles=10
    )
    l.draw()
    pass


if __name__ == '__main__':
    main()
