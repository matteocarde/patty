from __future__ import annotations
import copy
from typing import List, Set, Tuple

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

    def __init__(self):
        self.cluster = ""
        self.starting = None
        self.ending = None
        pass

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name

    def getPre(self) -> Formula:
        raise NotImplementedError()

    def getPost(self) -> Effects:
        raise NotImplementedError()

    @staticmethod
    def AICEs(b: ICEAction) -> List[Happening]:

        relativeHappenings: Set[Tuple[int, int, Happening]] = set()
        for i, c in enumerate(b.icond):
            t = c.fromTime.absolute(0, b.duration)
            h = HappeningCondition(c, b, i)
            relativeHappenings.add((t, 0, h))

        for i, e in enumerate(b.ieff):
            t = e.time.absolute(0, b.duration)
            h = HappeningEffect(e, b, i)
            relativeHappenings.add((t, 1, h))

        sortedRelativeHappenings = sorted(relativeHappenings)
        print(sortedRelativeHappenings)
        return [h for (t, o, h) in sortedRelativeHappenings]

    @classmethod
    def PICEs(cls, conditions: TimedConditions, effects: TimedEffects):
        relativeHappenings: Set[Tuple[int, int, Happening]] = set()
        c: PlanIntermediateCondition
        for i, c in enumerate(conditions):
            t = c.fromTime.absolute(0, 1000000000)
            h = HappeningCondition(c, c, i)
            relativeHappenings.add((t, 0, h))

        e: PlanIntermediateEffect
        for i, e in enumerate(effects):
            t = e.time.absolute(0, 1000000000)
            h = HappeningEffect(e, e, i)
            relativeHappenings.add((t, 1, h))

        sortedRelativeHappenings = sorted(relativeHappenings)
        return [h for (t, o, h) in sortedRelativeHappenings]

    @staticmethod
    def computeTime(h):
        if isinstance(h, HappeningCondition) and isinstance(h.condition, ActionIntermediateCondition):
            assert isinstance(h.parent, ICEAction)
            cond = h.condition
            anchor = cond.fromTime.anchor if isinstance(h, HappeningConditionStart) else cond.toTime.anchor
            time = 0 if anchor == ActionRelativeTimeAnchor.START else h.parent.duration
            k = h.condition.fromTime.k
            return time + k
        elif isinstance(h, HappeningEffect) and isinstance(h.effect, ActionIntermediateEffect):
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
        super().__init__()
        self.condition = condition
        self.original = condition
        self.parent = parent
        self.index = index
        parentName = self.parent.name if isinstance(self.parent, ICEAction) else "PIC"
        self.name = f"{parentName}-C{self.index}"

    def getPre(self):
        return self.condition.conditions

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

    def __init__(self, effect: IntermediateEffect, parent: ICEAction or TimedEffects, index: int):
        super().__init__()
        self.effect = effect
        self.original = effect
        self.parent = parent
        self.index = index
        self.type = IEFF
        parentName = self.parent.name if isinstance(self.parent, ICEAction) else "PIE"
        self.name = f"{parentName}-E{self.index}"

    def getPre(self):
        return Formula()

    def getPost(self):
        return self.effect.effects

    def inMutexWith(self, h: Happening) -> bool:
        if isinstance(h, HappeningCondition):
            return h.condition.inMutexWith(self.effect)

        if isinstance(h, HappeningEffect):
            return self.effect.inMutexWith(h.effect)

    def __deepcopy__(self, memodict={}):
        return HappeningEffect(self.effect, copy.deepcopy(self.parent), self.index)
