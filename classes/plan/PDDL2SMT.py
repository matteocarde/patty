from typing import Dict, Tuple, List

from Action import Action
from Atom import Atom
from BinaryPredicate import BinaryPredicate
from Domain import GroundedDomain
from Literal import Literal
from Problem import Problem
from classes.plan.ActionOrder import ActionOrder
from classes.plan.TransitionVariables import TransitionVariables
from classes.smt.SMTExpression import SMTExpression
from classes.smt.SMTNumericVariable import SMTNumericVariable
from classes.smt.SMTVariable import SMTVariable


class PDDL2SMT:
    domain: GroundedDomain
    problem: Problem

    def __init__(self, domain: GroundedDomain, problem: Problem, horizon: int):
        self.domain = domain
        self.problem = problem
        self.horizon = horizon

        self.transitionVariables: [TransitionVariables] = list()

        self.initial: [SMTExpression] = self.getInitialExpression()
        self.goal: [SMTExpression] = self.getGoalExpression()
        self.order = ActionOrder(self.domain, self.problem)

        self.transitions: [SMTExpression] = []

        for index in range(0, horizon + 1):
            var = TransitionVariables(self.domain, self.problem, index)
            self.transitionVariables.append(var)

        for index in range(1, horizon + 1):
            stepRules = self.getStepRules(self.transitionVariables[index])
            self.transitions.extend(stepRules)

    def getInitialExpression(self) -> List[SMTExpression]:
        tVars = self.transitionVariables[0]
        rules: [SMTExpression] = list()

        for assignment in self.problem.init:
            if isinstance(assignment, BinaryPredicate):
                rules.append(tVars.valueVariables[assignment.getAtom()] == float(str(assignment.rhs)))
            elif isinstance(assignment, Literal):
                rules.append(tVars.valueVariables[assignment.getAtom()] == 1)
            else:
                raise NotImplemented("Shouldn't go here")

        return rules

    def getGoalExpression(self) -> [SMTExpression]:
        tVars = self.transitionVariables[-1]
        rules: [SMTExpression] = list()

        for condition in self.problem.goal:
            if isinstance(condition, BinaryPredicate):
                expr = SMTExpression.fromPddl(condition, tVars.valueVariables)
                rules.append(expr)
            elif isinstance(condition, Literal):
                if condition.sign == "+":
                    rules.append(tVars.valueVariables[condition.getAtom()] > 0)
                else:
                    rules.append(tVars.valueVariables[condition.getAtom()] < 0)
            else:
                raise NotImplemented("Shouldn't go here")

        return rules

    def getDeltaStepRules(self, tVars: TransitionVariables) -> List[SMTExpression]:
        exprs: List[SMTExpression] = []

        prevAction: Action or None = None
        for action in self.order:
            if not prevAction:
                prevAction = action
                continue



            prevAction = action

        return exprs

    def getActStepRules(self, tVars: TransitionVariables) -> List[SMTExpression]:
        exprs: List[SMTExpression] = []

        return exprs

    def getPreStepRules(self, tVars: TransitionVariables) -> List[SMTExpression]:
        exprs: List[SMTExpression] = []

        return exprs

    def getEffStepRules(self, tVars: TransitionVariables) -> List[SMTExpression]:
        exprs: List[SMTExpression] = []

        return exprs

    def getFrameStepRules(self, tVars: TransitionVariables) -> List[SMTExpression]:
        exprs: List[SMTExpression] = []

        return exprs

    def getStepRules(self, tVars: TransitionVariables) -> List[SMTExpression]:
        exprs: List[SMTExpression] = []

        exprs.extend(self.getDeltaStepRules(tVars))
        exprs.extend(self.getActStepRules(tVars))
        exprs.extend(self.getPreStepRules(tVars))
        exprs.extend(self.getEffStepRules(tVars))
        exprs.extend(self.getFrameStepRules(tVars))

        return exprs
