from __future__ import annotations

from typing import Dict
from src.pddl.Action import Action


class CNFVariable:
    CNF_ID: int = 1
    ID2VAR: Dict[int, CNFVariable] = dict()

    name: str
    id: int

    def __init__(self, name: str):
        self.name = name
        self.id = CNFVariable.CNF_ID
        CNFVariable.CNF_ID += 1
        CNFVariable.ID2VAR[self.id] = self

    def __int__(self):
        return self.id

    def __invert__(self):
        return -self.id

    @staticmethod
    def reset():
        CNFVariable.CNF_ID = 1
        del CNFVariable.ID2VAR
        CNFVariable.ID2VAR = dict()


class CNFActionVariable(CNFVariable):
    action: Action

    def __init__(self, name: str, action: Action):
        super().__init__(name)
        self.action = action
