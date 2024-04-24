class RelayRace:

    def __init__(self, halfRunners: int, nOfBatonsPerType: int, L: int = 2):
        self.nOfRunners = 2 * halfRunners + 1
        self.nOfBatonsPerType = nOfBatonsPerType
        self.L = L

        self.runnersList = list(range(0, self.nOfRunners))
        self.halfRunnersList = list(range(0, halfRunners + 1))
        self.otherHalfRunnersList = list(range(halfRunners + 1, self.nOfRunners))
        self.pairs = [(i, i + 1) for i in range(0, self.nOfRunners - 1)]
        self.lettersList = list(range(0, self.nOfBatonsPerType))

    def toPDDL(self) -> str:
        n = " "

        return f"""
        (define (problem prob{self.nOfRunners})
            (:domain relay-race)
            (:objects
              {' '.join(f"r{i}" for i in self.runnersList)} - runner
              {' '.join(f"P{i}" for i in self.lettersList)} {' '.join(f"Q{i}" for i in self.lettersList)} - baton
            )
            
            (:init
                (= (L) {self.L})
                
                {n.join(f"(= (i r{i}) {i})" for i in self.runnersList)}
                {n.join(f"(next r{a} r{b})" for (a, b) in self.pairs)}
                
                {n.join(f"(= (x r{i}) {i * self.L})" for i in self.runnersList)}
                
                {n.join(f"(= (b r{i} P{j}) {1 if i == 0 else 0})" for i in self.runnersList for j in self.lettersList)}
                {n.join(f"(= (b r{i} Q{j}) {1 if i == 0 else 0})" for i in self.runnersList for j in self.lettersList)}
                {n.join(f"(= (h r{i}) {self.nOfBatonsPerType * 2 if i == 0 else 0})" for i in self.runnersList)}
                
                {n.join(f"(td r0 P{j})" for j in self.lettersList)}
                {n.join(f"(td r0 Q{j})" for j in self.lettersList)}
            )

            (:goal
                (and
                    {n.join(f"(td r{i} P{j})" for i in self.halfRunnersList for j in self.lettersList)}
                    {n.join(f"(not (td r{i} P{j}))" for i in self.otherHalfRunnersList for j in self.lettersList)}
                    {n.join(f"(td r{i} Q{j})" for i in self.runnersList for j in self.lettersList)}
                    {n.join(f"(= (b r0 P{j}) 1)" for j in self.lettersList)}
                    {n.join(f"(= (b r{self.nOfRunners - 1} Q{j}) 1)" for j in self.lettersList)}
                )
            )
        )"""
