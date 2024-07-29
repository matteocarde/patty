from src.ices.RelativeTime import RelativeTime
from src.ices.RelativeTimeAnchor import ActionRelativeTimeAnchor


class ActionRelativeTime(RelativeTime):
    anchor: ActionRelativeTimeAnchor
    k: int

    def __init__(self):
        super().__init__()
