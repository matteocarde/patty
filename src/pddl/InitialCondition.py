from __future__ import annotations

import copy
import math
import random
from typing import List, Dict, Set

import numpy as np

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
        self.allAtoms: Set[Atom] = set()
        self.predicates: Set[Atom] = set()
        self.functions: Set[Atom] = set()
        self.assignments = []
        self.numericAssignments = dict()

    @classmethod
    def partialize(cls, init: InitialCondition, ratio: float) -> InitialCondition:
        partial = copy.deepcopy(init)
        random.shuffle(partial.assignments)
        amount = math.floor(len(partial.assignments) * ratio)
        partial.assignments = partial.assignments[:amount]

        return partial

    @classmethod
    def noise(cls, init, amount):
        noise: InitialCondition = InitialCondition()
        for p in init.assignments:
            if isinstance(p, Literal):
                noise.assignments.append(p)

            if isinstance(p, BinaryPredicate):
                n = copy.deepcopy(p)
                if not isinstance(n.rhs, Constant):
                    raise Exception("Right hand side should be consant")
                n.rhs.value = np.random.normal(n.rhs.value, abs(n.rhs.value * amount / 100))
                noise.assignments.append(n)

        return noise

    def __str__(self):
        return str(self.assignments)

    def __repr__(self):
        return str(self)

    def __iter__(self):
        return iter(self.assignments)

    def __deepcopy__(self, m):
        cp = InitialCondition()
        cp.allAtoms = copy.deepcopy(self.allAtoms, m)
        cp.predicates = copy.deepcopy(self.predicates, m)
        cp.functions = copy.deepcopy(self.functions, m)
        cp.assignments = copy.deepcopy(self.assignments, m)
        cp.numericAssignments = copy.deepcopy(self.numericAssignments, m)
        return cp

    @classmethod
    def fromNode(cls, node: pddlParser.InitContext) -> InitialCondition:
        ic = cls()
        ic.assignments = set()
        for child in node.children:
            if isinstance(child, pddlParser.PositiveLiteralContext):
                lit = Literal.fromNode(child)
                ic.allAtoms.add(lit.getAtom())
                ic.predicates.add(lit.getAtom())
                ic.assignments.append(lit)
            if isinstance(child, pddlParser.AssignmentContext):
                assignment = BinaryPredicate.fromNode(child)
                ic.assignments.add(assignment)
                if not isinstance(assignment.rhs, Constant):
                    raise Exception(
                        "At the moment, this tool only support initial conditions with numeric constant assignments")
                ic.allAtoms.add(assignment.getAtom())
                ic.functions.add(assignment.getAtom())
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

    def addPredicate(self, l: Literal):
        self.assignments.append(l)

    def addNumericAssignment(self, atom: Atom, value: float):
        self.numericAssignments[atom] = value
        self.assignments.append(BinaryPredicate.fromAssignment(atom, value))

    @classmethod
    def fromString(cls, string: str):
        return InitialCondition.fromNode(Utilities.getParseTree(string).init())
