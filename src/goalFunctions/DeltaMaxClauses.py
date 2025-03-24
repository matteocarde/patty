from typing import Dict

from src.goalFunctions.DeltaClauses import DeltaClauses
from src.goalFunctions.GammaMaxClauses import GammaMaxClauses
from src.goalFunctions.GoalFunction import GoalFunction
from src.pddl.Atom import Atom
from src.pddl.BinaryPredicate import BinaryPredicate
from src.pddl.Formula import Formula
from src.pddl.Goal import Goal
from src.pddl.Literal import Literal
from src.pddl.State import State
from src.smt.SMTExpression import SMTExpression
from src.smt.SMTVariable import SMTVariable


class DeltaMaxClauses(GoalFunction):

    def __init__(self):
        super().__init__()

    @staticmethod
    def hasNumeric(g: Goal or Formula, init: State):
        if g.isAtomic():
            return False
        hasNumeric = False
        for phi in g.conditions:
            if not isinstance(phi, BinaryPredicate):
                continue
            iValue = init.getValue(phi.lhs - phi.rhs)
            if iValue != 0:
                hasNumeric = True
                break
        return hasNumeric

    @staticmethod
    def compute(s: State, g: Goal, init: State) -> float:
        if not DeltaMaxClauses.hasNumeric(g, init):
            return GammaMaxClauses.compute(s, g, init)
        deltas = [DeltaClauses.compute(s, phi, init) for phi in g.conditions]
        return max(deltas)

    @staticmethod
    def getExpression(vars: Dict[Atom, SMTVariable], g: Formula, init: State) -> SMTExpression:
        if not DeltaMaxClauses.hasNumeric(g, init):
            return GammaMaxClauses.getExpression(vars, g, init)
        deltas = [DeltaClauses.getExpression(vars, phi, init) for phi in g.conditions]
        return max(deltas)
