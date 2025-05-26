from typing import Dict

from src.goalFunctions.DeltaClauses import DeltaClauses
from src.goalFunctions.GoalFunctionClauses import GoalFunctionClauses
from src.pddl.Atom import Atom
from src.pddl.BinaryPredicate import BinaryPredicate
from src.pddl.Formula import Formula
from src.pddl.Goal import Goal
from src.pddl.State import State
from src.smt.SMTExpression import SMTExpression
from src.smt.SMTVariable import SMTVariable
from src.smt.expressions.ConstantExpression import ConstantExpression


class DeltaPlusClauses(GoalFunctionClauses):

    def __init__(self):
        super().__init__()

    @staticmethod
    def compute(s: State, g: Goal, init: State) -> float:
        if g.type == "OR":
            raise Exception("This goal function works only when goals are clauses")
        addends = [DeltaClauses.compute(s, phi, init) for phi in g.conditions if
                   isinstance(phi, BinaryPredicate)]
        if addends:
            return sum(addends)
        return 0

    @staticmethod
    def getExpression(vars: Dict[Atom, SMTVariable], g: Formula, init: State) -> SMTExpression:
        if g.type == "OR":
            raise Exception("This goal function works only when goals are clauses")
        addends = [DeltaClauses.getExpression(vars, phi, init) for phi in g.conditions if
                   isinstance(phi, BinaryPredicate)]
        if addends:
            return sum(addends)
        return ConstantExpression(0)
