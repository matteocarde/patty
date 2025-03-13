from typing import Dict

from src.goalFunctions.Gamma import Gamma
from src.goalFunctions.GammaMax import GammaMax
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


class GammaGoalCount(GoalFunction):

    def __init__(self):
        super().__init__()

    @staticmethod
    def compute(s: State, g: Goal) -> float:
        if g.type == "OR" or g.isAtomic():
            return GammaMax.computeFromFormula(s, g)
        gammas = [GammaMax.computeFromFormula(s, phi) for phi in g.conditions]
        return sum(*gammas)

    @staticmethod
    def getExpression(vars: Dict[Atom, SMTVariable], g: Formula, init: State) -> SMTExpression:
        if g.type == "OR" or g.isAtomic():
            return GammaMax.getExpressionForFormula(vars, g, init)
        gammas = [GammaMax.getExpressionForFormula(vars, phi, init) for phi in g.conditions]
        return sum(*gammas)
