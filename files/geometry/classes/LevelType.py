from enum import Enum
from typing import List

MOVEMENTS = {
    2: {
        "TOWER": [[1, 0], [0, 1], [-1, 0], [0, -1]],
        "QUEEN": [[1, 0], [1, 1], [0, 1], [-1, 1], [-1, 0], [-1, -1], [0, -1], [1, -1]]
    },
    3: {
        "TOWER": [
            [1, 0, 0], [0, 1, 0], [-1, 0, 0], [0, -1, 0], [0, 0, 1], [0, 0, -1]
        ],
        "QUEEN": [
            [1, 0, 0], [1, 1, 0], [0, 1, 0], [-1, 1, 0], [-1, 0, 0], [-1, -1, 0], [0, -1, 0], [1, -1, 0],
            [1, 0, 1], [1, 1, 1], [0, 1, 1], [-1, 1, 1], [-1, 0, 1], [-1, -1, 1], [0, -1, 1], [1, -1, 1],
            [1, 0, -1], [1, 1, -1], [0, 1, -1], [-1, 1, -1], [-1, 0, -1], [-1, -1, -1], [0, -1, -1], [1, -1, -1],
            [0, 0, 1], [0, 0, -1]
        ]
    }
}


class LevelType:

    def __init__(self, dimensions: int, movementType: str, obstacleType: str):
        self.dimensions = dimensions
        self.movements: List[List[int]] = MOVEMENTS[dimensions][movementType]
        self.obstacleType = obstacleType


class LevelTypes:
    T_2D_TOWER_RECT = LevelType(2, "TOWER", "RECT")
    T_2D_TOWER_POLY = LevelType(2, "TOWER", "POLY")
    T_2D_QUEEN_RECT = LevelType(2, "QUEEN", "RECT")
    T_2D_QUEEN_POLY = LevelType(2, "QUEEN", "POLY")
    T_3D_TOWER_RECT = LevelType(3, "TOWER", "RECT")
    T_3D_TOWER_POLY = LevelType(3, "TOWER", "POLY")
    T_3D_QUEEN_RECT = LevelType(3, "QUEEN", "RECT")
    T_3D_QUEEN_POLY = LevelType(3, "QUEEN", "POLY")
