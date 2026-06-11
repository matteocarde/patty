from src.pddl.Domain import GroundedDomain
from src.pddl.Plan import Plan
from src.pddl.Problem import Problem
from src.pddl.State import State
from src.plan.NumericEncoding import NumericEncoding
from src.plan.Pattern import Pattern
from src.relaxed.RelaxedClassicalEncoding import RelaxedClassicalEncoding
from src.search.Search import Search
from src.utils.Arguments import Arguments


class HeuristicSearch(Search):
    initialState: State
    staticPattern: Pattern

    def __init__(self, domain: GroundedDomain, problem: Problem, args: Arguments):
        super().__init__(domain, problem, args)
        self.enhanced = (self.args.pattern == "enhanced")
        self.incompleteSaturationLevel = 1
        self.hasCheckedComplete = False

    def solve(self) -> Plan:
        subgoalsAchieved = set()

        bound = 0
        I: State = State.fromInitialCondition(self.problem.init)

        self.initialState = I
        self.ts.start(f"Conversion to SMT at bound {bound}")
        encoding: NumericEncoding = NumericEncoding(
            domain=self.domain,
            problem=self.problem,
            state=I,
            pattern=Pattern.empty(),
            goalFunctionValue=0,
            bound=1,
            args=self.args
        )

        relaxed: RelaxedClassicalEncoding = RelaxedClassicalEncoding(
            domain=self.domain,
            problem=self.problem,
            heuristic=self.args.heuristic,
            stateVars=encoding.transitionVariables[-1].valueVariables
        )

        pass
