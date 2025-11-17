from typing import List, Set, Dict

from unified_planning.model import TimeInterval, FNode

from src.ices.PlanIntermediateCondition import PlanIntermediateCondition
from src.pddl.Atom import Atom


class TimedConditions:
    icond: Set[PlanIntermediateCondition]

    def __init__(self):
        self.icond = set()
        pass

    def __len__(self):
        return len(self.icond)

    def __iter__(self):
        return iter(self.icond)

    def addPlanIntermediateCondition(self, ic: PlanIntermediateCondition):
        self.icond.add(ic)

    @classmethod
    def fromUnifiedPlanning(cls, tgoals: Dict[TimeInterval, List[FNode]], atomDict: Dict[str, Atom]):
        tc = cls()
        for (time, cond) in tgoals.items():
            tc.addPlanIntermediateCondition(PlanIntermediateCondition.fromUnifiedPlanning(time, cond, atomDict))
        return tc

    def toANML(self):
        lines = []
        for cond in self.icond:
            for s in cond.toANML():
                lines.append(s)
        return lines
