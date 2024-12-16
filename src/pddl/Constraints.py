from __future__ import annotations

import copy
from typing import Dict, List

from src.pddl.Exists import Exists
from src.pddl.Forall import Forall
from src.pddl.Formula import Formula
from src.pddl.Problem import Problem
from src.pddl.Quantifier import Quantifier
from src.pddl.Type import Type
from src.pddl.grammar.pddlParser import pddlParser


class Constraints:
    constraints: List[Quantifier]

    def __init__(self):
        self.constraints = []
        pass

    def __deepcopy__(self, m):
        c = Constraints()
        c.constraints = copy.deepcopy(self.constraints, m)
        return c

    @classmethod
    def fromNode(cls, node: pddlParser.ConstraintsContext, types: Dict[str, Type]):
        c = cls()
        for child in node.children:
            if isinstance(child, pddlParser.ForallContext):
                c.constraints.append(Forall.fromNode(child, types))
            if isinstance(child, pddlParser.ExistsContext):
                c.constraints.append(Exists.fromNode(child, types))
        return c

    def ground(self, problem: Problem) -> Formula:
        f = Formula()
        f.type = "AND"
        f.conditions = [c.eliminate(problem) for c in self.constraints]
        return f
