from __future__ import annotations
from typing import Set, Dict

from src.pddl.Atom import Atom
from src.pddl.CEConditions import CEConditions
from src.pddl.CEEffects import CEEffects
from src.pddl.Predicate import Predicate
from src.pddl.grammar.pddlParser import pddlParser as p


class ConditionalEffect(Predicate):
    from src.pddl.CEEffects import CEEffects
    conditions: CEConditions
    effects: CEEffects

    def __init__(self):
        super().__init__()
        self.conditions = CEConditions()
        self.effects = CEEffects()

    @classmethod
    def fromNode(cls, node: p.CeContext):
        ce = cls()
        ce.conditions = CEConditions.fromNode(node.cond.getChild(0))
        ce.effects = CEEffects.fromNode(node.eff)
        return ce

    def __str__(self):
        return f"{self.conditions} -> {self.effects}"

    def __repr__(self):
        return str(self)

    def getPredicates(self) -> Set[Atom]:
        return self.conditions.getPredicates() | self.effects.getPredicates()

    def getFunctions(self) -> Set[Atom]:
        return self.conditions.getFunctions() | self.effects.getFunctions()

    def ground(self, subs: Dict[str, str], delta=1) -> ConditionalEffect:
        ce = ConditionalEffect()
        ce.conditions = self.conditions.ground(subs, delta)
        ce.effects = self.effects.ground(subs, delta)

        return ce

    def substitute(self, subs: Dict[Atom, float], default=None) -> ConditionalEffect:
        ce = ConditionalEffect()
        ce.conditions = self.conditions.substitute(subs, default)
        ce.effects = self.effects.substitute(subs, default)

        return ce
