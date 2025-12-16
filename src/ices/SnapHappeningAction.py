import copy
from typing import List, Dict

from src.ices.Happening import Happening, HappeningCondition, HappeningEffect
from src.ices.RelativeTime import RelativeTime
from src.pddl.Action import Action
from src.pddl.BinaryPredicate import BinaryPredicate
from src.pddl.Literal import Literal


class SnapHappeningAction(Action):
    originatingHappening: Happening or None

    def __init__(self):
        super().__init__()
        self.originatingHappening = None

    def __repr__(self):
        return f"{self.name} = <{self.preconditions}, {self.effects}>"

    @classmethod
    def fromHappening(cls, h: Happening, prev: List[Happening], execs: Dict[Happening, Literal]):
        pre = copy.deepcopy(h.getPre())
        for p in prev:
            pre.addClause(execs[p])
        post = copy.deepcopy(h.getPost())
        post.addEffect(execs[h])

        a = Action.fromProperties(h.name, [], pre, post)
        a.__class__ = SnapHappeningAction
        a.originatingHappening = h
        return a

    @classmethod
    def fromPlanHappening(cls, h: Happening, M: int, timeVar: Literal, execs: Dict[Happening, Literal]):
        pre = copy.deepcopy(h.getPre())
        if isinstance(h, HappeningCondition) and isinstance(h.condition.fromTime, RelativeTime):
            timeValue = h.condition.fromTime.absolute(0, M)
        elif isinstance(h, HappeningEffect) and isinstance(h.effect.time, RelativeTime):
            timeValue = h.effect.time.absolute(0, M)
        else:
            raise Exception()
        pre.addClause(BinaryPredicate.equality(timeVar, timeValue))
        post = copy.deepcopy(h.getPost())
        post.addEffect(execs[h])

        a = Action.fromProperties(h.name, [], pre, post)
        a.__class__ = SnapHappeningAction
        a.originatingHappening = h
        return a
