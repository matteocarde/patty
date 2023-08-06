import math
import random

from sympy import Point, Segment, Line, Expr

from classes.Obstacle import Obstacle


class Obstacle2DPoly(Obstacle):

    def __init__(self, gridSize: int):
        super().__init__(gridSize)

        radius: float = random.uniform(self.MIN_RADIUS, self.MAX_RADIUS)
        center: (float, float) = Point(random.uniform(0, gridSize),
                                       random.uniform(0, gridSize))
        sizes: int = random.randint(3, 3)
        angles = []
        startingAngle = random.uniform(0, 2 * math.pi)
        for s in range(0, sizes):
            angles.append(startingAngle + s * 2 * math.pi / sizes)

        # angles = [random.uniform(0, 2 * math.pi) for s in range(0, sizes)]
        # angles.sort()

        segments = [[i, i + 1] for i in range(0, sizes - 1)] + [[sizes - 1, 0]]
        points = [Point(center.x + radius * math.cos(theta), center.y + radius * math.sin(theta)) for theta in angles]

        self.segments: [Segment] = [Segment(points[s[0]], points[s[1]]) for s in segments]
        self.frontier: [Line] = [Line(points[s[0]], points[s[1]]) for s in segments]

        self.conditions: [Expr] = list()

        for l in self.frontier:
            coeff = l.coefficients
            sign = coeff[0] * center.x + coeff[1] * center.y + coeff[2]
            if sign > 0:
                cond = coeff[0] * self.x + coeff[1] * self.y + coeff[2] < 0
            else:
                cond = coeff[0] * self.x + coeff[1] * self.y + coeff[2] > 0
            self.conditions.append(cond)

        pass
