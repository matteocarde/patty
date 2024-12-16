from __future__ import annotations

from typing import Dict, List

from src.pddl.Exists import Exists
from src.pddl.Forall import Forall
from src.pddl.Type import Type
from src.pddl.grammar.pddlParser import pddlParser


class Constraints:
    constraints: List[Forall or Exists]

    def __init__(self):
        self.constraints = []
        pass

    @classmethod
    def fromNode(cls, node: pddlParser.ConstraintsContext, types: Dict[str, Type]):
        c = cls()
        for child in node.children:
            if isinstance(child, pddlParser.ForallContext):
                c.constraints.append(Forall.fromNode(child, types))
            if isinstance(child, pddlParser.ExistsContext):
                c.constraints.append(Exists.fromNode(child, types))
