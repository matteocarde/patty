import copy
import itertools
from typing import List, Dict, Set

from src.pddl.Atom import Atom
from src.pddl.Effects import Effects
from src.pddl.Formula import Formula
from src.pddl.Parameters import Parameters
from src.pddl.Predicate import Predicate
from src.pddl.Problem import Problem
from src.pddl.Quantifier import Quantifier
from src.pddl.Type import Type
from src.pddl.grammar.pddlParser import pddlParser


class Exists(Quantifier):
    parameters: Parameters
    formula: Formula

    def __init__(self):
        super().__init__()

    def __deepcopy__(self, memodict={}):
        ex = Exists()
        ex.parameters = copy.deepcopy(self.parameters, memodict)
        ex.body = copy.deepcopy(self.formula, memodict)
        return ex

    @classmethod
    def fromNode(cls, node: pddlParser.ExistsContext, types: Dict[str, Type]):
        ex = cls()
        ex.parameters = Parameters.fromNode(node.getChild(2), types)
        ex.formula = Formula.fromNode(node.getChild(3))
        return ex
