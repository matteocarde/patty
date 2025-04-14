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
from src.pddl.RelaxedIntervalState import RelaxedIntervalState
from src.pddl.State import State
from src.smt.SMTExpression import SMTExpression
from src.smt.SMTVariable import SMTVariable
from src.smt.expressions.ITEExpression import ITEExpression
from src.smt.expressions.MinExpression import MinExpression


class Delta(GoalFunction):

    def __init__(self):
        super().__init__()

    @staticmethod
    def compute(s: State or RelaxedIntervalState, g: Formula, init: State) -> float:
        if not g.isAtomic():
            raise Exception(f"Goal {g} is not atomic")
        g = g if isinstance(g, Predicate) else g.conditions[0]
        phi = g.lhs - g.rhs if isinstance(g, BinaryPredicate) else g
        initValue = init.getValue(phi)
        if isinstance(g, Literal) or (isinstance(g, BinaryPredicate) and initValue >= 0):
            return 0 if s.satisfies(g) else 1
        elif isinstance(g, BinaryPredicate):
            psi = s.getValue(g.lhs - g.rhs)
            return 0 if s.satisfies(g) else psi / initValue
        raise Exception("Here shold not go")

    @staticmethod
    def getExpression(vars: Dict[Atom, SMTVariable], g: Formula, init: State) -> SMTExpression:
        if not g.isAtomic():
            raise Exception(f"Goal {g} is not atomic")
        g = g if isinstance(g, Predicate) else g.conditions[0]
        phi = g.lhs - g.rhs if isinstance(g, BinaryPredicate) else g
        initValue = init.getValue(phi)
        gf = SMTExpression.fromFormula(g, vars)
        if isinstance(g, Literal) or (isinstance(g, BinaryPredicate) and initValue >= 0):
            return ITEExpression(gf, 0, 1)
        elif isinstance(g, BinaryPredicate):
            psi = SMTExpression.fromPddl(g.lhs - g.rhs, vars)
            return ITEExpression(gf, 0, MinExpression(1, psi / initValue))
