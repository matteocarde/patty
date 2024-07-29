from src.ices.ActionRelativeTime import ActionRelativeTime
from src.ices.IntermediateCondition import IntermediateCondition
from src.pddl.Formula import Formula


class ActionIntermediateCondition(IntermediateCondition):
    fromTime: ActionRelativeTime
    toTime: ActionRelativeTime
    conditions: Formula

    def __init__(self):
        super().__init__()
