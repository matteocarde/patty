from __future__ import annotations

from typing import Set

from classes.utils.Constants import EPSILON
from src.ices.Happening import HappeningActionStart, HappeningActionEnd, HappeningConditionStart, \
    HappeningConditionEnd, HappeningEffect, Happening
from src.ices.ICETask import ICETask
from src.ices.TimedICEAction import TimedICEAction


class TimedHappening:
    time: float
    happening: Happening

    def __init__(self, time: float, h: Happening):
        self.time = time
        self.happening = h

    def __str__(self):
        return f"<{self.time}, {self.happening}>"

    def __lt__(self, other):
        if not isinstance(other, TimedHappening):
            raise Exception()
        return self.time < other.time

    def __repr__(self):
        return str(self)

    @staticmethod
    def fromTimedICEAction(ticea: TimedICEAction) -> Set[TimedHappening]:
        timedHappenings: Set[TimedHappening] = set()

        t = ticea.time
        b = ticea.action
        d = ticea.duration

        timedHappenings.add(TimedHappening(t, HappeningActionStart(b)))
        timedHappenings.add(TimedHappening(t + d, HappeningActionEnd(b)))

        for c in b.icond:
            tau1 = c.fromTime
            tau2 = c.toTime
            timedHappenings.add(TimedHappening(tau1.absolute(t, t + d), HappeningConditionStart(c, b)))
            timedHappenings.add(TimedHappening(tau2.absolute(t, t + d), HappeningConditionEnd(c, b)))

        for e in b.ieff:
            tau = e.time
            timedHappenings.add(TimedHappening(tau.absolute(t + EPSILON, t + d + EPSILON), HappeningEffect(e, b)))

        return timedHappenings

    @staticmethod
    def fromICETask(task: ICETask, ms: float) -> Set[TimedHappening]:
        timedHappenings: Set[TimedHappening] = set()

        for c in task.goal:
            tau1 = c.fromTime
            tau2 = c.toTime
            timedHappenings.add(TimedHappening(tau1.absolute(0, ms), HappeningConditionStart(c, None)))
            timedHappenings.add(TimedHappening(tau2.absolute(0, ms), HappeningConditionEnd(c, None)))

        for e in task.init:
            tau = e.time
            timedHappenings.add(TimedHappening(tau.absolute(0, ms), HappeningEffect(e, None)))

        return timedHappenings
