from __future__ import annotations

from typing import Dict, Set, List, Any

from tarjan import tarjan

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

        self.neighbours: [AffectedGraphNode] = list()

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

    def isAffectedBy(self, node: AffectedGraphNode) -> bool:

        if self.pre["add"].intersection(node.eff["del"]):
            return True
        if self.pre["del"].intersection(node.eff["add"]):
            return True
        if self.pre["num"].intersection(node.eff["num"]):
            return True

        return False

    def addNeighbour(self, node: AffectedGraphNode):
        self.neighbours.append(node)


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
        bucketEff: Dict[str, Dict[Atom, Set[AffectedGraphNode]]] = dict((key, dict()) for key in keys)

        for node in graph.nodes:
            for key in keys:
                for atom in node.pre[key]:
                    bucketPre[key][atom] = bucketPre[key].setdefault(atom, set())
                    bucketPre[key][atom].add(node)
                for atom in node.eff[key]:
                    bucketEff[key][atom] = bucketEff[key].setdefault(atom, set())
                    bucketEff[key][atom].add(node)

        called = 0
        for nodeA in graph.nodes:
            connectedNodes = set()
            for p in nodeA.pre["add"]:
                connectedNodes |= bucketEff["del"][p] if p in bucketEff["del"] else set()
            for p in nodeA.pre["del"]:
                connectedNodes |= bucketEff["add"][p] if p in bucketEff["add"] else set()
            for p in nodeA.pre["num"]:
                connectedNodes |= bucketEff["num"][p] if p in bucketEff["num"] else set()
            for nodeB in connectedNodes:
                nodeA.addNeighbour(nodeB)

        return graph

    def getOrderFromGraph(self) -> [Action]:

        components = dict([(node, node.neighbours) for node in self.nodes])
        dag: [[AffectedGraphNode]] = tarjan(components)
        dag.reverse()

        return [n.action for group in dag for n in group]

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
