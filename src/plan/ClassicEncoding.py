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
        self.rules += self.getAddDeleteSequenceVariableRules()
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

        print(rules)

        return rules

    def getGoalExpression(self) -> [SMTExpression]:

        P = [g for g in self.problem.goal if g in self.subgoalsAchieved]
        GmP = [g for g in self.problem.goal if g not in self.subgoalsAchieved]

        def getCNFVars(subgoals: List[Literal]):
            cnfVars = []
            for g in subgoals:
                assert isinstance(g, Literal)
                v = g.atom
                m = self.vars.m[v]
                x = self.vars.cnfPosVars[v]
                x_ = self.vars.cnfNegVars[v]
                if g.sign == "+":
                    cnfVars.append(x[m - 1])
                if g.sign == "-":
                    cnfVars.append(x_[m - 1])
            return cnfVars

        return getCNFVars(P) + [SMTExpression.bigor(getCNFVars(GmP))]

    def getAddDeleteSequenceVariableRules(self) -> List[SMTExpression]:
        rules = []
        current = self.vars.currentState
        for v in self.domain.predicates:

            x = self.vars.cnfPosVars[v]
            m = self.vars.m[v]
            # Positive
            rules.append(~current[v] | x[-1])
            rules.append(current[v] | ~x[-1])
            for j in range(m):
                A_jx = self.vars.addSequence[v][j]
                D_jx = self.vars.deleteSequence[v][j]
                rules.append(~x[j] | x[j - 1] | SMTExpression.bigor(A_jx))
                for d in D_jx:
                    rules.append(~x[j] | ~d)

            # Negative
            del x
            x_ = self.vars.cnfNegVars[v]
            rules.append(current[v] | x_[-1])
            rules.append(~current[v] | ~x_[-1])
            for j in range(m):
                A_jx = self.vars.addSequence[v][j]
                D_jx = self.vars.deleteSequence[v][j]
                bigor = SMTExpression.bigor(D_jx)
                rules.append(~x_[j] | x_[j - 1] | bigor)
                for a in A_jx:
                    rules.append(~x_[j] | ~a | bigor)

        return rules

    def getPreRules(self) -> List[SMTExpression]:
        rules: List[SMTExpression] = []
        actions = self.vars.action

        for i, action in self.pattern.enumerate():
            a_i = actions[action]

            # if i == 25:
            #     rules.append(a_i)

            for pre in action.preconditions:
                if isinstance(pre, TruePredicate):
                    continue
                assert isinstance(pre, Literal)
                v = pre.atom
                m = self.vars.PI2SI[v][i]
                x = self.vars.cnfPosVars[v]
                x_ = self.vars.cnfNegVars[v]

                A_xmi = self.vars.getBoolActionsBeforeIndex(self.vars.addSequence[v][m - 1], i)
                D_xmi = self.vars.getBoolActionsBeforeIndex(self.vars.deleteSequence[v][m - 1], i)

                if pre.sign == "+":
                    rules.append(~a_i | x[m - 2] | SMTExpression.bigor(A_xmi))
                    for d in D_xmi:
                        rules.append(~a_i | ~d)

                else:
                    raise ("To be implemented")
                    rules.append(~a_i | x_[m - 2] | SMTExpression.bigor(D_xmi))
                    # for a in A_xmi:
                    #     rules.append(~a_i | ~a | SMTExpression.bigor(D_xmi))

        return rules

    def getPlanFromSolution(self, solution: SMTSolution, relaxed=False) -> NumericPlan:
        plan = NumericPlan()
        plan.solution = solution

        if not solution:
            return plan

        plan.actionRolling = dict()

        for i, a in self.pattern.enumerate():
            if solution.getVariable(self.vars.action[a]):
                plan.addAction(a)

        return plan
