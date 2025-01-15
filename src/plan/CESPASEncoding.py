from typing import Dict, Set

from src.ces.ActionStateTransitionFunction import ActionStateTransitionFunction
from src.ces.TransitionFunctionBDD import TransitionFunctionBDD
from src.pddl.Action import Action
from src.pddl.Atom import Atom
from src.pddl.Domain import Domain, GroundedDomain
from src.pddl.Literal import Literal
from src.pddl.NumericPlan import NumericPlan
from src.pddl.Problem import Problem
from src.pddl.State import State
from src.plan.Encoding import Encoding
from src.plan.PASTransitionVariables import PASTransitionVariables
from src.plan.TransitionRelations import TransitionRelations
from src.smt.SMTConjunction import SMTConjunction
from src.smt.SMTExpression import SMTExpression
from src.smt.SMTRulesTree import SMTRulesTree
from src.smt.SMTSolution import SMTSolution


class CESPASEncoding(Encoding):

    def __init__(self, liftedDomain: Domain, problem: Problem, domain: GroundedDomain, bound: int,
                 transitionRelations: TransitionRelations):
        super().__init__(domain, problem)
        self.domain: GroundedDomain = domain
        self.problem: Problem = problem
        self.liftedDomain: Domain = liftedDomain
        self.atoms = self.domain.predicates
        self.actions = self.domain.actions
        self.bound: int = bound
        self.relations: TransitionRelations = transitionRelations

        self.vars = PASTransitionVariables(self.domain, self.problem, self.bound)

        self.rulesByName = SMTRulesTree()

        self.rulesByName.append("init", 0, self.getInitRules())
        for i in range(0, self.bound):
            self.rulesByName.append("closure", i, self.getClosureRules(i))
            self.rulesByName.append("constraints", i, self.getConstraintRules(i))
            self.rulesByName.append("pre", i, self.getPreRules(i))
            self.rulesByName.append("eff", i, self.getEffRules(i))
            self.rulesByName.append("conflict", i, self.getConflictRules(i))
            self.rulesByName.append("frame", i, self.getFrameRules(i))
            self.rulesByName.append("amo", i, self.getAmoRules(i))
        self.rulesByName.append("goal", self.bound, self.getGoalRules())

        self.rules = self.rulesByName.getConjunction()

        # print("--- Rules ---")
        # self.rulesByName.print()
        #
        # exit()

        pass

    def getInitRules(self) -> SMTConjunction:

        rules: SMTConjunction = SMTConjunction()
        X0 = self.vars.stateVariables[0]

        trueAtoms: Set[Atom] = set()
        for l in self.problem.init:
            if not isinstance(l, Literal):
                raise Exception("In CESEncoding I cannot deal with numbers")
            v = l.getAtom()
            rules.append(X0[v])
            trueAtoms.add(v)

        for v in self.atoms - trueAtoms:
            rules.append(~X0[v])

        return rules

    def getConstraintRules(self, i: int) -> SMTConjunction:
        rules = SMTConjunction()
        X = self.vars.stateVariables

        rules.append(SMTExpression.fromFormula(self.domain.constraints, X[i]))
        rules.append(SMTExpression.fromFormula(self.domain.constraints, X[i + 1]))

        return rules

    def getClosureRules(self, i: int) -> SMTConjunction:
        rules = SMTConjunction()
        X = self.vars.stateVariables
        A = self.vars.actionVariables[i + 1]

        for a in self.actions:
            if a.isIdempotent():
                continue
            T_a: TransitionFunctionBDD = self.relations.closures[a][-1]
            groundExpr: SMTExpression = T_a.toGroundSMTExpression(a, self.domain, X[i], X[i + 1])
            rules.append(A[a].implies(groundExpr))

        return rules

    def getPreRules(self, i: int) -> SMTConjunction:
        rules = SMTConjunction()
        X = self.vars.stateVariables
        A = self.vars.actionVariables[i + 1]

        for a in self.actions:
            if a.isNonIdempotent():
                continue
            pre = ActionStateTransitionFunction.getPreconditionClauses(a, X[i], X[i + 1])
            print("PRE", a, A[a], SMTExpression.bigand(pre))
            rules.append(A[a].implies(SMTExpression.bigand(pre)))

        return rules

    def getEffRules(self, i: int) -> SMTConjunction:
        rules = SMTConjunction()
        X = self.vars.stateVariables
        A = self.vars.actionVariables[i + 1]

        for a in self.actions:
            if a.isNonIdempotent():
                continue
            eff = ActionStateTransitionFunction.getEffectClauses(a, X[i], X[i + 1])
            rules.append(A[a].implies(SMTExpression.bigand(eff)))

        return rules

    def getConflictRules(self, i: int) -> SMTConjunction:
        rules = SMTConjunction()
        X = self.vars.stateVariables
        A = self.vars.actionVariables[i + 1]

        for a in self.actions:
            if a.isNonIdempotent():
                continue
            conflict = ActionStateTransitionFunction.getConflictClauses(a, X[i], X[i + 1])
            rules.append(A[a].implies(SMTExpression.bigand(conflict)))

        return rules

    def getFrameRules(self, i: int) -> SMTConjunction:
        rules = SMTConjunction()
        X = self.vars.stateVariables
        A = self.vars.actionVariables[i + 1]

        for v in self.atoms:
            lhs = list()
            for a in self.actions:
                if v in a.addedAtoms or v in a.deletedAtoms:
                    lhs.append(~A[a])
            rules.append(SMTExpression.bigand(lhs).implies(X[i + 1][v].equal(X[i][v])))

        return rules

    def getAmoRules(self, i: int) -> SMTConjunction:
        rules = SMTConjunction()
        A = self.vars.actionVariables[i + 1]

        for a1 in self.actions:
            for a2 in self.actions:
                if a1 == a2:
                    continue
                rules.append(~(A[a1] & A[a2]))

        return rules

    def getGoalRules(self) -> SMTConjunction:
        rules = SMTConjunction()
        X = self.vars.stateVariables
        n = self.bound
        goal = SMTExpression.fromFormula(self.problem.goal, X[n])
        rules.append(goal)
        return rules

    def getState(self, exprs: Dict[Atom, SMTExpression], solution: SMTSolution) -> State:
        s = State()
        for v in self.atoms:
            s.setAtom(v, exprs[v].evaluate(solution))
        return s

    def repetitions(self, a: Action, s0: State, s2: State, m: int) -> int:
        for j in range(0, m + 1):
            T_a = self.relations.closures[a][j]
            if not T_a.reachable(a, s0, s2):
                continue

            if j == 0:
                return 1
            R_a = self.relations.reachability[a][j - 1]
            s1: State = R_a.jumpState(a, s0)
            return 2 ** (j - 1) + self.repetitions(a, s1, s2, j - 1)
        return 0

    def getRepetitions(self, a: Action, i: int, solution: SMTSolution):
        s0: State = self.getState(self.vars.stateVariables[i], solution)
        s2: State = self.getState(self.vars.stateVariables[i + 1], solution)
        m = len(self.relations.closures[a])
        return self.repetitions(a, s0, s2, m)

    def getPlanFromSolution(self, solution: SMTSolution) -> NumericPlan:
        plan = NumericPlan()

        if not solution:
            return plan

        for i in range(1, self.bound + 1):
            for a in self.actions:
                isExecuted = solution.getVariable(self.vars.actionVariables[i][a])
                if isExecuted:
                    r = self.getRepetitions(a, i - 1, solution) if a.isNonIdempotent() else 1
                    plan.addRepeatedAction(a, r)

        return plan
