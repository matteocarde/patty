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
        if s == "DELTA-MAX":
            return DeltaMax
        if s == "DELTA-PLUS":
            return DeltaPlus
        if s == "DELTA-XOR":
            return DeltaXOR
        if s == "GAMMA-GC":
            return GammaGoalCount
        if s == "GAMMA-MAX":
            return GammaMax
        if s == "GAMMA-PLUS":
            return GammaPlus
        if s == "GAMMA-XOR":
            return GammaXOR
