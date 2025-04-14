from typing import Dict

from src.goalFunctions.DeltaPlus import DeltaPlus
from src.goalFunctions.GoalFunction import GoalFunction
from src.pddl.Atom import Atom
from src.pddl.Formula import Formula
from src.pddl.Goal import Goal
from src.pddl.State import State
from src.smt.SMTExpression import SMTExpression
from src.smt.SMTVariable import SMTVariable
from src.smt.expressions.ITEExpression import ITEExpression
from src.smt.expressions.MaxExpression import MaxExpression
from src.utils.Constants import EPSILON


class DeltaXOR(GoalFunction):

    def __init__(self):
        super().__init__()

    @staticmethod
    def compute(s: State, g: Goal, init: State) -> float:
        G = len(g) if g.type == "AND" else 1
        groups = [g]
        if g.type == "AND" and not g.isAtomic():
            groups = g.conditions

        addends = []
        for subgoal in groups:
            deltaPlus = DeltaPlus.compute(s, subgoal, init)
            expr = 0 if s.satisfies(subgoal) else (G - 1 + deltaPlus) / G
            addends.append(expr)
        return 0 if s.satisfies(g) else max(EPSILON, sum(addends))

    @staticmethod
    def getExpression(vars: Dict[Atom, SMTVariable], g: Formula, init: State) -> SMTExpression:
        G = len(g) if g.type == "AND" else 1
        groups = [g]
        if g.type == "AND" and not g.isAtomic():
            groups = g.conditions

        gf = SMTExpression.fromFormula(g, vars)
        addends = []
        for subgoal in groups:
            deltaPlus = DeltaPlus.getExpression(vars, subgoal, init)
            e = (G - 1 + deltaPlus) / G
            expr = ITEExpression(SMTExpression.fromFormula(subgoal, vars), 0, e)
            addends.append(expr)
        return ITEExpression(gf, 0, MaxExpression(EPSILON, sum(addends)))
