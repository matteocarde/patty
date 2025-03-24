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
        if not g.isAtomic() or not g.type == "OR":
            raise Exception(f"Goal {g} is not atomic or an OR")

        if s.satisfies(g):
            return 0

        toMinimize: List[Tuple[float, float]] = []
        for phi in g.conditions:
            initValue = init.getValue(phi)
            if isinstance(g, BinaryPredicate) and initValue < 0:
                toMinimize.append((s.getValue(phi), initValue))

        return min([sPhi / iPhi + EPSILON for (sPhi, iPhi) in toMinimize] + [1])

    @staticmethod
    def getExpression(vars: Dict[Atom, SMTVariable], g: Formula, init: State) -> SMTExpression:
        if not g.isAtomic() or not g.type == "OR":
            raise Exception(f"Goal {g} is not atomic or an OR")

        toMinimize: List[Tuple[SMTExpression, float]] = []
        for phi in g.conditions:
            initValue = init.getValue(phi)
            if isinstance(g, BinaryPredicate) and initValue < 0:
                phiExpr = SMTExpression.fromFormula(phi, vars)
                toMinimize.append((phiExpr, initValue))

        minExpr = min([phi / iPhi + EPSILON for (phi, iPhi) in toMinimize] + [1])
        gExpr = SMTExpression.fromFormula(g, vars)
        return ITEExpression(gExpr, 0, minExpr)
