from src.pddl.Action import Action


class TemporalPlanInstantAction:
    action: Action

    def __init__(self, action: Action, time: float):
        self.action = action
        self.time = time

    def __str__(self):
        return f"({self.time}:{self.action})"

    def __repr__(self):
        return str(self)

    def __lt__(self, other):
        return self.time < other.time
