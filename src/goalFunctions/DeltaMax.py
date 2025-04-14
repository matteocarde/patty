from typing import Dict

from src.goalFunctions.Delta import Delta
from src.goalFunctions.Gamma import Gamma
from src.goalFunctions.GoalFunction import GoalFunction
from src.pddl.Atom import Atom
from src.pddl.Formula import Formula
from src.pddl.Goal import Goal
from src.pddl.State import State
from src.smt.SMTExpression import SMTExpression
from src.smt.SMTVariable import SMTVariable
from src.smt.expressions.ITEExpression import ITEExpression
from src.smt.expressions.MaxExpression import MaxExpression
from src.smt.expressions.MinExpression import MinExpression
from src.utils.Constants import EPSILON


class DeltaMax(GoalFunction):

    def __init__(self):
        super().__init__()

    @staticmethod
    def computeFromFormula(s: State, f: Formula, init: State):
        if f.isAtomic():
            return Delta.compute(s, f, init)
        deltas = [DeltaMax.computeFromFormula(s, phi, init) for phi in f.conditions]
        if f.type == "OR":
            return min(*deltas)
        if f.type == "AND":
            return max(*deltas)

    @staticmethod
    def compute(s: State, g: Goal, init: State) -> float:
        # G = len(g) if g.type == "AND" else 1
        groups = [g]
        if g.type == "AND" and not g.isAtomic():
            groups = g.conditions

        deltas = [DeltaMax.computeFromFormula(s, group, init) for group in groups]
        return 0 if s.satisfies(g) else max(EPSILON, *deltas)

    @staticmethod
    def getExpressionForFormula(vars: Dict[Atom, SMTVariable], f: Formula, init: State):
        if f.isAtomic():
            return Delta.getExpression(vars, f, init)
        deltas = [DeltaMax.getExpressionForFormula(vars, phi, init) for phi in f.conditions]
        if f.type == "OR":
            return MinExpression(*deltas)
        if f.type == "AND":
            return MaxExpression(*deltas)

    @staticmethod
    def getExpression(vars: Dict[Atom, SMTVariable], g: Formula, init: State) -> SMTExpression:
        # G = len(g) if g.type == "AND" else 1
        groups = [g]
        if g.type == "AND" and not g.isAtomic():
            groups = g.conditions

        deltas = [DeltaMax.getExpressionForFormula(vars, g, init) for g in groups]
        gf = SMTExpression.fromFormula(g, vars)
        return ITEExpression(gf, 0, MaxExpression(EPSILON, MaxExpression(*deltas)))
