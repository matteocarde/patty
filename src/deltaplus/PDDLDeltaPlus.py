import copy

from src.deltaplus.DeltaKnowledge import DeltaKnowledge
from src.pddl.Domain import Domain
from src.pddl.Predicate import Predicate
from src.pddl.Problem import Problem


class PDDLDeltaPlus:

    def __init__(self, domain: Domain, problem: Problem):
        self.domain: Domain = domain
        self.problem: Problem = problem

    def transformDomain(self, deltak: DeltaKnowledge) -> Domain:
        domain = copy.deepcopy(self.domain)

        # 1
        for v in deltak.variables:
            domain.predicates.add(Predicate.fromString(v))


        return domain

    def transformProblem(self, deltak: DeltaKnowledge) -> Problem:
        pass
