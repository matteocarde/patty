class MailRobots:

    def __init__(self, halfRobots: int, nOfLetters: int, L: int = 2):
        self.nOfRobots = 2 * halfRobots + 1
        self.nOfLetters = nOfLetters
        self.L = L

        self.robotList = list(range(0, self.nOfRobots))
        self.halfRobotsList = list(range(0, halfRobots + 1))
        self.pairs = [(i, i + 1) for i in range(0, self.nOfRobots - 1)]
        self.lettersList = list(range(0, self.nOfLetters))

    def toPDDL(self) -> str:
        n = " "

        return f"""
        (define (problem prob{self.nOfRobots})
            (:domain mail-robots)
            (:objects
              {' '.join(f"r{i}" for i in self.robotList)} - robot
              {' '.join(f"g{i}" for i in self.lettersList)} - green
              {' '.join(f"y{i}" for i in self.lettersList)} - yellow
            )
            
            (:init
                (= (L) {self.L})
                
                {n.join(f"(= (i r{i}) {i})" for i in self.robotList)}
                {n.join(f"(next r{a} r{b})" for (a, b) in self.pairs)}
                
                {n.join(f"(= (x r{i}) {i * self.L})" for i in self.robotList)}
                
                {n.join(f"(= (g r{i} g{j}) {1 if i == 0 else 0})" for i in self.robotList for j in self.lettersList)}
                {n.join(f"(= (y r{i} y{j}) {1 if i == 0 else 0})" for i in self.robotList for j in self.lettersList)}
                {n.join(f"(= (hg r{i}) {self.nOfLetters if i == 0 else 0})" for i in self.robotList)}
                {n.join(f"(= (hy r{i}) {self.nOfLetters if i == 0 else 0})" for i in self.robotList)}
            )

            (:goal
                (and
                    {n.join(f"(gsd r{i} g{j})" for i in self.halfRobotsList for j in self.lettersList)}
                    {n.join(f"(ysd r{i} y{j})" for i in self.robotList for j in self.lettersList)}
                    (= (hg r0) {self.nOfLetters})
                    (= (hy r{self.nOfRobots - 1}) {self.nOfLetters})
                )
            )
        )"""
