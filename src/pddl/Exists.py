import copy
from typing import Dict

from src.pddl.Formula import Formula
from src.pddl.Parameters import Parameters
from src.pddl.Problem import Problem
from src.pddl.Quantifier import Quantifier
from src.pddl.Type import Type
from src.pddl.grammar.pddlParser import pddlParser


class Exists(Quantifier):
    parameters: Parameters
    formula: Formula

    def __init__(self):
        super().__init__()

    def __deepcopy__(self, memodict=None):
        ex = Exists()
        ex.parameters = copy.deepcopy(self.parameters, memodict)
        ex.formula = copy.deepcopy(self.formula, memodict)
        return ex

    @classmethod
    def fromNode(cls, node: pddlParser.ExistsContext, types: Dict[str, Type]):
        from src.pddl.Forall import Forall
        ex = cls()
        ex.parameters = Parameters.fromNode(node.getChild(2), types)
        child = node.getChild(3)
        if isinstance(child, pddlParser.ForallContext):
            ex.formula = Forall.fromNode(child, types)
        elif isinstance(child, pddlParser.ExistsContext):
            ex.formula = Exists.fromNode(child, types)
        else:
            ex.formula = Formula.fromNode(node.getChild(3))
        return ex

    def eliminate(self, problem: Problem) -> Formula:
        subs = self.parameters.getAllSubstitutions(problem)
        f = Formula()
        f.type = "OR"
        subF = self.formula
        if isinstance(self.formula, Quantifier):
            subF = self.formula.eliminate(problem)

        for sub in subs:
            if subF.canHappen(sub):
                f.addClause(subF.ground(sub, problem))
        return f
