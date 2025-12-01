import copy
from typing import Set, Dict, List

from src.ices.Happening import Happening
from src.ices.ICEAction import ICEAction
from src.ices.ICETask import ICETask
from src.ices.SnapHappeningAction import SnapHappeningAction
from src.pddl.Action import Action
from src.pddl.Domain import GroundedDomain
from src.pddl.Goal import Goal
from src.pddl.Literal import Literal
from src.pddl.Predicate import Predicate
from src.pddl.State import State


class SnapTask(GroundedDomain):
    init: State
    goal: Goal
    actions: Set[Action]
    execsAction: Dict[ICEAction, List[Predicate]]
    execsCEs: List[Predicate]

    def __init__(self, task: ICETask):
        actions: Set[Action] = set()

        self.init = State.fromInitialCondition(task.init)
        self.goal = copy.deepcopy(task.goal)

        self.execsAction: Dict[ICEAction, Dict[Happening, Literal]] = dict()
        self.execsCEs = list()

        for b in task.actions:
            self.execsAction[b] = dict()
            AICEs = Happening.AICEs(b)
            # AICEs[0][0].starting = b
            # AICEs[-1][-1].ending = b
            for i, H in enumerate(AICEs):
                prev = AICEs[i-1] if i > 0 else list()
                for h in H:
                    ex = Literal.freshSimple(f"exec({h.name})")
                    self.execsAction[b][h] = ex
                    actions.add(SnapHappeningAction.fromHappening(h, prev, self.execsAction[b]))

        for i, h in enumerate(Happening.PICEs(task.conditions, task.effects)):
            ex = Literal.freshSimple(f"exec({h.name})")
            self.execsCEs.append(ex)
            self.goal.addClause(ex)
            actions.add(SnapHappeningAction.fromHappening(h, self.execsCEs, i))

        super().__init__("SnapPi", actions, set(), set(), set())
        self.computeLists()

        pass
