from typing import Dict, List, Tuple

from src.goalFunctions.GoalFunction import GoalFunction, EPSILON
from src.pddl.Atom import Atom
from src.pddl.BinaryPredicate import BinaryPredicate
from src.pddl.Domain import GroundedDomain
from src.pddl.Formula import Formula
from src.pddl.Goal import Goal
from src.pddl.Literal import Literal
from src.pddl.Predicate import Predicate
from src.pddl.Problem import Problem
from src.pddl.State import State
from src.smt.SMTExpression import SMTExpression
from src.smt.SMTVariable import SMTVariable
from src.smt.expressions.ITEExpression import ITEExpression
from src.smt.expressions.MinExpression import MinExpression


class DeltaClauses(GoalFunction):

    def __init__(self):
        super().__init__()

    @staticmethod
    def compute(s: State, g: Formula, init: State) -> float:
        if s.satisfies(g):
            return 0

        groups = [g] if g.isAtomic() else g.conditions

        toMinimize: List[Tuple[float, float]] = []
        for phi in groups:
            if isinstance(phi, BinaryPredicate):
                initValue = init.getValue(phi.lhs - phi.rhs)
                if initValue != 0:
                    toMinimize.append((s.getValue(phi), initValue))

        return min([sPhi / iPhi + EPSILON for (sPhi, iPhi) in toMinimize] + [1])

    @staticmethod
    def getExpression(vars: Dict[Atom, SMTVariable], g: Formula, init: State) -> SMTExpression:

        groups = [g] if g.isAtomic() else g.conditions

        toMinimize: List[Tuple[SMTExpression, float]] = []
        for phi in groups:
            if not isinstance(g, BinaryPredicate):
                continue
            initValue = init.getValue(phi.lhs - phi.rhs)
            if initValue >= 0:
                continue
            phiExpr = SMTExpression.fromFormula(phi, vars)
            toMinimize.append((phiExpr, initValue))

        minExpr = min([phi / iPhi + EPSILON for (phi, iPhi) in toMinimize] + [1])
        gExpr = SMTExpression.fromFormula(g, vars)
        return ITEExpression(gExpr, 0, minExpr)
