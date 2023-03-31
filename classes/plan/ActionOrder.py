from typing import List

from ARPG import ARPG
from Action import Action
from Domain import GroundedDomain
from Problem import Problem
from RPG import RPG


class ActionOrder:

    def __init__(self):
        self.__order: List[Action] = list()

    def append(self, action: Action):
        self.__order.append(action)

    def __iter__(self):
        return iter(self.__order)

    def __str__(self):
        return str(self.__order)

    def __repr__(self):
        return str(self)
