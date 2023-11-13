from __future__ import annotations

from typing import Dict, Set

from src.pddl.Action import Action
from src.pddl.Atom import Atom
from src.pddl.Domain import Domain
from src.pddl.Event import Event
from src.pddl.Operation import Operation
from src.pddl.Process import Process


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

    def __init__(self, name: str, actions: Set[Action], events: Set[Event], process: Set[Process], affectedGraph=None):
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

        from src.plan.AffectedGraph import AffectedGraph
        self.affectedGraph: AffectedGraph = affectedGraph

    def getOperationByPlanName(self, planName) -> Operation:
        return self.__operationsDict[planName]

    def substitute(self, sub: Dict[Atom, float], default=None) -> GroundedDomain:
        subActions: Set[Action] = {a.substitute(sub, default) for a in self.actions if a.canHappen(sub, default)}

        return GroundedDomain(self.name, subActions, self.events, self.processes, self.affectedGraph)

    def getARPG(self):
        return self.arpg

    def getStats(self) -> str:
        stats = []
        stats.append(f"|V_b|={len(self.predicates)}")
        stats.append(f"|V_n|={len(self.functions)}")
        stats.append(f"|A|={len(self.actions)}")
        stats.append(f"|Asgn(A)|={len(self.assList)}")
        return "\n".join(stats)
