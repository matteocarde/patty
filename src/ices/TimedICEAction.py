from __future__ import annotations

from typing import List, Tuple

from src.ices.ICEAction import ICEAction


class TimedICEAction:
    time: float
    action: ICEAction
    duration: float

    def __init__(self, t: float, b: ICEAction, d: float):
        self.time = t
        self.action = b
        self.duration = d

    def __hash__(self):
        return hash(str(self))

    def __eq__(self, other):
        return type(other) == type(self) and other.time == self.time and other.action == self.action \
            and other.duration == self.duration

    def __repr__(self):
        return str(self)

    def __lt__(self, other):
        return isinstance(other, TimedICEAction) and self.time < other.time

    def __str__(self):
        return f"<{self.time}, {self.action}, {self.duration}>"

    @classmethod
    def fixedDuration(cls, t: float, b: ICEAction) -> TimedICEAction:
        return cls(t, b, b.duration)


class TimedICEActionList(List[TimedICEAction]):

    def __init__(self):
        super().__init__()

    def tuples(self) -> List[Tuple[float, ICEAction, float]]:
        return [(tb.time, tb.action, tb.duration) for tb in self]
