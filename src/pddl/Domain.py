from __future__ import annotations

import copy
from typing import Dict, List, Set

from src.pddl.Action import Action
from src.pddl.Atom import Atom
from src.pddl.Event import Event
from src.pddl.Operation import Operation
from src.pddl.PDDLWriter import PDDLWriter
from src.pddl.Problem import Problem
from src.pddl.Process import Process
from src.pddl.State import State
from src.pddl.Type import Type
from src.pddl.TypedPredicate import TypedPredicate
from src.pddl.Utilities import Utilities
from src.pddl.grammar.pddlParser import pddlParser
from src.utils.LogPrint import LogPrint, LogPrintLevel


class Domain:
    name = str
    requirements: List[str]
    types: Dict[str, Type]
    predicates: set[TypedPredicate]
    functions: set[TypedPredicate]
    actions: set[Action]
    events: set[Event]
    processes: set[Process]
    constants: Dict[str, List[str]]
    __operationsDict: Dict[str, Operation]

    def __init__(self):
        self.types = dict()
        self.predicates = set()
        self.functions = set()
        self.actions = set()
        self.processes = set()
        self.events = set()
        self.requirements = list()
        self.constants = dict()
        self.isPredicateStatic: Dict[str, bool] = dict()
        pass

    def __deepcopy__(self, m=None):
        c = Domain()
        c.name = self.name
        c.requirements = copy.deepcopy(self.requirements, m)
        c.constants = copy.deepcopy(self.constants, m)
        c.types = copy.deepcopy(self.types, m)
        c.predicates = copy.deepcopy(self.predicates, m)
        c.functions = copy.deepcopy(self.functions, m)
        c.actions = copy.deepcopy(self.actions, m)
        c.events = copy.deepcopy(self.events, m)
        c.processes = copy.deepcopy(self.processes, m)
        c.isPredicateStatic = copy.deepcopy(self.isPredicateStatic, m)
        return c

    def ground(self, problem: Problem, avoidSimplification=False, console: LogPrint = None):

        from src.pddl.GroundedDomain import GroundedDomain

        problem.computeWhatCanHappen(self)

        gActions: Set[Action] = set(
            [g for action in self.actions for g in action.ground(problem, self.isPredicateStatic)])
        gEvents: Set[Event] = set([g for event in self.events for g in event.ground(problem, self.isPredicateStatic)])
        gProcess: Set[Process] = set(
            [g for process in self.processes for g in process.ground(problem, self.isPredicateStatic)])

        gDomain = GroundedDomain(self.name, gActions, gEvents, gProcess)

        if console:
            console.log("Static Grounding Stats:", LogPrintLevel.STATS)
            console.log(gDomain.getStats(), LogPrintLevel.STATS)

        if avoidSimplification:
            return gDomain

        from src.pddl.RPG import RPG
        from src.pddl.ARPG import ARPG

        constants: Dict[Atom, float] = dict()

        for op in gActions | gEvents | gProcess:
            for fun in op.getFunctions():
                if fun not in problem.init.numericAssignments:
                    # print(f"WARNING: {fun} was not initialized. Substituting it with 0")
                    constants[fun] = 0

        gDomain = gDomain.substitute(constants)

        rpg = RPG(gDomain, problem)
        orderedActions = rpg.getActionsOrder()
        initialState = State.fromInitialCondition(problem.init)
        gDomain.actions = set(orderedActions)

        arpg = ARPG(gDomain, initialState, problem.goal)
        constants: Dict[Atom, float] = arpg.getConstantAtoms()

        for op in gActions | gEvents | gProcess:
            for fun in op.getFunctions():
                if fun not in problem.init.numericAssignments:
                    # print(f"WARNING: {fun} was not initialized. Substituting it with 0")
                    constants[fun] = 0

        gDomain = gDomain.substitute(constants)
        orderedActions = [a.substitute(constants) for a in orderedActions if a.canHappen(constants)]
        problem.substitute(constants)
        gDomain.actions = set(orderedActions)

        from src.plan.AffectedGraph import AffectedGraph
        gDomain.actions = sorted(gDomain.actions, key=lambda a: a.name)
        gDomain.affectedGraph = AffectedGraph.fromActions(gDomain.actions)
        gDomain.arpg = ARPG(gDomain, initialState, problem.goal)

        if console:
            console.log("Dynamic Grounding Stats:", LogPrintLevel.STATS)
            console.log(gDomain.getStats(), LogPrintLevel.STATS)

        return gDomain

    @classmethod
    def fromNode(cls, node: pddlParser.DomainContext) -> Domain:

        domain = cls()

        for i in range(node.getChildCount()):
            child = node.getChild(i)
            if isinstance(child, pddlParser.DomainNameContext):
                domain.__setDomainName(child)
            elif isinstance(child, pddlParser.RequirementsContext):
                domain.__setRequirementsList(child)
            elif isinstance(child, pddlParser.TypesContext):
                domain.__setTypesList(child)
            elif isinstance(child, pddlParser.PredicatesContext):
                domain.__setPredicates(child)
            elif isinstance(child, pddlParser.FunctionsContext):
                domain.__setFunctions(child)
            elif isinstance(child, pddlParser.ActionContext):
                domain.actions.add(Action.fromNode(child, domain.types))
            elif isinstance(child, pddlParser.EventContext):
                domain.events.add(Event.fromNode(child, domain.types))
            elif isinstance(child, pddlParser.ProcessContext):
                domain.processes.add(Process.fromNode(child, domain.types))

        domain.isPredicateStatic: Dict[str, bool] = dict([(p.name, True) for p in domain.predicates | domain.functions])
        for action in domain.actions | domain.events | domain.processes:
            for eff in action.effects.getFunctions() | action.effects.getPredicates():
                domain.isPredicateStatic[eff.name] = False

        return domain

    @classmethod
    def fromFile(cls, filename) -> Domain:
        f = open(filename, 'r')
        domainString = f.read()
        f.close()
        domainString = Utilities.removeComments(domainString)

        parseTree: pddlParser = Utilities.getParseTree(domainString)
        return cls.fromNode(parseTree.domain())

    def __setDomainName(self, node: pddlParser.DomainNameContext):
        self.name = node.getChild(2).getText()

    def __setRequirementsList(self, node: pddlParser.RequirementsContext):
        for child in node.children:
            if not isinstance(child, pddlParser.RequireKeyContext):
                continue
            self.requirements.append(child.getText())

    def __setTypesList(self, node: pddlParser.TypesContext):
        for typeRows in node.children:
            if not isinstance(typeRows, pddlParser.TypeContext):
                continue

            parent = None
            if typeRows.parent:
                name = typeRows.parent.getChild(1).getText()
                self.types[name] = self.types.setdefault(name, Type(name))
                parent = self.types[name]

            for t in typeRows.children:
                if not isinstance(t, pddlParser.TypeNameContext):
                    continue
                name = t.getText()
                self.types[name] = self.types.setdefault(name, Type(name, parent))
                if parent:
                    parent.addChild(self.types[name])

        pass

    def __setPredicates(self, node: pddlParser.PredicatesContext):
        for child in node.children:
            if not isinstance(child, pddlParser.TypedPositiveLiteralContext):
                continue
            self.predicates.add(TypedPredicate.fromNode(child, self.types))

    def __setFunctions(self, node: pddlParser.FunctionsContext):
        for child in node.children:
            if not isinstance(child, pddlParser.TypedPositiveLiteralContext):
                continue
            self.functions.add(TypedPredicate.fromNode(child, self.types))

    def toPDDL(self, pw: PDDLWriter = PDDLWriter()):
        pw.write(f"(define (domain {self.name})")
        pw.increaseTab()
        # Types
        pw.write(f"(:types")
        pw.increaseTab()
        for type in self.types.values():
            type.toPDDL(pw)
        pw.decreaseTab()
        pw.write(f")")

        if self.constants:
            # Constants
            pw.write(f"(:constants")
            pw.increaseTab()
            for (type, objects) in self.constants.items():
                objStr = " ".join(objects)
                pw.write(f"{objStr} - {type}")
            pw.decreaseTab()
            pw.write(f")")

        # Predicates
        pw.write(f"(:predicates")
        pw.increaseTab()
        for p in self.predicates:
            p.toPDDL(pw)
        pw.decreaseTab()
        pw.write(f")")

        if self.functions:
            # Functions
            pw.write(f"(:functions")
            pw.increaseTab()
            for f in self.functions:
                f.toPDDL(pw)
            pw.decreaseTab()
            pw.write(f")")

        for h in self.actions | self.events | self.processes:
            h.toPDDL(pw)

        pw.decreaseTab()
        pw.write(f")")

        return pw
