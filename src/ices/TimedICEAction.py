from __future__ import annotations

from src.ices.ICEAction import ICEAction


class TimedICEAction:
    time: float
    action: ICEAction
    duration: float

    def __init__(self, t: float, b: ICEAction, d: float):
        self.time = t
        self.action = b
        self.duration = d

    def __repr__(self):
        return str(self)

    def __str__(self):
        return f"<{self.time}, {self.action}, {self.duration}>"

    @classmethod
    def fixedDuration(cls, t: float, b: ICEAction) -> TimedICEAction:
        return cls(t, b, b.duration)
