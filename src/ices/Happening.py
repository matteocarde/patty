from __future__ import annotations
import copy
from typing import List, Set, Tuple, Dict

from src.ices.ActionIntermediateCondition import ActionIntermediateCondition
from src.ices.ActionIntermediateEffect import ActionIntermediateEffect
from src.ices.ActionRelativeTime import ActionRelativeTimeAnchor
from src.ices.ICEAction import ICEAction
from src.ices.PlanIntermediateCondition import PlanIntermediateCondition
from src.ices.PlanIntermediateEffect import PlanIntermediateEffect
from src.ices.TimedConditions import TimedConditions
from src.ices.TimedEffects import TimedEffects
from src.ices.IntermediateCondition import IntermediateCondition
from src.ices.IntermediateEffect import IntermediateEffect
from src.pddl.Effects import Effects
from src.pddl.Formula import Formula
from src.pddl.Preconditions import Preconditions
from src.utils.Constants import EPSILON

ACTION_START = r"b^\vdash"
ACTION_END = r"b^\dashv"
ICOND_START = r"c^\vdash"
ICOND_END = r"c^\dashv"
IEFF = r"e"


class Happening:
    type: str
    name: str
    cluster: str
    starting: ICEAction or None
    ending: ICEAction or None
    parent: ICEAction or PlanIntermediateCondition or PlanIntermediateEffect
    original: IntermediateCondition or IntermediateEffect
    conditions: Formula
    effects: Effects

    def __init__(self, conditions: Formula, effects: Effects):
        self.cluster = ""
        self.starting = None
        self.ending = None
        self.snapConditions = conditions
        self.snapEffects = effects
        pass

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name

    def __lt__(self, other):
        if not isinstance(other, Happening):
            return False
        return self.name < other.name

    def __eq__(self, other):
        if not isinstance(other, Happening):
            return False
        return self.name == other.name

    def __hash__(self):
        return hash(self.name)

    def getPre(self) -> Formula:
        raise NotImplementedError()

    def getPost(self) -> Effects:
        raise NotImplementedError()

    @staticmethod
    def __ICEs(conditions, effects, parent, duration):
        TH: Dict[float, List[Happening]] = dict()

        toJoin: Dict[float, Happening] = dict()

        c: ActionIntermediateCondition
        for i, c in enumerate(conditions):
            t_start = c.fromTime.absolute(0, duration)
            t_end = c.toTime.absolute(0, duration)
            p = parent if parent else c
            h = HappeningCondition(c, p, i)
            # TH.add(th)
            if t_start == t_end:
                assert t_start not in toJoin
                toJoin[t_start] = h
            elif t_start in toJoin:
                h.snapConditions += toJoin[t_start].snapConditions
            t_start = round(t_start)
            TH.setdefault(t_start, list())
            TH[t_start].append(h)

        e: ActionIntermediateEffect
        for i, e in enumerate(effects):
            t = e.time.absolute(0, duration)
            p = parent if parent else e
            h = HappeningEffect(e, p, i, toJoin[t].snapConditions) if t in toJoin else HappeningEffect(e, p, i,
                                                                                                       Formula())
            # h = HappeningEffect(toJoin[t].conditions, e.effects) if t in toJoin else Happening(Formula(), e.effects)
            TH.setdefault(t, list())
            TH[t].append(h)

        ICEs = [H for (t, H) in sorted(TH.items())]
        return ICEs

    @staticmethod
    def AICEs(b: ICEAction) -> List[List[Happening]]:
        return Happening.__ICEs(b.icond, b.ieff, b, b.duration)

    @staticmethod
    def PICEs(conditions: TimedConditions, effects: TimedEffects) -> List[List[Happening]]:
        return Happening.__ICEs(conditions, effects, None, 10000000)
    #
    # @classmethod
    # def PICEs(cls, conditions: TimedConditions, effects: TimedEffects) -> List[List[Happening]]:
    #
    #     timedHappenings: Dict[float, List[Happening]] = dict()
    #     c: PlanIntermediateCondition
    #     for i, c in enumerate(conditions):
    #         t = c.fromTime.absolute(0, 1000000000)
    #         h = HappeningCondition(c, c, i)
    #         timedHappenings.setdefault(t, list())
    #         timedHappenings[t].append(h)
    #
    #     e: PlanIntermediateEffect
    #     for i, e in enumerate(effects):
    #         t = e.time.absolute(0, 1000000000) + EPSILON / 2
    #         h = HappeningEffect(e, e, i)
    #         timedHappenings.setdefault(t, list())
    #         timedHappenings[t].append(h)
    #
    #     PICEs = [H for (t, H) in sorted(timedHappenings.items())]
    #     return PICEs

    @staticmethod
    def computeTime(h):
        if isinstance(h.condition, ActionIntermediateCondition):
            assert isinstance(h.parent, ICEAction)
            cond = h.condition
            anchor = cond.fromTime.anchor if isinstance(h, HappeningConditionStart) else cond.toTime.anchor
            time = 0 if anchor == ActionRelativeTimeAnchor.START else h.parent.duration
            k = h.condition.fromTime.k
            return time + k
        elif isinstance(h.effect, ActionIntermediateEffect):
            assert isinstance(h.parent, ICEAction)
            time = 0 if h.effect.time.anchor == ActionRelativeTimeAnchor.START else h.parent.duration
            k = h.effect.time.k
            return time + k
        return None


