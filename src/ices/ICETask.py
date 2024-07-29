from typing import Set

from src.ices.ICEAction import ICEAction
from src.ices.ICEGoal import ICEGoal
from src.ices.ICEInitialCondition import ICEInitialCondition
from src.pddl.Atom import Atom


class ICETask:
    propVariables: Set[Atom]
    numVariables: Set[Atom]
    actions: Set[ICEAction]
    init: ICEInitialCondition
    goal: ICEGoal

    def __init__(self):
        self.propVariables = set()
        self.numVariables = set()
        self.actions = set()
        self.init = ICEInitialCondition()
        self.goal = ICEGoal()
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
