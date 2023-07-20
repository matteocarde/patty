from __future__ import annotations
from typing import Dict, List, Set

from src.pddl.Atom import Atom
from src.pddl.Operation import Operation
from src.pddl.Problem import Problem
from src.pddl.Utilities import Utilities
from src.pddl.Action import Action
from src.pddl.Event import Event
from src.pddl.Process import Process
from src.pddl.Type import Type
from src.pddl.TypedPredicate import TypedPredicate

from src.pddl.grammar.pddlParser import pddlParser


class Domain:
    name = str
    requirements: List[str]
    types: Dict[str, Type]
    predicates: set[TypedPredicate]
    functions: set[TypedPredicate]
    actions: set[Action]
    events: set[Event]
    processes: set[Process]
    __operationsDict: Dict[str, Operation]

    def __init__(self):
        self.types = dict()
        self.predicates = set()
        self.functions = set()
        self.actions = set()
        self.processes = set()
        self.events = set()
        self.requirements = list()
        self.constants = set()
        pass

    def ground(self, problem: Problem, avoidSimplification=False) -> GroundedDomain:

        gActions: Set[Action] = set([g for action in self.actions for g in action.ground(problem)])
        gEvents: Set[Event] = set([g for event in self.events for g in event.ground(problem)])
        gProcess: Set[Process] = set([g for process in self.processes for g in process.ground(problem)])

        gDomain = GroundedDomain(self.name, gActions, gEvents, gProcess)

        if avoidSimplification:
            return gDomain

        from src.pddl.RPG import RPG
        from src.pddl.ARPG import ARPG

        constants: Dict[Atom, float] = dict()

        for op in gActions | gEvents | gProcess:
            for fun in op.getFunctions():
                if fun not in problem.init.numericAssignments:
                    print(f"WARNING: {fun} was not initialized. Substituting it with 0")
                    constants[fun] = 0

        gDomain = gDomain.substitute(constants)

        rpg = RPG(gDomain, problem)
        orderedActions = rpg.getActionsOrder()
        arpg = ARPG(orderedActions, problem, gDomain)

        gDomain.actions = orderedActions
        constants: Dict[Atom, float] = arpg.getConstantAtoms()

        for op in gActions | gEvents | gProcess:
            for fun in op.getFunctions():
                if fun not in problem.init.numericAssignments:
                    # print(f"WARNING: {fun} was not initialized. Substituting it with 0")
                    constants[fun] = 0

        gDomain = gDomain.substitute(constants)
        orderedActions = [a.substitute(constants) for a in orderedActions if a.canHappen(constants)]
        problem.substitute(constants)

        gDomain.arpg = ARPG(orderedActions, problem, gDomain)
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
            if not isinstance(child, pddlParser.PositiveLiteralContext):
                continue
            self.predicates.add(TypedPredicate.fromNode(child, self.types))

    def __setFunctions(self, node: pddlParser.FunctionsContext):
        for child in node.children:
            if not isinstance(child, pddlParser.PositiveLiteralContext):
                continue
            self.functions.add(TypedPredicate.fromNode(child, self.types))


class GroundedDomain(Domain):
    __operationsDict: Dict[str, Operation] = dict()
    functions: Set[Atom]
    predicates: Set[Atom]
    pre: Dict[Atom, Set[Operation]]
    preN: Dict[Atom, Set[Operation]]
    preB: Dict[Atom, Set[Operation]]
    addList: Dict[Atom, Set[Operation]]
    delList: Dict[Atom, Set[Operation]]
    assList: Dict[Atom, Set[Operation]]

    def __init__(self, name: str, actions: Set[Action], events: Set[Event], process: Set[Process]):
        super().__init__()

        self.name = name
        self.actions = actions
        self.events = events
        self.processes = process

        self.substitutions = dict()

        self.operations: Set[Operation] = set()
        self.operations.update(self.actions)
        self.operations.update(self.events)
        self.operations.update(self.processes)

        self.functions: Set[Atom] = set()
        self.predicates: Set[Atom] = set()
        self.allAtoms: Set[Atom] = set()
        self.preB: Dict[Atom, Set[Operation]] = dict()
        self.addList: Dict[Atom, Set[Operation]] = dict()
        self.delList: Dict[Atom, Set[Operation]] = dict()
        self.assList: Dict[Atom, Set[Operation]] = dict()

        for op in self.operations:
            self.__operationsDict[op.planName] = op
            self.functions |= op.getFunctions()
            self.predicates |= op.getPredicates()

            for v in op.getPreB():
                self.preB.setdefault(v, set())
                self.preB[v].add(op)
            for v in op.getAddList():
                self.addList.setdefault(v, set())
                self.addList[v].add(op)
            for v in op.getDelList():
                self.delList.setdefault(v, set())
                self.delList[v].add(op)
            for v in op.getAssList():
                self.assList.setdefault(v, set())
                self.assList[v].add(op)

        self.allAtoms = self.functions | self.predicates
        self.arpg = None

    def getOperationByPlanName(self, planName) -> Operation:
        return self.__operationsDict[planName]

    def substitute(self, sub: Dict[Atom, float], default=None) -> GroundedDomain:
        subActions: Set[Action] = {a.substitute(sub, default) for a in self.actions if a.canHappen(sub, default)}

        return GroundedDomain(self.name, subActions, self.events, self.processes)


    def getARPG(self):
        return self.arpg
