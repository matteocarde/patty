from unified_planning.model import Timing, TimepointKind

from src.ices.RelativeTimeAnchor import RelativeTimeAnchor
from src.smt.SMTExpression import SMTExpression


class RelativeTime:
    anchor: RelativeTimeAnchor
    k: int

    def __init__(self):
        pass

    def __repr__(self):
        return str(self)

    def __str__(self):
        from src.ices.ActionRelativeTime import ActionRelativeTimeAnchor
        from src.ices.PlanRelativeTime import PlanRelativeTimeAnchor
        if self.anchor in {ActionRelativeTimeAnchor.START, PlanRelativeTimeAnchor.BEGIN}:
            sign = "+"
        else:
            sign = "-"
        if self.k > 0:
            return f"{self.anchor.value} {sign} {self.k}"
        else:
            return f"{self.anchor.value}"

    def __eq__(self, other):
        if not isinstance(other, RelativeTime):
            return False
        return other.k == self.k and other.anchor == self.anchor

    def absolute(self, a: SMTExpression or float, b: SMTExpression or float) -> SMTExpression or float:
        from src.ices.ActionRelativeTime import ActionRelativeTimeAnchor
        from src.ices.PlanRelativeTime import PlanRelativeTimeAnchor

        if self.anchor in {ActionRelativeTimeAnchor.START, PlanRelativeTimeAnchor.BEGIN}:
            return a + self.k
        if self.anchor in {ActionRelativeTimeAnchor.END, PlanRelativeTimeAnchor.FINISH}:
            return b - self.k
        raise Exception

    @classmethod
    def fromUnifiedPlanning(cls, time: Timing):
        t = cls()
        from src.ices.ActionRelativeTime import ActionRelativeTimeAnchor
        from src.ices.PlanRelativeTime import PlanRelativeTimeAnchor
        UP2TIME = {
            TimepointKind.START: ActionRelativeTimeAnchor.START,
            TimepointKind.END: ActionRelativeTimeAnchor.END,
            TimepointKind.GLOBAL_START: PlanRelativeTimeAnchor.BEGIN,
            TimepointKind.GLOBAL_END: PlanRelativeTimeAnchor.FINISH,
        }
        t.anchor = UP2TIME[time.timepoint.kind]
        t.k = time.delay

        return t

    def toANML(self):
        from src.ices.ActionRelativeTime import ActionRelativeTimeAnchor
        from src.ices.PlanRelativeTime import PlanRelativeTimeAnchor
        if self.anchor in {ActionRelativeTimeAnchor.START, PlanRelativeTimeAnchor.BEGIN}:
            anchor = "start"
            sign = "+"
        elif self.anchor in {ActionRelativeTimeAnchor.END, PlanRelativeTimeAnchor.FINISH}:
            anchor = "end"
            sign = "-"
        else:
            raise Exception()

        return f"{anchor} {sign} {self.k}" if self.k else f"{anchor}"
