from typing import List, Dict, Set

from src.goalFunctions.DeltaSingle import DeltaSingle
from src.pddl.Atom import Atom
from src.pddl.BinaryPredicate import BinaryPredicate
from src.pddl.Constant import Constant
from src.pddl.Domain import GroundedDomain
from src.pddl.Literal import Literal
from src.pddl.NumericPlan import NumericPlan
from src.pddl.Problem import Problem
from src.pddl.State import State
from src.plan.Encoding import Encoding
from src.plan.NumericTransitionVariables import NumericTransitionVariables
from src.plan.Pattern import Pattern
from src.smt.SMTExpression import SMTExpression
from src.smt.SMTNumericVariable import SMTNumericVariable, SMTRealVariable, SMTIntVariable
from src.smt.SMTSolution import SMTSolution
from src.smt.expressions.FalseExpression import FalseExpression
from src.utils.Arguments import Arguments
from src.utils.Constants import EPSILON

# BOUND = 1000
EXPLICIT_DELTA = False


class NumericEncoding(Encoding):
    domain: GroundedDomain
    problem: Problem

    def __init__(self, domain: GroundedDomain, problem: Problem, pattern: Pattern, bound: int,
                 args: Arguments,
                 subgoalsAchieved=None,
                 state: State = None,
                 minimizeGoalFunction=False,
                 goalAsSoftAsserts=False,
                 goalFunctionValue: float = 10000,
                 skipGoal: bool = False,
                 booleanActions: bool = False):

        super().__init__(domain, problem, pattern, bound)
        self.domain = domain
        self.problem = problem
        self.bound = bound

        self.subgoalsAchieved = subgoalsAchieved
        self.rollBound = args.rollBound
        self.binaryActions: int = args.binaryActions
        self.hasEffectAxioms = args.hasEffectAxioms
        self.goalFunction = DeltaSingle
        self.goalFunctionValue = goalFunctionValue
        self.minimizeGoalFunction = minimizeGoalFunction
        self.goalAsSoftAsserts = goalAsSoftAsserts
        self.initState = State.fromInitialCondition(self.problem.init)
        self.state = state if state else self.initState
        self.booleanActions = booleanActions

        self.transitionVariables: [NumericTransitionVariables] = list()

        self.transitions: [SMTExpression] = []

        self.pattern = pattern

        for index in range(0, bound + 1):
            var = NumericTransitionVariables(self.domain.predicates,
                                             self.domain.functions,
                                             self.domain.assList,
                                             self.pattern,
                                             index,
                                             self.hasEffectAxioms,
                                             booleanActions=self.booleanActions)
            self.transitionVariables.append(var)
            if index > 0:
                self.actionVariables.update(var.actionVariables.values())
        self.k = len(self.pattern)

        self.softRules: [SMTExpression] = []
        self.minimize: [SMTExpression] = []
        self.initial: [SMTExpression] = self.getInitialExpression()

        for index in range(1, bound + 1):
            stepRules = self.getStepRules(index)
            self.transitions.extend(stepRules)

        self.c = SMTRealVariable("costFunctionPatty")

        self.rules = []
        self.rules += self.initial
        self.rules += self.transitions
        if not skipGoal:
            self.rules += self.getGoalExpression()
        # self.rules += self.getMinimizeParameter()

        if self.minimizeGoalFunction:
            self.addGoalFunctionMinimization()

        if self.goalAsSoftAsserts:
            self.addGoalAsSoftRules()

        pass

    def getInitialExpression(self) -> List[SMTExpression]:
        tVars = self.transitionVariables[0]
        rules: [SMTExpression] = []

        seenAtoms: Set[Atom] = set()
        for (v, value) in self.state:

            if v not in tVars.valueVariables:
                continue

            if type(value) is bool:
                seenAtoms.add(v)
                if value:
                    rules.append(tVars.valueVariables[v])
                else:
                    rules.append(~tVars.valueVariables[v])
            else:
                rules.append(tVars.valueVariables[v].equal(value))

        for v in self.domain.predicates - seenAtoms:
            rules.append(~tVars.valueVariables[v])

        return rules

    def getGoalFunctionExpression(self):
        vars = self.transitionVariables[-1].sigmaVariables[self.k]
        init = State.fromInitialCondition(self.problem.init)
        expr = self.goalFunction.getExpression(vars, self.problem.goal.normalize(), init)
        return expr

    def getFullGoalExpressions(self):
        v = self.transitionVariables[-1].sigmaVariables[self.k]
        return [SMTExpression.fromFormula(g, v) for g in self.problem.goal]

    def getGoalExpression(self) -> [SMTExpression]:
        v = self.transitionVariables[-1].sigmaVariables[self.k]
        if self.goalAsSoftAsserts:
            c = self.goalFunctionValue
            expr: SMTExpression = self.c < max(c - EPSILON, 0) if self.minimizeGoalFunction else FalseExpression()
            P = [g for g in self.problem.goal if g in self.subgoalsAchieved]
            GmP = [g for g in self.problem.goal if g not in self.subgoalsAchieved]
            andGoal = [SMTExpression.fromFormula(g, v) for g in P]
            orGoal = [SMTExpression.fromFormula(g, v) for g in GmP] + [expr]
            return [SMTExpression.bigand(andGoal), SMTExpression.bigor(orGoal)]

        return [SMTExpression.fromFormula(self.problem.goal, v)]

    def getMinimizeParameter(self):
        if self.goalFunction:
            expr = self.getGoalFunctionExpression()
            assignment = self.c.equal(expr)
            return [assignment]
        return []

    def addGoalAsSoftRules(self):
        # vars = self.transitionVariables[-1].sigmaVariables[self.k
        v = self.transitionVariables[-1].sigmaVariables[self.k]

        for g in self.problem.goal:
            if g not in self.subgoalsAchieved:
                self.softRules.append(SMTExpression.fromPddl(g, v))

        pass

    def addGoalFunctionMinimization(self):
        self.minimize.append(self.getGoalFunctionExpression())
        pass

    def assignOrGetRule(self, stepVars, i, v, rhs, rules):
        if not self.hasEffectAxioms:
            stepVars.sigmaVariables[i][v] = rhs
        else:
            rules.append(stepVars.sigmaVariables[i][v].equal(rhs))

    def getDeltaStepRules(self, prevVars: NumericTransitionVariables, stepVars: NumericTransitionVariables) \
            -> List[SMTExpression]:

        rules: List[SMTExpression] = []

        for v in self.domain.allAtoms:
            self.assignOrGetRule(stepVars, 0, v, prevVars.valueVariables[v], rules)

        for i, action in self.pattern.enumerate():

            # Case a) Not influenced
            notInfluenced = self.domain.allAtoms - (action.getInfluencedAtoms())
            for v in notInfluenced:
                self.assignOrGetRule(stepVars, i, v, stepVars.sigmaVariables[i - 1][v], rules)

            # Case b) Boolean
            for v in action.getAddList() | action.getDelList():
                d_bv = stepVars.sigmaVariables[i - 1][v]
                b_n = stepVars.actionVariables[i]

                if v in action.getAddList():
                    self.assignOrGetRule(stepVars, i, v, (d_bv | (b_n > 0)), rules)

                if v in action.getDelList():
                    self.assignOrGetRule(stepVars, i, v, (d_bv & (b_n.equal(0))), rules)

            # Case c) Numeric increases or decreases
            modifications = [(+1, action.getIncreases()), (-1, action.getDecreases())]
            for sign, modificationDict in modifications:
                for v, funct in modificationDict.items():
                    d_bv = stepVars.sigmaVariables[i - 1][v]
                    k = SMTNumericVariable.fromPddl(funct, stepVars.sigmaVariables[i - 1])
                    b_n = stepVars.actionVariables[i]
                    rhs = (d_bv + (k * b_n)) if sign > 0 else (d_bv - (k * b_n))
                    self.assignOrGetRule(stepVars, i, v, rhs, rules)

            # Case d) Numeric assignments
            for v in action.getAssList():
                self.assignOrGetRule(stepVars, i, v, stepVars.auxVariables[i][v], rules)

        return rules

    def getAmoStepRules(self, stepVars: NumericTransitionVariables, n: int) -> List[SMTExpression]:
        rules: List[SMTExpression] = []

        if self.booleanActions:
            return rules

        for i, a in self.pattern.enumerate():
            a_n = stepVars.actionVariables[i]
            rules.append(a_n >= 0)
            if not a.couldBeRepeated():
                rules.append(a_n <= 1)
                continue
            if self.rollBound:
                rules.append(a_n <= self.rollBound)
                continue

        if len(self.domain.arpg.stateLevels) > 2:
            for (atom, interval) in self.domain.arpg.stateLevels[-1].intervals.items():
                if atom not in stepVars.valueVariables:
                    continue
                if interval.lb != float("-inf"):
                    rules.append(stepVars.valueVariables[atom] >= interval.lb)
                if interval.ub != float("+inf"):
                    rules.append(stepVars.valueVariables[atom] <= interval.ub)

        return rules

    def getPreStepRules(self, stepVars: NumericTransitionVariables) -> List[SMTExpression]:
        rules: List[SMTExpression] = []

        for i, a in self.pattern.enumerate():

            lhs0 = stepVars.actionVariables[i] > 0
            lhs1 = stepVars.actionVariables[i] > 1
            preconditions0 = None
            preconditions1 = None
            isPre1Impossible = False
            for pre in a.preconditions:
                if isinstance(pre, Literal):
                    v = pre.getAtom()
                    d_av = stepVars.sigmaVariables[i - 1][v]
                    rhs = d_av if pre.sign == "+" else ~d_av
                    preconditions0 = preconditions0 & rhs if preconditions0 else rhs
                    preconditions1 = preconditions1 & rhs if preconditions1 else rhs
                    continue

                precondition0 = SMTNumericVariable.fromPddl(pre, stepVars.sigmaVariables[i - 1])
                preconditions0 = preconditions0 & precondition0 if preconditions0 else precondition0

                subs: Dict[Atom, SMTExpression] = dict()
                # Searching for decrease effects
                for eff in a.effects:
                    if not isinstance(eff, BinaryPredicate):
                        continue
                    v = eff.lhs.getAtom()
                    rhsExpr = SMTNumericVariable.fromPddl(eff.rhs, stepVars.sigmaVariables[i - 1])
                    if eff.operator == "assign":
                        subs[v] = rhsExpr
                        continue
                    if eff.operator == "increase":
                        subs[v] = stepVars.sigmaVariables[i - 1][v] + rhsExpr * (stepVars.actionVariables[i] - 1)
                        pass
                    else:
                        subs[v] = stepVars.sigmaVariables[i - 1][v] - rhsExpr * (stepVars.actionVariables[i] - 1)

                for v in stepVars.sigmaVariables[i - 1].keys():
                    subs[v] = subs[v] if v in subs else stepVars.sigmaVariables[i - 1][v]

                # Transformed precondition
                precondition1 = SMTNumericVariable.fromPddl(pre, subs)
                if not precondition1:
                    isPre1Impossible = True
                else:
                    preconditions1 = preconditions1 & precondition1 if preconditions1 else precondition1

            if preconditions0:
                rules.append(lhs0.implies(preconditions0))

            if a.couldBeRepeated():
                if preconditions1 and not isPre1Impossible:
                    rules.append(lhs1.implies(preconditions1))

                if isPre1Impossible:
                    rules.append(~lhs1)

        return rules

    def getEffStepRules(self, stepVars: NumericTransitionVariables) -> List[SMTExpression]:
        rules: List[SMTExpression] = []

        for i, a in self.pattern.enumerate():
            for var, rhs in a.getAssignments().items():
                v_a = stepVars.auxVariables[i][var]
                a_n = stepVars.actionVariables[i]
                d_a_v = stepVars.sigmaVariables[i - 1][var]
                d_psi = rhs.value if isinstance(rhs, Constant) else \
                    SMTNumericVariable.fromPddl(rhs, stepVars.sigmaVariables[i - 1])

                rules.append((a_n > 0).implies(v_a.equal(d_psi)))
                rules.append((a_n.equal(0)).implies(v_a.equal(d_a_v)))

        return rules

    def getFrameStepRules(self, stepVars: NumericTransitionVariables) -> List[SMTExpression]:
        rules: List[SMTExpression] = []

        for v in sorted(self.domain.functions):
            v_first = stepVars.valueVariables[v]
            delta_g_v = stepVars.sigmaVariables[self.k][v]
            rules.append(v_first.equal(delta_g_v))

        for v in sorted(self.domain.predicates):
            v_first = stepVars.valueVariables[v]
            delta_g_v = stepVars.sigmaVariables[self.k][v]
            rules.append(v_first.equal(delta_g_v))

        return rules

    def getStepRules(self, index: int) -> List[SMTExpression]:
        prevVars = self.transitionVariables[index - 1]
        stepVars = self.transitionVariables[index]

        rules: List[SMTExpression] = []
        rules += self.getDeltaStepRules(prevVars, stepVars)
        rules += self.getAmoStepRules(stepVars, index)
        rules += self.getPreStepRules(stepVars)
        rules += self.getEffStepRules(stepVars)
        rules += self.getFrameStepRules(stepVars)

        return rules

    def getPlanFromSolution(self, solution: SMTSolution, relaxed=False) -> NumericPlan:
        plan = NumericPlan()
        plan.solution = solution

        if not solution:
            return plan

        plan.actionRolling = dict()

        for n in range(1, self.bound + 1):
            plan.actionRolling.setdefault(n, dict())
            stepVar = self.transitionVariables[n]
            for i, a in self.pattern.enumerate():
                if isinstance(stepVar.actionVariables[i], SMTIntVariable):
                    repetitions = int(str(solution.getVariable(stepVar.actionVariables[i]))) * a.linearizationTimes
                else:
                    repetitions = 1 if solution.getVariable(stepVar.actionVariables[i]) else 0
                plan.actionRolling[n][a] = repetitions
                if repetitions > 0:
                    plan.addRepeatedAction(a.linearizationOf, repetitions)

        return plan
