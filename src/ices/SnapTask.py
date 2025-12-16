import copy
import math
from typing import Set, Dict, List

from src.ices.Happening import Happening
from src.ices.ICEAction import ICEAction
from src.ices.ICETask import ICETask
from src.ices.SnapHappeningAction import SnapHappeningAction
from src.pddl.Action import Action
from src.pddl.BinaryPredicate import BinaryPredicate
from src.pddl.Domain import GroundedDomain
from src.pddl.Effects import Effects
from src.pddl.Formula import Formula
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

        for b in task.actions:
            self.execsAction[b] = dict()
            AICEs = Happening.AICEs(b)
            for i, H in enumerate(AICEs):
                prev = AICEs[i - 1] if i > 0 else list()
                for h in H:
                    ex = Literal.freshSimple(f"exec({h.name})")
                    self.execsAction[b][h] = ex
                    actions.add(SnapHappeningAction.fromHappening(h, prev, self.execsAction[b]))

        if task.conditions and task.effects:
            M = max([c.toTime.k for c in task.conditions.icond] + [e.time.k for e in task.effects.ieff])
        else:
            M = 0

        time = Literal.freshSimple(f"time_snap_patty")

        step = 10

        for i in range(0, M + step, step):
            pre = Formula()
            if i > 0:
                pre.addClause(BinaryPredicate.equality(time, float(i - step)))
            eff = Effects()
            eff.addEffect(BinaryPredicate.assign(time, i))
            a_i = SnapHappeningAction.fromProperties(f"time_flow_patty_{i}", [], pre, eff)
            actions.add(a_i)

        PICEs = Happening.PICEs(task.conditions, task.effects)
        self.execsCEs: Dict[Happening, Literal] = dict()
        for i, H in enumerate(PICEs):
            for h in H:
                ex = Literal.freshSimple(f"exec({h.name})")
                self.execsCEs[h] = ex
                self.goal.addClause(ex)
                actions.add(SnapHappeningAction.fromPlanHappening(h, M, time, self.execsCEs))

        super().__init__("SnapPi", actions, set(), set(), set())
        self.computeLists()

        pass
