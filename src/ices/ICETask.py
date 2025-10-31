from __future__ import annotations
from typing import Set

from src.ices.ICEAction import ICEAction
from src.ices.TimedConditions import TimedConditions
from src.ices.TimedEffects import TimedEffects
from src.pddl.Atom import Atom
from src.pddl.Domain import GroundedDomain
from src.pddl.Goal import Goal
from src.pddl.InitialCondition import InitialCondition
from src.pddl.Problem import Problem


class ICETask:
    propVariables: Set[Atom]
    numVariables: Set[Atom]
    actions: Set[ICEAction]
    init: InitialCondition
    goal: Goal
    conditions: TimedConditions
    effects: TimedEffects

    def __init__(self):
        self.propVariables = set()
        self.numVariables = set()
        self.actions = set()
        self.init = InitialCondition()
        self.goal = Goal()
        self.conditions = TimedConditions()
        self.effects = TimedEffects()
        pass

    def addPropVariables(self, atoms: Set[Atom]):
        cap = atoms.intersection(self.propVariables)
        if cap:
            raise Exception(f"Atoms {cap} already exists in prop variables")
        self.propVariables.update(atoms)

    def addPropVariable(self, atom: Atom):
        self.addPropVariables({atom})

    def addNumVariables(self, atoms: Set[Atom]):
        cap = atoms.intersection(self.numVariables)
        if cap:
            raise Exception(f"Atoms {cap} already exists in prop variables")
        self.numVariables.update(atoms)

    def addNumVariable(self, atom: Atom):
        self.addNumVariables({atom})

    def addAction(self, action: ICEAction):
        self.actions.add(action)

    def addActions(self, actions: Set[ICEAction]):
        self.actions.update(actions)

    @classmethod
    def fromTemporalNoICEs(cls, domain: GroundedDomain, problem: Problem) -> ICETask:
        task = cls()

        task.propVariables = domain.predicates
        task.numVariables = domain.functions
        task.init = problem.init
        task.goal = problem.goal

        action: ICEAction
        for action in domain.durativeActions:
            task.addAction(ICEAction.fromDurativeActionNOICEs(action))

        return task
