import random
from typing import Dict


class LineExchange:

    def __init__(self, nOfRobots: int, itemsPerRobot: int, distance: int, distribution: float):
        self.nOfRobots = nOfRobots

        self.totalItems = self.nOfRobots * itemsPerRobot
        self.distance = distance
        self.distribution = distribution

        self.items: Dict[int, int] = dict()

        robotList = list(range(0, self.nOfRobots))
        random.shuffle(robotList)

        fDist = self.distribution / 100
        total = 0
        for (n, i) in enumerate(robotList[0:-1]):
            rItems = self.totalItems - total
            rRobots = nOfRobots - n
            self.items[i] = round(rItems / rRobots * random.uniform(1 - fDist, 1 + fDist))
            total += self.items[i]
        assert total <= self.totalItems
        self.items[robotList[-1]] = self.totalItems - total

    def toPDDL(self) -> str:
        n = " "
        return f"""
        (define (problem prob01)
            (:domain line-exchange)
            (:objects
              {' '.join(f"r{i}" for i in range(0, self.nOfRobots))} - robot
            )
            
            (:init
                (= (D) {self.distance})
                
                {n.join(f"(= (i r{i}) {i})" for i in range(0, self.nOfRobots))}
                
                {n.join(f"(= (x r{i}) {i * self.distance + self.distance / 2})" for i in range(0, self.nOfRobots))}
                
                {n.join(f"(= (q r{i}) {self.items[i]})" for i in range(0, self.nOfRobots))}
                
                {n.join(f"(= (e r{i} r{i + 1}) 1)" for i in range(0, self.nOfRobots - 1))}
                
                {n.join(f"(next r{i} r{i + 1})" for i in range(0, self.nOfRobots - 1))}
            )

            (:goal
                (and
                    {n.join(f"(= (x r{i}) {i * self.distance + self.distance / 2})" for i in range(0, self.nOfRobots))}
                    
                    {n.join(f"(= (q r{i}) (q r{i + 1}))" for i in range(0, self.nOfRobots - 1))}
                )
            )
        )"""
