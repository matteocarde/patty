from typing import Set, Dict

from src.ices.ConditionHappenings import ConditionHappenings
from src.ices.Happening import Happening, HappeningActionStart, HappeningActionEnd, HappeningConditionStart, \
    HappeningConditionEnd, HappeningEffect
from src.ices.ICEAction import ICEAction
from src.ices.IntermediateCondition import IntermediateCondition
from src.ices.IntermediateEffect import IntermediateEffect


class ActionHappenings:
    action: ICEAction
    happenings: Set[Happening]
    start: HappeningActionStart
    end: HappeningActionEnd
    conditions: Dict[IntermediateCondition, ConditionHappenings]
    effects: Dict[IntermediateEffect, HappeningEffect]

    def __init__(self):
        self.happenings = set()
        self.conditions = dict()
        self.effects = dict()
        pass

    @classmethod
    def fromAction(cls, b: ICEAction):

        ah = cls()
        ah.action = b
        ah.start = HappeningActionStart(b)
        ah.end = HappeningActionEnd(b)
        ah.happenings.update({ah.start, ah.end})

        for i, c in enumerate(b.icond):
            ch = ConditionHappenings.fromCondition(c, b, i)
            ah.conditions[c] = ch
            ah.happenings.update({ch.start, ch.end})

        for i, e in enumerate(b.ieff):
            ah.effects[e] = HappeningEffect(e, b, i)
            ah.happenings.add(ah.effects[e])

        return ah
