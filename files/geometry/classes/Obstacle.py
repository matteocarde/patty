from typing import List

from sympy import Segment, Expr, symbols, Point

from classes.LevelType import LevelType


class Obstacle:

    def __init__(self, gridSize: int):
        self.gridSize = gridSize
        self.MIN_RADIUS = 1
        self.MAX_RADIUS = 3
        self.x, self.y = symbols("x y")
        self.segments: List[Segment] = list()
        self.conditions: List[Expr] = list()
        pass

    def isInside(self, point: Point):
        for c in self.conditions:
            if c.subs({self.x: point.x, self.y: point.y}):
                return False
        return True

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
