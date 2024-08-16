from src.ices.RelativeTimeAnchor import RelativeTimeAnchor
from src.smt.SMTExpression import SMTExpression


class RelativeTime:
    anchor: RelativeTimeAnchor
    k: int

    def __init__(self):
        pass

    def absolute(self, a: SMTExpression or float, b: SMTExpression or float):
        from src.ices.ActionRelativeTime import ActionRelativeTimeAnchor
        from src.ices.PlanRelativeTime import PlanRelativeTimeAnchor

        if self.anchor in {ActionRelativeTimeAnchor.START, PlanRelativeTimeAnchor.BEGIN}:
            return a + self.k
        if self.anchor in {ActionRelativeTimeAnchor.END, PlanRelativeTimeAnchor.FINISH}:
            return b - self.k
        raise Exception
