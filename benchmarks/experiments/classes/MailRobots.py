class MailRobots:

    def __init__(self, nOfRobots: int, nOfLetters: int, L: int = 2):
        self.nOfRobots = nOfRobots
        self.nOfLetters = nOfLetters
        self.L = L

        self.robotList = list(range(0, self.nOfRobots))
        self.pairs = [(i, i + 1) for i in range(0, self.nOfRobots - 1)]
        self.lettersList = list(range(0, self.nOfLetters))

    def toPDDL(self) -> str:
        n = " "

        return f"""
        (define (problem prob{self.nOfRobots})
            (:domain mail-robots)
            (:objects
              {' '.join(f"r{i}" for i in self.robotList)} - robot
              {' '.join(f"l{i}" for i in self.lettersList)} - letter
            )
            
            (:init
                (= (L) {self.L})
                
                {n.join(f"(= (i r{i}) {i})" for i in self.robotList)}
                {n.join(f"(next r{a} r{b})" for (a, b) in self.pairs)}
                
                {n.join(f"(= (x r{i}) {i * self.L})" for i in self.robotList)}
                
                {n.join(f"(= (p r{i} l{j}) {1 if i == 0 else 0})" for i in self.robotList for j in self.lettersList)}
                {n.join(f"(= (h r{i}) {self.nOfLetters if i == 0 else 0})" for i in self.robotList)}
            )

            (:goal
                (and
                    {n.join(f"(psd r{i} l{j})" for i in self.robotList for j in self.lettersList)}
                    (= (h r0) {self.nOfLetters})
                )
            )
        )"""
