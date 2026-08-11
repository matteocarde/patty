import itertools
import statistics
from typing import List, Set, Tuple

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
from src.sat.Invariants import Invariants
from src.sat.SATSolution import SATSolution
from src.utils.Arguments import Arguments
from src.utils.TimeStat import TimeStat


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
                 invariants: Invariants = None):

        super().__init__(domain, problem, pattern, 1)
        self.domain = domain
        self.problem = problem

        self.subgoalsAchieved = subgoalsAchieved
        self.initState = State.fromInitialCondition(self.problem.init)
        self.state = state if state else self.initState
        self.phases = []

        self.pattern = pattern

        self.k = len(self.pattern)
        self.vars: ClassicEncodingVariables = ClassicEncodingVariables(self.domain, self.pattern)

        self.cnf = CNF()
        self.addInitialExpression(self.cnf)
        self.addSequenceRules(self.cnf)
        self.addPreRules(self.cnf)
        self.addGoalExpression(self.cnf)
        t = TimeStat.startHolder("Adding Invariants to Goal")
        self.addInvariantsInGoal(self.cnf, invariants)
        t.endHolderMilliseconds()
        # t = TimeStat.startHolder("Adding Invariants to Sequence")
        # self.addInvariantsInSequence(self.cnf, invariants)
        # t.endHolderMilliseconds()

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
        GmPvars = getCNFVars(GmP)
        self.phases = [v.id for v in GmPvars]
        cnf.addClause(GmPvars)

    def addInvariantsInGoal(self, cnf: CNF, invariants: Invariants or None):
        if not invariants:
            return

        left: Literal
        right: Literal

        def getXm(l):
            v = l.atom
            m = self.vars.m[v]
            x = self.vars.cnfPosVars[v]
            x_ = self.vars.cnfNegVars[v]
            if l.sign == "+":
                return x[m - 1]
            if l.sign == "-":
                return x_[m - 1]

        for (left, right) in invariants:
            c = [getXm(left), getXm(right)]
            cnf.addClause(c)

    def addInvariantsInSequence(self, cnf: CNF, invariants: Invariants or None):
        if not invariants:
            return

        self.invStats = {
            "POSPOS": 0,
            "POSNEG": 0,
            "NEGNEG": 0
        }

        for i, a in self.pattern.enumerate():

            if i == len(self.pattern):
                continue

            invs: Set[Tuple[Literal, Literal]] = set()
            for l in a.effects:
                assert isinstance(l, Literal)
                v = l.atom
                invs |= invariants.getInvariantsConcerningAtom(v)

            left: Literal
            right: Literal
            for (left, right) in invs:
                if left.sign == "+" and right.sign == "+":
                    self.__addInvariantsInSequencePosPos(cnf, i, left, right)
                if left.sign == "+" and right.sign == "-":
                    self.__addInvariantsInSequencePosNeg(cnf, i, left, right)
                if left.sign == "-" and right.sign == "+":
                    self.__addInvariantsInSequencePosNeg(cnf, i, right, left)
                if left.sign == "-" and right.sign == "-":
                    self.__addInvariantsInSequenceNegNeg(cnf, i, left, right)

        print(self.invStats)

    def __addInvariantsInSequencePosPos(self, cnf: CNF, i: int, left: Literal, right: Literal):

        self.invStats["POSPOS"] += 1
        mx = self.vars.getPI2SI(left.atom, i)
        my = self.vars.getPI2SI(right.atom, i)
        x = self.vars.cnfPosVars[left.atom][mx - 2]
        y = self.vars.cnfPosVars[right.atom][my - 2]

        A_xmi = self.vars.getBoolActionsBeforeIndex(self.vars.addSequence[left.atom][mx - 1], i)
        D_xmi = self.vars.getBoolActionsBeforeIndex(self.vars.deleteSequence[left.atom][mx - 1], i)
        A_ymi = self.vars.getBoolActionsBeforeIndex(self.vars.addSequence[right.atom][my - 1], i)
        D_ymi = self.vars.getBoolActionsBeforeIndex(self.vars.deleteSequence[right.atom][my - 1], i)

        cnf.addClause([x, y] + A_xmi + A_ymi)
        for dy in D_ymi:
            cnf.addClause([x, ~dy] + A_xmi)
        for dx in D_xmi:
            cnf.addClause([y, ~dx] + A_ymi)
        for (dx, dy) in itertools.product(D_xmi, D_ymi):
            cnf.addClause([~dx, ~dy])

        pass

    def __addInvariantsInSequencePosNeg(self, cnf: CNF, i: int, left: Literal, right: Literal):

        self.invStats["POSNEG"] += 1
        mx = self.vars.getPI2SI(left.atom, i)
        my = self.vars.getPI2SI(right.atom, i)
        x = self.vars.cnfPosVars[left.atom][mx - 2]
        y_ = self.vars.cnfNegVars[right.atom][my - 2]

        A_xmi = self.vars.getBoolActionsBeforeIndex(self.vars.addSequence[left.atom][mx - 1], i)
        D_xmi = self.vars.getBoolActionsBeforeIndex(self.vars.deleteSequence[left.atom][mx - 1], i)
        D_ymi = self.vars.getBoolActionsBeforeIndex(self.vars.deleteSequence[right.atom][my - 1], i)

        cnf.addClause([x, y_] + A_xmi + D_xmi)
        for dx in D_xmi:
            cnf.addClause([y_, ~dx] + D_ymi)

        pass

    def __addInvariantsInSequenceNegNeg(self, cnf: CNF, i: int, left: Literal, right: Literal):

        self.invStats["NEGNEG"] += 1
        mx = self.vars.getPI2SI(left.atom, i)
        my = self.vars.getPI2SI(right.atom, i)
        x_ = self.vars.cnfNegVars[left.atom][mx - 2]
        y_ = self.vars.cnfNegVars[right.atom][my - 2]

        D_xmi = self.vars.getBoolActionsBeforeIndex(self.vars.deleteSequence[left.atom][mx - 1], i)
        D_ymi = self.vars.getBoolActionsBeforeIndex(self.vars.deleteSequence[right.atom][my - 1], i)

        cnf.addClause([x_, y_] + D_xmi + D_ymi)

        pass

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
                cnf.addClause([~x[j], x[j - 1], *A_jx])
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
                cnf.addClause([~x_[j], x_[j - 1], *D_jx])
                for a in A_jx:
                    cnf.addClause([~x_[j], ~a, *D_jx])

    def addPreRules(self, cnf: CNF):
        actions = self.vars.action

        for i, action in self.pattern.enumerate():
            a_i = actions[action]
            neg_a_i = ~a_i

            for pre in action.preconditions:
                if isinstance(pre, TruePredicate):
                    continue
                v = pre.atom
                m = self.vars.getPI2SI(v, i)
                x = self.vars.cnfPosVars[v]
                # x_ = self.vars.cnfNegVars[v]

                A_xmi = self.vars.getBoolActionsBeforeIndex(self.vars.addSequence[v][m - 1], i)
                D_xmi = self.vars.getBoolActionsBeforeIndex(self.vars.deleteSequence[v][m - 1], i)

                if pre.sign == "+":
                    cnf.addClause([neg_a_i, x[m - 2], *A_xmi])
                    for d in D_xmi:
                        cnf.addClause([neg_a_i, ~d])

                else:
                    raise Exception("To be implemented")
                    cnf.addClause([neg_a_i, x_[m - 2]] + list(D_xmi))
                    # for a in A_xmi:
                    #     rules.append(~a_i | ~a | SMTExpression.bigor(D_xmi))

    def getNVars(self):
        return CNFVariable.CNF_ID - 1

    def getNRules(self):
        return len(self.cnf.clauses)

    def getAvgRuleLength(self):
        return round(statistics.fmean(len(c) for c in self.cnf.clauses), 2)

    def getPlanFromSolution(self, solution: SATSolution or bool) -> NumericPlan:
        plan = NumericPlan()

        if not solution:
            return plan

        plan.actionRolling = dict()

        for i, a in self.pattern.enumerate():
            if solution.getVariable(self.vars.action[a]):
                plan.addAction(a)

        return plan
