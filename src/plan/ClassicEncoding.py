import statistics
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
from src.sat.CNF import CNF
from src.sat.CNFVariable import CNFVariable
from src.sat.SATSolution import SATSolution
from src.smt.SMTExpression import SMTExpression
from src.smt.SMTSolution import SMTSolution
from src.utils.Arguments import Arguments


class ClassicEncoding(Encoding):
    domain: GroundedDomain
    problem: Problem
    cnf: CNF

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

        self.cnf = CNF()
        self.addInitialExpression(self.cnf)
        self.addSequenceRules(self.cnf)
        self.addPreRules(self.cnf)
        self.addGoalExpression(self.cnf)

        pass

    def addInitialExpression(self, cnf: CNF):
        X = self.vars.currentState

        seenAtoms: Set[Atom] = set()
        for (v, value) in self.state:

            if v not in X:
                continue

            seenAtoms.add(v)
            if value:
                cnf.addClause([X[v]])
            else:
                cnf.addClause([~X[v]])

        for v in self.domain.predicates - seenAtoms:
            cnf.addClause([~X[v]])

    def addGoalExpression(self, cnf: CNF):

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

        for p in getCNFVars(P):
            cnf.addClause([p])
        cnf.addClause(getCNFVars(GmP))

    def addSequenceRules(self, cnf: CNF):
        current = self.vars.currentState
        for v in self.domain.predicates:

            x = self.vars.cnfPosVars[v]
            m = self.vars.m[v]
            # Positive
            cnf.addClause([~current[v], x[-1]])
            cnf.addClause([current[v], ~x[-1]])
            for j in range(m):
                A_jx = self.vars.addSequence[v][j]
                D_jx = self.vars.deleteSequence[v][j]
                cnf.addClause([~x[j], x[j - 1]] + list(A_jx))
                for d in D_jx:
                    cnf.addClause([~x[j], ~d])

            # Negative
            del x
            x_ = self.vars.cnfNegVars[v]
            cnf.addClause([current[v], x_[-1]])
            cnf.addClause([~current[v], ~x_[-1]])
            for j in range(m):
                A_jx = self.vars.addSequence[v][j]
                D_jx = self.vars.deleteSequence[v][j]
                cnf.addClause([~x_[j], x_[j - 1]] + list(D_jx))
                for a in A_jx:
                    cnf.addClause([~x_[j], ~a] + list(D_jx))

    def addPreRules(self, cnf: CNF) -> List[SMTExpression]:
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
                    cnf.addClause([~a_i, x[m - 2]] + list(A_xmi))
                    for d in D_xmi:
                        cnf.addClause([~a_i, ~d])

                else:
                    raise ("To be implemented")
                    cnf.addClause([~a_i, x_[m - 2]] + list(D_xmi))
                    # for a in A_xmi:
                    #     rules.append(~a_i | ~a | SMTExpression.bigor(D_xmi))

        return rules

    def getNVars(self):
        return CNFVariable.CNF_ID - 1

    def getNRules(self):
        return len(self.cnf.clauses)

    def getAvgRuleLength(self):
        return round(statistics.mean([len(c) for c in self.cnf.clauses]), 2)

    def getPlanFromSolution(self, solution: SATSolution or bool) -> NumericPlan:
        plan = NumericPlan()

        if not solution:
            return plan

        plan.actionRolling = dict()

        for i, a in self.pattern.enumerate():
            if solution.getVariable(self.vars.action[a]):
                plan.addAction(a)

        return plan
