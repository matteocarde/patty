from __future__ import annotations
from typing import Dict, List, Set

from src.pddl.Atom import Atom
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
        self.allAtoms: Set[Atom] = set()
        self.objectsByType = dict()

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

        problem.allAtoms = problem.init.allAtoms

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
