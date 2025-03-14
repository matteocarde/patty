from __future__ import annotations
from typing import Dict, Type

from src.pddl.Atom import Atom
from src.pddl.Formula import Formula
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

    @staticmethod
    def getGoalFunctionFromString(s: str) -> Type[GoalFunction]:
        from src.goalFunctions.DeltaMax import DeltaMax
        from src.goalFunctions.DeltaPlus import DeltaPlus
        from src.goalFunctions.DeltaXOR import DeltaXOR
        from src.goalFunctions.GammaGoalCount import GammaGoalCount
        from src.goalFunctions.GammaMax import GammaMax
        from src.goalFunctions.GammaPlus import GammaPlus
        from src.goalFunctions.GammaXOR import GammaXOR
        if s == "DELTA_MAX":
            return DeltaMax
        if s == "DELTA_PLUS":
            return DeltaPlus
        if s == "DELTA_XOR":
            return DeltaXOR
        if s == "GAMMA_GC":
            return GammaGoalCount
        if s == "GAMMA_MAX":
            return GammaMax
        if s == "GAMMA_PLUS":
            return GammaPlus
        if s == "GAMMA_XOR":
            return GammaXOR
