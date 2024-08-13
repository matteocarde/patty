from __future__ import annotations

from typing import Set

from src.ices.Happening import Happening
from src.ices.TimedICEAction import TimedICEAction


class TimedHappening:
    time: float
    happening: Happening

    def __init__(self, time: float, h: Happening):
        self.time = time
        self.happening = h

    @staticmethod
    def fromTimedICEAction(ticea: TimedICEAction) -> Set[TimedHappening]:
        pass
