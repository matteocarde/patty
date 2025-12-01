import copy
from typing import List, Dict

from src.ices.Happening import Happening
from src.pddl.Action import Action
from src.pddl.Literal import Literal


class SnapHappeningAction(Action):
    originatingHappening: Happening

    def __init__(self):
        super().__init__()

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
