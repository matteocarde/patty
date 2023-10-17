from __future__ import annotations

from typing import List, Dict, Set

from src.pddl.Atom import Atom
from src.pddl.BinaryPredicate import BinaryPredicate
from src.pddl.Constant import Constant
from src.pddl.Literal import Literal
from src.pddl.Predicate import Predicate
from src.pddl.Utilities import Utilities
from src.pddl.grammar.pddlParser import pddlParser


class InitialCondition:
    assignments: Set[Predicate]
    assignmentsByPropertyTree: Dict[str, Dict]
    numericAssignments: Dict[Atom, float]

    def __init__(self):
        self.assignments = set()
        self.numericAssignments = dict()

    def __str__(self):
        return str(self.assignments)

    def __repr__(self):
        return str(self)

    def __iter__(self):
        return iter(self.assignments)

    @classmethod
    def fromNode(cls, node: pddlParser.InitContext) -> InitialCondition:
        ic = cls()
        ic.assignments = set()
        for child in node.children:
            if isinstance(child, pddlParser.PositiveLiteralContext):
                lit = Literal.fromNode(child)
                ic.assignments.add(lit)
            if isinstance(child, pddlParser.AssignmentContext):
                assignment = BinaryPredicate.fromNode(child)
                ic.assignments.add(assignment)
                if not isinstance(assignment.rhs, Constant):
                    raise Exception(
                        "At the moment, this tool only support initial conditions with numeric constant assignments")
                ic.numericAssignments[assignment.getAtom()] = assignment.rhs.value

        # pTree = dict()
        # for assignment in ic.numericAssignments:
        #     name = assignment.name
        #     pTree[name] = pTree.setdefault(name, dict())
        #     node = pTree[name]
        #     lastAttr = None
        #     lastNode = None
        #     for attr in assignment.attributes:
        #         node[attr] = node.setdefault(attr, dict())
        #         lastAttr = attr
        #         lastNode = node
        #         node = node[attr]
        #     if lastAttr:
        #         lastNode[lastAttr] = True
        #
        # ic.assignmentsByPropertyTree = pTree

        return ic

    def getAssignment(self, atom: Atom) -> float:
        return self.numericAssignments[atom]
        pass

    @classmethod
    def fromString(cls, string: str):
        return InitialCondition.fromNode(Utilities.getParseTree(string).init())
