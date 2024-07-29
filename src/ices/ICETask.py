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
        pass
