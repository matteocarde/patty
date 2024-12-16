import copy
from typing import Tuple, Any, Dict

from src.pddl.Parameter import Parameter
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

    @classmethod
    def fromNode(cls, node: pddlParser.InequalityContext):
        ineq = cls()
        ineq.params = (node.a1.getText(), node.a2.getText())
        return ineq

    def ground(self, subs: Dict[str, str], delta=1) -> Predicate:
        if not self.canHappen(subs):
            raise Exception("Inequality not respected when grounding")
        return True

    def canHappen(self, subs: Dict[Any, Any], default=None) -> bool:
        return subs[self.params[0]] != subs[self.params[1]]
