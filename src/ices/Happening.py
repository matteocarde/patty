import copy

from src.ices.ICEAction import ICEAction
from src.ices.TimedConditions import TimedConditions
from src.ices.TimedEffects import TimedEffects
from src.ices.IntermediateCondition import IntermediateCondition
from src.ices.IntermediateEffect import IntermediateEffect

ACTION_START = r"b^\vdash"
ACTION_END = r"b^\dashv"
ICOND_START = r"c^\vdash"
ICOND_END = r"c^\dashv"
IEFF = r"e"


class Happening:
    type: str
    name: str

    def __init__(self):
        pass

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name


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

    def __init__(self, condition: IntermediateCondition, parent: ICEAction or TimedConditions, index: int):
        super().__init__()
        self.condition = condition
        self.parent = parent
        self.index = index

    def inMutexWith(self, h: Happening) -> bool:
        if isinstance(h, HappeningEffect):
            return self.condition.inMutexWith(h.effect)


class HappeningConditionStart(HappeningCondition):

    def __init__(self, condition: IntermediateCondition, parent: ICEAction or TimedConditions, index: int):
        super().__init__(condition, parent, index)
        self.type = ICOND_START
        parentName = self.parent.name if isinstance(self.parent, ICEAction) else "goal"
        self.name = f"{parentName}-C{self.index}-START"

    def __deepcopy__(self, memodict={}):
        return HappeningConditionStart(self.condition, copy.deepcopy(self.parent), self.index)


class HappeningConditionEnd(HappeningCondition):

    def __init__(self, condition: IntermediateCondition, parent: ICEAction or TimedConditions, index: int):
        super().__init__(condition, parent, index)
        self.type = ICOND_END
        parentName = self.parent.name if isinstance(self.parent, ICEAction) else "goal"
        self.name = f"{parentName}-C{self.index}-END"

    def __deepcopy__(self, memodict={}):
        return HappeningConditionEnd(self.condition, copy.deepcopy(self.parent), self.index)


class HappeningEffect(Happening):
    effect: IntermediateEffect
    parent: ICEAction or TimedEffects

    def __init__(self, effect: IntermediateEffect, parent: ICEAction or TimedEffects, index: str):
        super().__init__()
        self.effect = effect
        self.parent = parent
        self.index = index
        self.type = IEFF
        parentName = self.parent.name if isinstance(self.parent, ICEAction) else "init"
        self.name = f"{parentName}-E-{self.index}"

    def inMutexWith(self, h: Happening) -> bool:
        if isinstance(h, HappeningCondition):
            return h.condition.inMutexWith(self.effect)

        if isinstance(h, HappeningEffect):
            return self.effect.inMutexWith(h.effect)

    def __deepcopy__(self, memodict={}):
        return HappeningEffect(self.effect, copy.deepcopy(self.parent), self.index)
