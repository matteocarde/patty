from typing import Dict, Set

from src.ces.TransitionFunctionBDD import TransitionFunctionBDD
from src.pddl.Atom import Atom
from src.pddl.Domain import Domain, GroundedDomain
from src.pddl.Literal import Literal
from src.pddl.Problem import Problem
from src.plan.CESTransitionVariables import CESTransitionVariables
from src.plan.Encoding import Encoding
from src.plan.Pattern import Pattern
from src.plan.TransitionRelations import TransitionRelations
from src.smt.SMTConjunction import SMTConjunction
from src.smt.SMTExpression import SMTExpression
from src.smt.SMTSolution import SMTSolution


class CESEncoding(Encoding):

    def __init__(self, liftedDomain: Domain, problem: Problem, domain: GroundedDomain, pattern: Pattern, bound: int,
                 transitionRelations: TransitionRelations):
        super().__init__(domain, problem, pattern, bound)
        self.domain: GroundedDomain = domain
        self.problem: Problem = problem
        self.liftedDomain: Domain = liftedDomain
        self.pattern: Pattern = pattern
        self.k = len(pattern)
        self.atoms = self.domain.predicates
        self.bound: int = bound
        self.relations: TransitionRelations = transitionRelations

        self.vars = CESTransitionVariables(self.domain, self.pattern, self.relations)

        self.rulesByName: Dict[str, SMTConjunction] = dict()
        self.rulesByName["init"] = self.getInitRules()
        self.rulesByName["pre"] = self.getPreRules()
        self.rulesByName["closure"] = self.getClosureRules()
        self.rulesByName["frame"] = self.getFrameRules()
        self.rulesByName["goal"] = self.getGoalRules()

        self.rules = SMTConjunction()
        for conj in self.rulesByName.values():
            self.rules += conj

    def getInitRules(self) -> SMTConjunction:

        rules: SMTConjunction = SMTConjunction()

        trueAtoms: Set[Atom] = set()
        for l in self.problem.init:
            if not isinstance(l, Literal):
                raise Exception("In CESEncoding I cannot deal with numbers")
            v = l.getAtom()
            rules.append(self.vars.currentState[v])
            trueAtoms.add(v)

        for v in self.atoms - trueAtoms:
            rules.append(~self.vars.currentState[v])

        return rules

    def getClosureRules(self) -> SMTConjunction:
        rules = SMTConjunction()
        sigmas = self.vars.sigma
        for i, a in self.pattern.enumerate():
            if a.isIdempotent():
                continue
            T_a: TransitionFunctionBDD = self.relations.closures[a.lifted][-3]
            groundExpr: SMTExpression = T_a.toGroundSMTExpression(a, sigmas[i - 1], sigmas[i])
            rules.append(groundExpr)

        return rules

    def getPreRules(self) -> SMTConjunction:
        rules = SMTConjunction()

        sigmas = self.vars.sigma

        for i, a in self.pattern.enumerate():
            if a.isNonIdempotent():
                continue
            a_i = self.vars.actionVariables[i]
            rules.append(a_i.implies(SMTExpression.fromFormula(a.preconditions, sigmas[i - 1])))

        return rules

    def getFrameRules(self) -> SMTConjunction:
        rules = SMTConjunction()

        for v in self.atoms:
            rules.append(self.vars.nextState[v].iff(self.vars.sigma[self.k][v]))

        return rules

    def getGoalRules(self) -> SMTConjunction:
        rules = SMTConjunction()
        goal = SMTExpression.fromFormula(self.problem.goal, self.vars.nextState)
        rules.append(goal)
        return rules

    def getPlanFromSolution(self, solution: SMTSolution):
        print(solution)
