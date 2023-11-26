import random
from typing import Dict


class SideExchange:

    def __init__(self, nOfRobots: int, itemsPerBin: int = None):
        self.nOfRobots = nOfRobots
        self.itemsPerBin = itemsPerBin

    def toPDDL(self) -> str:
        n = " "

        M = self.nOfRobots
        Q = self.itemsPerBin

        return f"""
        (define (problem prob{Q})
            (:domain side-exchange)
            (:objects
              green yellow - color
              {' '.join(f"r{i}" for i in range(1, M + 1))} - robot
            )
            
            (:init
                
                {n.join(f"(= (q r{i}) 0)" for i in range(1, M + 1))}
                
                (= (b r1 yellow) {Q}) 
                (= (b r1 green) 0)
                (= (b r{M} yellow) 0) 
                (= (b r{M} green) {Q}) 
                
                (edge r1) 
                (edge r{M})
                {n.join(f"(next r{i} r{i + 1})" for i in range(1, M))}
            )

            (:goal
                (and
                    (= (b r1 yellow) 0) 
                    (= (b r1 green) {Q})
                
                    (= (b r{M} yellow) {Q}) 
                    (= (b r{M} green) 0) 
                )
            )
        )"""
