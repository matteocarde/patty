from src.ices.RelativeTime import RelativeTime
from src.pddl.Formula import Formula


class IntermediateCondition:
    fromTime: RelativeTime
    toTime: RelativeTime
    conditions: Formula

    def __init__(self):
        pass
