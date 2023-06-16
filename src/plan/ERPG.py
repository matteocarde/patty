from __future__ import annotations
from typing import List, Dict

from Action import Action
from RelaxedState import RelaxedState


class ERPGNode:
    __state: RelaxedState
    __children: Dict[Action, ERPGNode]

    def __init__(self, state: RelaxedState):
        self.__state = state
        self.__children = dict()

    def addChild(self, action: Action):
        child = ERPGNode(self.__state.applyAction(action))
        self.__children[action] = child


class ERPG:

    def __init__(self, state: RelaxedState, actions: List[Action]):
        pass
