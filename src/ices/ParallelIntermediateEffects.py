from typing import Set

from src.ices.IntermediateEffect import IntermediateEffect


class ParallelIntermediateEffects:
    time: float
    __hasTime: bool
    __ieffs: Set[IntermediateEffect]

    def __init__(self):
        self.__hasTime = False
        self.__ieffs = set()
        pass

    def add(self, ieff: IntermediateEffect):
        if not self.__hasTime:
            self.__hasTime = True
            self.time = ieff.time

        if ieff.time != self.time:
            raise Exception("Error: Trying to insert into ParallelIntermediateEffects "
                            "two IntermedateEffects with diffrent times")

        self.__ieffs.add(ieff)

    def __iter__(self):
        return iter(self.__ieffs)
