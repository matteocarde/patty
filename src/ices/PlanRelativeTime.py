from src.ices.RelativeTime import RelativeTime
from src.ices.RelativeTimeAnchor import PlanRelativeTimeAnchor


class PlanRelativeTime(RelativeTime):
    anchor: PlanRelativeTimeAnchor
    k: int

    def __init__(self):
        super().__init__()
