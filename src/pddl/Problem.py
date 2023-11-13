from __future__ import annotations

import copy
from typing import Dict, List, Tuple, Set

from src.pddl.Atom import Atom
from src.pddl.Literal import Literal
from src.pddl.PDDLWriter import PDDLWriter
from src.pddl.Predicate import Predicate
from src.pddl.InitialCondition import InitialCondition
from src.pddl.Goal import Goal
from src.pddl.Utilities import Utilities

from src.pddl.grammar.pddlParser import pddlParser


class Problem:
    name: str
    domainName: str
    objectsByType: Dict[str, List[str]]
    init: InitialCondition
    metric: Predicate or None = None
    goal: Goal

    def __init__(self):
        self.objectsByType = dict()
        self.isPredicateStatic: Dict[str, bool] = dict()
        self.canHappenValue: Set[str] = set()
        self.assignmentsTree: Dict = dict()

    def __deepcopy__(self, m=None) -> Problem:
        p = Problem()
        p.name = self.name
        p.domainName = self.domainName
        p.objectsByType = copy.deepcopy(self.objectsByType, m)
        p.init = copy.deepcopy(self.init, m)
        p.metric = copy.deepcopy(self.metric)
        p.goal = copy.deepcopy(self.goal)
        p.isPredicateStatic = copy.deepcopy(self.isPredicateStatic)
        p.canHappenValue = copy.deepcopy(self.canHappenValue)
        p.assignmentsTree = copy.deepcopy(self.assignmentsTree)

        return p

    @classmethod
    def fromNode(cls, node: pddlParser.ProblemContext) -> Problem:
        problem = cls()
        for node in node.getChildren():
            if isinstance(node, pddlParser.ProblemNameContext):
                problem.__setProblemName(node)
            if isinstance(node, pddlParser.ProblemDomainContext):
                problem.__setDomainName(node)
            if isinstance(node, pddlParser.ObjectsContext):
                problem.__addObjects(node)
            if isinstance(node, pddlParser.InitContext):
                problem.init = InitialCondition.fromNode(node)
            if isinstance(node, pddlParser.GoalContext):
                problem.goal = Goal.fromNode(node)
            if isinstance(node, pddlParser.MetricContext):
                problem.__setMetric(node)
        return problem

    @classmethod
    def fromString(cls, string: str):
        return cls.fromNode(Utilities.getParseTree(string).problem())

    def __setProblemName(self, node: pddlParser.ProblemNameContext):
        self.name = node.getChild(2).getText()

    def __setDomainName(self, node: pddlParser.ProblemDomainContext):
        self.domainName = node.getChild(2).getText()

    def __addObjects(self, node: pddlParser.ObjectsContext):
        for typeNode in node.children:
            if not isinstance(typeNode, pddlParser.TypedObjectsContext):
                continue
            typeStr: str = ""
            objects = []
            for child in typeNode.children:
                if isinstance(child, pddlParser.GroundAtomParameterContext):
                    objects.append(child.getText())
                elif isinstance(child, pddlParser.TypeNameContext):
                    typeStr = child.getText()
            self.objectsByType.setdefault(typeStr, [])
            self.objectsByType[typeStr].extend(objects)

    @classmethod
    def fromFile(cls, filename):
        f = open(filename, 'r')
        domainString = f.read()
        f.close()
        domainString = Utilities.removeComments(domainString)

        parseTree: pddlParser = Utilities.getParseTree(domainString)
        return Problem.fromNode(parseTree.problem())

    def __setMetric(self, node: pddlParser.MetricContext):
        return
        # To implement
        # if node.sign.text == "maximize":
        #     raise Exception("Maximize not supported")
        #
        # predicate = node.op.getChild(0)
        # if isinstance(predicate, BinaryPredicate):
        #     self.metric = BinaryPredicate.fromNode(predicate)
        # else:
        #     self.metric = Literal.fromNode(predicate)
        # return

    def substitute(self, substitutions):
        self.goal = self.goal.substitute(substitutions)
        pass

    def computeWhatCanHappen(self, domain):

        from src.pddl.Domain import Domain
        domain: Domain
        self.isPredicateStatic = domain.isPredicateStatic

        for init in self.init.assignments:
            if isinstance(init, Literal):
                subStr = ",".join([k for k in init.getAtom().attributes])
                atomStr = f"{init.getAtom().name}({subStr})"
                self.canHappenValue.add(atomStr)

                self.assignmentsTree[init.atom.name] = self.assignmentsTree.setdefault(init.atom.name, dict())
                root = self.assignmentsTree[init.atom.name]
                for i, attr in enumerate(init.atom.attributes):
                    root[i] = root.setdefault(i, dict())
                    root[i][attr] = root[i].setdefault(attr, set())
                    root[i][attr].add(init)

        pass

    def toPDDL(self, pw: PDDLWriter = PDDLWriter()):
        pw.write(f"(define (problem {self.name})")
        pw.increaseTab()
        pw.write(f"(:domain {self.domainName})")

        # Constants
        pw.write(f"(:objects")
        pw.increaseTab()
        for (type, objects) in self.objectsByType.items():
            objStr = " ".join(objects)
            pw.write(f"{objStr} - {type}")
        pw.decreaseTab()
        pw.write(f")")

        # Init
        pw.write(f"(:init")
        pw.increaseTab()
        for a in self.init.assignments:
            a.toPDDL(pw)
        pw.decreaseTab()
        pw.write(f")")

        # Goal
        pw.write(f"(:goal")
        pw.increaseTab()
        self.goal.toPDDL(pw)
        pw.decreaseTab()
        pw.write(f")")

        pw.decreaseTab()
        pw.write(f")")

        return pw
