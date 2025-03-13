from typing import Dict

from src.goalFunctions.Gamma import Gamma
from src.goalFunctions.GoalFunction import GoalFunction
from src.pddl.Atom import Atom
from src.pddl.Formula import Formula
from src.pddl.Goal import Goal
from src.pddl.State import State
from src.smt.SMTExpression import SMTExpression
from src.smt.SMTVariable import SMTVariable
from src.smt.expressions.MaxExpression import MaxExpression
from src.smt.expressions.MinExpression import MinExpression


class GammaMax(GoalFunction):

    def __init__(self):
        super().__init__()

    @staticmethod
    def computeFromFormula(s: State, f: Formula):
        if f.isAtomic():
            return Gamma.compute(s, f)
        gammas = [GammaMax.computeFromFormula(s, phi) for phi in f.conditions]
        if f.type == "OR":
            return min(*gammas)
        if f.type == "AND":
            return max(*gammas)

    @staticmethod
    def compute(s: State, g: Goal) -> float:
        if g.type == "OR" or g.isAtomic():
            return GammaMax.computeFromFormula(s, g)
        gammas = [GammaMax.computeFromFormula(s, phi) for phi in g.conditions]
        return max(*gammas)

    @staticmethod
    def getExpressionForFormula(vars: Dict[Atom, SMTVariable], f: Formula, init: State):
        if f.isAtomic():
            return Gamma.getExpression(vars, f, init)
        gammas = [GammaMax.getExpressionForFormula(vars, phi, init) for phi in f.conditions]
        if f.type == "OR":
            return MinExpression(*gammas)
        if f.type == "AND":
            return MaxExpression(*gammas)

    @staticmethod
    def getExpression(vars: Dict[Atom, SMTVariable], g: Formula, init: State) -> SMTExpression:
        if g.type == "OR" or g.isAtomic():
            return GammaMax.getExpressionForFormula(vars, g, init)
        gammas = [GammaMax.getExpressionForFormula(vars, phi, init) for phi in g.conditions]
        return MaxExpression(*gammas)
