import random
from enum import Enum

import numpy as np
from matplotlib import pyplot as plt
from sympy import Point

from classes.Obstacle import Obstacle
from classes.LevelType import LevelType


class Level:

    def __init__(self, levelType: LevelType, gridSize: int = 50, nOfObstacles: int = 1):
        random.seed(20121996)
        self.levelType: LevelType = levelType
        self.gridSize: int = gridSize
        self.obstacles: [Obstacle] = [Obstacle.fromType(levelType, gridSize) for i in range(0, nOfObstacles)]
        self.init = self.findPointNotInsideObstacles()
        self.goal = self.findPointNotInsideObstacles()
        pass

    def draw(self):
        plt.rcParams.update({
            "text.usetex": True,
            "figure.autolayout": True
        })
        plt.figure(1, figsize=(5, 5))
        plt.axes()
        plt.xlim([0, self.gridSize])
        plt.ylim([0, self.gridSize])


        for obstacle in self.obstacles:
            for segment in obstacle.segments:
                p1, p2 = segment.points
                line = plt.Line2D((p1.x, p2.x), (p1.y, p2.y), lw=1.5)
                plt.gca().add_line(line)
        plt.plot(self.init.x, self.init.y, marker="o", markersize=10, markerfacecolor="green")
        plt.plot(self.goal.x, self.goal.y, marker="o", markersize=10, markeredgecolor="green", markerfacecolor="white")

        plt.show()

    def findPointNotInsideObstacles(self) -> Point:
        while True:
            point = Point(random.uniform(0, self.gridSize), random.uniform(0, self.gridSize))
            isInside = False
            for obstacle in self.obstacles:
                isInside = obstacle.isInside(point)
                if isInside:
                    print(f"Point {point} was inside. Recomputing...")
                    break
            if not isInside:
                return point

    def getProblem(self) -> str:
        return ""

    def getDomain(self) -> str:
        return ""
