from __future__ import annotations

from typing import Dict, Set, List, Any

import tarjan as scc

from src.pddl.Action import Action
from src.pddl.Atom import Atom
from src.pddl.BinaryPredicate import BinaryPredicate, BinaryPredicateType
from src.pddl.Literal import Literal


class AffectedGraphNode:

    def __init__(self, action: Action):
        self.action = action
        self.preconditions: Dict[Atom, str] = dict()

        keys = ["add", "del", "num"]
        self.pre: Dict[str, Set[Atom]] = dict((key, set()) for key in keys)
        self.eff: Dict[str, Set[Atom]] = dict((key, set()) for key in keys)

        for lit in self.action.preconditions.getLiterals():
            if isinstance(lit, Literal):
                if lit.sign == "+":
                    self.pre["add"].add(lit.getAtom())
                if lit.sign == "-":
                    self.pre["del"].add(lit.getAtom())
            if isinstance(lit, BinaryPredicate):
                for atom in lit.getFunctions():
                    self.pre["num"].add(atom)

        for eff in self.action.effects.assignments:
            if isinstance(eff, Literal):
                atom = eff.getAtom()
                if eff.sign == "+":
                    self.eff["add"].add(atom)
                if eff.sign == "-":
                    self.eff["del"].add(atom)
            if isinstance(eff, BinaryPredicate):
                if eff.type == BinaryPredicateType.MODIFICATION:
                    self.eff["num"].add(eff.lhs.getAtom())

        self.neighbours: [AffectedGraphNode] = set()

    def pruneForSubgraph(self, actions: Set[Action]) -> AffectedGraphNode:
        pruned = AffectedGraphNode(self.action)
        pruned.neighbours = [n for n in self.neighbours if n.action in actions]

        return pruned

    def __hash__(self):
        return hash(self.action)

    def __eq__(self, other):
        if not isinstance(other, AffectedGraphNode):
            return False
        return self.action == other.action

    def __repr__(self):
        return repr(self.action)

    def __str__(self):
        return str(self.action)

    def addNeighbour(self, node: AffectedGraphNode):
        if self not in node.neighbours:
            self.neighbours.add(node)
        else:
            node.neighbours.remove(self)


class AffectedGraph:
    actions: [Action]
    nodes: [AffectedGraphNode]

    def __init__(self):
        self.actions: [Action] = list()
        self.nodes: [AffectedGraphNode] = list()

    @classmethod
    def fromActions(cls, actions: [Action]) -> AffectedGraph:

        graph: AffectedGraph = cls()
        graph.actions: [Action] = actions

        graph.nodes: [AffectedGraphNode] = [AffectedGraphNode(action) for action in graph.actions]

        keys = ["add", "del", "num"]
        bucketPre: Dict[str, Dict[Atom, Set[AffectedGraphNode]]] = dict((key, dict()) for key in keys)

        for node in graph.nodes:
            for key in keys:
                for atom in node.pre[key]:
                    bucketPre[key][atom] = bucketPre[key].setdefault(atom, set())
                    bucketPre[key][atom].add(node)

        for nodeA in graph.nodes:
            connectedNodes = set()
            for p in nodeA.eff["add"]:
                connectedNodes |= bucketPre["del"][p] if p in bucketPre["del"] else set()
            for p in nodeA.eff["del"]:
                connectedNodes |= bucketPre["add"][p] if p in bucketPre["add"] else set()
            for p in nodeA.eff["num"]:
                connectedNodes |= bucketPre["num"][p] if p in bucketPre["num"] else set()
            for nodeB in connectedNodes:
                if nodeA != nodeB:
                    nodeA.addNeighbour(nodeB)

        return graph

    def getSCC(self):
        components = dict([(node, node.neighbours) for node in self.nodes])
        dag: [[AffectedGraphNode]] = scc.tarjan(components)
        # dag.reverse()
        return dag

    def getOrderFromGraph(self) -> [Action]:
        return [n.action for group in self.getSCC() for n in group]

    def toDot(self):
        s = ["digraph G {"]
        for nodeA in self.nodes:
            s.append(f"\"{nodeA.action.name}\"")
            for nodeB in nodeA.neighbours:
                s.append(f"\"{nodeA.action.name}\" -> \"{nodeB.action.name}\"")
        s.append("}")

        return "\n".join(s)

    def getSubGraph(self, subActions: Set[Action]) -> AffectedGraph:
        subGraph = AffectedGraph()
        subGraph.actions = subActions
        subGraph.nodes = [node.pruneForSubgraph(subActions) for node in self.nodes if node.action in subActions]

        return subGraph
