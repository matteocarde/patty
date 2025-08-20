from typing import Dict

from src.goalFunctions.DeltaClauses import DeltaClauses
from src.goalFunctions.GoalFunctionClauses import GoalFunctionClauses, EPSILON
from src.pddl.Atom import Atom
from src.pddl.BinaryPredicate import BinaryPredicate
from src.pddl.Formula import Formula
from src.pddl.Goal import Goal
from src.pddl.State import State
from src.smt.SMTExpression import SMTExpression
from src.smt.SMTVariable import SMTVariable
from src.smt.expressions.ConstantExpression import ConstantExpression


class DeltaSingle(GoalFunctionClauses):

    def __init__(self):
        super().__init__()

    @staticmethod
    def compute(s: State, g: Goal, init: State) -> float:
        if g.type == "OR":
            raise Exception("This goal function works only when goals are clauses")
        if not g.hasOnlyOneNumericConditions():
            return 0
        phiPredicate: BinaryPredicate = g.conditions[0]
        iPhi = init.getValue(phiPredicate.lhs - phiPredicate.rhs)
        if iPhi >= 0:
            return ConstantExpression(0)
        phi = s.getValue(phiPredicate.lhs - phiPredicate.rhs)
        return phi / iPhi + EPSILON

    @staticmethod
    def getExpression(vars: Dict[Atom, SMTExpression], g: Formula, init: State) -> SMTExpression:
        if g.type == "OR":
            raise Exception("This goal function works only when goals are clauses")
        if not g.hasOnlyOneNumericConditions():
            return ConstantExpression(0)
        phiPredicate: BinaryPredicate = g.conditions[0]
        iPhi = init.getValue(phiPredicate.lhs - phiPredicate.rhs)
        if iPhi >= 0:
            return ConstantExpression(0)
        phi = SMTExpression.fromFormula(phiPredicate.lhs - phiPredicate.rhs, vars)
        return phi / iPhi + EPSILON
