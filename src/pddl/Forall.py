import copy
from typing import Dict

from src.pddl.Formula import Formula
from src.pddl.Parameters import Parameters
from src.pddl.Problem import Problem
from src.pddl.Quantifier import Quantifier
from src.pddl.Type import Type
from src.pddl.grammar.pddlParser import pddlParser


class Forall(Quantifier):
    parameters: Parameters
    formula: Formula

    def __init__(self):
        super().__init__()

    def __deepcopy__(self, memodict=None):
        fa = Forall()
        fa.parameters = copy.deepcopy(self.parameters, memodict)
        fa.formula = copy.deepcopy(self.formula, memodict)
        return fa

    @classmethod
    def fromNode(cls, node: pddlParser.ForallContext, types: Dict[str, Type]):
        forall = cls()
        forall.parameters = Parameters.fromNode(node.getChild(2), types)
        forall.formula = Formula.fromNode(node.getChild(3))
        return forall

    def eliminate(self, problem: Problem) -> Formula:
        subs = self.parameters.getAllSubstitutions(problem)
        f = Formula()
        f.type = "AND"
        for sub in subs:
            if self.formula.canHappenLifted(tuple(sub.values()), list(sub.keys()), problem):
                f.addClause(self.formula.ground(sub, problem))
        return f
