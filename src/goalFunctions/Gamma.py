from typing import Dict

from src.goalFunctions.GoalFunction import GoalFunction
from src.pddl.Atom import Atom
from src.pddl.Domain import GroundedDomain
from src.pddl.Goal import Goal
from src.pddl.Problem import Problem
from src.pddl.State import State
from src.smt.SMTExpression import SMTExpression
from src.smt.SMTVariable import SMTVariable
from src.smt.expressions.ITEExpression import ITEExpression


class Gamma(GoalFunction):

    def __init__(self):
        super().__init__()

    @staticmethod
    def compute(s: State, g: Goal) -> float:
        pass

    @staticmethod
    def getFormula(vars: Dict[Atom, SMTVariable], g: Goal, init: State) -> SMTExpression:
        if not g.isAtomic():
            raise Exception(f"Goal {g} is not atomic")
        return ITEExpression.simplify(SMTExpression.fromFormula(g, vars), 0, 1)
