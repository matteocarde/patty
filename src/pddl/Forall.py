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
    formula: Formula or Quantifier

    def __init__(self):
        super().__init__()

    def __deepcopy__(self, memodict=None):
        fa = Forall()
        fa.parameters = copy.deepcopy(self.parameters, memodict)
        fa.formula = copy.deepcopy(self.formula, memodict)
        return fa

    @classmethod
    def fromNode(cls, node: pddlParser.ForallContext, types: Dict[str, Type]):
        from src.pddl.Exists import Exists
        forall = cls()
        forall.parameters = Parameters.fromNode(node.getChild(2), types)
        child = node.getChild(3)
        if isinstance(child, pddlParser.ForallContext):
            forall.formula = Forall.fromNode(child, types)
        elif isinstance(child, pddlParser.ExistsContext):
            forall.formula = Exists.fromNode(child, types)
        else:
            forall.formula = Formula.fromNode(node.getChild(3))
        return forall

    def eliminate(self, problem: Problem) -> Formula:
        subs = self.parameters.getAllSubstitutions(problem)
        f = Formula()
        f.type = "AND"
        subF = self.formula
        if isinstance(self.formula, Quantifier):
            subF = self.formula.eliminate(problem)
        for sub in subs:
            if subF.canHappenLifted(tuple(sub.values()), list(sub.keys()), problem):
                f.addClause(subF.ground(sub, problem))
        return f
