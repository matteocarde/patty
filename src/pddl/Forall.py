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


class Forall(Quantifier):
    parameters: Parameters
    formula: Formula

    def __init__(self):
        super().__init__()

    def __deepcopy__(self, memodict={}):
        fa = Forall()
        fa.parameters = copy.deepcopy(self.parameters, memodict)
        fa.body = copy.deepcopy(self.formula, memodict)
        return fa

    @classmethod
    def fromNode(cls, node: pddlParser.ForallContext, types: Dict[str, Type]):
        forall = cls()
        forall.parameters = Parameters.fromNode(node.getChild(2), types)
        forall.formula = Formula.fromNode(node.getChild(3))
        return forall

    # def eliminate(self, problem: Problem) -> List[Predicate]:
    #     from src.pddl.ConditionalEffect import ConditionalEffect
    #     levels = self.parameters.getCombinations(problem)
    #     combinations = list(itertools.product(*levels))
    #
    #     params = [p.name for p in self.parameters]
    #     predicates = list()
    #     for comb in combinations:
    #         sub = dict([(p.name, comb[i]) for i, p in enumerate(self.parameters)])
    #         if isinstance(self.effect, ConditionalEffect):
    #             if self.effect.canHappenLifted(comb, params, problem):
    #                 predicates.append(self.effect.ground(sub))
    #         else:
    #             predicates.append(self.effect.ground(sub))
    #
    #     return predicates
