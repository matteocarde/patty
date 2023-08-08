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
        self.movementType = movementType
        self.movements: List[List[int]] = MOVEMENTS[dimensions][movementType]
        self.obstacleType = obstacleType
        self.domainName = f"{self.dimensions}_{self.movementType}_{self.obstacleType}"

    def getDomain(self) -> str:
        actions = []
        for versor in self.movements:
            actions.append(f"""
            (:action move_{"_".join([str(e) for e in versor])}
                :parameters ()
                :precondition (and 
                    (>= (+ (x) {versor[0]}) (minx))
                    (<= (+ (x) {versor[0]}) (maxx))
                    (>= (+ (y) {versor[1]}) (miny))
                    (<= (+ (y) {versor[1]}) (maxy))
                )
                :effect (and
                    (increase (x) {versor[0]})
                    (increase (y) {versor[1]})
                )
            )""")
        actions = "\n\n".join(actions)

        return f"""
        (define (domain geometry_{self.domainName})

            (:types 
                obstacle - object)

            (:functions (x)
                        (y)
                        (maxy)
                        (maxx)
                        (miny)
                        (minx)
                        (a1 ?b -obstacle)
                        (b1 ?b -obstacle)
                        (c1 ?b -obstacle)
                        (a2 ?b -obstacle)
                        (b2 ?b -obstacle)
                        (c2 ?b -obstacle)
                        (a3 ?b -obstacle)
                        (b3 ?b -obstacle)
                        (c3 ?b -obstacle)
                        (a4 ?b -obstacle)
                        (b4 ?b -obstacle)
                        (c4 ?b -obstacle)
            )

            {actions}

            (:constraint obstacle
                :parameters (?b - obstacle)
                :condition (or  
                    (>= (+ (* (x) (a1 ?b)) (* (y) (b1 ?b))) (c1 ?b))
                    (>= (+ (* (x) (a2 ?b)) (* (y) (b2 ?b))) (c2 ?b))
                    (>= (+ (* (x) (a3 ?b)) (* (y) (b3 ?b))) (c3 ?b))
                    (>= (+ (* (x) (a4 ?b)) (* (y) (b4 ?b))) (c4 ?b))
                )
            )
        )        
        """


class LevelTypes:
    T_2D_TOWER_RECT = LevelType(2, "TOWER", "RECT")
    T_2D_TOWER_POLY = LevelType(2, "TOWER", "POLY")
    T_2D_QUEEN_RECT = LevelType(2, "QUEEN", "RECT")
    T_2D_QUEEN_POLY = LevelType(2, "QUEEN", "POLY")
    T_3D_TOWER_RECT = LevelType(3, "TOWER", "RECT")
    T_3D_TOWER_POLY = LevelType(3, "TOWER", "POLY")
    T_3D_QUEEN_RECT = LevelType(3, "QUEEN", "RECT")
    T_3D_QUEEN_POLY = LevelType(3, "QUEEN", "POLY")
