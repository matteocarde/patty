import math
import random

from sympy import Point, Segment, Line, Expr

from classes.Obstacle import Obstacle


class Obstacle2DPoly(Obstacle):

    def __init__(self, gridSize: int):
        super().__init__(gridSize)

        center = self.center
        radius = self.radius
        sizes: int = random.randint(3, 3)
        angles = []
        startingAngle = random.uniform(0, 2 * math.pi)
        for s in range(0, sizes):
            angles.append(startingAngle + s * 2 * math.pi / sizes)

        # angles = [random.uniform(0, 2 * math.pi) for s in range(0, sizes)]
        # angles.sort()

        self.segmentIndexes = [[i, i + 1] for i in range(0, sizes - 1)] + [[sizes - 1, 0]]
        self.points = [Point(center.x + radius * math.cos(theta), center.y + radius * math.sin(theta)) for theta in
                       angles]

        pass
