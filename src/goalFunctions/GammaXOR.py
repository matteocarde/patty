from typing import Dict

from src.goalFunctions.Gamma import Gamma
from src.goalFunctions.GammaPlus import GammaPlus
from src.goalFunctions.GoalFunction import GoalFunction
from src.pddl.Atom import Atom
from src.pddl.Domain import GroundedDomain
from src.pddl.Formula import Formula
from src.pddl.Goal import Goal
from src.pddl.Problem import Problem
from src.pddl.State import State
from src.smt.SMTExpression import SMTExpression
from src.smt.SMTVariable import SMTVariable
from src.smt.expressions.ITEExpression import ITEExpression
from src.smt.expressions.MaxExpression import MaxExpression
from src.smt.expressions.MinExpression import MinExpression


class GammaXOR(GoalFunction):

    def __init__(self):
        super().__init__()

    @staticmethod
    def compute(s: State, g: Goal) -> float:
        G = len(g) if g.type == "AND" else 1
        groups = [g]
        if g.type == "AND" and not g.isAtomic():
            groups = g.conditions

        addends = []
        for subgoal in groups:
            gammaPlus = GammaPlus.computeFromFormula(s, g)
            e = (G - 1 + gammaPlus) / G
            expr = 0 if s.satisfies(subgoal) else e
            addends.append(expr)

        return sum(addends)

    @staticmethod
    def getExpression(vars: Dict[Atom, SMTVariable], g: Formula, init: State) -> SMTExpression:
        G = len(g) if g.type == "AND" else 1
        groups = [g]
        if g.type == "AND" and not g.isAtomic():
            groups = g.conditions

        addends = []
        for subgoal in groups:
            gammaPlus = GammaPlus.getExpression(vars, subgoal, init)
            e = (G - 1 + gammaPlus) / G
            expr = ITEExpression(SMTExpression.fromFormula(subgoal, vars), 0, e)
            addends.append(expr)

        return sum(addends)
