from typing import Dict

from src.goalFunctions.Gamma import Gamma
from src.goalFunctions.GammaMax import GammaMax
from src.goalFunctions.GammaPlusClauses import GammaPlusClauses
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


class GammaGoalCountClauses(GoalFunction):

    def __init__(self):
        super().__init__()

    @staticmethod
    def compute(s: State, g: Goal, init: State) -> float:
        return GammaPlusClauses.compute(s, g, init)

    @staticmethod
    def getExpression(vars: Dict[Atom, SMTVariable], g: Formula, init: State) -> SMTExpression:
        return GammaPlusClauses.getExpression(vars, g, init)
