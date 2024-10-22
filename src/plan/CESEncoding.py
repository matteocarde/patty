from src.pddl.Domain import Domain, GroundedDomain
from src.pddl.Problem import Problem
from src.plan.CESTransitionVariables import CESTransitionVariables
from src.plan.Pattern import Pattern
from src.plan.TransitionRelations import TransitionRelations


class CESEncoding:

    def __init__(self, liftedDomain: Domain, problem: Problem, domain: GroundedDomain, pattern: Pattern,
                 bound: int, transitionRelations: TransitionRelations):
        self.domain: GroundedDomain = domain
        self.problem: Problem = problem
        self.liftedDomain: Domain = liftedDomain
        self.pattern: Pattern = pattern
        self.bound: int = bound
        self.relations: TransitionRelations = transitionRelations

        self.vars = CESTransitionVariables(self.domain, self.pattern, self.relations)

        pass
