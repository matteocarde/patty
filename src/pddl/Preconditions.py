from __future__ import annotations

from typing import Dict, cast

from src.pddl.Formula import Formula
from src.pddl.grammar.pddlParser import pddlParser


class Preconditions(Formula):

    def __init__(self):
        super().__init__()

    @classmethod
    def fromNode(cls, node: pddlParser.PreconditionsContext) -> Preconditions:
        return cast(Preconditions, super().fromNode(node))

    def ground(self, sub: Dict[str, str]) -> Preconditions:
        return super().ground(sub)
