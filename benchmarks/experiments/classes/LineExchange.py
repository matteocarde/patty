import random
from typing import Dict


class LineExchange:

    def __init__(self, nOfRobots: int, itemsPerRobot: None or int = None, distance: int = 2,
                 distribution: float or str = 100, max_q: None or int = None, totalItems: None or int = None):
        self.nOfRobots = nOfRobots

        self.totalItems = self.nOfRobots * itemsPerRobot if itemsPerRobot else totalItems
        self.distance = distance
        self.distribution = distribution
        self.max_q = self.totalItems if not max_q else max_q

        self.items: Dict[int, int] = dict()
        robotList = list(range(0, self.nOfRobots))

        if distribution != "all-in-first":
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
        else:
            for (n, i) in enumerate(robotList):
                self.items[i] = self.totalItems if i == 0 else 0

    def toPDDL(self) -> str:
        n = " "

        if self.distribution == "all-in-first":
            goal = f"(= (q r{self.nOfRobots - 1}) {self.totalItems})"
        else:
            goal = n.join(f"(= (q r{i}) (q r{i + 1}))" for i in range(0, self.nOfRobots - 1))

        return f"""
        (define (problem prob01)
            (:domain line-exchange)
            (:objects
              {' '.join(f"r{i}" for i in range(0, self.nOfRobots))} - robot
            )
            
            (:init
                (= (D) {self.distance})
                
                (= (max_q) {self.max_q})
                
                {n.join(f"(= (i r{i}) {i})" for i in range(0, self.nOfRobots))}
                
                {n.join(f"(= (x r{i}) {i * self.distance + self.distance / 2})" for i in range(0, self.nOfRobots))}
                
                {n.join(f"(= (q r{i}) {self.items[i]})" for i in range(0, self.nOfRobots))}
                
                {n.join(f"(= (e r{i} r{i + 1}) 1)" for i in range(0, self.nOfRobots - 1))}
                
                {n.join(f"(next r{i} r{i + 1})" for i in range(0, self.nOfRobots - 1))}
            )

            (:goal
                (and
                    {n.join(f"(= (x r{i}) {i * self.distance + self.distance / 2})" for i in range(0, self.nOfRobots))}
                    
                    {goal}
                )
            )
        )"""
