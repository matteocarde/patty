import copy
from typing import Tuple, Any, Dict, List, Set

from src.pddl.Atom import Atom
from src.pddl.Predicate import Predicate
from src.pddl.grammar.pddlParser import pddlParser


class Inequality(Predicate):
    params: Tuple[str, str]

    def __init__(self):
        super().__init__()

    def __deepcopy__(self, memodict=None):
        i = Inequality()
        i.params = copy.deepcopy(self.params, memodict)
        return i

    def __str__(self):
        return f"({self.params[0]} != {self.params[1]})"

    def getPredicates(self) -> Set[Atom]:
        return set()

    def getFunctions(self) -> Set[Atom]:
        return set()

    @classmethod
    def fromNode(cls, node: pddlParser.InequalityContext):
        ineq = cls()
        ineq.params = (node.a1.getText(), node.a2.getText())
        return ineq

    def ground(self, subs: Dict[str, str], problem) -> Predicate:
        from src.pddl.TruePredicate import TruePredicate
        from src.pddl.FalsePredicate import FalsePredicate
        return TruePredicate() if self.canHappen(subs) else FalsePredicate()

    def canHappen(self, subs: Dict[Any, Any], default=None) -> bool:
        return subs[self.params[0]] != subs[self.params[1]]

    def canHappenLifted(self, sub: Tuple, params: List[str], problem) -> bool:
        a = sub[params.index(self.params[0])]
        b = sub[params.index(self.params[1])]
        return a != b
