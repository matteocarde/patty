from __future__ import annotations

import copy
from typing import List, Dict, Set

from graphlib import TopologicalSorter, CycleError

from src.pddl.Action import Action
from src.pddl.Atom import Atom
from src.pddl.ConditionalEffect import ConditionalEffect


class BDDVariableOrder:
    nodes: Dict[Atom, Set[Atom]]

    def __init__(self, action: Action):
        self.nodes = dict()
        for v in action.predicates:
            self.nodes[v] = set()

        # 1) v < v' -> Already dealt inside the bdd formulas

        # 2) v \in pre(a), w \nin \pre(a), v < w
        for v in action.preconditions.getPredicates():
            for w in action.predicates - action.preconditions.getPredicates():
                if v != w:
                    self.nodes[w].add(v)

        # 3) \forall e \in post(a), v \in cond(e), w \in post(e) -> v < w
        for e in action.effects:
            if not isinstance(e, ConditionalEffect):
                continue
            for v in e.conditions.getPredicates():
                for w in e.effects.getPredicates():
                    if v != w:
                        self.nodes[w].add(v)

    def getOrder(self) -> List[Atom]:
        nodes = copy.deepcopy(self.nodes)
        while True:
            try:
                ts = TopologicalSorter(nodes)
                return list(ts.static_order())
            except CycleError as e:
                cycle: List[Atom] = e.args[1]
                smallestAtom = sorted(cycle)[0]
                index = cycle.index(smallestAtom)
                nodes[cycle[index+1]].remove(cycle[index])

    def toDot(self):
        dot = ["digraph order {"]
        for v in self.nodes.keys():
            dot += [f'"{v}";']
            for w in self.nodes[v]:
                dot += [f'"{w}" -> "{v}";']
        dot += ["}"]

        return " ".join(dot)
