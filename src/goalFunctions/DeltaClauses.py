from typing import Dict, List, Tuple

from src.goalFunctions.GoalFunction import GoalFunction
from src.goalFunctions.GoalFunctionClauses import GoalFunctionClauses
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
from src.utils.Constants import EPSILON


class DeltaClauses(GoalFunctionClauses):

    def __init__(self):
        super().__init__()

    @staticmethod
    def compute(s: State, g: Formula or Predicate, init: State) -> float:
        if s.satisfies(g):
            return 0

        groups = g.conditions if isinstance(g, Formula) else [g]

        toMinimize: List[Tuple[float, float]] = []
        for phi in groups:
            if not isinstance(phi, BinaryPredicate):
                continue
            initValue = init.getValue(phi.lhs - phi.rhs)
            if initValue >= 0:
                continue
            toMinimize.append((s.getValue(phi.lhs - phi.rhs), initValue))

        v = min([sPhi / iPhi + EPSILON for (sPhi, iPhi) in toMinimize] + [1])
        return v

    @staticmethod
    def getExpression(vars: Dict[Atom, SMTVariable], g: Formula or Predicate, init: State) -> SMTExpression:

        groups = g.conditions if isinstance(g, Formula) else [g]

        toMinimize: List[Tuple[SMTExpression, float]] = []
        for phi in groups:
            if not isinstance(phi, BinaryPredicate):
                continue
            initValue = init.getValue(phi.lhs - phi.rhs)
            if initValue >= 0:
                continue
            phiExpr = SMTExpression.fromFormula(phi.lhs - phi.rhs, vars)
            toMinimize.append((phiExpr, initValue))

        tom = [phi / iPhi + EPSILON for (phi, iPhi) in toMinimize] + [1]
        minExpr = MinExpression(*tom) if len(tom) > 2 else tom[0]
        gExpr = SMTExpression.fromFormula(g, vars)
        return ITEExpression(gExpr, 0, minExpr)

    def getExpressionForSingle(vars: Dict[Atom, SMTVariable], phi: BinaryPredicate, init: State) -> SMTExpression:
        initValue = init.getValue(phi.lhs - phi.rhs)
        phiExpr = SMTExpression.fromFormula(phi.lhs - phi.rhs, vars)
        return phiExpr / initValue + EPSILON
