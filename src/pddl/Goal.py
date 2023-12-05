from __future__ import annotations

from typing import cast

from src.pddl.PDDLWriter import PDDLWriter
from src.pddl.grammar.pddlParser import pddlParser
from src.pddl.Preconditions import Preconditions


class Goal(Preconditions):

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
