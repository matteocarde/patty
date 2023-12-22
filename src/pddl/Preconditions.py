from __future__ import annotations

import copy

from typing import Dict, cast, Tuple

from src.pddl.Formula import Formula
from src.pddl.PDDLWriter import PDDLWriter
from src.pddl.grammar.pddlParser import pddlParser


class Preconditions(Formula):

    def __init__(self):
        super().__init__()

    def __deepcopy__(self, m=None):
        m = {} if m is None else m
        p = copy.deepcopy(super(), m)
        p.__class__ = Preconditions
        return cast(Preconditions, p)

    @classmethod
    def fromNode(cls, node: pddlParser.PreconditionsContext or pddlParser.OpDurativeConditionContext) -> Preconditions:
        p = super().fromNode(node)
        p.__class__ = Preconditions
        return cast(Preconditions, p)

    def ground(self, sub: Dict[str, str], delta=1) -> Preconditions:
        f = super().ground(sub, delta)
        f.__class__ = Preconditions
        return f

    def addPrecondition(self, param):
        self.addClause(param)

    def toPDDL(self, pw: PDDLWriter = PDDLWriter()):
        # pw.write(f":precondition ")
        # pw.increaseTab()
        super().toPDDL(pw)
        # pw.decreaseTab()



