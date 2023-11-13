from __future__ import annotations

from typing import cast

from src.pddl.Formula import Formula
from src.pddl.PDDLWriter import PDDLWriter
from src.pddl.grammar.pddlParser import pddlParser


class Goal(Formula):

    def __init__(self):
        super().__init__()

    @classmethod
    def fromNode(cls, node: pddlParser.GoalContext) -> Goal:
        return cast(Goal, super().fromNode(node.getChild(2)))

    def toPDDL(self, pw: PDDLWriter = PDDLWriter()):
        pw.write(f":goal ")
        # pw.increaseTab()
        super().toPDDL(pw)
        # pw.decreaseTab()
