from typing import Set

from src.ices.ICEAction import ICEAction
from src.ices.TimedConditions import TimedConditions
from src.ices.TimedEffects import TimedEffects
from src.pddl.Atom import Atom
from src.pddl.Goal import Goal
from src.pddl.InitialCondition import InitialCondition


class ICETask:
    propVariables: Set[Atom]
    numVariables: Set[Atom]
    actions: Set[ICEAction]
    init: InitialCondition
    goal: Goal
    conditions: TimedEffects
    effects: TimedConditions

    def __init__(self):
        self.propVariables = set()
        self.numVariables = set()
        self.actions = set()
        self.init = InitialCondition()
        self.goal = Goal()
        self.conditions = TimedEffects()
        self.effects = TimedConditions()
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