class HappeningAction(Happening):
    action: ICEAction

    def __init__(self, action: ICEAction):
        super().__init__()
        self.action = action


class HappeningActionStart(HappeningAction):

    def __init__(self, action: ICEAction):
        super().__init__(action)
        self.type = ACTION_START
        self.name = f"{self.action.name}-START"

    def __deepcopy__(self, memodict={}):
        return HappeningActionStart(copy.deepcopy(self.action))


class HappeningActionEnd(HappeningAction):

    def __init__(self, action: ICEAction):
        super().__init__(action)
        self.type = ACTION_END
        self.name = f"{self.action.name}-END"

    def __deepcopy__(self, memodict={}):
        return HappeningActionEnd(copy.deepcopy(self.action))


class HappeningCondition(Happening):
    condition: IntermediateCondition
    parent: ICEAction or TimedConditions

    def __init__(self, condition: IntermediateCondition, parent: ICEAction or PlanIntermediateCondition, index: int):
        super().__init__(condition.conditions, Effects())
        self.condition = condition
        self.original = condition
        self.parent = parent
        self.index = index
        parentName = self.parent.name if isinstance(self.parent, ICEAction) else "C"
        self.name = f"{parentName}[{condition.fromTime}, {condition.toTime}]"

    def getPre(self):
        return self.snapConditions

    def getPost(self):
        return Effects()

    def inMutexWith(self, h: Happening) -> bool:
        if isinstance(h, HappeningEffect):
            return self.condition.inMutexWith(h.effect)


class HappeningConditionStart(HappeningCondition):

    def __init__(self, condition: IntermediateCondition, parent: ICEAction or TimedConditions, index: int):
        super().__init__(condition, parent, index)
        self.type = ICOND_START
        parentName = self.parent.name if isinstance(self.parent, ICEAction) else "PIC"
        self.name = f"{parentName}-C{self.index}-START"

    def __deepcopy__(self, memodict={}):
        return HappeningConditionStart(self.condition, copy.deepcopy(self.parent), self.index)


class HappeningConditionEnd(HappeningCondition):

    def __init__(self, condition: IntermediateCondition, parent: ICEAction or TimedConditions, index: int):
        super().__init__(condition, parent, index)
        self.type = ICOND_END
        parentName = self.parent.name if isinstance(self.parent, ICEAction) else "PIC"
        self.name = f"{parentName}-C{self.index}-END"

    def __deepcopy__(self, memodict={}):
        return HappeningConditionEnd(self.condition, copy.deepcopy(self.parent), self.index)


class HappeningEffect(Happening):
    effect: IntermediateEffect
    parent: ICEAction or TimedEffects

    def __init__(self,
                 effect: IntermediateEffect,
                 parent: ICEAction or TimedEffects,
                 index: int,
                 condition: Formula):
        super().__init__(condition, effect.effects)
        self.effect = effect
        self.original = effect
        self.parent = parent
        self.index = index
        self.type = IEFF
        parentName = self.parent.name if isinstance(self.parent, ICEAction) else "E"
        self.name = f"{parentName}[{effect.time}]"

    def getPre(self):
        return self.snapConditions

    def getPost(self):
        return self.snapEffects

    def inMutexWith(self, h: Happening) -> bool:
        if isinstance(h, HappeningCondition):
            return h.condition.inMutexWith(self.effect)

        if isinstance(h, HappeningEffect):
            return self.effect.inMutexWith(h.effect)

    def __deepcopy__(self, memodict={}):
        return HappeningEffect(self.effect, copy.deepcopy(self.parent), self.index)
