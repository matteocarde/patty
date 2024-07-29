from typing import List

from src.ices.ActionIntermediateCondition import ActionIntermediateCondition
from src.ices.ActionIntermediateEffect import ActionIntermediateEffect


class ICEAction:
    icond: List[ActionIntermediateCondition]
    ieff: List[ActionIntermediateEffect]
    duration: int

    def __init__(self):
        self.icond = list()
        self.ieff = list()
        self.duration = 0
