class MailRobots:

    def __init__(self, halfRobots: int, L: int = 2):
        self.nOfRobots = 2 * halfRobots + 1
        self.middleRobot = halfRobots
        self.L = L

        self.robotList = list(range(0, self.nOfRobots))

    def toPDDL(self) -> str:
        n = " "

        return f"""
        (define (problem prob{self.nOfRobots})
            (:domain mail-robots)
            (:objects
              {' '.join(f"r{i}" for i in self.robotList if i != self.middleRobot)} - robot
              r{self.middleRobot} - mailrobot
            )
            
            (:init
                (= (L) {self.L})
                
                {n.join(f"(= (i r{i}) {i})" for i in self.robotList)}
                
                {n.join(f"(= (x r{i}) {i * self.L})" for i in self.robotList)}
                
                {n.join(f"(= (p r{i}) {1 if i == 0 else 0})" for i in self.robotList)}
                {n.join(f"(= (q r{i}) {1 if i == 0 else 0})" for i in self.robotList)}
            )

            (:goal
                (and
                    (psd)
                    (qsd)
                    (= (p r0) 1)
                    (= (q r{self.nOfRobots - 1}) 1)
                )
            )
        )"""
