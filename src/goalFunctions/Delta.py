from typing import Dict

from src.goalFunctions.GoalFunction import GoalFunction
from src.pddl.Atom import Atom
from src.pddl.BinaryPredicate import BinaryPredicate
from src.pddl.Domain import GroundedDomain
from src.pddl.Formula import Formula
from src.pddl.Goal import Goal
from src.pddl.Literal import Literal
from src.pddl.Predicate import Predicate
from src.pddl.Problem import Problem
from src.pddl.State import State
from src.smt.SMTExpression import SMTExpression
from src.smt.SMTVariable import SMTVariable
from src.smt.expressions.ITEExpression import ITEExpression
from src.smt.expressions.MinExpression import MinExpression


class Delta(GoalFunction):

    def __init__(self):
        super().__init__()

    @staticmethod
    def compute(s: State, g: Formula) -> float:
        pass

    @staticmethod
    def getFormula(vars: Dict[Atom, SMTVariable], g: Formula, init: State) -> SMTExpression:
        if not g.isAtomic():
            raise Exception(f"Goal {g} is not atomic")
        g = g.conditions[0]
        initValue = init.getRealization(g)
        gf = SMTExpression.fromFormula(g, vars)
        if isinstance(g, Literal) or isinstance(g, BinaryPredicate) and initValue >= 0:
            return ITEExpression(gf, 0, 1)
        elif isinstance(g, BinaryPredicate):
            psi = SMTExpression.fromPddl(g.lhs - g.rhs, vars)
            return ITEExpression(gf, 0, MinExpression(1, psi / initValue))
