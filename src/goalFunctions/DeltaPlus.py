from typing import Dict

from src.goalFunctions.Delta import Delta
from src.goalFunctions.Gamma import Gamma
from src.goalFunctions.GoalFunction import GoalFunction, EPSILON
from src.pddl.Atom import Atom
from src.pddl.Formula import Formula
from src.pddl.Goal import Goal
from src.pddl.State import State
from src.smt.SMTExpression import SMTExpression
from src.smt.SMTVariable import SMTVariable
from src.smt.expressions.ITEExpression import ITEExpression
from src.smt.expressions.MaxExpression import MaxExpression
from src.smt.expressions.MinExpression import MinExpression


class DeltaPlus(GoalFunction):

    def __init__(self):
        super().__init__()

    @staticmethod
    def computeFromFormula(s: State, f: Formula):
        if f.isAtomic():
            return Gamma.compute(s, f)
        deltas = [DeltaPlus.computeFromFormula(s, phi) for phi in f.conditions]
        if f.type == "OR":
            return min(*deltas)
        if f.type == "AND":
            n = len(deltas)
            return 1 / n * sum(deltas)

    @staticmethod
    def compute(s: State, g: Goal) -> float:
        # G = len(g) if g.type == "AND" else 1
        groups = [g]
        if g.type == "AND" and not g.isAtomic():
            groups = g.conditions

        deltas = [DeltaPlus.computeFromFormula(s, group) for group in groups]
        return 0 if s.satisfies(g) else max(EPSILON, sum(*deltas))

    @staticmethod
    def getExpressionForFormula(vars: Dict[Atom, SMTVariable], f: Formula, init: State):
        if f.isAtomic():
            return Delta.getExpression(vars, f, init)
        deltas = [DeltaPlus.getExpressionForFormula(vars, phi, init) for phi in f.conditions]
        if f.type == "OR":
            return MinExpression(*deltas)
        if f.type == "AND":
            n = len(deltas)
            return 1 / n * sum(deltas)

    @staticmethod
    def getExpression(vars: Dict[Atom, SMTVariable], g: Formula, init: State) -> SMTExpression:
        # G = len(g) if g.type == "AND" else 1
        groups = [g]
        if g.type == "AND" and not g.isAtomic():
            groups = g.conditions

        deltas = [DeltaPlus.getExpressionForFormula(vars, g, init) for g in groups]
        gf = SMTExpression.fromFormula(g, vars)
        return ITEExpression(gf, 0, MaxExpression(EPSILON, sum(*deltas)))
