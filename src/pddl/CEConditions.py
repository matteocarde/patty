from __future__ import annotations

import copy
from typing import Dict, cast

from src.pddl.Atom import Atom
from src.pddl.Formula import Formula
from src.pddl.Literal import Literal


class CEConditions(Formula):

    def __init__(self):
        super().__init__()

    def getPositive(self):
        return {e.getAtom() for e in self.conditions if isinstance(e, Literal) and e.sign == "+"}

    def getNegative(self):
        return {e.getAtom() for e in self.conditions if isinstance(e, Literal) and e.sign == "-"}

    def ground(self, subs: Dict[str, str], delta=1) -> CEConditions:
        g = super().ground(subs, delta)
        g.__class__ = CEConditions
        return cast(CEConditions, g)

    def substitute(self, subs: Dict[Atom, float], default=None) -> CEConditions:
        s = super().substitute(subs, default)
        s.__class__ = CEConditions
        return cast(CEConditions, s)

    def __deepcopy__(self, m=None):
        m = {} if m is None else m
        f = copy.deepcopy(super(), m)
        f.__class__ = CEConditions
        return cast(CEConditions, f)
