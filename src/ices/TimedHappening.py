from __future__ import annotations

from typing import Set

from classes.utils.Constants import EPSILON
from src.ices.Happening import HappeningActionStart, HappeningActionEnd, HappeningConditionStart, \
    HappeningConditionEnd, HappeningEffect, Happening, ACTION_START, ICOND_START, \
    ICOND_END, IEFF, ACTION_END
from src.ices.ICETask import ICETask
from src.ices.TimedICEAction import TimedICEAction

ORDER = [
    ACTION_START,
    ICOND_START,
    ICOND_END,
    IEFF,
    ACTION_END
]
ORDER_INDEX = dict([(c, i) for (i, c) in enumerate(ORDER)])


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
        if self.time < other.time:
            return True
        if self.time == other.time and ORDER_INDEX[self.happening.type] < ORDER_INDEX[other.happening.type]:
            return True
        return False

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

        for i, c in enumerate(b.icond):
            tau1 = c.fromTime
            tau2 = c.toTime
            timedHappenings.add(
                TimedHappening(tau1.absolute(t, t + d), HappeningConditionStart(c, b, i)))
            timedHappenings.add(
                TimedHappening(tau2.absolute(t, t + d), HappeningConditionEnd(c, b, i)))

        for i, e in enumerate(b.ieff):
            tau = e.time
            timedHappenings.add(TimedHappening(tau.absolute(t, t + d), HappeningEffect(e, b, i)))

        return timedHappenings

    @staticmethod
    def fromICETask(task: ICETask, ms: float) -> Set[TimedHappening]:
        timedHappenings: Set[TimedHappening] = set()

        for i, c in enumerate(task.goal):
            tau1 = c.fromTime
            tau2 = c.toTime
            timedHappenings.add(TimedHappening(tau1.absolute(0, ms), HappeningConditionStart(c, task.goal, i)))
            timedHappenings.add(TimedHappening(tau2.absolute(0, ms), HappeningConditionEnd(c, task.goal, i)))

        for i, e in enumerate(task.init):
            tau = e.time
            timedHappenings.add(TimedHappening(tau.absolute(EPSILON, ms), HappeningEffect(e, task.init, i)))

        return timedHappenings
