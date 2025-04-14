from typing import Dict

from src.goalFunctions.DeltaClauses import DeltaClauses
from src.goalFunctions.GoalFunctionClauses import GoalFunctionClauses
from src.pddl.Atom import Atom
from src.pddl.Formula import Formula
from src.pddl.Goal import Goal
from src.pddl.State import State
from src.smt.SMTExpression import SMTExpression
from src.smt.SMTVariable import SMTVariable


class DeltaXORClauses(GoalFunctionClauses):

    def __init__(self):
        super().__init__()

    @staticmethod
    def compute(s: State, g: Goal, init: State) -> float:
        if g.type == "OR":
            raise Exception("This goal function works only when goals are clauses")

        G = len(g)
        groups = [g]
        if g.type == "AND" and not g.isAtomic():
            groups = g.conditions

        addends = []
        deltas = []
        for subgoal in groups:
            delta = DeltaClauses.compute(s, subgoal, init)
            deltas.append(delta)
            expr = (G - 1 + delta) / G
            addends.append(expr)
        return sum(addends)

    @staticmethod
    def getExpression(vars: Dict[Atom, SMTVariable], g: Formula, init: State) -> SMTExpression:
        if g.type == "OR":
            raise Exception("This goal function works only when goals are clauses")

        G = len(g)
        groups = [g]
        if g.type == "AND" and not g.isAtomic():
            groups = g.conditions

        addends = []
        for subgoal in groups:
            delta = DeltaClauses.getExpression(vars, subgoal, init)
            expr = (G - 1 + delta) / G
            addends.append(expr)
        return sum(addends)
