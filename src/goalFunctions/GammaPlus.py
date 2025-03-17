from typing import Dict

from src.goalFunctions.Gamma import Gamma
from src.goalFunctions.GoalFunction import GoalFunction
from src.pddl.Atom import Atom
from src.pddl.Domain import GroundedDomain
from src.pddl.Formula import Formula
from src.pddl.Goal import Goal
from src.pddl.Problem import Problem
from src.pddl.State import State
from src.smt.SMTExpression import SMTExpression
from src.smt.SMTVariable import SMTVariable
from src.smt.expressions.MaxExpression import MaxExpression
from src.smt.expressions.MinExpression import MinExpression


class GammaPlus(GoalFunction):

    def __init__(self):
        super().__init__()

    @staticmethod
    def computeFromFormula(s: State, f: Formula, init: State):
        if f.isAtomic():
            return Gamma.compute(s, f, init)
        gammas = [GammaPlus.computeFromFormula(s, phi, init) for phi in f.conditions]
        if f.type == "OR":
            return min(*gammas)
        if f.type == "AND":
            n = len(gammas)
            return 1 / n * sum(gammas)

    @staticmethod
    def compute(s: State, g: Goal, init: State) -> float:
        if g.type == "OR" or g.isAtomic():
            return GammaPlus.computeFromFormula(s, g, init)
        gammas = [GammaPlus.computeFromFormula(s, phi, init) for phi in g.conditions]
        return sum(gammas)

    @staticmethod
    def getExpressionForFormula(vars: Dict[Atom, SMTVariable], f: Formula, init: State):
        if f.isAtomic():
            return Gamma.getExpression(vars, f, init)
        gammas = [GammaPlus.getExpressionForFormula(vars, phi, init) for phi in f.conditions]
        if f.type == "OR":
            return MinExpression(*gammas)
        if f.type == "AND":
            n = len(gammas)
            return 1 / n * sum(gammas)

    @staticmethod
    def getExpression(vars: Dict[Atom, SMTVariable], g: Formula, init: State) -> SMTExpression:
        if g.isAtomic() or g.type == "OR":
            return GammaPlus.getExpressionForFormula(vars, g, init)
        gammas = [GammaPlus.getExpressionForFormula(vars, phi, init) for phi in g.conditions]
        return sum(gammas)
