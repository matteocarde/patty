from src.pddl.Action import Action
from typing import List


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
