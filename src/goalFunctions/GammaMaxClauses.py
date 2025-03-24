from typing import Dict

from src.goalFunctions.Delta import Delta
from src.goalFunctions.Gamma import Gamma
from src.goalFunctions.GoalFunction import GoalFunction, EPSILON
from src.goalFunctions.GoalFunctionClauses import GoalFunctionClauses
from src.pddl.Atom import Atom
from src.pddl.Formula import Formula
from src.pddl.Goal import Goal
from src.pddl.State import State
from src.smt.SMTExpression import SMTExpression
from src.smt.SMTVariable import SMTVariable
from src.smt.expressions.ITEExpression import ITEExpression
from src.smt.expressions.MaxExpression import MaxExpression
from src.smt.expressions.MinExpression import MinExpression


class GammaMaxClauses(GoalFunctionClauses):

    def __init__(self):
        super().__init__()

    @staticmethod
    def compute(s: State, g: Goal, init: State) -> float:
        return 0 if s.satisfies(g) else 1

    @staticmethod
    def getExpression(vars: Dict[Atom, SMTVariable], g: Formula, init: State) -> SMTExpression:
        if g.type == "OR":
            raise Exception("This goal function works only when goals are clauses")

        gf = SMTExpression.fromFormula(g, vars)
        return ITEExpression(gf, 0, 1)
