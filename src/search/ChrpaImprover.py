import copy
from typing import Set

from src.pddl.BinaryPredicate import BinaryPredicate
from src.pddl.Domain import GroundedDomain
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

    def solve(self) -> NumericPlan or None:

        hatPlan = NumericPlan()
        n = len(self.satPlan)

        s = State.fromInitialCondition(self.problem.init)
        for action in self.satPlan:
            hatAction = copy.deepcopy(action)
            for bp in action.getNormalizedNumericAssignments():
                hatAction.preconditions.addClause(BinaryPredicate.equality(bp, s.getValue(bp)))
            s = s.applyAction(action)
            hatPlan.addAction(action)

        removed: Set[int] = set()

        s = State.fromInitialCondition(self.problem.init)
        for i in range(n):
            a_i = self.satPlan[i]

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

            if s_.satisfies(self.problem.goal):
                removed = removed | marks
            else:
                s = s.applyAction(a_i)

        improvedPlan = NumericPlan()
        for i in range(0, n):
            if i in removed:
                continue
            improvedPlan.addAction(self.satPlan[i])

        return improvedPlan
