import math
import random

from sympy import Expr, Point, Line, symbols, Segment

from classes.Obstacle import Obstacle

# Has to be ordered clockwise for generating the lines
VERSORS = [Point(1, 1), Point(1, -1), Point(-1, -1), Point(-1, 1)]
SEGMENTS = [[0, 1], [1, 2], [2, 3], [3, 0]]


class Obstacle2DRect(Obstacle):

    def __init__(self, gridSize: int):
        super().__init__(gridSize)

        radius: float = random.uniform(self.MIN_RADIUS, self.MAX_RADIUS)
        center: (float, float) = Point(random.uniform(radius, gridSize - radius),
                                       random.uniform(radius, gridSize - radius))

        points = [center + v * radius for v in VERSORS]

        self.segments: [Segment] = [Segment(points[s[0]], points[s[1]]) for s in SEGMENTS]
        frontier: [Line] = [Line(points[s[0]], points[s[1]]) for s in SEGMENTS]

        self.conditions: [Expr] = list()

        for l in frontier:
            coeff = l.coefficients
            sign = coeff[0] * center.x + coeff[1] * center.y + coeff[2]
            if sign > 0:
                cond = coeff[0] * self.x + coeff[1] * self.y + coeff[2] < 0
            else:
                cond = coeff[0] * self.x + coeff[1] * self.y + coeff[2] > 0
            self.conditions.append(cond)

        pass
