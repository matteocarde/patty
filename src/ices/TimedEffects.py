from typing import List, Set, Dict

from unified_planning.model import Timing, Effect

from pyeda_linux.boolalg.expr import Atom
from src.ices.PlanIntermediateEffect import PlanIntermediateEffect


class TimedEffects:
    ieff: Set[PlanIntermediateEffect]

    def __init__(self):
        self.ieff = set()
        pass

    def __len__(self):
        return len(self.ieff)

    def __str__(self):
        return str(self.ieff)

    def __iter__(self):
        return iter(self.ieff)

    def addPlanIntermediateEffect(self, ie: PlanIntermediateEffect):
        self.ieff.add(ie)

    @classmethod
    def fromUnifiedPlanning(cls, teffects: Dict[Timing, List[Effect]], atomDict: Dict[str, Atom]):
        te = cls()
        for (time, eff) in teffects.items():
            te.addPlanIntermediateEffect(PlanIntermediateEffect.fromUnifiedPlanning(time, eff, atomDict))
        return te
