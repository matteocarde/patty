from src.pddl.Action import Action
from src.pddl.DurativeAction import DurativeAction


class TemporalPlanAction:
    action: DurativeAction

    def __init__(self, action: DurativeAction, time: float, duration: float):
        self.action = action
        self.time = time
        self.duration = duration

    def __str__(self):
        return f"({self.time}:{self.action.originalName}) [{self.duration}]"

    def __repr__(self):
        return str(self)

    def __lt__(self, other):
        return self.time < other.time
