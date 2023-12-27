from __future__ import annotations

import copy
from typing import Dict, List, Set

from src.pddl.Action import Action
from src.pddl.Atom import Atom
from src.pddl.DurativeAction import DurativeAction
from src.pddl.Event import Event
from src.pddl.Operation import Operation
from src.pddl.PDDLWriter import PDDLWriter
from src.pddl.Problem import Problem
from src.pddl.Process import Process
from src.pddl.SnapAction import SnapAction
from src.pddl.State import State
from src.pddl.TimePredicate import TimePredicateType
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
    __operationsDict: Dict[str, Operation]

    def __init__(self):
        self.types = dict()
        self.predicates = set()
        self.functions = set()
        self.actions = set()
        self.durativeActions = set()
        self.processes = set()
        self.events = set()
        self.requirements = list()
        self.constants = set()
        self.isPredicateStatic: Dict[str, bool] = dict()
        pass

    def __deepcopy__(self, m):
        m = {} if m is None else m
        domain = Domain()
        domain.name = self.name

        domain.requirements = copy.deepcopy(self.requirements, m)
        domain.types = copy.deepcopy(self.requirements, m)
        domain.predicates = copy.deepcopy(self.predicates, m)
        domain.actions = copy.deepcopy(self.actions, m)
        domain.events = copy.deepcopy(self.events, m)
        domain.processes = copy.deepcopy(self.processes, m)
        domain.durativeActions = copy.deepcopy(self.durativeActions, m)
        domain.constants = copy.deepcopy(self.constants, m)
        return domain

    def ground(self, problem: Problem, avoidSimplification=False, console: LogPrint = None, delta=1) -> GroundedDomain:

        problem.computeWhatCanHappen(self)

        gActions: Set[Action] = set([g for action in self.actions for g in action.ground(problem, delta=delta)])
        gEvents: Set[Event] = set([g for event in self.events for g in event.ground(problem, delta=delta)])
        gProcess: Set[Process] = set([g for process in self.processes for g in process.ground(problem, delta=delta)])
        gDurativeActions: Set[DurativeAction] = set(
            [g for dAction in self.durativeActions for g in dAction.ground(problem, delta=delta)])

        gDomain = GroundedDomain(self.name, gActions, gEvents, gProcess, gDurativeActions)
        gDomain.allAtoms |= problem.allAtoms
        gDomain.functions |= problem.functions
        gDomain.predicates |= problem.predicates

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
        orderedActions = set(orderedActions)
        gDomain.actions = set()
        for a in orderedActions:
            if not isinstance(a, SnapAction):
                gDomain.actions.add(a)
                continue
            if a.durativeAction.start in orderedActions:
                gDomain.actions.add(a)

        # gDomain.actions = set(orderedActions)

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
            elif isinstance(child, pddlParser.DurativeActionContext):
                domain.durativeActions.add(DurativeAction.fromNode(child, domain.types))
            elif isinstance(child, pddlParser.EventContext):
                domain.events.add(Event.fromNode(child, domain.types))
            elif isinstance(child, pddlParser.ProcessContext):
                domain.processes.add(Process.fromNode(child, domain.types))

            # dAction: DurativeAction
            # for dAction in domain.durativeActions:
            #     types = [TimePredicateType.AT_START, TimePredicateType.OVER_ALL, TimePredicateType.AT_END]
            #     for t in types:
            #         a: SnapAction = SnapAction.fromDurativeAction(dAction, t)
            #         if a.predicates or a.functions:
            #             domain.actions.add(a)
            #             dAction.addSnapAction(t, a)

        domain.isPredicateStatic: Dict[str, bool] = dict([(p.name, True) for p in domain.predicates | domain.functions])
        for action in domain.actions | domain.events | domain.processes | domain.durativeActions:
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

    def getSignatures(self) -> Dict[str, Operation]:
        signatures: Dict[str, Operation] = dict()
        for h in self.actions | self.events | self.processes:
            signatures[h.getSignature()] = h
        return signatures


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

    def __init__(self, name: str, actions: Set[Action], events: Set[Event], process: Set[Process],
                 durativeActions: Set[DurativeAction], affectedGraph=None):
        super().__init__()

        self.name = name
        self.actions = actions
        self.events = events
        self.processes = process
        self.durativeActions = durativeActions

        types = [TimePredicateType.AT_START, TimePredicateType.OVER_ALL, TimePredicateType.AT_END]
        for dAction in self.durativeActions:
            for type in types:
                sa = dAction.getSnapAction(type)
                if sa.predicates or sa.functions:
                    self.actions.add(sa)

        self.substitutions = dict()

        self.operations: Set[Operation] = set()
        self.operations.update(self.actions)
        self.operations.update(self.events)
        self.operations.update(self.processes)
        # self.operations.update(self.durativeActions)

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

            pass

        self.allAtoms = self.functions | self.predicates
        self.arpg = None

        from src.plan.AffectedGraph import AffectedGraph
        self.affectedGraph: AffectedGraph = affectedGraph

    def getOperationByPlanName(self, planName) -> Operation:
        return self.__operationsDict[planName]

    def substitute(self, sub: Dict[Atom, float], default=None) -> GroundedDomain:
        subActions: Set[Action] = {a.substitute(sub, default) for a in self.actions if a.canHappen(sub, default)}

        return GroundedDomain(self.name, subActions, self.events, self.processes, self.durativeActions,
                              self.affectedGraph)

    def getARPG(self):
        return self.arpg

    def getStats(self) -> str:
        stats = []
        stats.append(f"|V_b|={len(self.predicates)}")
        stats.append(f"|V_n|={len(self.functions)}")
        stats.append(f"|A|={len(self.actions)}")
        stats.append(f"|Asgn(A)|={len(self.assList)}")
        return "\n".join(stats)

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
            for (type, objects) in self.constants:
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
