from typing import Set, Dict

from pyeda.boolalg.bdd import BDDVariable, BinaryDecisionDiagram

from src.pddl.Atom import Atom
from src.pddl.Formula import Formula
from src.pddl.Parameters import Parameters
from src.pddl.Predicate import Predicate


class Quantifier(Predicate):
    parameters: Parameters
    formula: Formula

    def __init__(self):
        super().__init__()

    def getFunctions(self) -> Set[Atom]:
        return self.formula.getFunctions()

    def getPredicates(self) -> Set[Atom]:
        return self.formula.getPredicates()

    def eliminate(self, problem):
        raise NotImplementedError()

    def toBDD(self, vars: Dict[Atom, BDDVariable]) -> BinaryDecisionDiagram:
        raise NotImplementedError()
