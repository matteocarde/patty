from __future__ import annotations

import copy
from typing import Dict, List

from src.pddl.Exists import Exists
from src.pddl.Forall import Forall
from src.pddl.Formula import Formula
from src.pddl.Predicate import Predicate
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

    def ground(self, problem: Problem) -> Formula or Predicate:
        from src.pddl.TruePredicate import TruePredicate
        from src.pddl.FalsePredicate import FalsePredicate
        f: Formula = Formula()
        f.type = "AND"
        for c in self.constraints:
            subF = c.eliminate(problem)
            if isinstance(subF, TruePredicate):
                continue
            if isinstance(subF, FalsePredicate):
                return FalsePredicate()
            f.conditions.append(subF)
        return f.simplify()
