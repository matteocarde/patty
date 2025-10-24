import copy
from typing import List

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
    def fromHappening(cls, h: Happening, execs: List[Literal], i: int):
        pre = copy.deepcopy(h.getPre())
        if i > 0:
            pre.addClause(execs[i - 1])
        post = copy.deepcopy(h.getPost())
        post.addEffect(execs[i])

        a = Action.fromProperties(h.name, [], pre, post)
        a.__class__ = SnapHappeningAction
        a.originatingHappening = h
        print(f"{a.name} = <{pre}, {post}>")
        return a
