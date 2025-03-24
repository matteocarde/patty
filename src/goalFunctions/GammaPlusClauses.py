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
from src.smt.expressions.ITEExpression import ITEExpression
from src.smt.expressions.MaxExpression import MaxExpression
from src.smt.expressions.MinExpression import MinExpression


class GammaPlusClauses(GoalFunction):

    def __init__(self):
        super().__init__()

    @staticmethod
    def compute(s: State, g: Goal, init: State) -> float:
        if g.type == "OR":
            raise Exception("This goal function works only when goals are clauses")
        gammas = [0 if s.satisfies(phi) else 1 for phi in g.conditions]
        return sum(gammas)

    @staticmethod
    def getExpression(vars: Dict[Atom, SMTVariable], g: Formula, init: State) -> SMTExpression:
        if g.type == "OR":
            raise Exception("This goal function works only when goals are clauses")

        addends = []
        for phi in g.conditions:
            expr = SMTExpression.fromFormula(phi, vars)
            addends.append(ITEExpression(expr, 0, 1))

        return sum(addends)
