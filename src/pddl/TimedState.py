from src.pddl.State import State


class TimedState:
    time: float
    state: State

    def __init__(self, time: float, state: State):
        self.time = time
        self.state = state

    def __repr__(self):
        return f"{self.time} {self.state}"
