from __future__ import annotations

from typing import List, Dict, Set

from src.pddl.Atom import Atom
from src.pddl.BinaryPredicate import BinaryPredicate, BinaryPredicateType
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

        return ic

    def getAssignment(self, atom: Atom) -> float:
        return self.numericAssignments[atom]
        pass

    def addPropositionalAssignment(self, literal: Literal):
        self.assignments.add(literal)

    @classmethod
    def fromString(cls, string: str):
        return InitialCondition.fromNode(Utilities.getParseTree(string).init())

    def addNumericAssignment(self, costLit: Literal, value: float):
        bp = BinaryPredicate()
        bp.lhs = costLit
        bp.rhs = Constant(value)
        bp.operator = "="
        bp.type = BinaryPredicateType.COMPARATION

        self.assignments.add(bp)
        self.numericAssignments[costLit.atom] = value

        pass
