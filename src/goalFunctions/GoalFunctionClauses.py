from __future__ import annotations
from typing import Dict, Type

from src.pddl.Atom import Atom
from src.pddl.Formula import Formula
from src.pddl.State import State
from src.smt.SMTExpression import SMTExpression
from src.smt.SMTVariable import SMTVariable

EPSILON = 0.01


class GoalFunctionClauses:

    def __init__(self):
        pass

    @staticmethod
    def compute(s: State, g: Formula, init: State) -> float:
        raise NotImplementedError()

    @staticmethod
    def getExpression(vars: Dict[Atom, SMTVariable], f: Formula, I: State) -> SMTExpression:
        raise NotImplementedError()

    @classmethod
    def assertGoalIsRightForm(cls, normalizedGoal: Formula) -> bool:
        if normalizedGoal.isCNF():
            return True
        raise Exception("Goal should be in CNF")
