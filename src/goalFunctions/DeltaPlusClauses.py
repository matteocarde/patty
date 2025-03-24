from typing import Dict

from src.goalFunctions.Delta import Delta
from src.goalFunctions.DeltaClauses import DeltaClauses
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


class DeltaPlusClauses(GoalFunction):

    def __init__(self):
        super().__init__()

    @staticmethod
    def compute(s: State, g: Goal, init: State) -> float:
        if g.type == "OR":
            raise Exception("This goal function works only when goals are clauses")

        groups = [g]
        if not g.isAtomic():
            groups = g.conditions

        addends = [DeltaClauses.compute(s, g, init) for g in groups]
        return sum(addends)

    @staticmethod
    def getExpression(vars: Dict[Atom, SMTVariable], g: Formula, init: State) -> SMTExpression:
        if g.type == "OR":
            raise Exception("This goal function works only when goals are clauses")

        groups = [g]
        if not g.isAtomic():
            groups = g.conditions

        addends = [DeltaClauses.getExpression(vars, g, init) for g in groups]
        return sum(addends)
