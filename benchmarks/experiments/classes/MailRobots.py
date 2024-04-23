class MailRobots:

    def __init__(self, nOfRobots: int, L: int = 2):
        self.nOfRobots = nOfRobots
        self.L = L

        self.robotList = list(range(0, self.nOfRobots))

    def toPDDL(self) -> str:
        n = " "

        return f"""
        (define (problem prob{self.nOfRobots})
            (:domain mail-robots)
            (:objects
              {' '.join(f"r{i}" for i in self.robotList)} - robot
            )
            
            (:init
                (= (L) {self.L})
                
                {n.join(f"(= (i r{i}) {i})" for i in self.robotList)}
                
                {n.join(f"(= (x r{i}) {i * self.L})" for i in self.robotList)}
                
                {n.join(f"(= (p r{i}) {1 if i == 0 else 0})" for i in self.robotList)}
            )

            (:goal
                (and
                    {n.join(f"(psd r{i})" for i in self.robotList)}
                    (= (p r0) 1)
                )
            )
        )"""
