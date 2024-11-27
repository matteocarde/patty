from __future__ import annotations

import copy
from typing import List, Dict

from graphlib import TopologicalSorter, CycleError

from src.pddl.Action import Action
from src.pddl.Atom import Atom
from src.pddl.ConditionalEffect import ConditionalEffect


class BDDVariableOrder:
    nodes: Dict[Atom, List[Atom]]

    def __init__(self, action: Action):
        self.nodes = dict()
        for v in action.predicates:
            self.nodes[v] = list()

        # 1) v < v' -> Already dealt inside the bdd formulas

        # 2) v \in pre(a), w \nin \pre(a), v < w
        for v in action.preconditions.getPredicates():
            for w in action.predicates - action.preconditions.getPredicates():
                self.nodes[w].append(v)

        # 3) \forall e \in post(a), v \in cond(e), w \in post(e) -> v < w
        for e in action.effects:
            if not isinstance(e, ConditionalEffect):
                continue
            for v in e.conditions.getPredicates():
                for w in e.effects.getPredicates():
                    self.nodes[w].append(v)

    def getOrder(self) -> List[Atom]:
        nodes = copy.deepcopy(self.nodes)
        while True:
            try:
                ts = TopologicalSorter(nodes)
                return list(ts.static_order())
            except CycleError as e:
                cycle = e.args[1]
                nodes[cycle[1]].remove(cycle[0])

    def toDot(self):
        dot = ["digraph order {"]
        for v in self.nodes.keys():
            dot += [f'"{v}";']
            for w in self.nodes[v]:
                dot += [f'"{v}" -> "{w}";']
        dot += ["}"]

        return " ".join(dot)
