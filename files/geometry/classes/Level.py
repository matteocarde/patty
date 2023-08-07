import random
from enum import Enum

import numpy as np
from matplotlib import pyplot as plt
from sympy import Point

from classes.Obstacle import Obstacle
from classes.LevelType import LevelType

MAX_NUM_CONDITIONS = 4


class Level:

    def __init__(self, levelType: LevelType, gridSize: int = 50, nOfObstacles: int = 1):
        self.levelType: LevelType = levelType
        self.gridSize: int = gridSize
        self.obstacles: [Obstacle] = [Obstacle.fromType(levelType, gridSize) for i in range(0, nOfObstacles)]
        self.init = self.findPointNotInsideObstacles()
        self.goal = self.findPointNotInsideObstacles()
        pass

    def draw(self, filename: None or str = None):
        plt.rcParams.update({
            "text.usetex": True,
            "figure.figsize": [7.50, 7.50],
            "figure.autolayout": True
        })
        plt.figure(1, figsize=(5, 5))
        plt.axes()
        ticks = np.arange(0, self.gridSize, 1)
        plt.xticks(ticks, labels=["" if t % 5 else str(t) for t in ticks])
        plt.yticks(ticks, labels=["" if t % 5 else str(t) for t in ticks])
        plt.grid()
        plt.xlim([0, self.gridSize])
        plt.ylim([0, self.gridSize])

        for obstacle in self.obstacles:
            for segment in obstacle.segments:
                p1, p2 = segment.points
                line = plt.Line2D((p1.x, p2.x), (p1.y, p2.y), lw=1.5)
                plt.gca().add_line(line)
        plt.plot(self.init.x, self.init.y, marker="o", markersize=10, markerfacecolor="green")
        plt.plot(self.goal.x, self.goal.y, marker="o", markersize=10, markeredgecolor="green", markerfacecolor="white")

        if filename:
            plt.savefig(f'{filename}')

        plt.show()

    def findPointNotInsideObstacles(self) -> Point:
        # return Point(random.uniform(0, self.gridSize), random.uniform(0, self.gridSize))
        while True:
            point = Point(random.randint(0, self.gridSize), random.randint(0, self.gridSize))
            isInside = False
            for obstacle in self.obstacles:
                isInside = obstacle.isInside(point)
                if isInside:
                    print(f"Point {point} was inside. Recomputing...")
                    break
            if not isInside:
                return point

    def getProblem(self) -> str:

        obstaclesName = [f"ob_{i}" for i in range(0, len(self.obstacles))]
        coordinates = []
        for index, ob in enumerate(self.obstacles):
            if len(ob.conditions) > 4:
                raise Exception("Obstacles with more than 4 conditions are, at the moment not supported")

            for j in range(0, MAX_NUM_CONDITIONS):
                coeff = ob.coefficients[j] if j < len(ob.coefficients) else [0, 0, 0]
                row = f"(= (a{j + 1} ob_{index}) {coeff[0]}) (= (b{j + 1} ob_{index}) {coeff[1]}) (= (c{j + 1} ob_{index}) {coeff[2]})"
                coordinates.append(row)

        coordinates = "\n".join(coordinates)

        return f"""
        (define
            (problem geometry)
            (:domain {self.levelType.domainName})

            (:objects {" ".join(obstaclesName)} - obstacle)

            (:init

                (= (x) {self.init.x}) (= (y) {self.init.y})

                (= (maxx) {self.gridSize}) 
                (= (maxy) {self.gridSize}) 
                (= (minx) 0) 
                (= (miny) 0)
                {coordinates}
    
            )
            (:goal (and
                (= (x) {self.goal.x}) (= (y) {self.goal.y})
            ))
        )        
        """
