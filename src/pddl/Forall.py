import itertools
from typing import List, Dict, Set

from src.pddl.Atom import Atom
from src.pddl.Effects import Effects
from src.pddl.Parameter import Parameter
from src.pddl.Parameters import Parameters
from src.pddl.Predicate import Predicate
from src.pddl.Problem import Problem
from src.pddl.Type import Type
from src.pddl.grammar.pddlParser import pddlParser


class Forall(Predicate):
    parameters: Parameters
    effects: Effects

    def __init__(self):
        super().__init__()

    @classmethod
    def fromNode(cls, node: pddlParser.ForallContext, types: Dict[str, Type]):
        forall = cls()
        forall.parameters = Parameters.fromNode(node.getChild(2), types)
        forall.effects = Effects.fromNode(node.getChild(3), types)
        return forall

    def eliminate(self, problem: Problem) -> List[Predicate]:
        predicates: List[Predicate] = list()
        levels = self.parameters.getCombinations(problem)
        # combinations: list(itertools.product(*levels))

        return predicates

    def getFunctions(self) -> Set[Atom]:
        return self.effects.getFunctions()

    def getPredicates(self) -> Set[Atom]:
        return self.effects.getPredicates()
