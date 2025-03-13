from typing import Dict

from src.pddl.Atom import Atom
from src.pddl.Domain import GroundedDomain
from src.pddl.Formula import Formula
from src.pddl.Goal import Goal
from src.pddl.Problem import Problem
from src.pddl.State import State
from src.smt.SMTExpression import SMTExpression
from src.smt.SMTVariable import SMTVariable

EPSILON = 0.01


class GoalFunction:

    def __init__(self):
        pass

    @staticmethod
    def compute(s: State, g: Formula) -> float:
        raise NotImplementedError()

    @staticmethod
    def getExpression(vars: Dict[Atom, SMTVariable], f: Formula, I: State) -> SMTExpression:
        raise NotImplementedError()
