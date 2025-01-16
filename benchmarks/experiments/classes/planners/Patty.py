import re

from classes.planners.Planner import Planner
from classes.Result import Result

NAME = "PATTY"


class Patty(Planner):
    name = NAME

    def __init__(self, name, search="static",
                 maximize=False,
                 useSCCs=False,
                 noCompression=False,
                 pattern="enhanced",
                 quality="none",
                 tcTime=0,
                 hasEffectAxioms=False,
                 rollBound=0,
                 temporalConstraints=None,
                 avoidClosure=False,
                 avoidClosureRelaxation=False):
        self.search = search
        self.maximize = maximize
        self.name = name
        self.useSCCs = useSCCs
        self.noCompression = noCompression
        self.pattern = pattern
        self.quality = quality
        self.hasEffectAxioms = hasEffectAxioms
        self.rollBound = rollBound
        self.temporalConstraints = temporalConstraints
        self.tcTime = tcTime
        self.avoidClosure = avoidClosure
        self.avoidClosureRelaxation = avoidClosureRelaxation
        super().__init__()

    @staticmethod
    def parseOutput(r: Result, stdout: str):
        r.solved = len(re.findall(r"Plan is valid", stdout)) > 0
        r.time = Result.parseTime(stdout)
        reBound = re.findall(r"^Bound: (\d*?)$", stdout, re.MULTILINE)
        r.bound = -1 if not reBound else int(reBound[0])
        r.plan = re.findall(r"^\d*?: (\(.*?\))$", stdout, re.MULTILINE)
        r.planLength = len(r.plan)
        reNOfVars = re.findall(r"Bound .*? - Vars = (.*?)$", stdout, re.MULTILINE)
        r.nOfVars = -1 if not reNOfVars else int(reNOfVars[-1])
        reNOfRules = re.findall(r"Bound .*? - Rules = (.*?)$", stdout, re.MULTILINE)
        r.nOfRules = -1 if not reNOfRules else int(reNOfRules[-1])
        reLastSearchedBound = re.findall(r"Started Solving Bound (\d*?)$", stdout, re.MULTILINE)
        r.lastSearchedBound = -1 if not reLastSearchedBound else int(reLastSearchedBound[-1])

        lastCallsToSolver = re.findall(r"Calls to Solver: (\d*?)$", stdout, re.MULTILINE)
        r.lastCallsToSolver = -1 if not lastCallsToSolver else int(lastCallsToSolver[-1])

        transitiveClosureTime = re.findall(r"Ended Computing Transitive Closure: (\d*?)$", stdout, re.MULTILINE)
        print(transitiveClosureTime)
        r.transitiveClosureTime = -1 if not transitiveClosureTime else int(transitiveClosureTime[-1])

        boolVariables = re.findall(r"^\|V_b\|=(\d*?)$", stdout, re.MULTILINE)
        r.boolVariables = -1 if not boolVariables else int(boolVariables[-1])

        numVariables = re.findall(r"^\|V_n\|=(\d*?)$", stdout, re.MULTILINE)
        r.numVariables = -1 if not numVariables else int(numVariables[-1])

        actions = re.findall(r"^\|A\|=(\d*?)$", stdout, re.MULTILINE)
        r.actions = -1 if not actions else int(actions[-1])

        patternLength = re.findall(r"Bound .*? - Pattern Length = (.*?)$", stdout, re.MULTILINE)
        r.patternLength = -1 if not patternLength else int(patternLength[-1])

        maxRolling = re.findall(r"Max Rolling: (.*?)$", stdout, re.MULTILINE)
        r.maxRolling = -1 if not maxRolling else int(maxRolling[0])

        distinctActionsInPlan = re.findall(r"Distinct Actions: (.*?)$", stdout, re.MULTILINE)
        r.distinctActionsInPlan = -1 if not distinctActionsInPlan else int(distinctActionsInPlan[0])

        avgVarsInRules = re.findall(r"Bound .*? - Avg Rule Length = (.*?)$", stdout, re.MULTILINE)
        r.avgVarsInRules = -1 if not avgVarsInRules else float(avgVarsInRules[-1])

        rolledActionsInPlan = re.findall(r"Rolled Actions: (.*?)$", stdout, re.MULTILINE)
        r.rolledActionsInPlan = -1 if not rolledActionsInPlan else int(rolledActionsInPlan[0])

        return r

    def getCommand(self, domain: str, problem: str):
        cmd = [
            "patty",
            # "-pp",
            "-o", domain,
            "-f", problem,
            "--pattern", self.pattern,
            "--quality", self.quality,
            "-pp"
        ]
        if self.rollBound:
            cmd += ["--roll-bound", str(self.rollBound)]
        if self.hasEffectAxioms:
            cmd += ["--effect-axioms"]
        if self.noCompression:
            cmd += ["--no-compression"]
        if self.maximize:
            cmd += ["--maximize"]
        if self.useSCCs:
            cmd += ["--use-sccs"]
        if self.tcTime:
            cmd += ["--max-closure-time", str(self.tcTime)]
        if self.temporalConstraints:
            cmd += ["--temporal-constraints", self.temporalConstraints]
        if self.avoidClosure:
            cmd += ["--avoid-closure"]
        if self.avoidClosureRelaxation:
            cmd += ["--avoid-closure-relaxation"]
        return cmd
