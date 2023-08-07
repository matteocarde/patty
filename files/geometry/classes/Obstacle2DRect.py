import math
import random

from sympy import Expr, Point, Line, symbols, Segment

from classes.Obstacle import Obstacle

# Has to be ordered clockwise for generating the lines
VERSORS = [Point(1, 1), Point(1, -1), Point(-1, -1), Point(-1, 1)]


class Obstacle2DRect(Obstacle):

    def __init__(self, gridSize: int):
        super().__init__(gridSize)

        self.points = [self.center + v * self.radius for v in VERSORS]
        sizes = 4
        self.segmentIndexes = [[i, i + 1] for i in range(0, sizes - 1)] + [[sizes - 1, 0]]
        self.computeCoefficients()
        pass
