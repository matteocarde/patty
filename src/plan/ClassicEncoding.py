from typing import List, Set

from src.pddl.Atom import Atom
from src.pddl.Domain import GroundedDomain
from src.pddl.Literal import Literal
from src.pddl.NumericPlan import NumericPlan
from src.pddl.Problem import Problem
from src.pddl.State import State
from src.pddl.TruePredicate import TruePredicate
from src.plan.ClassicEncodingVariables import ClassicEncodingVariables
from src.plan.Encoding import Encoding
from src.plan.Pattern import Pattern
from src.smt.SMTExpression import SMTExpression
from src.smt.SMTSolution import SMTSolution
from src.utils.Arguments import Arguments


class ClassicEncoding(Encoding):
    domain: GroundedDomain
    problem: Problem

    def __init__(self, domain: GroundedDomain,
                 problem: Problem,
                 pattern: Pattern,
                 args: Arguments,
                 subgoalsAchieved=None,
                 state: State = None,
                 goalAsSoftAsserts=False):

        super().__init__(domain, problem, pattern, 1)
        self.domain = domain
        self.problem = problem

        self.subgoalsAchieved = subgoalsAchieved
        self.goalAsSoftAsserts = goalAsSoftAsserts
        self.initState = State.fromInitialCondition(self.problem.init)
        self.state = state if state else self.initState

        self.pattern = pattern

        self.k = len(self.pattern)
        self.vars: ClassicEncodingVariables = ClassicEncodingVariables(self.domain, self.pattern)

        self.rules = []
        self.rules += self.getInitialExpression()
        self.rules += self.getPreRules()
        self.rules += self.getGoalExpression()

        pass

    def getInitialExpression(self) -> List[SMTExpression]:
        X = self.vars.currentState
        rules: [SMTExpression] = []

        seenAtoms: Set[Atom] = set()
        for (v, value) in self.state:

            if v not in X:
                continue

            seenAtoms.add(v)
            if value:
                rules.append(X[v])
            else:
                rules.append(~X[v])

        for v in self.domain.predicates - seenAtoms:
            rules.append(~X[v])

        return rules

    def getGoalExpression(self) -> [SMTExpression]:
        sigmas = self.vars.sigma[self.k]
        if self.goalAsSoftAsserts:
            P = [g for g in self.problem.goal if g in self.subgoalsAchieved]
            GmP = [g for g in self.problem.goal if g not in self.subgoalsAchieved]
            andGoal = [SMTExpression.fromFormula(g, sigmas) for g in P]
            orGoal = [SMTExpression.fromFormula(g, sigmas) for g in GmP]
            return [SMTExpression.bigand(andGoal), SMTExpression.bigor(orGoal)]

        return [SMTExpression.fromFormula(self.problem.goal, sigmas)]

    def getPreRules(self) -> List[SMTExpression]:
        rules: List[SMTExpression] = []
        actions = self.vars.action

        for i, a in self.pattern.enumerate():

            sigma = self.vars.sigma[i - 1]

            if a.preconditions.type == "OR":
                raise Exception("Cannot deal with disjunctive preconditions")

            for pre in a.preconditions:
                if isinstance(pre, TruePredicate):
                    continue
                if not isinstance(pre, Literal):
                    raise Exception("Cannot deal with preconditions not being literals")
                v = pre.getAtom()
                sigma_v = sigma[v] if pre.sign == "+" else ~sigma[v]
                rules.append(actions[i].implies(sigma_v))

        return rules

    def getPlanFromSolution(self, solution: SMTSolution, relaxed=False) -> NumericPlan:
        plan = NumericPlan()
        plan.solution = solution

        if not solution:
            return plan

        plan.actionRolling = dict()

        for i, a in self.pattern.enumerate():
            if solution.getVariable(self.vars.action[i]):
                plan.addAction(a)

        return plan
