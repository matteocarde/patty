import math
import random
from typing import List

from sympy import Segment, Expr, symbols, Point, Line

from classes.LevelType import LevelType

MIN_RADIUS = 1
MAX_RADIUS = 3


class Obstacle:

    def __init__(self, gridSize: int):
        self.gridSize = gridSize
        self.x, self.y = symbols("x y")
        self.radius: float = random.uniform(MIN_RADIUS, MAX_RADIUS)
        self.center: (float, float) = Point(random.uniform(self.radius, gridSize - self.radius),
                                            random.uniform(self.radius, gridSize - self.radius))
        self.segments: List[Segment] = list()
        self.conditions: List[Expr] = list()
        self.coefficients: [[int]] = list()
        self.points: List[Point] = list()
        self.segmentIndexes: List[List[int]] = list()
        pass

    def isInside(self, point: Point):
        for c in self.conditions:
            if c.subs({self.x: point.x, self.y: point.y}):
                return False
        return True

    def computeCoefficients(self):
        self.segments: [Segment] = [Segment(self.points[s[0]], self.points[s[1]]) for s in self.segmentIndexes]
        frontier: [Line] = [Line(self.points[s[0]], self.points[s[1]]) for s in self.segmentIndexes]

        for l in frontier:
            coeff = l.coefficients
            sign = coeff[0] * self.center.x + coeff[1] * self.center.y + coeff[2]
            sign = sign / math.fabs(sign)
            cond = -sign * coeff[0] * self.x + -sign * coeff[1] * self.y + -sign * coeff[2] > 0
            self.coefficients.append([-sign * coeff[0], -sign * coeff[1], sign * coeff[2]])
            self.conditions.append(cond)

    @staticmethod
    def fromType(levelType: LevelType, gridSize: int):
        from classes.Obstacle2DPoly import Obstacle2DPoly
        from classes.Obstacle2DRect import Obstacle2DRect
        from classes.Obstacle3DPoly import Obstacle3DPoly
        from classes.Obstacle3DRect import Obstacle3DRect

        if levelType.dimensions == 2:
            if levelType.obstacleType == "RECT":
                return Obstacle2DRect(gridSize)
            elif levelType.obstacleType == "POLY":
                return Obstacle2DPoly(gridSize)
        if levelType.dimensions == 3:
            if levelType.obstacleType == "RECT":
                return Obstacle3DRect(gridSize)
            elif levelType.obstacleType == "POLY":
                return Obstacle3DPoly(gridSize)
