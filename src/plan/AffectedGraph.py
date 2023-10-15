from __future__ import annotations

from typing import Dict, Set

from tarjan import tarjan

from src.pddl.Action import Action
from src.pddl.Atom import Atom
from src.pddl.BinaryPredicate import BinaryPredicate, BinaryPredicateType
from src.pddl.Literal import Literal


class AffectedGraphNode:

    def __init__(self, action: Action):
        self.action = action
        self.preconditions: Dict[Atom, str] = dict()
        for lit in self.action.preconditions.getLiterals():
            if isinstance(lit, Literal):
                self.preconditions[lit.getAtom()] = lit.sign
            if isinstance(lit, BinaryPredicate):
                for atom in lit.getFunctions():
                    self.preconditions[atom] = "+"

        self.neighbours: [AffectedGraphNode] = list()

    def __repr__(self):
        return repr(self.action)

    def __str__(self):
        return str(self.action)

    def isAffectedBy(self, node: AffectedGraphNode) -> bool:

        for eff in node.action.effects.assignments:
            if isinstance(eff, Literal):
                atom = eff.getAtom()
                if atom not in self.preconditions:
                    continue
                if eff.sign == "+" and self.preconditions[atom] == "-":
                    return True
                if eff.sign == "-" and self.preconditions[atom] == "+":
                    return True
            if isinstance(eff, BinaryPredicate):
                if eff.type == BinaryPredicateType.MODIFICATION and eff.lhs.getAtom() in self.preconditions:
                    return True

        return False

    def addNeighbour(self, node: AffectedGraphNode):
        self.neighbours.append(node)


class AffectedGraph:

    def __init__(self, actions: Set[Action]):
        self.actions: Set[Action] = actions
        self.nodes: [AffectedGraphNode] = [AffectedGraphNode(action) for action in self.actions]

        for nodeA in self.nodes:
            for nodeB in self.nodes:
                if nodeA == nodeB:
                    continue
                if nodeA.isAffectedBy(nodeB):
                    nodeA.addNeighbour(nodeB)

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
