import copy
from typing import Set

from src.pddl.BinaryPredicate import BinaryPredicate
from src.pddl.Domain import GroundedDomain
from src.pddl.Goal import Goal
from src.pddl.InitialCondition import InitialCondition
from src.pddl.NumericPlan import NumericPlan
from src.pddl.Problem import Problem
from src.pddl.State import State
from src.search.Search import Search
from src.utils.Arguments import Arguments


class ChrpaImprover(Search):
    satPlan: NumericPlan

    def __init__(self, domain: GroundedDomain, problem: Problem, args: Arguments,
                 satPlan: NumericPlan):
        super().__init__(domain, problem, args)
        self.satPlan = satPlan

    @staticmethod
    def improve(plan: NumericPlan, problem: Problem, P: State = None):
        hatPlan = NumericPlan()
        n = len(plan)

        s = State.fromInitialCondition(problem.init)
        for action in plan:
            hatAction = copy.deepcopy(action)
            for bp in action.getNormalizedNumericAssignments():
                hatAction.preconditions.addClause(BinaryPredicate.equality(bp, s.getValue(bp)))
            s = s.applyAction(action)
            hatPlan.addAction(hatAction)

        removed: Set[int] = set()

        s = State.fromInitialCondition(problem.init)
        for i in range(n):
            a_i = plan[i]

            marks: Set[int] = set()

            if i in removed:
                continue

            marks.add(i)
            s_: State = copy.deepcopy(s)

            for j in range(i + 1, n):
                aHat_j = hatPlan[j]
                if j in removed:
                    continue
                if s_.satisfiesPreconditions(aHat_j):
                    s_ = s_.applyAction(aHat_j)
                else:
                    marks.add(j)

            if not P and s_.satisfies(problem.goal):
                removed = removed | marks
            elif P and s_ == P:
                removed = removed | marks
            else:
                s = s.applyAction(a_i)

        improvedPlan = NumericPlan()
        for i in range(0, n):
            if i in removed:
                continue
            improvedPlan.addAction(plan[i])

        return improvedPlan

    def solve(self) -> NumericPlan or None:
        return ChrpaImprover.improve(self.satPlan, self.problem)
